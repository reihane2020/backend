from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from software.models import Software
from datetime import date, timedelta
from setting.models import Setting
from rest_framework.exceptions import APIException
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class HasPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            softCreator = Software.objects.get(
                id=request.data['software']
            ).created_by
            return softCreator == request.user
        except:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.software.created_by == request.user


class RatingEvaluateViewSet(viewsets.ModelViewSet):
    serializer_class = RatingEvaluateSerializer
    queryset = RatingEvaluate.objects.all()
    filterset_fields = ['software']
    permission_classes = [permissions.IsAuthenticated, HasPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        publish = False
        extension = False
        try:
            publish = self.request.data['publish']
        except:
            pass

        try:
            extension = self.request.data['extension']
        except:
            pass

        if publish:
            # validate

            time_threshold = timezone.now() - timedelta(days=30)
            res = self.queryset.filter(
                created_by=self.request.user,
                published_datetime__gt=time_threshold,
                publish=True
            )

            if res.count() >= 1 and not "rating" in self.request.user.can_publish_evaluation:
                raise APIException(
                    code="LIMIT_EVALUATION",
                    detail="You can publish 1 evaluation per month"
                )

            if "rating" in self.request.user.can_publish_evaluation:
                self.request.user.can_publish_evaluation.remove("rating")
                self.request.user.save()

            days = Setting.objects.get(pk=1).evaluation_days
            serializer.save(
                deadline=date.today() + timedelta(days=days),
                publish=True,
                is_active=True,
                published_datetime=timezone.now()
            )

        if extension:
            days = Setting.objects.get(pk=1).evaluation_days
            ev = self.queryset.get(pk=self.kwargs['pk'])
            m = ev.deadline
            if (m - date.today()).total_seconds() < 0:
                m = date.today()
            serializer.save(
                deadline=m + timedelta(days=days),
                publish=True,
                is_active=True
            )

        return super().perform_update(serializer)


# ****

class RatingEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = RatingEvaluationSerializer
    queryset = RatingEvaluate.objects.filter(
        is_active=True,
        publish=True,
        max__gt=F('evaluates'),
        deadline__gt=date.today()
    )
    filterset_fields = ['software']

    def perform_create(self, serializer):
        ev = RatingEvaluate.objects.get(
            id=self.request.data['evaluate_id']
        )
        result, created = RatingEvaluateResult.objects.get_or_create(
            evaluate=ev,
            evaluated_by=self.request.user,
        )
        my = self.request.data['data']
        if my['id'] == None:
            result.rating = my['rating']
            result.save()

        if created:
            ev.evaluates = ev.evaluates + 1
            ev.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(True, status=status.HTTP_201_CREATED, headers=headers)


class RatingResultViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RatingResultSerializer
    queryset = RatingEvaluate.objects.filter(
        publish=True,
    )
    filterset_fields = ['software']

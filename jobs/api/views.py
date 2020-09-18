from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now

from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(
        last_date__gte=now()).order_by('-created_at')


class SearchApiView(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        if 'location' in self.request.GET and 'title' in self.request.GET:
            return self.serializer_class.Meta.model.objects.filter(location__contains=self.request.GET['location'],
                                                                   title__contains=self.request.GET['title'])
        else:
            return self.serializer_class.Meta.model.objects.all().order_by('-created_at')


class ApplyJobApiView(CreateAPIView):
    serializer_class = ApplicantSerializer
    http_method_names = [u'post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

import requests
from django.views.generic import ListView
from apicourse.models import Course
from apicourse.serializers import CourseSerializer
from rest_framework import filters, viewsets


class CourseViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'time_start']

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def get_response_api():
    URL = "http://127.0.0.1:8000/api/course/"
    response = requests.get(URL)
    return response.json()


class CourseHome(ListView):
    model = Course
    template_name = 'apicourse/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = get_response_api()
        return context

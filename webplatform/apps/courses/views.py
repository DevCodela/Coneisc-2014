from rest_framework.renderers import JSONRenderer

from .models import Course, Chapter, Article

from .serializers import ChaptersSerializer, ArticlesSerializer

from django.views.generic import DetailView
from braces.views import LoginRequiredMixin


class CourseDetailView(LoginRequiredMixin, DetailView):

    context_object_name = 'course'
    model = Course
    template_name = 'home/course_detail.html'
    slug_field = 'slug'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)

        slug_course = self.kwargs['slug']

        chapters_qs = self.get_chapters(slug_course)
        articles_qs = self.get_articles(slug_course)

        chapters_serializer = ChaptersSerializer(chapters_qs, many=True)
        articles_serializer = ArticlesSerializer(articles_qs, many=True)
        
        chapters_json = JSONRenderer().render(chapters_serializer.data)
        articles_json = JSONRenderer().render(articles_serializer.data)

        context.update(dict(chapters=chapters_json))
        context.update(dict(articles=articles_json))

        return context

    def get_chapters(self, slug):
        return Chapter.objects.by_course_and_released_asc(slug=slug)

    def get_articles(self, slug):
        return Article.objects.by_course_and_released_asc(slug=slug)
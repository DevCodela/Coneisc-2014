#encoding:utf-8
from django.views.generic import FormView, TemplateView

from braces.views import LoginRequiredMixin

from django.contrib.auth.models import User
from apps.courses.models import Course, UserEnrolled
from .forms import EnrollForm

from django.core.urlresolvers import reverse_lazy


class HomeDashboardTemplateView(TemplateView):

    template_name = 'home/index.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):

        context = super(HomeDashboardTemplateView, self).get_context_data(**kwargs)
        
        user_login = self.request.user

        if user_login.is_authenticated():

            user_enrolled = User.objects.get(username=user_login)
            enrolled_courses = user_enrolled.course_set.all()

            all_courses_released = Course.objects.filter(released=True)
            available_courses = all_courses_released.exclude(pk__in=enrolled_courses)

            context['enrolled_courses'] = enrolled_courses
            context['available_courses'] = available_courses

        return context


class Enroll(FormView):

    form_class = EnrollForm
    success_url = '/'

    def form_valid(self, form):
        user_enroll = self.request.user
        course_slug = form.cleaned_data['course']

        course = Course.objects.get(slug=course_slug)

        user_enrolled = UserEnrolled()
        user_enrolled.user = user_enroll
        user_enrolled.course = course
        user_enrolled.save()

        return super(Enroll, self).form_valid(form)
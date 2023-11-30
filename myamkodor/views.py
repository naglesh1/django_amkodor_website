from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'myamkodor/index.html'


class GeneralView(TemplateView):
    template_name = 'myamkodor/general.html'


class AboutView(TemplateView):
    template_name = ...

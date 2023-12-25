from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from myamkodor.models import News, Contact, Vacancy, Tender, Rent, Products, ProductCategory, Nelekvidi, TransportBY, \
    Services
from .functions import new_get_queryset




class IndexView(TemplateView):
    template_name = 'myamkodor/home.html'
    # title = 'Главная страница'
    extra_context = {'title': 'Главная',
                     }


class GeneralView(TemplateView):
    template_name = 'myamkodor/general.html'
    extra_context = {'title': 'Общее',
                     }


class NewsView(ListView):
    template_name = 'myamkodor/news.html'
    context_object_name = 'newss'
    paginate_by = 2

    def get_queryset(self):
        return new_get_queryset(News.objects.get_is_published(), 3)

    extra_context = {'title': 'Новости',
                     }


class ShowNews(DetailView):
    template_name = 'myamkodor/index.html'
    context_object_name = 'obj'
    slug_url_kwarg = 'news_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(News.objects.get_is_published(), slug=self.kwargs[self.slug_url_kwarg])

    extra_context = {'title': "Новости",
                     }


class AboutView(TemplateView):
    template_name = 'myamkodor/about.html'

    extra_context = {'title': "О компании",
                     }


class ContactView(ListView):
    template_name = 'myamkodor/contact.html'
    context_object_name = 'contacts'

    extra_context = {'title': "Контакты",
                     }

    def get_queryset(self):
        return new_get_queryset(Contact.objects.all(), 4)


class VacancyView(ListView):
    template_name = 'myamkodor/vacancy.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return new_get_queryset(Vacancy.objects.all(), 3)

    extra_context = {'title': "Вакансии",
                     }


class ShowVacancy(DetailView):
    template_name = 'myamkodor/vacancepage.html'
    context_object_name = 'vacancy'
    slug_url_kwarg = 'vacancy_slug'

    extra_context = {'title': "Контакты",
                     }

    def get_object(self, queryset=None):
        return get_object_or_404(Vacancy.objects.all(), slug=self.kwargs[self.slug_url_kwarg])


class TenderView(ListView):
    template_name = 'myamkodor/tender.html'
    context_object_name = 'tenders'

    def get_queryset(self):
        return Tender.objects.all()

    extra_context = {'title': "Тендеры",
                     }


class ShowTender(DetailView):
    template_name = 'myamkodor/showtender.html'
    context_object_name = 'tender'
    slug_url_kwarg = 'tender_slug'

    extra_context = {'title': "Тендер",
                     }

    def get_object(self, queryset=None):
        return get_object_or_404(Tender.objects.all(), slug=self.kwargs[self.slug_url_kwarg])


class RentView(ListView):
    template_name = 'myamkodor/rent.html'
    context_object_name = 'rents'

    def get_queryset(self):
        return Rent.objects.all()

    extra_context = {'title': "Аренда",
                     }


class ProductsView(ListView):
    template_name = 'myamkodor/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()

        context['title'] = 'Продукция'

        return context

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        return new_get_queryset(
            Products.objects.filter(category_id=category_id) if category_id else Products.objects.all(), 3)


class ShowProduct(DetailView):
    template_name = 'myamkodor/index.html'
    context_object_name = 'obj'
    slug_url_kwarg = 'product_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Products.objects.all(), slug=self.kwargs[self.slug_url_kwarg])

    extra_context = {'title': "Продукция",
                     }


class NelekvidiView(ListView):
    template_name = 'myamkodor/nelekvidi.html'
    context_object_name = 'nelekvidis'

    def get_queryset(self):
        return new_get_queryset(Nelekvidi.objects.all(), 2)

    extra_context = {'title': "Нелеквиды",
                     }


class RealizationView(ListView):
    template_name = 'myamkodor/realization.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        return new_get_queryset(TransportBY.objects.all(), 3)

    extra_context = {'title': "Реализация",
                     }


class ShowTransport(DetailView):
    template_name = 'myamkodor/index.html'
    context_object_name = 'obj'
    slug_url_kwarg = 'product_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(TransportBY.objects.all(), slug=self.kwargs[self.slug_url_kwarg])

    extra_context = {'title': "Транспорт Б/У",
                     }


class SecvicesView(ListView):
    template_name = 'myamkodor/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return new_get_queryset(Services.objects.all(), 3)

    extra_context = {'title': "Услуги",
                     }


class ShowServices(DetailView):
    template_name = 'myamkodor/index.html'
    context_object_name = 'obj'
    slug_url_kwarg = 'product_slug'

    extra_context = {'title': "Услуги",
                     }

    def get_object(self, queryset=None):
        return get_object_or_404(Services.objects.all(), slug=self.kwargs[self.slug_url_kwarg])

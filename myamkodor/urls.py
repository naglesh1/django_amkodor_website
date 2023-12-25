from django.urls import path

from . import views

app_name = 'amkodor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('general/', views.GeneralView.as_view(), name='general'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('rent/', views.RentView.as_view(), name='rent'),

    path('vacancy/<int:page>/', views.VacancyView.as_view(), name='vacancy'),
    path('vacancy/<slug:vacancy_slug>/', views.ShowVacancy.as_view(), name='showvacancy'),

    path('services/', views.SecvicesView.as_view(), name='services'),
    path('services/<slug:product_slug>/', views.ShowServices.as_view(), name='showservices'),

    path('nelekvidi/', views.NelekvidiView.as_view(), name='nelekvidi'),
    path('realization/<int:page>/', views.RealizationView.as_view(), name='realization'),
    path('transportby/<slug:product_slug>/', views.ShowTransport.as_view(), name='showtransport'),

    path('tender/', views.TenderView.as_view(), name='tender'),
    path('tender/<slug:tender_slug>/', views.ShowTender.as_view(), name='showtender'),

    path('newspage/<int:page>/', views.NewsView.as_view(), name='newspage'),
    path('newspage/<slug:news_slug>/', views.ShowNews.as_view(), name='shownews'),

    path('products/<int:page>/', views.ProductsView.as_view(), name='products'),
    # path('productspage/<int:page>/', views.ProductsView.as_view(), name='productspage'),
    path('category/<int:category_id>/', views.ProductsView.as_view(), name='category'),
    path('products/<slug:product_slug>/', views.ShowProduct.as_view(), name='showproduct'),

]

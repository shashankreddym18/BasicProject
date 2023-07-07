from django.urls import include, re_path
import MyApp1.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^$', MyApp1.views.index, name='index'),
    re_path(r'^about$', MyApp1.views.index, name='about'),
    re_path(r'^home$', MyApp1.views.index, name='home')
]
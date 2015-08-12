from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
	url(r'books/$', views.books_list),
	url(r'^books/(?P<pk>[0-9]+)/$', views.books_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
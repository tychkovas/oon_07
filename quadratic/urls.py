from django.conf.urls import url

from . import views

app_name = 'quadratic'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^results/$', views.rez_nul, name='rez_nul'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
                  #/?a=1&b=3&c=5  a=(?P<a>[0-9]+)
    #url(r'^results/\?a=(?P<a>[0-9]+)\&b=(?P<b>[0-9]+)\&c=(?P<c>[0-9]+)$', views.quadratic_results, name='results'),
    url(r'^results/a=(?P<a>[0-9]+)/b=(?P<b>[0-9]+)/c=(?P<c>[0-9]+)/$', views.quadratic_results, name='results'),
]
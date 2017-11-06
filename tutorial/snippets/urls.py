from django.conf.urls import url

from snippets.views.fbv import snippet_list, snippet_detail

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet_detail'),
]


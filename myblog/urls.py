# myblog/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv


urlpatterns = [
    # 최상위 주소 설정, 함수 () 형태가 아닌 함수 자체 호출
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^freeboard/$', views_cbv.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),

    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^comments/$', views.comment_list, name='comment_list'),

    url(r'^cbv/new/$', views_cbv.post_new),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete),
]
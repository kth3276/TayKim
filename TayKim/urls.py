from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect, render

urlpatterns = [

    url(r'^$', lambda request: render(request, 'index.html'), name='root'),
    # url(r'^$', lambda r: redirect('myblog:post_list'), name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^myblog/', include('myblog.urls', namespace='myblog')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^cover/', include('cover.urls', namespace='cover')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
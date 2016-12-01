"""slamnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import include, url


from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^channel/1$', views.channel, name='channel'),
    url(r'^activate$', views.activate, name='activate'),
    url(r'^logout$', views.logout, name='logout'),
    #url(r'^edit$', views.edit, name='edit'),
    url(r'^ajax$', views.ajax, name='ajax'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

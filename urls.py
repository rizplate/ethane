"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from tokens import views as tokenViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', tokenViews.token_distribution),

    url(r'^api/token/(?P<symbol>[A-z]+)/$',
        tokenViews.TokenAPIView.as_view(),
        name='token-view'),

    url(r'^api/tokens/$',
        tokenViews.TokensCollectionView.as_view(),
        name='tokens-list-view'),

    url(r'^api/account/$',
        tokenViews.EthereumAccountView.as_view(),
        name='eth-account-view'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

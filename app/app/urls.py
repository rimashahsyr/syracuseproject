"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from Events import views as Events_views
from Profile import views as Profile_views
from Login import views as loginViews
from django.conf import settings


urlpatterns = [
    url(r'^Event/$', Events_views.Event_Creation.as_view()),
    url(r'^$', loginViews.index),
    url(r'^event_creation_post/$', Events_views.event_creation_post),
    url(r"^created_event/(.*)$", Events_views.Created_Event.as_view()),
    url(r"^delete_event/(.*)$", Events_views.Delete_Event.as_view()),
    url(r"^edit_event/(?P<id>\d+)/$", Events_views.Event_Data_Fetch.as_view()),
    url(r"^edit_event_post/(.*)$", Events_views.edit_event_post),
    url(r'^Profile/$', Profile_views.Profile_Creation.as_view()),
    url(r'^profile_creation_post/$', Profile_views.profile_creation_post),
    url(r'^created_profile/(.*)$', Profile_views.Created_Profile.as_view()),
    url(r'^login_post/$', loginViews.login_post), 
    url(r'^login/$', loginViews.index, name='auth-social'),
    url(r'auth-social/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')), # new
    path('admin/', admin.site.urls),

]

from django.urls import path,include, re_path

from . import views


from django.conf import settings
from django.conf.urls.static import static
from django_downloadview import ObjectDownloadView
from .models import *
from django.contrib import admin
from MyPortfolioApp import views
from django.views.static import serve



appapp_name='auctions'
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("about", views.about, name="about"),
    path("project", views.project, name="project"),
    # path("project/<int:id>", views.project_id, name="project_id"),
    path("cactus", views.cactus, name="cactus"),
    path("myforms", views.myforms, name="myforms"),
    path("createtest", views.createtest, name="createtest"),
    path("createport", views.createport, name="createport"),
    path("createexp", views.createexp, name="createexp"),
    path("createedu", views.createedu, name="createedu"),
    path("createcou", views.createcou, name="createcou"),
    path("createskill", views.createskill, name="createskill"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    re_path(r"^download/(?P<path>.*)$", serve,{'document_root':settings.MEDIA_ROOT}),
    
    # path("downloadfile", views.downloadfile, name="downloadfile"),




    # path('motech/', views.motech, name="motech"),
    # path('youtube/', views.youtube, name='youtube'),
    # path('form/', views.uploadForm, name='form'),
    # path('upload/', views.uploadFile, name='upload'),
    # path('files/', views.FileView.as_view(), name='files'),
    # path('pelcon/', views.PelconView.as_view(), name='pelcon'),
    # path('myupload/', views.myUpload, name='myupload'),
    # path('pelconUpload/', views.pelconUpload, name='pelconUpload'),


    path('<slug:category_slug>', views.about, name='resume_by_speciality'),
    path('<slug:category_slug>', views.project, name='portfolio_by_speciality'),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

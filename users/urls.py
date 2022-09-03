from django.urls import path,include
from django.views.generic import TemplateView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',TemplateView.as_view(template_name='login.html')),
    path('login/',login.as_view(),name='login'),
    path('signup/',signup.as_view(),name='signup'),
    path('otp',otp.as_view(),name='otp'),
]+ static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
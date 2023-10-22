from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [path('', views.PostView.as_view()),
               path('titul/', views.TitulView.as_view())] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
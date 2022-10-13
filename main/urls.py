from django.urls import path
from main import views
from main.views import CarView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('login/', views.login, name='login'),
    path('car/', CarView.as_view(), name='car'),
    path('', views.home, name="home"),
    path('car/subaru/', views.subaru),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from core import views as news_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news', news_views.NewsList.as_view(), name='news'),
    path('news/<uuid:guid>/', news_views.NewsDetail.as_view(), name='retrieve-news')
]

from django.urls import path
from . import views

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('home', views.BlogPostListView.as_view(), name='blog_home'),
    path('blog_detail/<int:pk>', views.BlogPostDetail.as_view(), name= 'blog_detail'),
    # path('shop', views.ProductListView.as_view(), name='shop'),
    # path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

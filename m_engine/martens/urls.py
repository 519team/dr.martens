from django.conf.urls import url
from .views import *

urlpatterns = [
    url('blog/', blog, name='blog_posts_url'),
    url('post/<slug>/', post_detail, name='post_detail_url')
]

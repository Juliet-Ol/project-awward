from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from awwardsproject.forms import PostForm
from . import views
from awwardsproject import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('edit-profile', views.editProfile, name='edit-profile'),
    path('post', views.post, name='new-post'),
    path('post', views.PostForm, name='post-form'),
    path('view-post/<int:id>', views.viewPost, name="view-post"),
    path('rate-post/<rating>/post/<int:post_id>/scale/<int:scale>', views.storeRating, name='store-rating')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
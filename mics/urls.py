from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.image_list, name="indexImages"),
    path("search/", views.search_results, name="search_results"),
    path("image/<int:image_id>/", views.image, name="viewImage"),
    path("image/<int:image_id>/comment/", views.add_comment, name="add_comment"),
    path("signup/", views.signup, name="signup"),
    path("create/image/", views.create_image, name="create_image"),
    path("create/category/", views.create_category, name="create_category"),
    path("create/location/", views.create_location, name="create_location"),
    path("create/tag/", views.create_tag, name="create_tag"),
    path("like/<int:image_id>/", views.like_image, name="like_image"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

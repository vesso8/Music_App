from django.urls import path

from exam_web.web.views import show_home, add_album, album_details, edit_album, delete_album, profile_details, \
    delete_profile, create_profile

urlpatterns = (
    path('', show_home, name='home'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),

)
from django.urls import path
from .views import register,user_login,upload_music,music_list,indexView,logout_view

urlpatterns = [
       path('',indexView, name='home'),

    path('register/',register, name='register'),
    
    path('login/', user_login, name='login'),
     path('upload/', upload_music, name='upload'),
    #  path('public/', public_music_list, name='public_music_list'),
   #   path('private/', private_music_list, name='private_music_list'),
    # # other URL patterns
         path('list/', music_list, name='list'),
         path('logout/', logout_view, name='logout'),
]

from . import views
from django.urls import path

urlpatterns = [

    
    path("index/",views.movieList,name='index'),
    path('create/',views.createMovie,name='create'),
    path('details/<int:show_id>/',views.movieDetails,name='detail'),
    path('movie_details/<int:show_id>/',views.movieEdit,name='movie_edit'),
    path('movie_delete/<int:show_id>/',views.movieDelete,name='delete'),
    path("register/",views.register,name='register'),
    path("",views.userLogin,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('createuser/',views.userCreate,name='createuser'),
    path('userdetails/<int:id>/',views.userDetails,name='user_details'),
]
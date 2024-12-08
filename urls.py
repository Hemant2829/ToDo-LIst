from django.contrib import admin
from django.urls import path
from todoapp import views
from todoapp.views import signup,loginn,todo,edit_todo,delete_todo,signout

urlpatterns = [
    path('admin/',admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginn,name='login'),
    path('todopage/',views.todo,name='todopage'),
    path('edit_todo/<int:srno>',views.edit_todo,name="edit_todo"),
    path('delete_todo/<int:srno>',views.delete_todo,name="delete_todo"),
    path("signout/",views.signout,name='signout')

    
]

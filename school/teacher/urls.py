
from django.contrib import admin
from django.urls import include, path
from teacher import views

urlpatterns = [
    path('admin_panel/add_user',views.add_user, name='add_user'),
    path('admin_panel/view_user',views.view_user, name='view_user'),
    path('admin_panel/remove_user/<int:id>', views.remove_user, name='remove_user'),
    path('admin_panel/edit_user/<int:id>',views.edit_user, name='edit_user'),
    path('admin_panel/edit_user/update_user/<int:id>',views.update_user, name='update_user'),

]

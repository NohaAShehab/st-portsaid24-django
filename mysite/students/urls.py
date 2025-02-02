# add all students urls to this file


from django.urls import path
from students.views import itiview
from students.views import (home, profile,
    all_students, std_profile, std_list, index, show, delete, create,
                            edit, create_via_form , create_via_model_form)
urlpatterns = [
    path('iti', itiview),
    path('home', home),
    path('profile/<username>', profile),
    path('stds', all_students),
    path('stds/<int:id>',std_profile,name='std_profile'),
    path('', std_list, name='std_list'),
    path('index', index,name='students.index'),
    path('index/<int:id>', show, name='students.show'),
    path('<int:id>/delete', delete, name='students.delete'),
    path('create', create, name='students.create'),
    path('<int:id>/edit', edit, name='students.edit'),
    path('forms/create',create_via_form, name='students.forms' ),
    path('forms/modelcreate', create_via_model_form, name='students.modelforms' ),
]


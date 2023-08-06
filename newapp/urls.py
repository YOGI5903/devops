from django.urls import path
from .import views
urlpatterns=[
    path("index",views.index,name="index"),
    path("add/",views.add,name="add"),
    path("add/addrecord/",views.addrecord,name="addrecord"),
    #path("delete/<int:id>",views.delete,name="delete"),
    #path("delete/<i",views.delete,name="delete")
    path("todo",views.todo,name="todo"),
    path("add1",views.add_list,name="add"),
    path("delete/<int:id>",views.delete_list,name="delete"),
    path("deleteall",views.delete_all,name="deleteall"),

]
from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path("list/", TodoList.as_view(), name="list"),       # views.pyのTodoListへの指定
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),   # views.pyのTodoDetailへの指定 <int:pk>でprimarykeyの指定をする
    path("create/", TodoCreate.as_view(), name="create"),    # views.pyのTodoCreateへの指定
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),    # views.pyのTodoDeleteへの指定
    path("update/<int:pk>", TodoUpdate.as_view(), name="update")
]

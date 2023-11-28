from django.urls import path


urlpatterns = [
    path("", index.as_view(), name="index")
]

app_name = "todo"

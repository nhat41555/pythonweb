from django.urls import path
from patientweb import views
urlpatterns = [
    path("",views.home,name="home"),
    # path('<int:id>/', views.view()),
]
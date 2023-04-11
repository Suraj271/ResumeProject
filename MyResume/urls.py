from django.urls import path
from . import views

urlpatterns = [

    path('', views.aboutme_view , name = "aboutme"),
    path('skills/' , views.skills_view , name = "skills"),
    path('project/' , views.project_view , name= "project"),
    path('qualification/' , views.qualification_view , name = "qualification"),
    path('experience/' , views.experience_view , name = "experience"),
    path('contactme/' , views.contact_view , name = "contactme")

]
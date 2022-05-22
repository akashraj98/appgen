from django.urls import path

from create_proj.views import ProjectChoicesView, ProjectCreateView

urlpatterns = [
    path('choices/', ProjectChoicesView.as_view(), name="project-choices"),
    path('create/', ProjectCreateView.as_view(), name="project-create"),
]

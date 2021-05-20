from django.urls import path

from . import views

# we specify app_name so Django knows which app view to create for a url when using the {% url %} template tag
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name="detail"),
    path('results/<int:question_id>/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

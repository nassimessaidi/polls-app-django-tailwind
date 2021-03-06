from django.urls import path
from . import views

# we specify app_name so Django knows which app view to create for a url when using the {% url %} template tag
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('admin/', views.joke, name="nice-try"),
]


""" Old Way
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name="detail"),
    path('results/<int:question_id>/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
"""

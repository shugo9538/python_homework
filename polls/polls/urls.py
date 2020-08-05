from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('/polls/5/', views.detail, name='detail'),
    # path('/polls/5/results/', views.results, name='results'),
    # path('/polls/5/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
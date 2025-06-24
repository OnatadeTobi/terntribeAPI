# --- causes/urls.py ---
from django.urls import path
from .views import CauseListCreateView, CauseDetailView, ContributeToCause

urlpatterns = [
    path('causes/', CauseListCreateView.as_view(), name='cause-list-create'),
    path('causes/<int:pk>/', CauseDetailView.as_view(), name='cause-detail'),
    path('causes/<int:pk>/contribute/', ContributeToCause.as_view(), name='contribute'),
]

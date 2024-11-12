from django.urls import path
from .views import DiaryEntryListCreateView, DiaryEntryRetrieveView, DiaryEntryUpdateView, DiaryEntryDestroyView,generating_code

urlpatterns = [
    path('entries/', DiaryEntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', DiaryEntryRetrieveView.as_view(), name='entry-retrieve'), 
    path('entries/update/<int:pk>/', DiaryEntryUpdateView.as_view(), name='entry-update'),  
    path('entries/delete/<int:pk>/', DiaryEntryDestroyView.as_view(), name='entry-destroy'), 
    
    #redis part
    path('generate-code/', generating_code, name='generate_code') 
]

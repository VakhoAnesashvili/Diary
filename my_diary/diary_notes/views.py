from rest_framework import generics, permissions
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer


# checking diary owner
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


# diary entries list and create view methods "GET" "POST"
class DiaryEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# diary entries retrive view vith pk "GET"
class DiaryEntryRetrieveView(generics.RetrieveAPIView):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)
    

# diary entries update view vith pk "PUT"
class DiaryEntryUpdateView(generics.UpdateAPIView):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)
    

# diary entries delete view vith pk "DELETE"
class DiaryEntryDestroyView(generics.DestroyAPIView):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)
    
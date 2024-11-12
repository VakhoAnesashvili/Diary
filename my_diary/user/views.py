from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics, permissions



# user registration with APIView
class RegisterView(APIView):
    def post(self, request):
        # checking data validation from RegisterSerializer
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# creating/generate JWT token 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # create token
        token = super().get_token(user)
        # insert token
        token['username'] = user.username
        return token
    

# user login with TokenObtainPairView
class LoginView(TokenObtainPairView):
    # serializer using for this API
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # choose JWT token for user
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({
                "message": "Login successful",
                "data": response.data
            }, status=status.HTTP_200_OK)
        return response


# logout view
class LogoutView(APIView):
    # only authorized users could use this
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # give users refresh token which is needed for logout
            refresh_token = request.data['refresh']
            # variable for save refreshtoken from JWT
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# user profile GET method
class UserProfileRetrieveView(generics.RetrieveAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# PUT method 
class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

    # DELETE method
class UserProfileDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Employer
from .serializers import Sign_Up_Seri, Login_Seri,Employer_Seri,User_Seri
from .permissions import Is_Right
from rest_framework.permissions import IsAuthenticated, AllowAny



class Sign_Up_View( generics.CreateAPIView):
    serializer_class= Sign_Up_Seri
    permission_classes= [AllowAny]


class Login_View(generics.GenericAPIView):
    serializer_class= Login_Seri
    permission_classes= [AllowAny]
    def post(self, request):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)

        return Response( serializer.validated_data)


    
class Profile_View(generics.RetrieveAPIView):
    serializer_class= User_Seri
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user    


class Employer_View(viewsets.ModelViewSet):
    serializer_class = Employer_Seri
    permission_classes = [IsAuthenticated, Is_Right]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class All_Employers_View(generics.ListAPIView):
    serializer_class= Employer_Seri
    permission_classes= [AllowAny]
    queryset= Employer.objects.all()        


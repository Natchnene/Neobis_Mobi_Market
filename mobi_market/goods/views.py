from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from .serializers import CardProductShortSerializer, CardProductLongSerializer
from .models import CardProduct


class CardProductLongCreateAPIView(viewsets.ModelViewSet):
    serializer_class = CardProductLongSerializer
    queryset = CardProduct.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.is_verified:
            return Response({'message': 'You need to confirm your phone number.'})
        else:
            request.data['user'] = user.id
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        request.data['user'] = user.id
        instance = get_object_or_404(CardProduct, pk=kwargs.get('pk'), user=user)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardProductShortAllListAPIView(generics.ListAPIView):
    serializer_class = CardProductShortSerializer
    queryset = CardProduct.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CardProductShortUserListAPIView(generics.ListAPIView):
    serializer_class = CardProductShortSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return CardProduct.objects.filter(user_id=user.id)


class CardProductShortLikedListAPIView(generics.ListAPIView):
    serializer_class = CardProductShortSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return user.likes.all()


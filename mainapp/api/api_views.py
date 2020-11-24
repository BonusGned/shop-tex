from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer, SmartphoneSerializer
from ..models import Category, Smartphone


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     price, title = self.request.query_params.get('price'), self.request.query_params.get('title')
    #     search_params = {'price__iexact': price, 'title__iexact': title}
    #     return qs.filter(price__iexact=price)

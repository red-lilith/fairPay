from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

from .models import Order
from .serializers import OrderSerializer


@api_view(['GET'])
def get_orders(request):
    start_date = request.GET.get('start_date', None)
    if not start_date:
        return Response([])
    start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
    end_date = request.GET.get('end_date', None)
    if end_date:
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()
    orders = Order.get_orders(start_date, end_date)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def delete_orders(request):
    start_date = request.data.start_date
    end_date = request.data.end_date
    orders_deleted = Order.delete_orders(start_date, end_date)
    return Response({
        'ordersDeleted': orders_deleted
    })

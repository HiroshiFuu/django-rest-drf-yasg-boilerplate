from ..base_views import *

from django.core.exceptions import ObjectDoesNotExist

from ..models import Shape
from ..utils import get_model_from_shape_type, get_serializer_from_model
from .serializers import *


CUR_VERSION = 'v1'
SHAPE_TYPE_PATH_PARAMETER = openapi.Parameter('shape_type', openapi.IN_PATH, required=True, description='Shape Type', type=openapi.TYPE_STRING)
SHAPE_ID_PATH_PARAMETER = openapi.Parameter('shape_id', openapi.IN_PATH, required=True, description='Shape ID', type=openapi.TYPE_STRING)


class ListShapeByTypeView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='List Shapes by Type', responses={200: openapi.Response('')}, tags=['Shape'])
    def get(self, request, shape_type=None):
        if shape_model := get_model_from_shape_type(shape_type):
            shape_model_serializer = get_serializer_from_model(shape_model)
            queryset = shape_model.objects.all()
            serializer = shape_model_serializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape Type not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)


class ReadDeleteShapeView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Retrieve Shape by ID', responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def get(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            instance = shape_model.objects.get(id=shape_id)
            shape_model_serializer = get_serializer_from_model(shape_model)
            serializer = shape_model_serializer(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Remove Shape by ID', responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def delete(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateShapeView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Create a Shape', request_body=ShapeTypeSerializer, responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def post(self, request):
        for serializer in [TriangleSerializer, RectangleSerializer, SquareSerializer, DiamondSerializer]:
            shape_serializer = serializer(data=request.data)
            if shape_serializer.is_valid():
                shape_serializer.save()
                return Response(data=shape_serializer.data, status=status.HTTP_200_OK)
        res_data = copy.deepcopy(RESPONSE_400_DATA)
        res_data['message'] = 'Data inputed is NOT correct.'
        return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Update a Shape', request_body=ShapeIDSerializer, responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def put(self, request):
        try:
            data = request.data
            shape_id = data['shape_id']
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            shape_model_serializer = get_serializer_from_model(shape_model)
            data['shape_type'] = shape_instance.shape_type
            instance = shape_model.objects.get(id=shape_id)
            serializer = shape_model_serializer(instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            print(serializer.errors)
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Data inputed is NOT correct.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Update a Shape', request_body=ShapeIDSerializer, responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def patch(self, request):
        try:
            data = request.data
            shape_id = data['shape_id']
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            shape_model_serializer = get_serializer_from_model(shape_model)
            data['shape_type'] = shape_instance.shape_type
            instance = shape_model.objects.get(id=shape_id)
            serializer = shape_model_serializer(instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            print(serializer.errors)
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Data inputed is NOT correct.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)


class CalculateShapeAreaPerimeterView(APIView):

    @authentication_classes([TokenAuthentication])
    @swagger_auto_schema(operation_description='Shape calculations by ID', responses={200: openapi.Response('')}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @check_token_auth()
    def get(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            instance = shape_model.objects.get(id=shape_id)
            serializer = ShapeAreaPerimeterSerializer(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            res_data = copy.deepcopy(RESPONSE_400_DATA)
            res_data['message'] = 'Shape not found.'
            return Response(data=res_data, status=status.HTTP_400_BAD_REQUEST)


# Token 9ac22bd1b3a5bc48032fe3f4ddda5a933c432c94
test_data = {
  "shape_type": "triangle",
  "width": 2,
  "height": 3
}
test_data = {
  "shape_id": 3,
  "width": 3,
  "height": 4
}

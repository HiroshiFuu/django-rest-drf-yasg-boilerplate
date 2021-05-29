from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_settings

from core.yasg_inspector import ExampleSerializerInspector


class NameAsOperationIDAutoSchema(SwaggerAutoSchema):
    def get_operation_id(self, operation_keys):
        operation_id = super(NameAsOperationIDAutoSchema, self).get_operation_id(operation_keys)
        # print(operation_id, operation_keys)
        return operation_id


class SwaggerExampleAutoSchema(SwaggerAutoSchema):

    field_inspectors = [
        ExampleSerializerInspector,
    ] + swagger_settings.DEFAULT_FIELD_INSPECTORS
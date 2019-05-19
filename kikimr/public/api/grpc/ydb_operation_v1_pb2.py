# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_operation_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_operation_v1.proto',
  package='Ydb.Operation.V1',
  syntax='proto3',
  serialized_pb=_b('\n-kikimr/public/api/grpc/ydb_operation_v1.proto\x12\x10Ydb.Operation.V1\x1a,kikimr/public/api/protos/ydb_operation.proto2m\n\x10OperationService\x12Y\n\x0cGetOperation\x12#.Ydb.Operations.GetOperationRequest\x1a$.Ydb.Operations.GetOperationResponseB\x1d\n\x1b\x63om.yandex.ydb.operation.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.yandex.ydb.operation.v1'))

_OPERATIONSERVICE = _descriptor.ServiceDescriptor(
  name='OperationService',
  full_name='Ydb.Operation.V1.OperationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=113,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOperation',
    full_name='Ydb.Operation.V1.OperationService.GetOperation',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._GETOPERATIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._GETOPERATIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OPERATIONSERVICE)

DESCRIPTOR.services_by_name['OperationService'] = _OPERATIONSERVICE

# @@protoc_insertion_point(module_scope)
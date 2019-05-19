# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_experimental_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_experimental_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_experimental_v1.proto',
  package='Ydb.Experimental.V1',
  syntax='proto3',
  serialized_pb=_b('\n6kikimr/public/api/grpc/draft/ydb_experimental_v1.proto\x12\x13Ydb.Experimental.V1\x1a/kikimr/public/api/protos/ydb_experimental.proto2\xab\x03\n\x13\x45xperimentalService\x12W\n\nUploadRows\x12#.Ydb.Experimental.UploadRowsRequest\x1a$.Ydb.Experimental.UploadRowsResponse\x12Z\n\x0bReadColumns\x12$.Ydb.Experimental.ReadColumnsRequest\x1a%.Ydb.Experimental.ReadColumnsResponse\x12l\n\x11GetShardLocations\x12*.Ydb.Experimental.GetShardLocationsRequest\x1a+.Ydb.Experimental.GetShardLocationsResponse\x12q\n\x12\x45xecuteStreamQuery\x12+.Ydb.Experimental.ExecuteStreamQueryRequest\x1a,.Ydb.Experimental.ExecuteStreamQueryResponse0\x01\x42 \n\x1e\x63om.yandex.ydb.experimental.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.yandex.ydb.experimental.v1'))

_EXPERIMENTALSERVICE = _descriptor.ServiceDescriptor(
  name='ExperimentalService',
  full_name='Ydb.Experimental.V1.ExperimentalService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=129,
  serialized_end=556,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadRows',
    full_name='Ydb.Experimental.V1.ExperimentalService.UploadRows',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._UPLOADROWSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._UPLOADROWSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadColumns',
    full_name='Ydb.Experimental.V1.ExperimentalService.ReadColumns',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._READCOLUMNSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._READCOLUMNSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShardLocations',
    full_name='Ydb.Experimental.V1.ExperimentalService.GetShardLocations',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._GETSHARDLOCATIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._GETSHARDLOCATIONSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteStreamQuery',
    full_name='Ydb.Experimental.V1.ExperimentalService.ExecuteStreamQuery',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._EXECUTESTREAMQUERYREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__experimental__pb2._EXECUTESTREAMQUERYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXPERIMENTALSERVICE)

DESCRIPTOR.services_by_name['ExperimentalService'] = _EXPERIMENTALSERVICE

# @@protoc_insertion_point(module_scope)
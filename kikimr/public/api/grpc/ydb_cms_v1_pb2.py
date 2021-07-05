# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_cms_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_cms_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_cms_v1.proto',
  package='Ydb.Cms.V1',
  syntax='proto3',
  serialized_options=b'\n\025com.yandex.ydb.cms.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'kikimr/public/api/grpc/ydb_cms_v1.proto\x12\nYdb.Cms.V1\x1a&kikimr/public/api/protos/ydb_cms.proto2\x9c\x04\n\nCmsService\x12Q\n\x0e\x43reateDatabase\x12\x1e.Ydb.Cms.CreateDatabaseRequest\x1a\x1f.Ydb.Cms.CreateDatabaseResponse\x12Z\n\x11GetDatabaseStatus\x12!.Ydb.Cms.GetDatabaseStatusRequest\x1a\".Ydb.Cms.GetDatabaseStatusResponse\x12N\n\rAlterDatabase\x12\x1d.Ydb.Cms.AlterDatabaseRequest\x1a\x1e.Ydb.Cms.AlterDatabaseResponse\x12N\n\rListDatabases\x12\x1d.Ydb.Cms.ListDatabasesRequest\x1a\x1e.Ydb.Cms.ListDatabasesResponse\x12Q\n\x0eRemoveDatabase\x12\x1e.Ydb.Cms.RemoveDatabaseRequest\x1a\x1f.Ydb.Cms.RemoveDatabaseResponse\x12l\n\x17\x44\x65scribeDatabaseOptions\x12\'.Ydb.Cms.DescribeDatabaseOptionsRequest\x1a(.Ydb.Cms.DescribeDatabaseOptionsResponseB\x17\n\x15\x63om.yandex.ydb.cms.v1b\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_CMSSERVICE = _descriptor.ServiceDescriptor(
  name='CmsService',
  full_name='Ydb.Cms.V1.CmsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=96,
  serialized_end=636,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateDatabase',
    full_name='Ydb.Cms.V1.CmsService.CreateDatabase',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._CREATEDATABASEREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._CREATEDATABASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatabaseStatus',
    full_name='Ydb.Cms.V1.CmsService.GetDatabaseStatus',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._GETDATABASESTATUSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._GETDATABASESTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AlterDatabase',
    full_name='Ydb.Cms.V1.CmsService.AlterDatabase',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._ALTERDATABASEREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._ALTERDATABASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListDatabases',
    full_name='Ydb.Cms.V1.CmsService.ListDatabases',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._LISTDATABASESREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._LISTDATABASESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveDatabase',
    full_name='Ydb.Cms.V1.CmsService.RemoveDatabase',
    index=4,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._REMOVEDATABASEREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._REMOVEDATABASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeDatabaseOptions',
    full_name='Ydb.Cms.V1.CmsService.DescribeDatabaseOptions',
    index=5,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._DESCRIBEDATABASEOPTIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__cms__pb2._DESCRIBEDATABASEOPTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CMSSERVICE)

DESCRIPTOR.services_by_name['CmsService'] = _CMSSERVICE

# @@protoc_insertion_point(module_scope)

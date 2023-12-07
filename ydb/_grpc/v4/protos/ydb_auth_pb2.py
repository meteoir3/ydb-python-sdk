# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protos/ydb_auth.proto\x12\x08Ydb.Auth\x1a\x1aprotos/ydb_operation.proto\"i\n\x0cLoginRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"=\n\rLoginResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x1c\n\x0bLoginResult\x12\r\n\x05token\x18\x01 \x01(\tBQ\n\x13tech.ydb.proto.authZ7github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Auth\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ydb_auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023tech.ydb.proto.authZ7github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Auth\370\001\001'
  _LOGINREQUEST._serialized_start=63
  _LOGINREQUEST._serialized_end=168
  _LOGINRESPONSE._serialized_start=170
  _LOGINRESPONSE._serialized_end=231
  _LOGINRESULT._serialized_start=233
  _LOGINRESULT._serialized_end=261
# @@protoc_insertion_point(module_scope)

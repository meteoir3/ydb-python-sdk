# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_federation_discovery.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%protos/ydb_federation_discovery.proto\x12\x17Ydb.FederationDiscovery\x1a\x1aprotos/ydb_operation.proto\"\xf9\x01\n\x0c\x44\x61tabaseInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12<\n\x06status\x18\x06 \x01(\x0e\x32,.Ydb.FederationDiscovery.DatabaseInfo.Status\x12\x0e\n\x06weight\x18\x07 \x01(\x03\"O\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\r\n\tREAD_ONLY\x10\x02\x12\x0f\n\x0bUNAVAILABLE\x10\x03\" \n\x1eListFederationDatabasesRequest\"O\n\x1fListFederationDatabasesResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x9b\x01\n\x1dListFederationDatabasesResult\x12\x1e\n\x16\x63ontrol_plane_endpoint\x18\x01 \x01(\t\x12\x43\n\x14\x66\x65\x64\x65ration_databases\x18\x02 \x03(\x0b\x32%.Ydb.FederationDiscovery.DatabaseInfo\x12\x15\n\rself_location\x18\x03 \x01(\tB\x8b\x01\n#tech.ydb.proto.federation.discoveryB\x19\x46\x65\x64\x65rationDiscoveryProtosZFgithub.com/ydb-platform/ydb-go-genproto/protos/Ydb_FederationDiscovery\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ydb_federation_discovery_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#tech.ydb.proto.federation.discoveryB\031FederationDiscoveryProtosZFgithub.com/ydb-platform/ydb-go-genproto/protos/Ydb_FederationDiscovery\370\001\001'
  _DATABASEINFO._serialized_start=95
  _DATABASEINFO._serialized_end=344
  _DATABASEINFO_STATUS._serialized_start=265
  _DATABASEINFO_STATUS._serialized_end=344
  _LISTFEDERATIONDATABASESREQUEST._serialized_start=346
  _LISTFEDERATIONDATABASESREQUEST._serialized_end=378
  _LISTFEDERATIONDATABASESRESPONSE._serialized_start=380
  _LISTFEDERATIONDATABASESRESPONSE._serialized_end=459
  _LISTFEDERATIONDATABASESRESULT._serialized_start=462
  _LISTFEDERATIONDATABASESRESULT._serialized_end=617
# @@protoc_insertion_point(module_scope)

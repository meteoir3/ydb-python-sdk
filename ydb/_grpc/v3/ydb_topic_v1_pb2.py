# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_topic_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v3.protos import ydb_topic_pb2 as protos_dot_ydb__topic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb_topic_v1.proto',
  package='Ydb.Topic.V1',
  syntax='proto3',
  serialized_options=b'\n\027tech.ydb.proto.topic.v1Z4github.com/ydb-platform/ydb-go-genproto/Ydb_Topic_V1\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12ydb_topic_v1.proto\x12\x0cYdb.Topic.V1\x1a\x16protos/ydb_topic.proto2\xbc\x05\n\x0cTopicService\x12\x65\n\x0bStreamWrite\x12(.Ydb.Topic.StreamWriteMessage.FromClient\x1a(.Ydb.Topic.StreamWriteMessage.FromServer(\x01\x30\x01\x12\x62\n\nStreamRead\x12\'.Ydb.Topic.StreamReadMessage.FromClient\x1a\'.Ydb.Topic.StreamReadMessage.FromServer(\x01\x30\x01\x12O\n\x0c\x43ommitOffset\x12\x1e.Ydb.Topic.CommitOffsetRequest\x1a\x1f.Ydb.Topic.CommitOffsetResponse\x12L\n\x0b\x43reateTopic\x12\x1d.Ydb.Topic.CreateTopicRequest\x1a\x1e.Ydb.Topic.CreateTopicResponse\x12R\n\rDescribeTopic\x12\x1f.Ydb.Topic.DescribeTopicRequest\x1a .Ydb.Topic.DescribeTopicResponse\x12[\n\x10\x44\x65scribeConsumer\x12\".Ydb.Topic.DescribeConsumerRequest\x1a#.Ydb.Topic.DescribeConsumerResponse\x12I\n\nAlterTopic\x12\x1c.Ydb.Topic.AlterTopicRequest\x1a\x1d.Ydb.Topic.AlterTopicResponse\x12\x46\n\tDropTopic\x12\x1b.Ydb.Topic.DropTopicRequest\x1a\x1c.Ydb.Topic.DropTopicResponseBR\n\x17tech.ydb.proto.topic.v1Z4github.com/ydb-platform/ydb-go-genproto/Ydb_Topic_V1\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[protos_dot_ydb__topic__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_TOPICSERVICE = _descriptor.ServiceDescriptor(
  name='TopicService',
  full_name='Ydb.Topic.V1.TopicService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=61,
  serialized_end=761,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamWrite',
    full_name='Ydb.Topic.V1.TopicService.StreamWrite',
    index=0,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._STREAMWRITEMESSAGE_FROMCLIENT,
    output_type=protos_dot_ydb__topic__pb2._STREAMWRITEMESSAGE_FROMSERVER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamRead',
    full_name='Ydb.Topic.V1.TopicService.StreamRead',
    index=1,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._STREAMREADMESSAGE_FROMCLIENT,
    output_type=protos_dot_ydb__topic__pb2._STREAMREADMESSAGE_FROMSERVER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CommitOffset',
    full_name='Ydb.Topic.V1.TopicService.CommitOffset',
    index=2,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._COMMITOFFSETREQUEST,
    output_type=protos_dot_ydb__topic__pb2._COMMITOFFSETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTopic',
    full_name='Ydb.Topic.V1.TopicService.CreateTopic',
    index=3,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._CREATETOPICREQUEST,
    output_type=protos_dot_ydb__topic__pb2._CREATETOPICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeTopic',
    full_name='Ydb.Topic.V1.TopicService.DescribeTopic',
    index=4,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._DESCRIBETOPICREQUEST,
    output_type=protos_dot_ydb__topic__pb2._DESCRIBETOPICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeConsumer',
    full_name='Ydb.Topic.V1.TopicService.DescribeConsumer',
    index=5,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._DESCRIBECONSUMERREQUEST,
    output_type=protos_dot_ydb__topic__pb2._DESCRIBECONSUMERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AlterTopic',
    full_name='Ydb.Topic.V1.TopicService.AlterTopic',
    index=6,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._ALTERTOPICREQUEST,
    output_type=protos_dot_ydb__topic__pb2._ALTERTOPICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DropTopic',
    full_name='Ydb.Topic.V1.TopicService.DropTopic',
    index=7,
    containing_service=None,
    input_type=protos_dot_ydb__topic__pb2._DROPTOPICREQUEST,
    output_type=protos_dot_ydb__topic__pb2._DROPTOPICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOPICSERVICE)

DESCRIPTOR.services_by_name['TopicService'] = _TOPICSERVICE

# @@protoc_insertion_point(module_scope)

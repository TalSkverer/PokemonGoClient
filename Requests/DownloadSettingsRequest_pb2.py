# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Requests/DownloadSettingsRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Requests/DownloadSettingsRequest.proto',
  package='Protos.Requests',
  syntax='proto3',
  serialized_pb=_b('\n&Requests/DownloadSettingsRequest.proto\x12\x0fProtos.Requests\"\'\n\x17\x44ownloadSettingsRequest\x12\x0c\n\x04hash\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADSETTINGSREQUEST = _descriptor.Descriptor(
  name='DownloadSettingsRequest',
  full_name='Protos.Requests.DownloadSettingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='Protos.Requests.DownloadSettingsRequest.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['DownloadSettingsRequest'] = _DOWNLOADSETTINGSREQUEST

DownloadSettingsRequest = _reflection.GeneratedProtocolMessageType('DownloadSettingsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSREQUEST,
  __module__ = 'Requests.DownloadSettingsRequest_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Requests.DownloadSettingsRequest)
  ))
_sym_db.RegisterMessage(DownloadSettingsRequest)


# @@protoc_insertion_point(module_scope)
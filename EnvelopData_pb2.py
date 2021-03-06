# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EnvelopData.proto

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
  name='EnvelopData.proto',
  package='Protos',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x45nvelopData.proto\x12\x06Protos\"Z\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12#\n\x05token\x18\x02 \x01(\x0b\x32\x14.Protos.AuthInfo.JWT\x1a\x17\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\"E\n\nAuthTicket\x12\r\n\x05token\x18\x01 \x01(\x0c\x12\x1b\n\x13\x65xpire_timestamp_ms\x18\x02 \x01(\x04\x12\x0b\n\x03sig\x18\x03 \x01(\x0c\"g\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12+\n\x08unknown2\x18\x02 \x01(\x0b\x32\x19.Protos.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='Protos.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='Protos.AuthInfo.JWT.contents', index=0,
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
  serialized_start=96,
  serialized_end=119,
)

_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='Protos.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='Protos.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='Protos.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=119,
)


_AUTHTICKET = _descriptor.Descriptor(
  name='AuthTicket',
  full_name='Protos.AuthTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='Protos.AuthTicket.token', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_timestamp_ms', full_name='Protos.AuthTicket.expire_timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='Protos.AuthTicket.sig', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=121,
  serialized_end=190,
)


_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='Protos.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='Protos.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=267,
  serialized_end=295,
)

_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='Protos.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='Protos.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='Protos.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=295,
)

_AUTHINFO_JWT.containing_type = _AUTHINFO
_AUTHINFO.fields_by_name['token'].message_type = _AUTHINFO_JWT
_UNKNOWN6_UNKNOWN2.containing_type = _UNKNOWN6
_UNKNOWN6.fields_by_name['unknown2'].message_type = _UNKNOWN6_UNKNOWN2
DESCRIPTOR.message_types_by_name['AuthInfo'] = _AUTHINFO
DESCRIPTOR.message_types_by_name['AuthTicket'] = _AUTHTICKET
DESCRIPTOR.message_types_by_name['Unknown6'] = _UNKNOWN6

AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

  JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
    DESCRIPTOR = _AUTHINFO_JWT,
    __module__ = 'EnvelopData_pb2'
    # @@protoc_insertion_point(class_scope:Protos.AuthInfo.JWT)
    ))
  ,
  DESCRIPTOR = _AUTHINFO,
  __module__ = 'EnvelopData_pb2'
  # @@protoc_insertion_point(class_scope:Protos.AuthInfo)
  ))
_sym_db.RegisterMessage(AuthInfo)
_sym_db.RegisterMessage(AuthInfo.JWT)

AuthTicket = _reflection.GeneratedProtocolMessageType('AuthTicket', (_message.Message,), dict(
  DESCRIPTOR = _AUTHTICKET,
  __module__ = 'EnvelopData_pb2'
  # @@protoc_insertion_point(class_scope:Protos.AuthTicket)
  ))
_sym_db.RegisterMessage(AuthTicket)

Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

  Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
    DESCRIPTOR = _UNKNOWN6_UNKNOWN2,
    __module__ = 'EnvelopData_pb2'
    # @@protoc_insertion_point(class_scope:Protos.Unknown6.Unknown2)
    ))
  ,
  DESCRIPTOR = _UNKNOWN6,
  __module__ = 'EnvelopData_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Unknown6)
  ))
_sym_db.RegisterMessage(Unknown6)
_sym_db.RegisterMessage(Unknown6.Unknown2)


# @@protoc_insertion_point(module_scope)

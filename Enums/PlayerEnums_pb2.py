# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Enums/PlayerEnums.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Enums/PlayerEnums.proto',
  package='Protos.Enums',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x45nums/PlayerEnums.proto\x12\x0cProtos.Enums*7\n\tTeamColor\x12\x0b\n\x07NEUTRAL\x10\x00\x12\x08\n\x04\x42LUE\x10\x01\x12\x07\n\x03RED\x10\x02\x12\n\n\x06YELLOW\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TEAMCOLOR = _descriptor.EnumDescriptor(
  name='TeamColor',
  full_name='Protos.Enums.TeamColor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEUTRAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=41,
  serialized_end=96,
)
_sym_db.RegisterEnumDescriptor(_TEAMCOLOR)

TeamColor = enum_type_wrapper.EnumTypeWrapper(_TEAMCOLOR)
NEUTRAL = 0
BLUE = 1
RED = 2
YELLOW = 3


DESCRIPTOR.enum_types_by_name['TeamColor'] = _TEAMCOLOR


# @@protoc_insertion_point(module_scope)

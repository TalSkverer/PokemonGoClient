# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/AvatarDetails.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import PlayerEnums_pb2 as Enums_dot_PlayerEnums__pb2

from Enums.PlayerEnums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Player/AvatarDetails.proto',
  package='Protos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x1aPlayer/AvatarDetails.proto\x12\rProtos.Player\x1a\x17\x45nums/PlayerEnums.proto\"\xab\x01\n\rAvatarDetails\x12\x0c\n\x04skin\x18\x02 \x01(\x05\x12\x0c\n\x04hair\x18\x03 \x01(\x05\x12\r\n\x05shirt\x18\x04 \x01(\x05\x12\r\n\x05pants\x18\x05 \x01(\x05\x12\x0b\n\x03hat\x18\x06 \x01(\x05\x12\r\n\x05shoes\x18\x07 \x01(\x05\x12$\n\x06gender\x18\x08 \x01(\x0e\x32\x14.Protos.Enums.Gender\x12\x0c\n\x04\x65yes\x18\t \x01(\x05\x12\x10\n\x08\x62\x61\x63kpack\x18\n \x01(\x05P\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_PlayerEnums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AVATARDETAILS = _descriptor.Descriptor(
  name='AvatarDetails',
  full_name='Protos.Player.AvatarDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skin', full_name='Protos.Player.AvatarDetails.skin', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hair', full_name='Protos.Player.AvatarDetails.hair', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shirt', full_name='Protos.Player.AvatarDetails.shirt', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pants', full_name='Protos.Player.AvatarDetails.pants', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hat', full_name='Protos.Player.AvatarDetails.hat', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='Protos.Player.AvatarDetails.shoes', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='Protos.Player.AvatarDetails.gender', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eyes', full_name='Protos.Player.AvatarDetails.eyes', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backpack', full_name='Protos.Player.AvatarDetails.backpack', index=8,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=71,
  serialized_end=242,
)

_AVATARDETAILS.fields_by_name['gender'].enum_type = Enums_dot_PlayerEnums__pb2._GENDER
DESCRIPTOR.message_types_by_name['AvatarDetails'] = _AVATARDETAILS

AvatarDetails = _reflection.GeneratedProtocolMessageType('AvatarDetails', (_message.Message,), dict(
  DESCRIPTOR = _AVATARDETAILS,
  __module__ = 'Player.AvatarDetails_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Player.AvatarDetails)
  ))
_sym_db.RegisterMessage(AvatarDetails)


# @@protoc_insertion_point(module_scope)

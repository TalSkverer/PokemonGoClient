# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Responses/GetPlayerResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Player import LocalPlayer_pb2 as Player_dot_LocalPlayer__pb2
Player_dot_AvatarDetails__pb2 = Player_dot_LocalPlayer__pb2.Player_dot_AvatarDetails__pb2
Enums_dot_PlayerEnums__pb2 = Player_dot_LocalPlayer__pb2.Enums_dot_PlayerEnums__pb2
Player_dot_DailyBonus__pb2 = Player_dot_LocalPlayer__pb2.Player_dot_DailyBonus__pb2
Player_dot_EquippedBadge__pb2 = Player_dot_LocalPlayer__pb2.Player_dot_EquippedBadge__pb2
Enums_dot_PlayerEnums__pb2 = Player_dot_LocalPlayer__pb2.Enums_dot_PlayerEnums__pb2
Player_dot_ContactSettings__pb2 = Player_dot_LocalPlayer__pb2.Player_dot_ContactSettings__pb2
Player_dot_Currency__pb2 = Player_dot_LocalPlayer__pb2.Player_dot_Currency__pb2

from Player.LocalPlayer_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Responses/GetPlayerResponse.proto',
  package='Protos.Responses',
  syntax='proto3',
  serialized_pb=_b('\n!Responses/GetPlayerResponse.proto\x12\x10Protos.Responses\x1a\x18Player/LocalPlayer.proto\"W\n\x11GetPlayerResponse\x12\x10\n\x08unknown1\x18\x01 \x01(\r\x12\x30\n\x0clocal_player\x18\x02 \x01(\x0b\x32\x1a.Protos.Player.LocalPlayerP\x00\x62\x06proto3')
  ,
  dependencies=[Player_dot_LocalPlayer__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPLAYERRESPONSE = _descriptor.Descriptor(
  name='GetPlayerResponse',
  full_name='Protos.Responses.GetPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='Protos.Responses.GetPlayerResponse.unknown1', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_player', full_name='Protos.Responses.GetPlayerResponse.local_player', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=81,
  serialized_end=168,
)

_GETPLAYERRESPONSE.fields_by_name['local_player'].message_type = Player_dot_LocalPlayer__pb2._LOCALPLAYER
DESCRIPTOR.message_types_by_name['GetPlayerResponse'] = _GETPLAYERRESPONSE

GetPlayerResponse = _reflection.GeneratedProtocolMessageType('GetPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERRESPONSE,
  __module__ = 'Responses.GetPlayerResponse_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Responses.GetPlayerResponse)
  ))
_sym_db.RegisterMessage(GetPlayerResponse)


# @@protoc_insertion_point(module_scope)

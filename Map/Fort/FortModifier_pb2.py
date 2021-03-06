# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Map/Fort/FortModifier.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import InventoryEnums_pb2 as Enums_dot_InventoryEnums__pb2

from Enums.InventoryEnums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Map/Fort/FortModifier.proto',
  package='Protos.Map.Fort',
  syntax='proto3',
  serialized_pb=_b('\n\x1bMap/Fort/FortModifier.proto\x12\x0fProtos.Map.Fort\x1a\x1a\x45nums/InventoryEnums.proto\"x\n\x0c\x46ortModifier\x12%\n\x07item_id\x18\x01 \x01(\x0e\x32\x14.Protos.Enums.ItemId\x12\x1f\n\x17\x65xpiration_timestamp_ms\x18\x02 \x01(\x03\x12 \n\x18\x64\x65ployer_player_codename\x18\x03 \x01(\tP\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_InventoryEnums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTMODIFIER = _descriptor.Descriptor(
  name='FortModifier',
  full_name='Protos.Map.Fort.FortModifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='Protos.Map.Fort.FortModifier.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_timestamp_ms', full_name='Protos.Map.Fort.FortModifier.expiration_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployer_player_codename', full_name='Protos.Map.Fort.FortModifier.deployer_player_codename', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=76,
  serialized_end=196,
)

_FORTMODIFIER.fields_by_name['item_id'].enum_type = Enums_dot_InventoryEnums__pb2._ITEMID
DESCRIPTOR.message_types_by_name['FortModifier'] = _FORTMODIFIER

FortModifier = _reflection.GeneratedProtocolMessageType('FortModifier', (_message.Message,), dict(
  DESCRIPTOR = _FORTMODIFIER,
  __module__ = 'Map.Fort.FortModifier_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Map.Fort.FortModifier)
  ))
_sym_db.RegisterMessage(FortModifier)


# @@protoc_insertion_point(module_scope)

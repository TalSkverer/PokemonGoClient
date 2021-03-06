# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Map/Fort/FortLureInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import PokemonEnums_pb2 as Enums_dot_PokemonEnums__pb2

from Enums.PokemonEnums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Map/Fort/FortLureInfo.proto',
  package='Protos.Map.Fort',
  syntax='proto3',
  serialized_pb=_b('\n\x1bMap/Fort/FortLureInfo.proto\x12\x0fProtos.Map.Fort\x1a\x18\x45nums/PokemonEnums.proto\"\x88\x01\n\x0c\x46ortLureInfo\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x01\x12\x32\n\x11\x61\x63tive_pokemon_id\x18\x03 \x01(\x0e\x32\x17.Protos.Enums.PokemonId\x12!\n\x19lure_expires_timestamp_ms\x18\x04 \x01(\x03P\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_PokemonEnums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTLUREINFO = _descriptor.Descriptor(
  name='FortLureInfo',
  full_name='Protos.Map.Fort.FortLureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='Protos.Map.Fort.FortLureInfo.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='Protos.Map.Fort.FortLureInfo.unknown2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_pokemon_id', full_name='Protos.Map.Fort.FortLureInfo.active_pokemon_id', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lure_expires_timestamp_ms', full_name='Protos.Map.Fort.FortLureInfo.lure_expires_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=75,
  serialized_end=211,
)

_FORTLUREINFO.fields_by_name['active_pokemon_id'].enum_type = Enums_dot_PokemonEnums__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['FortLureInfo'] = _FORTLUREINFO

FortLureInfo = _reflection.GeneratedProtocolMessageType('FortLureInfo', (_message.Message,), dict(
  DESCRIPTOR = _FORTLUREINFO,
  __module__ = 'Map.Fort.FortLureInfo_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Map.Fort.FortLureInfo)
  ))
_sym_db.RegisterMessage(FortLureInfo)


# @@protoc_insertion_point(module_scope)

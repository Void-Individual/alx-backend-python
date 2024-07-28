#!/usr/bin/env python3
"""Test module for the utils file"""

access_nested_map = __import__('utils').access_nested_map

print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "c")))

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Sphinx customization.
"""
import re
import typing

from forml.io import dsl
from sphinx.ext import autodoc, autosummary

import openschema

VERSION = openschema.__version__


class ClassDocumenter(autodoc.ClassDocumenter):
    """Custom class documenter with dsl.Schema specific workarounds."""

    @classmethod
    def can_document_member(cls, member: typing.Any, membername: str, isattr: bool, parent: typing.Any) -> bool:
        return isinstance(member, dsl.Table)

    def import_object(self, raiseerror: bool = False) -> bool:
        """Schemas are not rendered properly due to the fact they are turned to dsl.Table instances."""
        ret = super().import_object(raiseerror)
        if isinstance(self.object, dsl.Table):
            self.object = self.object.schema
            self.doc_as_attr = False
        return ret


class AttributeDocumenter(autodoc.AttributeDocumenter):
    """Custom attribute documenter with dsl.Field specific workarounds."""

    @classmethod
    def can_document_member(cls, member: typing.Any, membername: str, isattr: bool, parent: typing.Any) -> bool:
        return isinstance(member, dsl.Field)

    def import_object(self, raiseerror: bool = False) -> bool:
        """Fields are not rendered properly due to the fact they are turned to dsl.Column instances."""
        ret = super().import_object(raiseerror)
        if isinstance(self.parent, dsl.Table):
            self.object = self.object.origin.schema[self.object.name]
            self.parent.schema.__qualname__ = self.parent.__class__.__qualname__
            self.parent = self.parent.schema
            self.parent.__annotations__.setdefault(self.object_name, self.object.kind.__type__)
        return ret

    def should_suppress_value_header(self) -> bool:
        """Don't display the value."""
        return True


class Autosummary(autosummary.Autosummary):
    """Patched Autosummary with custom formatting for the catalog objects."""

    RE_OPENSCHEMA = re.compile(rf'(?={openschema.__name__})(?:\w+\.)*(\w+)$')

    @classmethod
    def __format_name(cls, display_name: str, sig: str, summary: str, real_name: str):
        """Custom name formatting."""
        if match := cls.RE_OPENSCHEMA.match(display_name):
            display_name = match.group(1).title()
        return display_name, sig, summary, real_name

    def get_items(self, names):
        return [self.__format_name(*i) for i in super().get_items(names)]

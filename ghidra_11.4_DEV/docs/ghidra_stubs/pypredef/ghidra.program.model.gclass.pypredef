from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.program.model.data
import java.lang # type: ignore


class ClassUtils(java.lang.Object):
    """
    Utility class for Class-related software modeling.
    """

    class_: typing.ClassVar[java.lang.Class]
    VBPTR: typing.Final = "{vbptr}"
    """
    Standard field name for a virtual base table pointer found within a class
    """

    VFPTR: typing.Final = "{vfptr}"
    """
    Standard field name for a virtual function table pointer found within a class
    """

    VXPTR_TYPE: typing.Final[ghidra.program.model.data.PointerDataType]
    """
    Type used for :obj:`.VBPTR` and :obj:`.VFPTR` fields in a class
    """


    @staticmethod
    def getBaseClassDataTypePath(composite: ghidra.program.model.data.Composite) -> ghidra.program.model.data.DataTypePath:
        """
        Returns the data type path for a suitable base class
        
        :param ghidra.program.model.data.Composite composite: the class composite
        :return: the base class data type path
        :rtype: ghidra.program.model.data.DataTypePath
        """

    @staticmethod
    def getClassInternalsPath(composite: ghidra.program.model.data.Composite) -> ghidra.program.model.data.CategoryPath:
        """
        Returns the category for class internals
        
        :param ghidra.program.model.data.Composite composite: the class composite
        :return: the category path
        :rtype: ghidra.program.model.data.CategoryPath
        """

    @staticmethod
    def getSelfBaseType(composite: ghidra.program.model.data.Composite) -> ghidra.program.model.data.Composite:
        """
        Returns the "self-base" composite for the specified class composite.  This could be
        the composite argument itself of could be a component of it
        
        :param ghidra.program.model.data.Composite composite: the main class type
        :return: the self-base composite
        :rtype: ghidra.program.model.data.Composite
        """



__all__ = ["ClassUtils"]

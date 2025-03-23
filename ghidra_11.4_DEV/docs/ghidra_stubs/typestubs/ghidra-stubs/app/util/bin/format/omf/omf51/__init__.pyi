from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import java.lang # type: ignore
import java.util # type: ignore


class Omf51ModuleEnd(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`Omf51ModuleEnd` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :raises IOException: if an IO-related error occurred
        """

    def getRegisterMask(self) -> int:
        """
        :return: the register mask
        :rtype: int
        """

    @property
    def registerMask(self) -> jpype.JByte:
        ...


class Omf51SegmentDefs(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, largeSegmentId: typing.Union[jpype.JBoolean, bool]):
        """
        Creates a new :obj:`Omf51SegmentDefs` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :param jpype.JBoolean or bool largeSegmentId: True if the segment ID is 2 bytes; false if 1 byte
        :raises IOException: if an IO-related error occurred
        """

    def getSegments(self) -> java.util.List[Omf51Segment]:
        """
        :return: the list of segments
        :rtype: java.util.List[Omf51Segment]
        """

    @property
    def segments(self) -> java.util.List[Omf51Segment]:
        ...


class Omf51Segment(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]
    CODE: typing.Final = 0
    XDATA: typing.Final = 1
    DATA: typing.Final = 2
    IDATA: typing.Final = 3
    BIT: typing.Final = 4
    ABS: typing.Final = 0
    UNIT: typing.Final = 1
    BITADDRESSABLE: typing.Final = 2
    INPAGE: typing.Final = 3
    INBLOCK: typing.Final = 4
    PAGE: typing.Final = 5

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, largeSegmentId: typing.Union[jpype.JBoolean, bool]):
        """
        Creates a new :obj:`Omf51Segment`
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the segment definition
        :param jpype.JBoolean or bool largeSegmentId: True if the segment ID is 2 bytes; false if 1 byte
        :raises IOException: if an IO-related error occurred
        """

    def base(self) -> int:
        """
        :return: the segment base address
        :rtype: int
        """

    def getType(self) -> int:
        """
        :return: the segment type (CODE, XDATA, etc)
        :rtype: int
        """

    def id(self) -> int:
        """
        :return: the segment id
        :rtype: int
        """

    def info(self) -> int:
        """
        :return: the segment info
        :rtype: int
        """

    def isAbsolute(self) -> bool:
        """
        :return: whether or not this segment is absolute
        :rtype: bool
        """

    def isCode(self) -> bool:
        """
        :return: whether or not this segment is code
        :rtype: bool
        """

    def name(self) -> ghidra.app.util.bin.format.omf.OmfString:
        """
        :return: the segment name
        :rtype: ghidra.app.util.bin.format.omf.OmfString
        """

    def relType(self) -> int:
        """
        :return: the segment relocation type
        :rtype: int
        """

    def size(self) -> int:
        """
        :return: the segment size
        :rtype: int
        """

    @property
    def code(self) -> jpype.JBoolean:
        ...

    @property
    def absolute(self) -> jpype.JBoolean:
        ...

    @property
    def type(self) -> jpype.JInt:
        ...


class Omf51FixupRecord(ghidra.app.util.bin.format.omf.OmfRecord):

    class Omf51Fixup(java.lang.Record):
        """
        OMF-51 fixup metadata
        """

        class_: typing.ClassVar[java.lang.Class]

        def __init__(self, refLoc: typing.Union[jpype.JInt, int], refType: typing.Union[jpype.JByte, int], operand: typing.Union[jpype.JInt, int]):
            ...

        def equals(self, o: java.lang.Object) -> bool:
            ...

        def hashCode(self) -> int:
            ...

        def operand(self) -> int:
            ...

        def refLoc(self) -> int:
            ...

        def refType(self) -> int:
            ...

        def toString(self) -> str:
            ...


    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`Omf51FixupRecord` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :raises IOException: if an IO-related error occurred
        """

    def getFixups(self) -> java.util.List[Omf51FixupRecord.Omf51Fixup]:
        """
        Gets a :obj:`List` of fixups
        
        :return: A :obj:`List` of fixups
        :rtype: java.util.List[Omf51FixupRecord.Omf51Fixup]
        """

    @property
    def fixups(self) -> java.util.List[Omf51FixupRecord.Omf51Fixup]:
        ...


class Omf51RecordTypes(java.lang.Object):
    """
    OMF-51 record types
    
    
    .. seealso::
    
        | `OMF-51 Object Module Format <https://turbo51.com/documentation/omf-51-object-module-format>`_
    """

    class_: typing.ClassVar[java.lang.Class]
    ModuleHDR: typing.Final = 2
    ModuleEND: typing.Final = 4
    Content: typing.Final = 6
    Fixup: typing.Final = 8
    SegmentDEF: typing.Final = 14
    ScopeDEF: typing.Final = 16
    DebugItem: typing.Final = 18
    PublicDEF: typing.Final = 22
    ExternalDEF: typing.Final = 24
    LibModLocs: typing.Final = 38
    LibModNames: typing.Final = 40
    LibDictionary: typing.Final = 42
    LibHeader: typing.Final = 44
    KeilContent: typing.Final = 7
    KeilFixup: typing.Final = 9
    KeilSegmentDEF: typing.Final = 15
    KeilScopeDEF: typing.Final = 17
    KeilDebugItemOBJ: typing.Final = 34
    KeilDebugItemSRC: typing.Final = 35
    KeilModuleSourceName: typing.Final = 36
    KeilPublicDEF: typing.Final = 23
    KeilSourceBrowserFiles: typing.Final = 97
    KeilDebugData62: typing.Final = 98
    KeilDebugData63: typing.Final = 99
    KeilDebugData64: typing.Final = 100

    def __init__(self):
        ...

    @staticmethod
    def getName(type: typing.Union[jpype.JInt, int]) -> str:
        """
        Gets the name of the given record type
        
        :param jpype.JInt or int type: The record type
        :return: The name of the given record type
        :rtype: str
        """


class Omf51RecordFactory(ghidra.app.util.bin.format.omf.AbstractOmfRecordFactory):
    """
    A class for reading/creating OMF-51 records
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, provider: ghidra.app.util.bin.ByteProvider):
        """
        Creates a new :obj:`Omf51RecordFactory`
        
        :param ghidra.app.util.bin.ByteProvider provider: The :obj:`ByteProvider` that contains the records
        """


class Omf51ModuleHeader(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`Omf51ModuleHeader` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :raises IOException: if an IO-related error occurred
        """

    def getTrnId(self) -> int:
        """
        :return: the TRN ID
        :rtype: int
        """

    @property
    def trnId(self) -> jpype.JByte:
        ...


class Omf51Content(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, largeSegmentId: typing.Union[jpype.JBoolean, bool]):
        """
        Creates a new :obj:`Omf51Content` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :param jpype.JBoolean or bool largeSegmentId: True if the segment ID is 2 bytes; false if 1 byte
        :raises IOException: if an IO-related error occurred
        """

    def getDataIndex(self) -> int:
        """
        :return: the start of the data in the reader
        :rtype: int
        """

    def getDataSize(self) -> int:
        """
        :return: the data size in bytes
        :rtype: int
        """

    def getOffset(self) -> int:
        """
        :return: the offset
        :rtype: int
        """

    def getSegId(self) -> int:
        """
        :return: the segment ID
        :rtype: int
        """

    @property
    def segId(self) -> jpype.JInt:
        ...

    @property
    def offset(self) -> jpype.JInt:
        ...

    @property
    def dataIndex(self) -> jpype.JLong:
        ...

    @property
    def dataSize(self) -> jpype.JInt:
        ...



__all__ = ["Omf51ModuleEnd", "Omf51SegmentDefs", "Omf51Segment", "Omf51FixupRecord", "Omf51RecordTypes", "Omf51RecordFactory", "Omf51ModuleHeader", "Omf51Content"]

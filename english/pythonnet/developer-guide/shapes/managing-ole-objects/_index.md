---
title: Managing OLE Objects
type: docs
weight: 50
url: /python-net/managing-ole-objects/
---

## **Introduction**

OLE (Object Linking and Embedding) is Microsoft's framework for a compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and information objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.

OLE (Object Linking and Embedding) is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.

### **Inserting OLE Objects into the Worksheet**

Aspose.Cells for Python via .NET supports adding, extracting and manipulating OLE objects in worksheets. For this reason, Aspose.Cells for Python via .NET has the [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection) class, used to add a new OLE Object to the collection list. Another class, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), represents an OLE Object. It has some important members:

- The [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.
- The [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.

The following example shows how to add an OLE Object(s) into a worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Extracting OLE Objects in the Workbook**

The following example shows how to extract OLE Objects in a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLS, PPT, PDF, etc.) based on the OLE object’s file format type.

After running the code, we can save different files based on their respective OLE Objects format types.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Extracting Embedded MOL File**

Aspose.Cells for Python via .NET supports extracting objects of uncommon types like MOL(Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting embedded MOL file and saving it to disk by using this [sample excel file](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Advance topics**
- [Access and Modify the Display Label of the Linked Ole Object](/cells/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatically Refresh OLE object](/cells/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extract OLE Objects from Workbook](/cells/python-net/extract-ole-objects-from-workbook/)
- [Get or Set the Class Identifier of the Embedded OLE Object](/cells/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserting a WAV file as an Ole Object](/cells/python-net/inserting-a-wav-file-as-an-ole-object/)


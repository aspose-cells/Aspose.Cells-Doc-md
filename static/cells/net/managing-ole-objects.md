##Managing OLE Objects
## **Introduction**
OLE (Object Linking and Embedding) is Microsoft's framework for a compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and information objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.
OLE (Object Linking and Embedding) is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.
### **Inserting OLE Objects into the Worksheet**
Aspose.Cells supports adding, extracting and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) class, used to add a new OLE Object to the collection list. Another class, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), represents an OLE Object. It has some important members:
- The [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.
- The [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.
The following example shows how to add an OLE Object(s) into a worksheet.
### **Extracting OLE Objects in the Workbook**
The following example shows how to extract OLE Objects in a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLS, PPT, PDF, etc.) based on the OLE object’s file format type.
After running the code, we can save different files based on their respective OLE Objects format types.
### **Extracting Embedded MOL File**
Aspose.Cells supports extracting objects of uncommon types like MOL(Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting embedded MOL file and saving it to disk by using this [sample excel file](94896196.xlsx).
## **Advance topics**
- [Access and Modify the Display Label of the Linked Ole Object](https://docs.aspose.com/cells/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatically refresh OLE object via Microsoft Excel using Aspose.Cells](https://docs.aspose.com/cells/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extract OLE Objects from Workbook](https://docs.aspose.com/cells/net/extract-ole-objects-from-workbook/)
- [Get or Set the Class Identifier of the Embedded OLE Object](https://docs.aspose.com/cells/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserting a WAV file as an Ole Object](https://docs.aspose.com/cells/net/inserting-a-wav-file-as-an-ole-object/)

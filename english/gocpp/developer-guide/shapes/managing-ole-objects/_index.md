---
title: Managing OLE Objects with Golang via C++
linktitle: Managing OLE Objects
type: docs
weight: 50
url: /go-cpp/managing-ole-objects/
description: Learn how to add, extract, and manipulate OLE objects in worksheets using Aspose.Cells with Golang via C++.
---

## **Introduction**

OLE (Object Linking and Embedding) is Microsoft's framework for a compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and informational objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.

OLE (Object Linking and Embedding) is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.

### **Inserting OLE Objects into the Worksheet**

Aspose.Cells supports adding, extracting, and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [**OleObjectCollection**](https://reference.aspose.com/cells/go-cpp/oleobjectcollection/) class, used to add a new OLE object to the collection list. Another class, [**OleObject**](https://reference.aspose.com/cells/go-cpp/oleobject/), represents an OLE object. It has some important members:

- The [**ImageData**](https://reference.aspose.com/cells/go-cpp/oleobject/getimagedata/) property specifies the image (icon) data as a byte array. The image will be displayed to represent the OLE object in the worksheet.
- The [**ObjectData**](https://reference.aspose.com/cells/go-cpp/oleobject/getobjectdata/) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double‑click on the OLE object icon.

The following example shows how to add OLE object(s) into a worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingOleObjects.go" >}}

### **Extracting OLE Objects from the Workbook**

The following example shows how to extract OLE objects from a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLSX, PPT, PDF, etc.) based on the OLE object’s file‑format type.

After running the code, we can save different files based on their respective OLE object format types.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingOleObjects-1.go" >}}

### **Extracting an Embedded MOL File**

Aspose.Cells supports extracting objects of uncommon types like MOL (Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting an embedded MOL file and saving it to disk using this [sample Excel file](94896196.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingOleObjects-2.go" >}}

## **Advanced Topics**
- [Access and Modify the Display Label of the Linked Ole Object](/cells/go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatically refresh OLE object via Microsoft Excel using Aspose.Cells](/cells/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extract OLE Objects from Workbook](/cells/go-cpp/extract-ole-objects-from-workbook/)
- [Get or Set the Class Identifier of the Embedded OLE Object](/cells/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserting a WAV file as an Ole Object](/cells/go-cpp/inserting-a-wav-file-as-an-ole-object/)
{{< app/cells/assistant language="go" >}}

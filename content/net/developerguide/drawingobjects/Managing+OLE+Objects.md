+++
title = "Managing OLE Objects" 
description = "" 
weight = 12288 
+++

Aspose.Cells for .NET : Managing OLE Objects  

# Aspose.Cells for .NET : Managing OLE Objects


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#ManagingOLEObjects-Introduction)
    *   1.1 [Inserting OLE Objects into the Worksheet](#ManagingOLEObjects-InsertingOLEObjectsintotheWorksheet)
    *   1.2 [Extracting OLE Objects in the Workbook](#ManagingOLEObjects-ExtractingOLEObjectsintheWorkbook)
    *   1.3 [Extracting Embedded MOL File](#ManagingOLEObjects-ExtractingEmbeddedMOLFile)
{{< /panel >}}
 

## Introduction

OLE (Object Linking and Embedding) is Microsoft's framework for a compound document technology. Briefly, a compound document is something like a display desktop that can contain visual and information objects of all kinds: text, calendars, animations, sound, motion video, 3D, continually updated news, controls, and so forth. Each desktop object is an independent program entity that can interact with a user and also communicate with other objects on the desktop.

OLE (Object Linking and Embedding) is supported by many different programs and is used to make content created in one program available in another. For example, you can insert a Microsoft Word document into Microsoft Excel. To see what types of content you can insert, click **Object** on the **Insert** menu. Only programs that are installed on the computer and that support OLE objects appear in the **Object type** box.

#### Inserting OLE Objects into the Worksheet

Aspose.Cells supports adding, extracting and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [OleObjectCollection](https://apireference.aspose.com/net/cells/aspose.cells.drawing/oleobjectcollection) class, used to add a new OLE Object to the collection list. Another class, [OleObject](https://apireference.aspose.com/net/cells/aspose.cells.drawing/oleobject), represents an OLE Object. It has some important members:

*   The [ImageData](https://apireference.aspose.com/net/cells/aspose.cells.drawing/oleobject/properties/imagedata) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.
*   The [ObjectData](https://apireference.aspose.com/net/cells/aspose.cells.drawing/oleobject/properties/objectdata) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.

The following example shows how to add an OLE Object(s) into a worksheet.

#### Extracting OLE Objects in the Workbook

The following example shows how to extract OLE Objects in a Workbook. The example gets different OLE objects from an existing XLS file and saves different files (DOC, XLS, PPT, PDF, etc.) based on the OLE object’s file format type.

After running the code, we can save different files based on their respective OLE Objects format types.

#### Extracting Embedded MOL File

Aspose.Cells supports extracting objects of uncommon types like MOL(Molecular data file containing information about atoms and bonds). The following code snippet demonstrates extracting embedded MOL file and saving it to disk by using this [sample excel file](https://docs2.aspose.com/cells/net/attachments/5017133/94896196.xlsx).

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [EmbeddedMolSample.xlsx](https://docs2.aspose.com/cells/net/attachments/5017133/94896196.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  


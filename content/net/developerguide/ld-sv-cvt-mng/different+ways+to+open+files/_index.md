---
title : "Different Ways to Open Files" 
description : "" 
weight : 12060 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/different+ways+to+open+files/
---

# Aspose.Cells for .NET : Different Ways to Open Files


With Aspose.Cells it is possible to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Opening a File via a Path](#opening-a-file-via-a-path)
*   2 [Opening a File using a Stream](#opening-a-file-using-a-stream)
*   3 [Opening a File with Data only](#opening-a-file-with-data-only)
*   4 [Loading Visible Sheets only](#loading-visible-sheets-only)
{{< /panel >}}
 

## Opening a File via a Path

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

## Opening a File using a Stream

It is also possible to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream *object that contains the file.

## Opening a File with Data only

To open a file with data only, use the [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) and [LoadFilter](https://apireference.aspose.com/net/cells/aspose.cells/loadfilter) classes to set the related attribute and options of the classes for the template file to be loaded.

## Loading Visible Sheets only

While loading a [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) sometimes you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom function that inherits the [LoadFilter](https://apireference.aspose.com/net/cells/aspose.cells/loadfilter) class and pass its instance to [LoadOptions.LoadFilter](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/loadfilter) property.

  
Here is the implementation of the *CustomnLoad *class referenced in the above snippet.

An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.

There are fair chances that the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the Memory Preferences.


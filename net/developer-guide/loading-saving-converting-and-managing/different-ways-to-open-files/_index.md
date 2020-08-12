---
title: Different Ways to Open Files
type: docs
weight: 10
url: /net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

With Aspose.Cells it is possible to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **Opening a File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the **[Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook)** class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Opening a File using a Stream**

It is also possible to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Opening a File with Data only**

To open a file with data only, use the **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** and **[LoadFilter](https://apireference.aspose.com/cells/net/aspose.cells/loadfilter)** classes to set the related attribute and options of the classes for the template file to be loaded.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Loading Visible Sheets only**

While loading a **[Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook)** sometimes you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom function that inherits the **[LoadFilter](https://apireference.aspose.com/cells/net/aspose.cells/loadfilter)** class and pass its instance to **[LoadOptions.LoadFilter](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)** property.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Here is the implementation of the *CustomnLoad* class referenced in the above snippet.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

There are fair chances that the **[Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook)** constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the Memory Preferences.

{{% /alert %}}

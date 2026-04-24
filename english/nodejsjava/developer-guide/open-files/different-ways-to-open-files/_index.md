---
title: Different Ways to Open Files
type: docs
weight: 10
url: /nodejs-java/different-ways-to-open-files/
description: This article explains how to open an Excel file using the Aspose.Cells for Node.js via Java API.
keywords: Node.js via Java Open an Excel file without Excel, How do I open an Excel File.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

With Aspose.Cells, it is simple to open files, for example to retrieve data or to use a designer template to speed up the development process.

{{% /alert %}}

## **How to Open an Excel File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/nodejs/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

[Example File](./Book1.xlsx)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningFilesThroughPath-1.js" >}}

## **How to Open an Excel File via a Stream**

It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

[Example File](./Book2.xls)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningFilesThroughStream-1.js" >}}

## **How to Open a File with Data Only**

To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/nodejs/loadoptions) and [**LoadFilter**](https://reference.aspose.com/cells/nodejs/loadfilter) classes to set the related attributes and options for the template file to be loaded.

[Example File](./Book1.xlsx)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningFilewithDataOnly-1.js" >}}
<!--
## **How to Load Visible Sheets Only**

While loading a [**Workbook**](https://reference.aspose.com/cells/nodejs/workbook), you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom class that inherits the [**LoadFilter**](https://reference.aspose.com/cells/nodejs/loadfilter) class and pass its instance to the [**LoadOptions.setLoadFilter(LoadFilter value)**](https://reference.aspose.com/cells/nodejs/LoadOptions#setLoadFilter) property.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-LoadVisibleSheetsOnly-1.js" >}}

Here is the implementation of the *CustomLoad* class referenced in the above snippet.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-LoadVisibleSheetsOnly-2.js" >}}

{{% alert color="primary" %}}

An exception will be thrown if you try to open non‐native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) using Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

There is a fair chance that the [**Workbook**](https://reference.aspose.com/cells/nodejs/workbook) constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception indicates that the available memory is insufficient to completely load the spreadsheet into memory; therefore, the spreadsheet must be loaded with the Memory Preferences enabled.
-->
{{% /alert %}}
<!--{{< app/cells/assistant language="csharp" >}}-->
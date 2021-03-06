---
title: Workbook and Worksheet Print Preview
type: docs
weight: 140
url: /net/workbook-and-worksheet-print-preview/
---

## **Usage Scenario**

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes to find out the total number of pages.

## **Workbook and Worksheet Print Preview**

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class by passing [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) and [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objects to the constructor. The [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class provides an [**EvaluatedPageCount**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview. Similar to [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class, the [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class by passing [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) and [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objects to the constructor. The [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class also provides an [**EvaluatedPageCount**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview.

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes by using the [sample excel file](94896177.xlsx).

### **Sample Code**

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

The following is the output generated by executing the above code.

### **Console Output**

Workbook page count: 1
Worksheet page count: 1

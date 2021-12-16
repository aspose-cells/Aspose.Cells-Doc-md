---
title: Printing Workbooks
type: docs
weight: 70
url: /net/printing-workbooks/
---

{{% alert color="primary" %}}

After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.

{{% /alert %}}

## **Introduction**

Microsoft Excel assumes that you want to print the entire worksheet area unless you specify a selection. To print using Aspose.Cells, first import the Aspose.Cells.Rendering namespace to the program. It has several useful classes, for example, [**SheetRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) and [**WorkbookRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Print Using SheetRender**

The [**Aspose.Cells.Rendering.SheetRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet and has the [**ToPrinter**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) method which can print a worksheet. The following sample code shows how to print a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Print Using WorkbookRender**

To print a whole workbook, iterate through the sheets and print them, or use the [**WorkbookRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) class.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells also provides overloads for the [**WorkbookRender.ToPrinter()**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) and [**SheetRender.ToPrinter()**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) methods, so it's possible to set the print job name while printing Excel spreadsheets. By default, all print jobs are created with the name "Document".

{{% /alert %}}

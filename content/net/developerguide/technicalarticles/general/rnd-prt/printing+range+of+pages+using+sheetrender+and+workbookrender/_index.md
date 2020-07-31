---
title : "Printing Range of Pages using SheetRender and WorkbookRender" 
description : "" 
weight : 20380 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/printing+range+of+pages+using+sheetrender+and+workbookrender/
---

# Aspose.Cells for .NET : Printing Range of Pages using SheetRender and WorkbookRender


Microsoft Excel allows you to print range of pages of workbook or worksheet. The following screenshot shows the Microsoft Excel interface to specify the range of pages.

Aspose.Cells provides the `WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` and `SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` methods for this purpose.

## Microsoft Excel Interface to specify the Range of Pages to Print

The following sample code illustrates the use of `WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` and `SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` methods. It prints the pages 2-5 of the workbook and worksheet.


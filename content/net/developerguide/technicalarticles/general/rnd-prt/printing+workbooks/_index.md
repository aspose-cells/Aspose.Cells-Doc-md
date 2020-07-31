---
title : "Printing Workbooks" 
description : "" 
weight : 20362 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/printing+workbooks/
---

# Aspose.Cells for .NET : Printing Workbooks


After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
    *   1.1 [Print Using `SheetRender`](#print-using-`sheetrender`)
    *   1.2 [Print Using `WorkbookRender`](#print-using-`workbookrender`)
{{< /panel >}}
 

 

# Introduction

Microsoft Excel assumes that you want to print the entire worksheet area unless you specify a selection. To print using Aspose.Cells, first import the Aspose.Cells.Rendering namespace to the program. It has several useful classes, for example, [SheetRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender) and [WorkbookRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/workbookrender).

## Print Using `SheetRender`

The [Aspose.Cells.Rendering.SheetRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender) class represents a worksheet and has the [ToPrinter](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender/methods/toprinter/index) method which can print a worksheet. The following sample code shows how to print a worksheet.

## Print Using `WorkbookRender`

To print a whole workbook, iterate through the sheets and print them, or use the [WorkbookRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/workbookrender) class.

Aspose.Cells also provides overloads for the [WorkbookRender.ToPrinter()](https://apireference.aspose.com/net/cells/aspose.cells.rendering.workbookrender/toprinter/methods/3) and [SheetRender.ToPrinter()](https://apireference.aspose.com/net/cells/aspose.cells.rendering.sheetrender/toprinter/methods/2) methods, so it's possible to set the print job name while printing Excel spreadsheets. By default, all print jobs are created with the name "Document".


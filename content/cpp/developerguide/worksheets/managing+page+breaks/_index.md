---
title : "Managing Page Breaks" 
description : "" 
weight : 12046 
toc : false
type: docs
url: /cpp/developerguide/worksheets/managing+page+breaks/
---

# Aspose.Cells for C++ : Managing Page Breaks


According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

The location of the cell where the page break is added, the page is ended and all rest of the data after the page break is printed on the next page while printing. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

*   Horizontal page break
*   Vertical page break

In the rest of the discussion, we will describe how can you add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Page Breaks](#page-breaks)
    *   1.1 [Adding Page Breaks](#adding-page-breaks)
{{< /panel >}}
 

 

## Page Breaks

Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) that represents an Excel file. The [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class contains a [Worksheets](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class provides a wide range of methods used to manage a worksheet. To add the page breaks, use the [AddPageBreaks](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/#a5f8dd5624b81e0ee2e7455f2b83380f6) method of the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class.

### Adding Page Breaks


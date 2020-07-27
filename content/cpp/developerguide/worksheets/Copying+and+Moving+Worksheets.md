+++
title = "Copying and Moving Worksheets" 
description = "" 
weight = 12044 
+++

Aspose.Cells for C++ : Copying and Moving Worksheets  

# Aspose.Cells for C++ : Copying and Moving Worksheets


Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.

Aspose.Cells supports copying and moving worksheets within or between workbooks. A worksheet, complete with data, formatting, tables, matrices, charts, images and other objects, are copied with the highest degree of precision.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Moving or Copying Sheets using Microsoft Excel](#CopyingandMovingWorksheets-MovingorCopyingSheetsusingMicrosoftExcel)
    *   1.1 [Copy Worksheets within a Workbook with Aspose.Cells](#CopyingandMovingWorksheets-CopyWorksheetswithinaWorkbookwithAspose.Cells)
    *   1.2 [Move Worksheets within Workbook](#CopyingandMovingWorksheets-MoveWorksheetswithinWorkbook)
{{< /panel >}}
 

 

## Moving or Copying Sheets using Microsoft Excel

The following are the steps involved in copying and moving worksheets within or between workbooks in Microsoft Excel.

1.  To move or copy sheets to another workbook, open the workbook that will receive the sheets.
2.  Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
3.  On the **Edit** menu, click **Move or Copy Sheet**.
4.  In the **To book** dialog, click the workbook to receive the sheets.
5.  To move or copy the selected sheets to a new workbook, click **New Book**.
6.  In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
7.  To copy the sheets instead of moving them, select the **Create a copy** checkbox.

### Copy Worksheets within a Workbook with Aspose.Cells

Aspose.Cells provides an overloaded method [AddCopy()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/#aa1e73c54ea19bb7aa0f9f197c2baa5ba) that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet. The following example shows how to copy an existing worksheet within a workbook.

### Move Worksheets within Workbook

Aspose.Cells provides a method [MoveTo()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/#a240bf1d3d52ea8c8bfd54ffa320921b7) that is used to move a worksheet to another location in the same spreadsheet. The method takes the target worksheet index as a parameter. The following example shows how to move a worksheet to another location within the workbook.


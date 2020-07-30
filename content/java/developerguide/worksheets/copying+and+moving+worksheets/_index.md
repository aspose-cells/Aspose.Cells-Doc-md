---
title : "Copying and Moving Worksheets" 
description : "" 
weight : 12127 
toc : false
type: docs
url: /java/developerguide/worksheets/copying+and+moving+worksheets/
---

# Aspose.Cells for Java : Copying and Moving Worksheets


Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.

Aspose.Cells supports copying and moving worksheets within or between workbooks. Worksheet, complete with data, formatting, tables, matrices, charts, images and other objects, are copied with the highest degree of precision.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Moving or Copying Sheets using Microsoft Excel](#moving-or-copying-sheets-using-microsoft-excel)
    *   1.1 [Copy Worksheets within a Workbook](#copy-worksheets-within-a-workbook)
    *   1.2 [Copy Worksheets between Workbooks](#copy-worksheets-between-workbooks)
    *   1.3 [Move Worksheets within Workbook](#move-worksheets-within-workbook)
{{< /panel >}}
 

 

## Moving or Copying Sheets using Microsoft Excel

Following are the steps involved for copying and moving worksheets within or between workbooks.

1.  To move or copy sheets to another workbook, open the workbook that will receive the sheets.
2.  Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
3.  On the **Edit** menu, click **Move or Copy Sheet**.
4.  In the To book box, click the workbook to receive the sheets.
5.  To move or copy the selected sheets to a new workbook, click **new book**.
6.  In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
7.  To copy the sheets instead of moving them, select the **Create a copy** checkbox.

### Copy Worksheets within a Workbook

Aspose.Cells provides an overloaded method, [WorksheetCollection.addCopy()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#addCopy(int)), that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.


### Copy Worksheets between Workbooks

Aspose.Cells provides a method, [Worksheet.copy()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), used to copy data and formatting from a source worksheet to another worksheet within or between the workbooks. The method takes the source worksheet object as a parameter.

The following example shows how to copy a worksheet from one workbook to another workbook.

The following example shows how to copy a worksheet from one workbook to another.

### Move Worksheets within Workbook

Aspose.Cells provides a method, [Worksheet.moveTo()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#moveTo(int)), used to move a worksheet to another location in the same spreadsheet.

The following example shows how to move a worksheet to another location within the workbook.


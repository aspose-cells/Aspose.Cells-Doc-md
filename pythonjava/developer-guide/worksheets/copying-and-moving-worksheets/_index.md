---
title: Copying and Moving Worksheets
type: docs
weight: 20
url: /pythonjava/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.

Aspose.Cells supports copying and moving worksheets within or between workbooks. Worksheets, complete with data, formatting, tables, matrices, charts, images, and other objects, are copied with the highest degree of precision.

{{% /alert %}} 
## **Moving or Copying Sheets using Microsoft Excel**
The following are the steps involved in copying and moving worksheets within or between workbooks.

1. Open the workbook that will receive the sheets.
1. Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
1. On the **Edit** menu, click **Move or Copy Sheet**.
1. In the To book box, click the workbook to receive the sheets.
1. To move or copy the selected sheets to a new workbook, click **new book**.
1. In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
1. To copy the sheets instead of moving them, select the **Create a copy** checkbox.
### **Copy Worksheets within a Workbook**
Aspose.Cells provides an overloaded [WorksheetCollection.addCopy()](https://apireference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) method that is used to copy an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copy Worksheets between Workbooks**
Aspose.Cells provides the [Worksheet.copy()](https://apireference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) method used to copy worksheets to other workbooks. The method takes the source worksheet object as a parameter.

The following example shows how to copy a worksheet from one workbook to another workbook.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Move Worksheets within Workbook**
Aspose.Cells provides the [Worksheet.moveTo()](https://apireference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) method used to move a worksheet to another location in the same spreadsheet.

The following example shows how to move a worksheet to another location within the workbook.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}

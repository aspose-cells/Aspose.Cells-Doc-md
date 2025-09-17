##Copying and Moving Worksheets
This article includes sample code and describes how to copy and move worksheets programmatically both within an Excel workbook and across Excel workbooks using the C# API or .NET Library.
Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.
Aspose.Cells supports copying and moving worksheets within or between workbooks. Worksheet, complete with data, formatting, tables, matrices, charts, images and other objects, are copied with the highest degree of precision.
## **Moving or Copying Sheets using Microsoft Excel**
Following are the steps involved for copying and moving worksheets within or between workbooks in Microsoft Excel.
1. To move or copy sheets to another workbook, open the workbook that will receive the sheets.
1. Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
1. On the **Edit** menu, click **Move or Copy Sheet**.
1. In the **To book** dialog, click the workbook to receive the sheets.
1. To move or copy the selected sheets to a new workbook, click **New Book**.
1. In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
1. To copy the sheets instead of moving them, select the **Create a copy** checkbox.
### **Copy Worksheets within a Workbook with Aspose.Cells**
Aspose.Cells provides an overloaded method, [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index), that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.
The following example shows how to copy an existing worksheet within a workbook.
### **Copy Worksheets between Workbooks**
Aspose.Cells provides a method, [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) used to copy data and formatting from a source worksheet to another worksheet within or between workbooks. The method takes the source worksheet object as a parameter.
The following example shows how to copy a worksheet from one workbook to another workbook.
The following example shows how to copy a worksheet from one workbook to another.
### **Move Worksheets within Workbook**
Aspose.Cells provides a method [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) which is used to move a worksheet to another location in the same spreadsheet. The method takes the target worksheet index as a parameter.
The following example shows how to move a worksheet to another location within the workbook.

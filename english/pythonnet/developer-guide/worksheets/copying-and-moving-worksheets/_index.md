---
title: Copying and Moving Worksheets
type: docs
weight: 10
url: /python-net/copying-and-moving-worksheets/
description: This article includes sample code and describes how to copy and move worksheets programmatically both within an Excel workbook and across Excel workbooks using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python copy worksheet, Python move worksheet, Python Copy Worksheets between Workbooks, Python Move Worksheets within Workbook, Python Copy Worksheets between Workbooks, Python Copy Worksheets within a Workbook.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you do need a number of worksheets with common formatting and data. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it.

Aspose.Cells for Python via .NET supports copying and moving worksheets within or between workbooks. **Worksheets**, complete with data, formatting, tables, matrices, charts, images and other objects, are copied with the highest degree of precision.

{{% /alert %}}

## **How to Move or Copy Sheets using Microsoft Excel**

Following are the steps involved for copying and moving worksheets within or between workbooks in Microsoft Excel.

1. To move or copy sheets to another workbook, open the workbook that will receive the sheets.  
2. Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.  
3. On the **Edit** menu, click **Move or Copy Sheet**.  
4. In the **To book** dialog, click the workbook to receive the sheets.  
5. To move or copy the selected sheets to a new workbook, click **New Book**.  
6. In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.  
7. To copy the sheets instead of moving them, select the **Create a copy** checkbox.  

## **How to Copy Worksheets within a Workbook with Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET provides an overloaded method, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **How to Copy Worksheets between Workbooks**

Aspose.Cells for Python via .NET provides a method, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet), used to copy data and formatting from a source worksheet to another worksheet within or between workbooks. The method takes the source worksheet object as a parameter.

The following example shows how to copy a worksheet from one workbook to another workbook.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

The following example shows how to copy a worksheet from one workbook to another.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **How to Move Worksheets within Workbook**

Aspose.Cells for Python via .NET provides a method, [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int), which is used to move a worksheet to another location in the same spreadsheet. The method takes the target worksheet index as a parameter.

The following example shows how to move a worksheet to another location within the workbook.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

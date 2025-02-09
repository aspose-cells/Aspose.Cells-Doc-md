---
title: Copy and Move Worksheets Within and Between Workbooks
type: docs
weight: 80
url: /python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Sometimes, you do need a number of worksheets with common formatting and data entry. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it three times.

Aspose.Cells for Python via .NET supports copying or moving worksheets within or between workbooks. Worksheets including data, formatting, tables, matrices, charts, images and other objects are copied with the highest degree of precision.

{{% /alert %}}

## **Copying and Moving Worksheets**

### **Copying a Worksheet within a Workbook**

The initial steps are the same for all examples.

1. Create two workbooks with some data in Microsoft Excel. For the purposes of this example, we created two new workbooks in Microsoft Excel and input some data into the worksheets.

- FirstWorkbook.xlsx (3 worksheets).
- SecondWorkbook.xlsx (1 worksheet).

1. Download and install Aspose.Cells for Python via .NET:
   1. [Download Aspose.Cells for Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Install it on your development computer.
      All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
1. Create a project and add references:   
1. Copy the worksheet within a workbook
   The first example copies the first worksheet (Copy) within FirstWorkbook.xlsx.

When executing the code, the worksheet named Copy is copied within FirstWorkbook.xlsx with the name Last Sheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Moving a Worksheet within a Workbook**

The code below shows how to move a worksheet from one position in a workbook to another. Executing the code moves the worksheet called Move from index 1 to index 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Copying a Worksheet between Workbooks**

Executing the code copies the worksheet named Copy is to SecondWorkbook.xlsx with the name Sheet2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Moving a Worksheet between Workbooks**

Executing the code moves the worksheet named Move from FirstWorkbook.xlsx to SecondWorkbook.xlsx with the name Sheet3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}

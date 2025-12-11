---
title: Copy and Move Worksheets Within and Between Workbooks with Golang via C++
linktitle: Copy and Move Worksheets
type: docs
weight: 80
url: /go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Learn how to copy and move worksheets within and between Excel workbooks using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes, you need multiple worksheets with common formatting and data entry. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it multiple times.

Aspose.Cells supports copying or moving worksheets within or between workbooks. Worksheets, including data, formatting, tables, matrices, charts, images, and other objects, are copied with the highest degree of precision.

{{% /alert %}}

## **Copying and Moving Worksheets**

### **Copying a Worksheet within a Workbook**

The initial steps are the same for all examples:

1. Create two workbooks with some data in Microsoft Excel. For the purposes of this example, we created two new workbooks in Microsoft Excel and input some data into the worksheets:
   - FirstWorkbook.xlsx (3 worksheets)
   - SecondWorkbook.xlsx (1 worksheet)

2. Download and install Aspose.Cells:
   1. [Download Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Install it on your development computer

3. Create a project:
   1. Create a new C++ project in your preferred IDE

4. Add references:
   1. Add Aspose.Cells for C++ library to your project

5. Copy the worksheet within a workbook. The first example copies the first worksheet (Copy) within FirstWorkbook.xlsx.

When executing the code, the worksheet named Copy is copied within FirstWorkbook.xlsx with the name Last Sheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}

### **Moving a Worksheet within a Workbook**

The code below shows how to move a worksheet from one position in a workbook to another. Executing the code moves the worksheet called Move from index 1 to index 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}

### **Copying a Worksheet between Workbooks**

Executing the code copies the worksheet named Copy to SecondWorkbook.xlsx with the name Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}

### **Moving a Worksheet between Workbooks**

Executing the code moves the worksheet named Move from FirstWorkbook.xlsx to SecondWorkbook.xlsx with the name Sheet3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
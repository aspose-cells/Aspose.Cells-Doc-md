---
title: Apply Conditional Formatting in Worksheets with Golang via C++
linktitle: Apply Conditional Formatting
description: How to use Aspose.Cells library in C++ to apply conditional formatting in worksheets. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Conditional Formatting, Go, Worksheet, Formatting
type: docs
weight: 130
url: /go-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

This article is designed to provide a detailed understanding of how to add conditional formatting to a range of cells in a worksheet.

Conditional formatting is an advanced feature in Microsoft Excel that allows you to apply formats to a range of cells and have that formatting change depending on the value of the cell or a formula. For example, the background of a cell may be red to highlight a negative value, or the text color might be green for a positive value. When the value of the cell meets the format condition, the format is applied. If the value of the cell does not meet the format condition, the cell's default formatting is used.

It's possible to apply conditional formatting with Microsoft Office Automation, but that has its drawbacks. There are several reasons and issues involved: for example, security, stability, scalability, and speed. The main reason for finding another solution is that Microsoft itself strongly recommends against Office Automation for software solutions.

This article shows how to create a console application and add conditional formatting to cells with a few simple lines of code using the Aspose.Cells API.

{{% /alert %}}

## **Using Aspose.Cells to Apply Conditional Formatting Based on Cell Value**

1. **Download and Install Aspose.Cells**.  
   - Download Aspose.Cells for Go via C++.  
   - Install it on your development computer.  
     All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into the produced documents.

2. **Create a project**.  
   Start your C++ development environment and create a new console application.

3. **Add references**.  
   Add a reference to Aspose.Cells to your project, for example, add a reference to `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

4. **Apply conditional formatting based on cell value**.  
   Below is the code used to accomplish the task. It applies conditional formatting to a cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyConditionalFormattingInWorksheets.go" >}}

When the above code is executed, conditional formatting is applied to cell **A1** in the first worksheet of the output file (`output.xls`). The conditional formatting applied to A1 depends on the cell value. If the cell value of A1 is between 50 and 100, the background color is red due to the conditional formatting applied.

## **Using Aspose.Cells to Apply Conditional Formatting Based on Formula**

1. **Applying conditional formatting based on a formula (Code Snippet)**  
   Below is the code to accomplish the task. It applies conditional formatting to cell **B3**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyConditionalFormattingInWorksheets-1.go" >}}

When the above code is executed, conditional formatting is applied to cell **B3** in the first worksheet of the output file (`output.xls`). The conditional formatting applied depends on a formula that calculates the value of B3 as the sum of B1 and B2.

{{< app/cells/assistant language="go" >}}

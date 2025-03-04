---
title: Apply Conditional Formatting in Worksheets
linktitle: Apply Conditional Formatting in Worksheets
description: How to use Aspose.Cells library in Node.js via C++ to apply conditional formatting in worksheets for better control over cell appearance.
keywords: Aspose.Cells, Conditional Formatting, Node.js via C++, Worksheet, Formatting
type: docs
weight: 130
url: /nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

This article is designed to provide a detailed understanding of how to add conditional formatting to a range of cells in a worksheet.

Conditional formatting is an advanced feature in Microsoft Excel that allows you to apply formats to a range of cells, and have that formatting change depending on the value of the cell or the value of a formula. For example, the background of a cell may be red to highlight a negative value, or the text color might be green for a positive value. When the value of the cell meets the format condition, the format is applied. If the value of the cell does not meet the format condition, the cell's default formatting is used.

It's possible to apply conditional formatting with Microsoft Office Automation but that has its drawbacks. There are several reasons and issues involved: for example, security, stability, scalability and speed. The main reason for finding another solution is that Microsoft themselves strongly recommends against Office Automation for software solutions.

This article shows how to create a console application, add conditional formatting on cells with a few simplest lines of code using the Aspose.Cells API.

{{% /alert %}}

## **Using Aspose.Cells to Apply Conditional Formatting Based on Cell Value**

1. **Download and Install Aspose.Cells**.
   1. Download Aspose.Cells for Node.js via C++.
1. Install it on your development computer.
   All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
1. **Create a project**.
   Start your Node.js project by initializing it. This example creates a Node.js console application.
1. **Add references**.
   Add a reference to Aspose.Cells to your project, for example by requiring the package as follows:
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. **Apply conditional formatting based on cell value**.
   Below is the code used to accomplish the task. It applies conditional formatting on a cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


When the above code is executed, conditional formatting is applied to cell “A1” in the first worksheet of the output file (output.xls). The conditional formatting applied to A1 depends on the cell value. If the cell value of A1 is between 50 and 100 the background color is red due to the conditional formatting applied.

## **Using Aspose.Cells to Apply Conditional Formatting Based on Formula**

1. Applying conditional formatting depending on formula (Code Snippet)
   Below is the code to accomplish the task. It applies conditional formatting on B3.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

When the above code is executed, conditional formatting is applied to cell “B3” in the first worksheet of the output file (output.xls). The conditional formatting applied depends on the formula which calculates the value of “B3” as the sum of B1 & B2.

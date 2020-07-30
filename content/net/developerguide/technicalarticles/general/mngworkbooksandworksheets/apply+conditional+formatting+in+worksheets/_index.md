---
title : "Apply Conditional Formatting in Worksheets" 
description : "" 
weight : 20434 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/apply+conditional+formatting+in+worksheets/
---

# Aspose.Cells for .NET : Apply Conditional Formatting in Worksheets


This article is designed to provide a detailed understanding of how to add conditional formatting to a range of cells in a worksheet.

Conditional formatting is an advanced feature in Microsoft Excel that allows you to apply formats to a range of cells, and have that formatting change depending on the value of the cell or the value of a formula. For example, the background of a cell may be red to highlight a negative value, or the text color might be green for a positive value. When the value of the cell meets the format condition, the format is applied. If the value of the cell does not meet the format condition, the cell's default formatting is used.

It's possible to apply conditional formatting with Microsoft Office Automation but that has its drawbacks. There are several reasons and issues involved: for example, security, stability, scalability and speed. The main reason for finding another solution is that Microsoft themselves strongly recommends against Office Automation for software solutions.

This article shows how to create a console application, add conditional formatting on cells with a few simplest lines of code using the Aspose.Cells API.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Aspose.Cells to Apply Conditional Formatting Based on Cell Value](#using-aspose.cells-to-apply-conditional-formatting-based-on-cell-value)
*   2 [Using Aspose.Cells to Apply Conditional Formatting Based on Formula](#using-aspose.cells-to-apply-conditional-formatting-based-on-formula)
{{< /panel >}}
 

 

## Using Aspose.Cells to Apply Conditional Formatting Based on Cell Value

1.  **Download and Install Aspose.Cells**.
    1.  Download Aspose.Cells for .NET.
2.  Install it on your development computer.  
    All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
3.  **Create a project**.  
    Start Visual Studio.NET and create a new console application. This example creates a C# console application, but you can use VB.NET too.
4.  **Add references**.  
    Add a reference to Aspose.Cells to your project, for example add a reference to ….\\Program Files\\Aspose\\Aspose.Cells\\Bin\\Net1.0\\Aspose.Cells.dll
5.  \*Apply conditional formatting based on cell value.  
    Below is the code used to accomplish the task. I applies conditional formatting on a cell.

When the above code is executed, conditional formatting is applied to cell “A1” in first worksheet of the output file (output.xls). The conditional formatting applied to A1 depends on the cell value. If the cell value of A1 is between 50 and 100 the background color is red due to the conditional formatting applied.

## Using Aspose.Cells to Apply Conditional Formatting Based on Formula

1.  Applying conditional formatting depending on formula (Code Snippet)  
    Below is the code to accomplish the task. It applies conditional formatting on B3.

  
When the above code is executed, conditional formatting is applied to cell “B3” in the first worksheet of the output file (output.xls). The conditional formatting applied depends on the formula which calculates the value of “B3” as sum of B1 & B2.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Apply Conditional Formatting in Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5017697/5112178.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Apply Conditional Formatting in Worksheets-002.png](https://docs2.aspose.com/cells/net/attachments/5017697/5112177.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Apply Conditional Formatting in Worksheets-003.png](https://docs2.aspose.com/cells/net/attachments/5017697/5112176.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Apply Conditional Formatting in Worksheets-004.png](https://docs2.aspose.com/cells/net/attachments/5017697/5112175.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Apply Conditional Formatting in Worksheets-005.png](https://docs2.aspose.com/cells/net/attachments/5017697/5112174.png) (image/png)  


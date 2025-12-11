---  
title: Apply Conditional Formatting in Worksheets  
description: How to use Aspose.Cells for Python via .NET library to apply conditional formatting in worksheets. By adjusting these criteria, you have more control over how cells look and appear.  
keywords: Aspose.Cells, Conditional Formatting, Python, Worksheet, Formatting  
type: docs  
weight: 130  
url: /python-net/apply-conditional-formatting-in-worksheets/  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

{{% alert color="primary" %}}  

This article is designed to provide a detailed understanding of how to add conditional formatting to a range of cells in a worksheet.  

Conditional formatting is an advanced feature in Microsoft Excel that allows you to apply formats to a range of cells, and have that formatting change depending on the value of the cell or the value of a formula. For example, the background of a cell may be red to highlight a negative value, or the text color might be green for a positive value. When the value of the cell meets the format condition, the format is applied. If the value of the cell does not meet the format condition, the cell's default formatting is used.  

It's possible to apply conditional formatting with Microsoft Office Automation, but that has its drawbacks. There are several reasons and issues involved: for example, security, stability, scalability, and speed. The main reason for finding another solution is that Microsoft itself strongly recommends against Office Automation for software solutions.  

This article shows how to create a console application, add conditional formatting to cells with a few simple lines of code using the Aspose.Cells API.  

{{% /alert %}}  

## **Using Aspose.Cells to Apply Conditional Formatting Based on Cell Value**  

1. **Download and Install Aspose.Cells**.  
   1. Download Aspose.Cells for Python via .NET.  
2. Install it on your development computer.  
   All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.  
3. **Create a project**.  
   Start Visual Studio.NET and create a new console application. This example creates a Python console application, but you can use VB.NET too.  
4. **Add references**.  
   Add a reference to Aspose.Cells to your project.  
5. **Apply conditional formatting based on cell value**.  
   Below is the code used to accomplish the task. It applies conditional formatting to a cell.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingCellValue-1.py" >}}  

When the above code is executed, conditional formatting is applied to cell “A1” in the first worksheet of the output file (output.xls). The conditional formatting applied to A1 depends on the cell value. If the cell value of A1 is between 50 and 100, the background color is red due to the conditional formatting applied.  

## **Using Aspose.Cells to Apply Conditional Formatting Based on Formula**  

1. Applying conditional formatting depending on a formula (Code Snippet)  
   Below is the code to accomplish the task. It applies conditional formatting to B3.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingFormula-1.py" >}}  

When the above code is executed, conditional formatting is applied to cell “B3” in the first worksheet of the output file (output.xls). The conditional formatting applied depends on the formula which calculates the value of “B3” as the sum of B1 and B2.  

{{< app/cells/assistant language="python-net" >}}

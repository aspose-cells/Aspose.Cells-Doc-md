+++
title = "Conditional Formatting" 
description = "" 
weight = 12194 
+++

Aspose.Cells for .NET : Conditional Formatting  

# Aspose.Cells for .NET : Conditional Formatting


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#ConditionalFormatting-Introduction)
*   2 [Applying Conditional Formatting](#ConditionalFormatting-ApplyingConditionalFormatting)
    *   2.1 [Using Designer Spreadsheet](#ConditionalFormatting-UsingDesignerSpreadsheet)
    *   2.2 [Using the Copy Method](#ConditionalFormatting-UsingtheCopyMethod)
*   3 [Applying Conditional Formatting at Runtime](#ConditionalFormatting-ApplyingConditionalFormattingatRuntime)
    *   3.1 [Set Font](#ConditionalFormatting-SetFont)
    *   3.2 [Set Border](#ConditionalFormatting-SetBorder)
    *   3.3 [Set Pattern](#ConditionalFormatting-SetPattern)
{{< /panel >}}
 

## Introduction

Conditional formatting is an advanced Microsoft Excel feature that allows you to apply formats to a cell or range of cells and have that formatting change depending on the value of the cell or the value of a formula. For example, you can have a cell appear bold only when the value of the cell is greater than 500. When the value of the cell meets the condition, the specified format is applied to the cell. If the value of the cell does not meet the format condition, the cell's default formatting is used. In Microsoft Excel, select **Format**, then **Conditional Formatting** to open the Conditional Formatting dialog.

Aspose.Cells supports applying conditional formatting to cells at runtime. This article explains how. It also explains how to calculate the color used by Excel for color scale conditional formatting.

## Applying Conditional Formatting

Aspose.Cells supports conditional formatting in several ways:

*   Using designer spreadsheet
*   Using the copy method.
*   Creating conditional formatting at runtime.

### Using Designer Spreadsheet

Developers can create a designer spreadsheet that contains conditional formatting in Microsoft Excel and then open that spreadsheet with Aspose.Cells. Aspose.Cells loads and saves the designer spreadsheet, keeping any conditional formatting setting.

### Using the Copy Method

Aspose.Cells allows developers to copy conditional format settings from one cell to another in the worksheet by calling the [Range.Copy()](https://apireference.aspose.com/net/cells/aspose.cells/range/methods/copy/index) method.

## Applying Conditional Formatting at Runtime

Aspose.Cells lets you both add and remove conditional formatting at runtime. The code samples below show how to set conditional formatting:

1.  Instantiate a workbook.
2.  Add an empty conditional format.
3.  Set the range that the formatting should apply to.
4.  Define the formatting conditions.
5.  Save the file.

After this example comes a number of other smaller examples that show how to apply font settings, borders settings, and patterns.

Microsoft Excel 2007 added more advanced conditional formatting that Aspose.Cells also support. The examples here, illustrate how to use simple formatting, the Microsoft Excel 2007 examples show how to apply more advanced conditional formatting.

### Set Font

You can only change font style, text color, underline style, and strikeout style.

### Set Border

You can only use thin line styles to the outline border. Diagonal lines are not allowed.

### Set Pattern


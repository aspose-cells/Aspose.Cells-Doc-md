---
title: Set Conditional Formats of Excel and ODS files.
linktitle: Conditional Formats
type: docs
weight: 60
url: /net/conditional-formatting/
description: How to apply conditional formats to Excel and ODS files in CSharp.
keywords: apply conditional formats 
---

## **Introduction**

Conditional formatting is an advanced Microsoft Excel feature that allows you to apply formats to a cell or range of cells and have that formatting change depending on the value of the cell or the value of a formula. For example, you can have a cell appear bold only when the value of the cell is greater than 500. When the value of the cell meets the condition, the specified format is applied to the cell. If the value of the cell does not meet the format condition, the cell's default formatting is used. In Microsoft Excel, select **Format**, then **Conditional Formatting** to open the Conditional Formatting dialog.

Aspose.Cells supports applying conditional formatting to cells at runtime. This article explains how. It also explains how to calculate the color used by Excel for color scale conditional formatting.

## **Applying Conditional Formatting**

Aspose.Cells supports conditional formatting in several ways:

- Using designer spreadsheet
- Using the copy method.
- Creating conditional formatting at runtime.

### **Using Designer Spreadsheet**

Developers can create a designer spreadsheet that contains conditional formatting in Microsoft Excel and then open that spreadsheet with Aspose.Cells. Aspose.Cells loads and saves the designer spreadsheet, keeping any conditional formatting setting.

### **Using the Copy Method**

Aspose.Cells allows developers to copy conditional format settings from one cell to another in the worksheet by calling the [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Applying Conditional Formatting at Runtime**

Aspose.Cells lets you both add and remove conditional formatting at runtime. The code samples below show how to set conditional formatting:

1. Instantiate a workbook.
1. Add an empty conditional format.
1. Set the range that the formatting should apply to.
1. Define the formatting conditions.
1. Save the file.

After this example comes a number of other smaller examples that show how to apply font settings, borders settings, and patterns.

Microsoft Excel 2007 added more advanced conditional formatting that Aspose.Cells also support. The examples here, illustrate how to use simple formatting, the Microsoft Excel 2007 examples show how to apply more advanced conditional formatting.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Set Font**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

You can only change font style, text color, underline style, and strikeout style.

{{% /alert %}}

### **Set Border**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

You can only use thin line styles to the outline border. Diagonal lines are not allowed.

{{% /alert %}}

### **Set Pattern**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Advance topics**
- [Adding 2-Color Scale and 3-Color Scale Conditional Formattings](/cells/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Apply Advanced Conditional Formatting](/cells/net/apply-advanced-conditional-formatting/)
- [Apply Conditional Formatting in Worksheets](/cells/net/apply-conditional-formatting-in-worksheets/)
- [Apply Shading to Alternate Rows and Columns with Conditional Formatting](/cells/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generate Conditional Formatting DataBars Images](/cells/net/generate-conditional-formatting-databars-images/)
- [Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting](/cells/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
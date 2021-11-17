---
title: Modify an Existing Style
type: docs
weight: 40
url: /net/modify-an-existing-style/
---

{{% alert color="primary" %}}

To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns etc., named and stored as a set. When applied, all of the formatting in that style are applied.

You can also use an existing style, save it with the workbook and use to format information with the same attributes.

When cells aren't explicitly formatted, the **Normal** style (the workbook's default style) is applied. Microsoft Excel predefines several styles in addition to the Normal style including Comma, Currency, and Percent.

Aspose.Cells allows modifying any of these styles or any other style that you define with your desired attributes.

{{% /alert %}}

## **Using Microsoft Excel**

To update a style in Microsoft Excel 97-2003:

1. On the **Format** menu, click **Style**.
1. Select the style you want to modify from the **Style name** list.
1. Click **Modify**.
1. Select the style options that you want using the tabs in the Format Cells dialog.
1. Click **OK**.
1. Under **Style includes**, specify the style features you want.
1. Click **OK** to save the style and apply it to the selected range.

## **Using Aspose.Cells**

The following examples demonstrate how to use [**Style.Update**](https://apireference.aspose.com/cells/net/aspose.cells/style/methods/update) method.

### **Creating and Modifying a Style**

This example creates a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object, applies it to a range of cells and modifies the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object. The modifications are automatically applied to the cell and the range the style was applied to.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modifying an Existing Style**

This example uses a simple template Excel file in which a style called Percent has already been applied to a range. The example:

1. gets the style,
1. creates a style object and
1. modifies the style formatting.

The modifications are automatically applied to the range the style was applied to.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}

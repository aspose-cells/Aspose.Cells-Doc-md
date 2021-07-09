---
title: Modify an Existing Style
type: docs
weight: 50
url: /java/modify-an-existing-style/
description: Learn how to change styles in Excel with Microsoft Excel and with Aspose.Cells for Java API.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---

{{% alert color="primary" %}}

To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns, etc., named and stored as a set. When applied, all of the formatting in that style are applied.

You can also use an existing style, save it with the workbook and use it to format information with the same attributes.

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

Aspose.Cells provides the [**Style.update**](https://apireference.aspose.com/cells/java/com.aspose.cells/style#update()) method for updating an existing style.

To change a named style, whether created dynamically using Aspose.Cells or predefined, call the [**Style.update**](https://apireference.aspose.com/cells/java/com.aspose.cells/style#update()) method to reflect any changes in style applied to a cell or range.

The [**Style.update**](https://apireference.aspose.com/cells/java/com.aspose.cells/style#update()) method behaves like the **OK** button in the Style dialog: after making changes to an existing style, call to implement the change. If you have already applied a style to a range of cells, modify the style attributes and call the method, the formatting of those cells is updated automatically

### **Creating and Modifying a Style**

This example creates a style object, applies it to a range of cells and modifies the style object. The modifications are automatically applied to the cell and the range the style was applied to.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modifying an Existing Style**

This example uses a simple template Excel file in which a style called Percent has already been applied to a range. The example:

1. gets the style,
1. creates a style object and
1. modifies the style formatting.

The modifications are automatically applied to the range the style was applied to.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}

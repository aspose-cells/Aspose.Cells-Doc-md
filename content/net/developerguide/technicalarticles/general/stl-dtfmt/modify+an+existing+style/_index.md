---
title : "Modify an Existing Style" 
description : "" 
weight : 20397 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/stl-dtfmt/modify+an+existing+style/
---

# Aspose.Cells for .NET : Modify an Existing Style


To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns etc., named and stored as a set. When applied, all of the formatting in that style are applied.

You can also use an existing style, save it with the workbook and use to format information with the same attributes.

When cells aren't explicitly formatted, the **Normal** style (the workbook's default style) is applied. Microsoft Excel predefines several styles in addition to the Normal style including Comma, Currency, and Percent.

Aspose.Cells allows modifying any of these styles or any other style that you define with your desired attributes.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Microsoft Excel](#using-microsoft-excel)
*   2 [Using Aspose.Cells](#using-aspose.cells)
    *   2.1 [Creating and Modifying a Style](#creating-and-modifying-a-style)
    *   2.2 [Modifying an Existing Style](#modifying-an-existing-style)
{{< /panel >}}
 

 

## Using Microsoft Excel

To update a style in Microsoft Excel 97-2003:

1.  On the **Format** menu, click **Style**.
2.  Select the style you want to modify from the **Style name** list.
3.  Click **Modify**.
4.  Select the style options that you want using the tabs in the Format Cells dialog.
5.  Click **OK**.
6.  Under **Style includes**, specify the style features you want.
7.  Click **OK** to save the style and apply it to the selected range.

## Using Aspose.Cells

The following examples demonstrate how to use [Style.Update](https://apireference.aspose.com/net/cells/aspose.cells/style/methods/update) method.

### Creating and Modifying a Style

This example creates a [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object, applies it to a range of cells and modifies the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object. The modifications are automatically applied to the cell and the range the style was applied to.

### Modifying an Existing Style

This example uses a simple template Excel file in which a style called Percent has already been applied to a range. The example:

1.  gets the style,
2.  creates a style object and
3.  modifies the style formatting.

The modifications are automatically applied to the range the style was applied to.


---
title: Format cells
linktitle: Format cells
type: docs
weight: 125
url: /net/cells-formatting/
aliases: [/net/data-formatting/,/net/format-cells-using-getstyle-and-setstyle-methods/,/net/data-formatting-selected-characters]
description: Set number format, border and background color for Excel files on .NET Framework, .NET Core, Mono or Xamarin Platforms.
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells provides the [**GetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) and [**SetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) methods of the [Cell](https://apireference.aspose.com/cells/net/aspose.cells/cell) class, used to get/set the formatting style of a cell. Aspose.Cells also provides a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) class.

{{% /alert %}}

## **Format Cells using GetStyle and SetStyle Methods**

Apply different kinds of formatting styles on cells to set background or foreground colors, borders, fonts, horizontal and vertical alignments, indentation level, text direction, rotation angle and much more.

### **Using the GetStyle and SetStyle Methods**

If developers need to apply different formatting styles to different cells then it's better to get the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) of the cell using [**Cell.GetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) method, specify the style attributes and then apply the formatting using [**Cell.SetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) method. An example is given below to demonstrate this approach to apply various formatting on a cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Using Style Object to Format Different Cells**

If developers need to apply the Same formatting style to different cells then they can use [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object. Please follow the steps below to use the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object:

1. Add a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object by calling the [**CreateStyle**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) method of the [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class
1. Access the newly added [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object
1. Set the desired properties/attributes of the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to apply desired formatting settings
1. Assign the configured [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to your desired cells

This approach can greatly improve the efficiency of your applications and save memory too.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Using Microsoft Excel 2007 Predefined Styles**

If you need to apply different formatting styles for Microsoft Excel 2007, apply styles using the Aspose.Cells API. An example is given below to demonstrate this approach to apply a predefined style on a cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Formatting Selected Characters in a Cell**

Dealing with Font Settings explains how to format text in cells, but it only explains how to format all of the cell content. What if you want to format only selected characters?

Aspose.Cells supports this feature too. This topic explains how to we use this feature effectively.

### **Formatting Selected Characters**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains the [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Each item in the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection represents an object of the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class.

The [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class provides the [**Characters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/characters) method that takes the following parameters to select a range of characters inside a cell:

- **Start Index**, the index of the character that the selection starts from.
- **Number of Characters**, the number of characters to select.

The [**Characters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/characters) method returns an instance of the [**FontSetting**](https://apireference.aspose.com/cells/net/aspose.cells/fontsetting) class that allows developers to format the characters in the same way as they would a cell as shown below in the code example. In the output file, in the A1 cell, the word 'Visit' will be formatted with the default font but 'Aspose!' is bold and blue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

If you are interested in formatting a portion of Rich Text in a cell, consider using the [**Cell.GetCharacters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) methods. The [[**Cell.GetCharacters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) method is to be used to access the portions of the text and then amendments can be done using the [**Cell.SetCharacters**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) method whereas the **Get** method returns an array of [**FontSetting**](https://apireference.aspose.com/cells/net/aspose.cells/fontsetting) objects which can be manipulated to set various properties such as font name, font color, boldness, etc. and **Set** method can be used to apply the changes.

{{% /alert %}}

## **Formatting Rows and Columns**

Sometimes, developers need to apply the same formatting on rows or columns. Applying formatting on cells one by one often takes longer and is not a good solution.
To address this issue, Aspose.Cells provides a simple, fast way discussed in detail in this article.

### **Formatting Rows & Columns**

Aspose.Cells provides a class, the [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection provides a [**Rows**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/rows) collection.

### **Formatting a Row**

Each item in the [**Rows**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/rows) collection represents a [**Row**](https://apireference.aspose.com/cells/net/aspose.cells/row) object. The [**Row**](https://apireference.aspose.com/cells/net/aspose.cells/row) object offers the [**ApplyStyle**](https://apireference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) method used to set the row's formatting. To apply the same formatting to a row, use the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object. The steps below show how to use it.

1. Add a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to the [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class by calling its [**CreateStyle**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) method.
1. Set the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object's properties to apply formatting settings.
1. Make the relevant attributes ON for the [**StyleFlag**](https://apireference.aspose.com/cells/net/aspose.cells/styleflag) object.
1. Assign the configured [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to the [**Row**](https://apireference.aspose.com/cells/net/aspose.cells/row) object.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Formatting a Column**

The [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection also provides a [**Columns**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collection. Each item in the [**Columns**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collection represents a [**Column**](https://apireference.aspose.com/cells/net/aspose.cells/column) object. Similar to a [**Row**](https://apireference.aspose.com/cells/net/aspose.cells/row) object, the [**Column**](https://apireference.aspose.com/cells/net/aspose.cells/column) object also offers the [**ApplyStyle**](https://apireference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) method for formatting a column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Advance topics**
- [Access and Update the Portions of Rich Text of Cell](/cells/net/access-and-update-the-portions-of-rich-text-of-cell/)
- [Alignment Settings](/cells/net/cells-alignment-settings/)
- [Border Settings](/cells/net/cells-border-settings/)
- [Create Style object using CellsFactory class](/cells/net/create-style-object-using-cellsfactory-class/)
- [Excel Themes and Colors](/cells/net/excel-themes-and-colors/)
- [Fill Settings](/cells/net/cells-fill-settings/)
- [Font Settings](/cells/net/cells-font-settings/)
- [Format and Modify Named Ranges](/cells/net/format-and-modify-named-ranges/)
- [Modify an Existing Style](/cells/net/modify-an-existing-style/)
- [Number Settings](/cells/net/cells-number-settings/)
- [Using Built-in Styles](/cells/net/using-built-in-styles/)


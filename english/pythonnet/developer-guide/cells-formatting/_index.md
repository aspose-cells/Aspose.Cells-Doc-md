---
title: Format cells
description: Learn how to format and style cells in Aspose.Cells for Python via .NET, including number formatting, date formatting, font styles, and other cell style options. Our guide will help you create attractive and professional-looking spreadsheets.
keywords: Aspose.Cells for Python via .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Format cells
type: docs
weight: 120
url: /python-net/cells-formatting/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides the [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) and [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) methods of the [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class, used to get/set the formatting style of a cell. Aspose.Cells for Python via .NET also provides a [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) class.

{{% /alert %}}

## **How to Format Cells using GetStyle and SetStyle Methods**

Apply different kinds of formatting styles to cells to set background or foreground colors, borders, fonts, horizontal and vertical alignments, indentation level, text direction, rotation angle, and much more.

### **How to Use the GetStyle and SetStyle Methods**

If developers need to apply different formatting styles to different cells, then it's better to get the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) of the cell using [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) method, specify the style attributes, and then apply the formatting using [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) method. An example is given below to demonstrate this approach to apply various formatting to a cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **How to Use Style Object to Format Different Cells**

If developers need to apply the same formatting style to different cells, then they can use a [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object. Please follow the steps below to use the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object:

1. Add a [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object by calling the [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) method of the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class  
1. Access the newly added [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object  
1. Set the desired properties/attributes of the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object to apply the required formatting settings  
1. Assign the configured [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object to your desired cells  

This approach can greatly improve the efficiency of your applications and save memory, too.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **How to Use Microsoft Excel 2007 Predefined Styles**

If you need to apply different formatting styles for Microsoft Excel 2007, you can apply styles using the Aspose.Cells for Python via .NET API. An example is given below to demonstrate this approach to apply a predefined style on a cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **How to Format Selected Characters in a Cell**

Dealing with Font Settings explains how to format text in cells, but it only explains how to format all of the cell content. What if you want to format only selected characters?

Aspose.Cells for Python via .NET supports this feature too. This topic explains how to use this feature effectively.

### **How to Format Selected Characters**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains the **worksheets** collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a **cells** collection. Each item in the **cells** collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.

The [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class provides the **characters** method that takes the following parameters to select a range of characters inside a cell:

- **Start Index**, the index of the character that the selection starts from.  
- **Number of Characters**, the number of characters to select.  

The **characters** method returns an instance of the [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) class that allows developers to format the characters in the same way as they would format a cell, as shown below in the code example. In the output file, in the A1 cell, the word *Visit* will be formatted with the default font but *Aspose!* is bold and blue.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

If you are interested in formatting a portion of rich text in a cell, consider using the [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) & [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) methods. The **Cell.get_characters** method is used to access portions of the text, and then modifications can be made using the **Cell.set_characters** method, whereas the **Get** method returns an array of [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objects which can be manipulated to set various properties such as font name, font color, boldness, etc., and the **Set** method can be used to apply the changes.

{{% /alert %}}

## **How to Format Rows and Columns**

Sometimes, developers need to apply the same formatting to rows or columns. Applying formatting to cells one by one often takes longer and is not an efficient solution.  
To address this issue, Aspose.Cells for Python via .NET provides a simple, fast way discussed in detail in this article.

### **Formatting Rows & Columns**

Aspose.Cells for Python via .NET provides a class, the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a **worksheets** collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a **cells** collection. The **cells** collection provides a **rows** collection.

### **How to Format a Row**

Each item in the **rows** collection represents a **Row** object. The **Row** object offers the **apply_style** method used to set the row's formatting. To apply the same formatting to a row, use the **Style** object. The steps below show how to use it.

1. Add a **Style** object to the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class by calling its **create_style** method.  
1. Set the **Style** object's properties to apply formatting settings.  
1. Make the relevant attributes ON for the **StyleFlag** object.  
1. Assign the configured **Style** object to the **Row** object.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **How to Format a Column**

The **cells** collection also provides a **columns** collection. Each item in the **columns** collection represents a **Column** object. Similar to a **Row** object, the **Column** object also offers the **apply_style** method for formatting a column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Advanced topics**
- [Alignment Settings](/cells/python-net/cells-alignment-settings/)
- [Border Settings](/cells/python-net/cells-border-settings/)
- [Set Conditional Formats of Excel and ODS files.](/cells/python-net/conditional-formatting/)
- [Excel Themes and Colors](/cells/python-net/excel-themes-and-colors/)
- [Fill Settings](/cells/python-net/cells-fill-settings/)
- [Font Settings](/cells/python-net/cells-font-settings/)
- [Format Worksheet Cells in a Workbook](/cells/python-net/format-worksheet-cells-in-a-workbook/)
- [Implement 1904 Date System](/cells/python-net/implement-1904-date-system/)
- [Merging and Unmerging Cells](/cells/python-net/merging-and-unmerging-cells/)
- [Number Settings](/cells/python-net/cells-number-settings/)
- [Get and Set Style for cells](/cells/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="python-net" >}}

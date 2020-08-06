---
title: Data Formatting
type: docs
weight: 100
url: /net/data-formatting/
---

## **Introduction**
Properly formatting worksheet cells makes it easier for users to read the data. There are multiple ways to format cells and their contents. The simplest way is to use Microsoft Excel in a WYSIWYG environment and create a designer spreadsheet. Another way to format cells and their contents is to use the Aspose.Cells API. This topic describes two approaches to format cells and their contents with the use of Aspose.Cells API.
## **Format Data in Cells**
Developers can format cells and their contents using the flexible API of Aspose.Cells. Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.
## **Setting Display Formats of Numbers and Dates**
A very strong feature of Microsoft Excel is that it allows users to set the display formats of numeric values and dates. We know that numeric data can be used to represent different values including decimal, currency, percentage, fraction or accounting values, etc. All these numerical values are displayed in different formats depending on the type of information it represents. Similarly, there are many formats in which a date or time can be displayed.
Aspose.Cells supports this functionality and allows developers to set any display format for a number or date.
### **Setting Display Formats in Microsoft Excel**
To set display formats in Microsoft Excel:

1. Right-click any cell.
1. Select **Format Cells**. A dialog will appear that is used to set the display formats of any kind of value.

In the left side of the dialog, there are many categories of values like **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage,** etc. Aspose.Cells supports all of these display formats.

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

Aspose.Cells provides [GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle) and [SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle) methods for the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class. These methods are used to get and set a cell's formatting. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) class provides some useful properties for dealing with the display formats of numbers and dates.
### **Using Built-in Number Formats**
Aspose.Cells offers some built-in number formats to configure the display formats of the numbers and dates. These built-in number formats can be applied by using the [Number](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/number) property of the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object. All built-in number formats are given unique numeric values. Developers can assign any desired numeric value to the [Number](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/number) property of the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object to apply the display format. This approach is fast. The built-in number formats supported by Aspose.Cells are listed below.

|**Value**|**Type**|**Format String**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}
### **Using Custom Number Formats**
To define your own customized format string for setting the display format, use the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [Custom](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/custom) property. This approach is not as fast as using pre-set formats but it is more flexible.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}} 

If you use the [Custom](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/custom) property to set the number format, any previous format set using the [Number](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/number) property is overridden and vice versa.

{{% /alert %}} 
## **Formatting Selected Characters in a Cell**
Dealing with Font Settings explains how to format text in cells, but it only explains how to format all of the cell content. What if you want to format only selected characters?

Aspose.Cells supports this feature too. This topic explains how to we use this feature effectively.
### **Formatting Selected Characters**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains the [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

The [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class provides the [Characters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/characters) method that takes the following parameters to select a range of characters inside a cell:

- **Start Index**, the index of the character that the selection starts from.
- **Number of Characters**, the number of characters to select.

The [Characters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/characters) method returns an instance of the [FontSetting](https://apireference.aspose.com/net/cells/aspose.cells/fontsetting) class that allows developers to format the characters in the same way as they would a cell as shown below in the code example. In the output file, in the A1 cell, the word 'Visit' will be formatted with the default font but 'Aspose!' is bold and blue.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}} 

If you are interested in formatting a portion of Rich Text in a cell, consider using the [Cell.GetCharacters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getcharacters) & [Cell.SetCharacters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setcharacters) methods. The [Cell.GetCharacters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getcharacters) method is to be used to access the portions of the text and then amendments can be done using the [Cell.SetCharacters](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setcharacters) method whereas the **Get** method returns an array of [FontSetting](https://apireference.aspose.com/net/cells/aspose.cells/fontsetting) objects which can be manipulated to set various properties such as font name, font color, boldness, etc and **Set** method can be used to apply the changes.

{{% /alert %}} 
## **Activating Sheets and Making an Active Cell in the Worksheet**
Sometimes, you need a specific worksheet to be active and displayed when a user opens a Microsoft Excel file in Excel. Similarly, you might want to activate a specific cell and set the scrollbars to show the active cell.
Aspose.Cells is capable of doing all these tasks.

An **active sheet** is a sheet you're working on: the active sheet's name on the tab is bold by default.

An **active cell** is a selected cell, the cell into which data is entered when you begin typing. Only one cell is active at a time. The active cell is highlighted by a heavy border.
### **Activating Sheets and Making a Cell Active**
Aspose.Cells provides specific API calls for activating a sheet and a cell. For Example, the [Aspose.Cells.WorksheetCollection.ActiveSheetIndex](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/properties/activesheetindex) property is useful for setting the active sheet in a workbook.
Similarly, [Aspose.Cells.Worksheet.ActiveCell](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/activecell) property is used to set and get an active cell in the worksheet.

To make sure that the horizontal or vertical scrollbars are at the row and column index position you want to show specific data, use the [Aspose.Cells.Worksheet.FirstVisibleRow](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/firstvisiblerow) and [Aspose.Cells.Worksheet.FirstVisibleColumn](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/firstvisiblecolumn) properties.

The following example shows how to activate a worksheet and make an active cell in it. In the generated output, the scrollbars will be scrolled to make the 2nd row and 2nd column as their first visible row and column.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}
## **Formatting Rows and Columns**
Sometimes, developers need to apply the same formatting on rows or columns. Applying formatting on cells one by one often takes longer and is not a good solution.
To address this issue, Aspose.Cells provides a simple, fast way discussed in detail in this article.
### **Formatting Rows & Columns**
Aspose.Cells provides a class, the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection provides a [Rows](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/rows) collection.
### **Formatting a Row**
Each item in the [Rows](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/rows) collection represents a [Row](https://apireference.aspose.com/net/cells/aspose.cells/row) object. The [Row](https://apireference.aspose.com/net/cells/aspose.cells/row) object offers the [ApplyStyle](https://apireference.aspose.com/net/cells/aspose.cells/row/methods/applystyle) method used to set the row's formatting. To apply the same formatting to a row, use the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object. The steps below show how to use it.

1. Add a [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object to the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class by calling its [CreateStyle](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/createstyle) method.
1. Set the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's properties to apply formatting settings.
1. Make the relevant attributes ON for the [StyleFlag](https://apireference.aspose.com/net/cells/aspose.cells/styleflag) object.
1. Assign the configured [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object to the [Row](https://apireference.aspose.com/net/cells/aspose.cells/row) object.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}
### **Formatting a Column**
The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection also provides a [Columns](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/columns) collection. Each item in the [Columns](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/columns) collection represents a [Column](https://apireference.aspose.com/net/cells/aspose.cells/column) object. Similar to a [Row](https://apireference.aspose.com/net/cells/aspose.cells/row) object, the [Column](https://apireference.aspose.com/net/cells/aspose.cells/column) object also offers the [ApplyStyle](https://apireference.aspose.com/net/cells/aspose.cells/column/methods/applystyle) method for formatting a column.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

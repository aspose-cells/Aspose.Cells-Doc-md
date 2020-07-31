---
title : "Named Ranges" 
description : "" 
weight : 12174 
toc : false
type: docs
url: /java/developerguide/data/named+ranges/
---

# Aspose.Cells for Java : Named Ranges



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating a Named Range](#creating-a-named-range)
    *   1.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   1.2 [Using Aspose.Cells](#using-aspose.cells)
        *   1.2.1 [Accessing All Named Ranges in a Spreadsheet](#accessing-all-named-ranges-in-a-spreadsheet)
        *   1.2.2 [Access a Specific Named Range](#access-a-specific-named-range)
        *   1.2.3 [Identify Cells in a Named Range](#identify-cells-in-a-named-range)
        *   1.2.4 [Input Data into the Cells in the Named Range](#input-data-into-the-cells-in-the-named-range)
        *   1.2.5 [Format Ranges...Setting Background Color and Font Attributes to a Named Range](#format-ranges...setting-background-color-and-font-attributes-to-a-named-range)
        *   1.2.6 [Format Ranges...Adding Borders to a Named Range](#format-ranges...adding-borders-to-a-named-range)
        *   1.2.7 [Apply style to cells in a Range](#apply-style-to-cells-in-a-range)
        *   1.2.8 [Remove a Named Range](#remove-a-named-range)
{{< /panel >}}
 

Normally, column and row labels are used to refer to individual cells. It is possible to create descriptive names to represent cells, ranges of cells, formulas, or constant values. The word **name** may refer to a string of characters that represents a cell, range of cells, formula, or a constant value. Assigning a name to a range means that that range of cells can be referred to by its name. Use easy-to-understand names, such as Products, to refer to hard to understand ranges, such as Sales!C20:C30. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. \*Named ranges are among the most powerful features of Microsoft Excel, especially when used as the source range for list controls, pivot tables, charts and so on.

### Creating a Named Range

#### Using Microsoft Excel

The following steps describe how to name a cell or range of cells using Microsoft Excel. This method applies to Microsoft Office Excel 2003, Microsoft Excel 97, 2000, and 2002.

1.  Select the cell, range of cells that you want to name.
2.  Click the Name Box at the left end of the formula bar.
3.  Type the name for the cells.
4.  Press ENTER.

You cannot name a cell while you are changing the contents of the cell.

#### Using Aspose.Cells

Here, we use the Aspose.Cells API to do the task.

Aspose.Cells provides a class, [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook), that represents a Microsoft Excel file. The [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) class contains a [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection) that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection.

It is possible to create a named range by calling the overloaded [createRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#createRange(java.lang.String,%20java.lang.String)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. A typical version of the [createRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#createRange(java.lang.String,%20java.lang.String)) method takes the following parameters:

*   Name of the upper-left cell, the name of the top-left cell in the range.
*   Name of the lower right cell, the name of the bottom right cell in the range.

When the [createRange](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#createRange(java.lang.String,%20java.lang.String)) method is called, it returns the newly created named range as an instance of [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) class.

The following example shows how to create a named range of cells that extends over B4:G14.

##### Accessing All Named Ranges in a Spreadsheet

Call the [getNamedRanges](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#getNamedRanges()) method of the [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection) to get all named ranges in a spreadsheet. The [getNamedRanges](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#getNamedRanges()) method returns an array of all named ranges in the [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection).

The following example shows how to access all the named ranges in a workbook.

##### Access a Specific Named Range

Call the [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection) collection's [getRangeByName](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#getRangeByName(java.lang.String)) method to get a specified range by name. A typical [getRangeByName](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheetcollection#getRangeByName(java.lang.String)) method takes the name of the named range and returns the specified named range as an instance of the [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) class.

The following example shows how to access a specified range by its name.

##### Identify Cells in a Named Range

Using Aspose.Cells, you can insert data into the individual cells of a range. Suppose, you have a named range of cells.i.e., A1:C4. So the matrix would make 4 \* 3 = 12 cells and the individual range cells are arranged sequentially. Aspose.Cells provides you some useful Properties of [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) class to access the individual cells in the range. You may use the following methods to identify the cells in the range:

*   [getFirstRow](https://apireference.aspose.com/java/cells/com.aspose.cells/range#FirstRow) returns the index of the first row in the named range.
*   [getFirstColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/range#FirstColumn) returns the index of the first column in the named range.

The following example shows how to input some values into the cells of a specified range.

##### Input Data into the Cells in the Named Range

Using Aspose.Cells, you can insert data into the individual cells of a range. Suppose, you have a named range of cells i.e., H1:J4. So the matrix would make 4 \* 3 = 12 cells and the individual range cells are arranged sequentially. Aspose.Cells provides you some useful Properties of [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) class to access the individual cells in the range. You may use the following properties to identify the cells in the range:

*   [getFirstRow](https://apireference.aspose.com/java/cells/com.aspose.cells/range#FirstRow) returns the index of the first row in the named range.
*   [getFirstColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/range#FirstColumn) returns the index of the first column in the named range.

The following example shows how to input some values into the cells of a specified range.

##### Format Ranges...Setting Background Color and Font Attributes to a Named Range

To apply formatting, define a [Style](https://apireference.aspose.com/java/cells/com.aspose.cells/style) object to specify style settings and apply it to the [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) object.

The following example shows how to set solid fill color (shading color) with font settings to a range.

##### Format Ranges...Adding Borders to a Named Range

It is possible to add borders to a range of cells instead of just a single cell. The [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range) object provides a [setOutlineBorders](https://apireference.aspose.com/java/cells/com.aspose.cells/range#setOutlineBorders(int,%20com.aspose.cells.Color)) method that takes the following parameters to add a border to the range of cells:

*   borderStyle: the type of border, selected from the [CellBorderType](https://apireference.aspose.com/java/cells/com.aspose.cells/CellBorderType) enumeration.
*   borderColor: the line color of the border, selected from the [Color](https://apireference.aspose.com/java/cells/com.aspose.cells/Color) enumeration.

The following example shows how to set an outline border to a range.

  
The following output would be generated after executing the above code:  
  
![](https://docs2.aspose.com/cells/java/attachments/5276725/5473128.png)

##### Apply style to cells in a Range

Sometimes, you want to create apply a style to the cells in a [Range](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Range). For this, you may iterate over the cells in the range and use the [Cell.setStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setStyle(com.aspose.cells.Style)) method to apply the style to the cell.

The following example shows how to apply styles to cells in a Range.

##### Remove a Named Range

Aspose.Cells provides the [NameCollection.RemoveAt()](https://apireference.aspose.com/java/cells/com.aspose.cells/namecollection#removeAt(int)) method to erase the name of the range. To clear the contents of the range, use [Cells.ClearRange()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#clearRange(com.aspose.cells.CellArea)) method.  
The following example shows how to remove a named range with its contents.

`  
borderColors`


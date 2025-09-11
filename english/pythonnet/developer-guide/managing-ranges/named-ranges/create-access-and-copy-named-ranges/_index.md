---
title: Create Access and Copy Named Ranges
type: docs
weight: 200
url: /python-net/create-access-and-copy-named-ranges/
description: This article shows how to Create Access and Copy Named Ranges by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Create Access and Copy Named Ranges, Python Create Named Ranges, Python Copy Named Ranges, Python Access All the Named Ranges in a Spreadsheet.
---

## **Introduction**

Normally, column and row labels are used refer to individual cells. It is possible to create descriptive names to represent cells, ranges of cells, formulas, or constant values. The word **name** may refer to a string of characters that represents a cell, range of cells, formula, or constant value. Assigning a name to a range means that that range of cells can be referred to by its name. Use easy-to-understand names, such as Products, to refer to hard to understand ranges, such as Sales!C20:C30. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. *Named ranges are among the most powerful features of Microsoft Excel, especially when used as the source range for list controls, pivot tables, charts and so on.

## **Working with Named Range Using Microsoft Excel**

### **Create Named Ranges**

The following steps describe how to name a cell or range of cells using **MS Excel**. This method applies to **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** and **2002**.

1. Select the cell, range of cells that you want to name.
1. Click the **Name Box** at the left end of the formula bar.
1. Type the name for the cells.
1. Press ENTER.

{{% alert color="primary" %}}

You cannot name a cell while you are changing the contents of the cell.

{{% /alert %}}

## **Working with Named Range Using Aspose.Cells for Python Excel Library**

Here, we use the Aspose.Cells for Python via .NET API to do the task.
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection.

### **Create Named Range**

It is possible to create a named range by calling the overloaded [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) method of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection. A typical version of [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) method takes the following parameters:

- Name of the upper left cell, the name of the top left cell in the range.
- Name of the lower right cell, the name of the bottom right cell in the range.

When the [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) method is called, it returns the newly created range as an instance of the [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) class. Use this [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object to configure the named range. For example, set the name of the range using the [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name) property. The following example shows how to create a named range of cells that extends over B4:G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

### **Input Data into the Cells in the Named Range**

You can insert data into the individual cells of a range following the pattern

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Say you have a named range of cells that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Use the following properties to identify the cells in the range:

- FirstRow returns the index of the first row in the named range.
- FirstColumn returns the index of the first column in the named range.
- RowCount returns the total number of rows in the named range.
- ColumnCount returns the total number of columns in the named range.

The following example shows how to input some values into the cells of a specified range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

### **Identify Cells in the Named Range**

You can insert data into the individual cells of a range following the pattern:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

If you have a named range that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Use the following properties to identify the cells in the range:

- FirstRow returns the index of the first row in the named range.
- FirstColumn returns the index of the first column in the named range.
- RowCount returns the total number of rows in the named range.
- ColumnCount returns the total number of columns in the named range.

The following example shows how to input some values into the cells of a specified range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Access Named Ranges**

#### **Access a Specific Named Range**

Call the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) collection's [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) method to get a range by the specified name. A typical [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) method takes the name of the named range and returns the specified named range as an instance of the [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) class. The following example shows how to access a specified range by its name.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Access All the Named Ranges in a Spreadsheet**

Call the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) collection's [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) method to get all named ranges in a spreadsheet. The [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) method returns an array of all names ranges in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) collection.

The following example shows how to access all the named ranges in a workbook.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Copy Named Ranges**

Aspose.Cells for Python via .NET provides [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) method to copy a range of cells with formatting into another range.

The following example shows how to copy a source range of cells to another named range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
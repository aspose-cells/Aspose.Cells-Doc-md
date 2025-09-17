##Manage data of Excel files
This article describes how to view and edit data of Excel files with Aspose.Cells for Python via .NET library.
In [Accessing Cells of a Worksheet](https://docs.aspose.com/cells/python-net/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.
## **How to Add Data to Cells**
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) collection. Each item in the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.
Aspose.Cells for Python via .NET allows developers to add data to the cells in worksheets by calling the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class' [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) method. Aspose.Cells for Python via .NET provides overloaded versions of the [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) method, it is possible to add a Boolean, string, double, integer or date/time, etc. values to the cell.
## **How to Improve Efficiency**
If you use [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.
## **How to Retrieve Data from Cells**
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows access to worksheets in the file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) collection. Each item in the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.
The [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:
- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): returns the string value of the cell.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): returns the double value of the cell.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): returns the boolean value of the cell.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): returns the date/time value of the cell.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): returns the float value of the cell.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): returns the integer value of the cell.
When a field is not filled, cells with [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) or [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) throws an exception.
The type of data contained in a cell can also be checked by using the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class' [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) property. In fact, the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class' [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) property is based on the [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) enumeration whose pre-defined values are listed below:
|**Cell Value Types**|**Description**|
| :- | :- |
|IS_BOOL|Specifies that cell value is Boolean.|
|IS_DATE_TIME|Specifies that cell value is date/time.|
|IS_NULL|Represents a blank cell.|
|IS_NUMERIC|Specifies that cell value is numeric.|
|IS_STRING|Specifies that cell value is a string.|
|IS_ERROR|Specifies that cell value is an error value.|
|IS_UNKNOWN|Specifies that cell value is unknown.|
You can also use the above pre-defined cell value types to compare with the Type of data present in each cell.
While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text or date/time values. With Aspose.Cells for Python via .NET, you can get the appropriate values from the cells according to their data types.
## **Advance topics**
- [Accessing Cells of a Worksheet](https://docs.aspose.com/cells/python-net/accessing-cells-of-a-worksheet/)
- [Convert Text Numeric Data to Number](https://docs.aspose.com/cells/python-net/convert-text-numeric-data-to-number/)
- [Creating Subtotals](https://docs.aspose.com/cells/python-net/creating-subtotals/)
- [Data Filtering](https://docs.aspose.com/cells/python-net/data-filtering/)
- [Data Sorting](https://docs.aspose.com/cells/python-net/sort-data-of-excel/)
- [Data Validation](https://docs.aspose.com/cells/python-net/data-validation/)
- [Get Cell String Value with and without Formatting](https://docs.aspose.com/cells/python-net/get-cell-string-value-with-format-strategy/)
- [Adding HTML Rich Text inside the Cell](https://docs.aspose.com/cells/python-net/adding-html-rich-text-inside-the-cell/)
- [Find or Search Data](https://docs.aspose.com/cells/python-net/find-or-search-data/)
- [Insert Hyperlinks into Excel or OpenOffice](https://docs.aspose.com/cells/python-net/insert-hyperlinks-to-excel/)
- [Measure the Width and Height of the Cell Value in Unit of Pixels](https://docs.aspose.com/cells/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Conversion between cell name and row/column index](https://docs.aspose.com/cells/python-net/names-and-indices/)
- [Populate Data First by Row then by Column](https://docs.aspose.com/cells/python-net/populate-data-first-by-row-then-by-column/)
- [Preserve Single Quote Prefix of Cell Value or Range](https://docs.aspose.com/cells/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Access and Update the Portions of Rich Text of Cell](https://docs.aspose.com/cells/python-net/access-and-update-the-portions-of-rich-text-of-cell/)

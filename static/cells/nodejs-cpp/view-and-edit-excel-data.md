##Manage data of Excel files
This article describes how to view and edit data of Excel files with Aspose.Cells library for Node.js via C++.
In [Accessing Cells of a Worksheet](https://docs.aspose.com/cells/nodejs-cpp/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.
## **How to Add Data to Cells**
Aspose.Cells for Node.js via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.
Aspose.Cells allows developers to add data to the cells in worksheets by calling the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) method. Aspose.Cells provides overloaded versions of the [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) method, it is possible to add a Boolean, string, double, integer, or date/time, etc. values to the cell.
## **How to Improve Efficiency**
If you use [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.
## **How to Retrieve Data from Cells**
Aspose.Cells for Node.js via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to worksheets in the file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.
The [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:
- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): returns the string value of the cell.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): returns the double value of the cell.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): returns the boolean value of the cell.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): returns the date/time value of the cell.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): returns the float value of the cell.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): returns the integer value of the cell.
When a field is not filled, cells with [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) or [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) throws an exception.
The type of data contained in a cell can also be checked by using the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) method. In fact, the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) method is based on the [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype) enumeration whose pre-defined values are listed below:
|**Cell Value Types**|**Description**|
| :- | :- |
|IsBool|Specifies that cell value is Boolean.|
|IsDateTime|Specifies that cell value is date/time.|
|IsNull|Represents a blank cell.|
|IsNumeric|Specifies that cell value is numeric.|
|IsString|Specifies that cell value is a string.|
|IsUnknown|Specifies that cell value is unknown.|
You can also use the above pre-defined cell value types to compare with the Type of data present in each cell.
While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text, or date/time values. With Aspose.Cells, you can get the appropriate values from the cells according to their data types.
## **Advance topics**
- [Accessing Cells of a Worksheet](https://docs.aspose.com/cells/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Convert Text Numeric Data to Number](https://docs.aspose.com/cells/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Creating Subtotals](https://docs.aspose.com/cells/nodejs-cpp/creating-subtotals/)
- [Data Filtering](https://docs.aspose.com/cells/nodejs-cpp/data-filtering/)
- [Data Sorting](https://docs.aspose.com/cells/nodejs-cpp/sort-data-of-excel/)
- [Data Validation](https://docs.aspose.com/cells/nodejs-cpp/data-validation/)
- [Find or Search Data](https://docs.aspose.com/cells/nodejs-cpp/find-or-search-data/)
- [Get Cell String Value with and without Formatting](https://docs.aspose.com/cells/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Adding HTML Rich Text inside the Cell](https://docs.aspose.com/cells/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Insert Hyperlinks into Excel or OpenOffice](https://docs.aspose.com/cells/nodejs-cpp/insert-hyperlinks-to-excel/)
- [How and Where to Use Enumerators](https://docs.aspose.com/cells/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Measure the Width and Height of the Cell Value in Unit of Pixels](https://docs.aspose.com/cells/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Reading Cell Values in Multiple Threads Simultaneously](https://docs.aspose.com/cells/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion between cell name and row/column index](https://docs.aspose.com/cells/nodejs-cpp/names-and-indices/)
- [Populate Data First by Row then by Column](https://docs.aspose.com/cells/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Preserve Single Quote Prefix of Cell Value or Range](https://docs.aspose.com/cells/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Access and Update the Portions of Rich Text of Cell](https://docs.aspose.com/cells/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)

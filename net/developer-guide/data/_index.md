---
title: Data
type: docs
weight: 110
url: /net/add-and-retrieve-data/
aliases: [/net/data/]
---

{{% alert color="primary" %}}

In [Accessing Cells of a Worksheet](/cells/net/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}}

## **Adding Data to Cells**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Each item in the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection represents an object of the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method. Aspose.Cells provides overloaded versions of the [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method, it is possible to add a Boolean, string, double, integer or date/time, etc. values to the cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

### **Improving Efficiency**

If you use [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.

## **Retrieving Data from Cells**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to worksheets in the file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Each item in the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection represents an object of the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class.

The [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:

- [**StringValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): returns the string value of the cell.
- [**DoubleValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): returns the double value of the cell.
- [**BoolValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): returns the boolean value of the cell.
- [**DateTimeValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): returns the date/time value of the cell.
- [**FloatValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): returns the float value of the cell.
- [**IntValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): returns the integer value of the cell.

When a field is not filled, cells with [**DoubleValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) or [**FloatValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) throws an exception.

The type of data contained in a cell can also be checked by using the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**Type**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/type) property. In fact, the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class' [**Type**](https://apireference.aspose.com/cells/net/aspose.cells/cell/properties/type) property is based on the [**CellValueType**](https://apireference.aspose.com/cells/net/aspose.cells/cellvaluetype) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|IsBool|Specifies that cell value is Boolean.|
|IsDateTime|Specifies that cell value is date/time.|
|IsNull|Represents a blank cell.|
|IsNumeric|Specifies that cell value is numeric.|
|IsString|Specifies that cell value is a string.|
|IsUnknown|Specifies that cell value is unknown.|

You can also use the above pre-defined cell value types to compare with the Type of data present in each cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text or date/time values. With Aspose.Cells, you can get the appropriate values from the cells according to their data types.

{{% /alert %}}

## **Advance topics**
- [Accessing Cells of a Worksheet](/net/accessing-cells-of-a-worksheet/)
- [Add Signature line to the worksheet](/net/add-signature-line/)
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Create Access and Copy Named Ranges](/net/create-access-and-copy-named-ranges/)
- [Create Union Range](/net/create-union-range/)
- [Creating Subtotals](/net/creating-subtotals/)
- [Data Filtering](/net/data-filtering/)
- [Data Sorting](/net/data-sorting/)
- [Data Validation](/net/data-validation/)
- [Export Data from Worksheet](/net/export-data-from-worksheet/)
- [Export HTML String Value of the Cells to the DataTable](/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Find or Search Data](/net/find-or-search-data/)
- [Get Address Cell Count Offset Entire Column and Entire Row of the Range](/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
- [Import Data into Worksheet](/net/import-data-into-worksheet/)
- [Merging and Unmerging Cells](/net/merging-and-unmerging-cells/)
- [Precedents and Dependents](/net/precedents-and-dependents/)
- [Preserve Single Quote Prefix of Cell Value or Range](/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Rename duplicate columns automatically while exporting worksheet data](/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
- [Setting Formula for Named Range](/net/setting-formula-for-named-range/)
- [Shift First Row down when inserting Cells Data Table Rows](/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [Sort Data in Column with Custom Sort List](/net/sort-data-in-column-with-custom-sort-list/)
- [Specify Formula Fields while Importing Data to Worksheet](/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Specifying Sort Warning While Sorting Data](/net/specifying-sort-warning-while-sorting-data/)
- [Working with Hyperlinks to Link Data](/net/working-with-hyperlinks-to-link-data/)





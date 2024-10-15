---
title: Add and Retrieve Data
type: docs
weight: 20
url: /java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accessing Cells of a Worksheet](/cells/java/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}} 
## **Adding Data to Cells**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class.

Aspose.Cells allows developers to add data to cells in worksheets by calling the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class' [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) property. By using the [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) property, it is possible to add Boolean, string, double, integer or date/time, etc. values to the cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Improving Efficiency**
{{% alert color="primary" %}} 

If you use the [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) property to add a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.

{{% /alert %}} 

While working on worksheets, users may add different types of data in the cells. These data items may include boolean, integer, floating-point, text or date/time values. You can get the appropriate values from the cells according to their data types using Aspose.Cells.
## **Retrieving Data from Cells**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)that represents an Excel file. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class.

The [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), the cell's string value.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), returns the cell's double value.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), the cell's Boolean value.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), the cell's date/time value.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), the cell's float value.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), the cell's integer value.

Moreover, the type of data contained in a cell can also be checked by using the [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) property of the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class. In fact, the [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class' [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) property is based on [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Specifies that the cell value is Boolean.|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Specifies that the cell value is date/time.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Represents that the cell contains an error value|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Represents a blank cell.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Specifies that the cell value is numeric.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Specifies that the cell value is a string.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Specifies that the cell value is unknown.|
You can also use the above pre-defined cell value types to compare with the type of the data present in each cell.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
{{< app/cells/assistant language="java" >}}
---
title: Add and Retrieve Data
type: docs
weight: 20
url: /net/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accessing Cells of a Worksheet](/cells/net/accessing-cells-of-a-worksheet-html/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}} 
## **Adding Data to Cells**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class' [PutValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/putvalue/index) method. Aspose.Cells provides overloaded versions of the [PutValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/putvalue/index) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [PutValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/putvalue/index) method, it is possible to add a Boolean, string, double, integer or date/time, etc. values to the cell.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}
### **Improving Efficiency**
If you use [PutValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/putvalue/index) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.
## **Retrieving Data from Cells**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to worksheets in the file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

The [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:

- [StringValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/stringvalue): returns the string value of the cell.
- [DoubleValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/doublevalue): returns the double value of the cell.
- [BoolValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/boolvalue): returns the boolean value of the cell.
- [DateTimeValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/datetimevalue): returns the date/time value of the cell.
- [FloatValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/floatvalue): returns the float value of the cell.
- [IntValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/intvalue): returns the integer value of the cell.

When a field is not filled, cells with [DoubleValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/doublevalue) or [FloatValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/floatvalue) throws an exception.

The type of data contained in a cell can also be checked by using the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class' [Type](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/type) property. In fact, the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class' [Type](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/type) property is based on the [CellValueType](https://apireference.aspose.com/net/cells/aspose.cells/cellvaluetype) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|IsBool|Specifies that cell value is Boolean.|
|IsDateTime|Specifies that cell value is date/time.|
|IsNull|Represents a blank cell.|
|IsNumeric|Specifies that cell value is numeric.|
|IsString|Specifies that cell value is a string.|
|IsUnknown|Specifies that cell value is unknown.|
You can also use the above pre-defined cell value types to compare with the Type of data present in each cell.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}} 

While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text or date/time values. With Aspose.Cells, you can get the appropriate values from the cells according to their data types.

{{% /alert %}}

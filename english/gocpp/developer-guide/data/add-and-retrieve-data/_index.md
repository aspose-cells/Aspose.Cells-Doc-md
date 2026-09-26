---
title: Add and Retrieve Data
type: docs
weight: 20
url: /go-cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accessing Cells of a Worksheet](/cells/go-cpp/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}} 

## **Adding Data to Cells**

Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. Each item in the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection represents an object of the [Cell](https://reference.aspose.com/cells/go-cpp/cell/) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [Cell](https://reference.aspose.com/cells/go-cpp/cell/) class **PutValue** method. Aspose.Cells provides overloaded versions of the **PutValue** method that **let** developers add different kinds of data to cells. Using these overloaded versions of the **PutValue** method, it is possible to add a Boolean, string, double, integer, or date/time value to the cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddAndRetrieveData.go" >}}

### **Improving Efficiency**

If you use the **PutValue** method to put a large amount of data into a worksheet, you should add values to the cells first by rows and then by columns. This approach greatly improves the efficiency of your applications.

## **Retrieving Data from Cells**

Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to worksheets in the file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. Each item in the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection represents an object of the [Cell](https://reference.aspose.com/cells/go-cpp/cell/) class.

The [Cell](https://reference.aspose.com/cells/go-cpp/cell/) class provides several methods that allow developers to retrieve values from the cells according to their data types. These methods include:

- [GetStringValue](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/), returns the string value of the cell.  
- [GetDoubleValue](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/), returns the double value of the cell.  
- [GetBoolValue](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/), returns the boolean value of the cell.  
- [GetDateTimeValue](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/), returns the date/time value of the cell.  
- [GetFloatValue](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/), returns the float value of the cell.  
- [GetIntValue](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/), returns the integer value of the cell.

When a field is not filled, calls to **GetDoubleValue** or **GetFloatValue** throw an exception.

The type of data contained in a cell can also be checked by using the [Cell](https://reference.aspose.com/cells/go-cpp/cell/) class **GetType** method. In fact, the **GetType** method is based on the [CellValueType](https://reference.aspose.com/cells/go-cpp/cellvaluetype/) enumeration whose pre‑defined values are listed below:

| **Cell Value Types**            | **Description**                     |
| --------------------------------| ------------------------------------|
| CellValueType_IsBool            | Specifies that cell value is Boolean. |
| CellValueType_IsDateTime        | Specifies that cell value is date/time. |
| CellValueType_IsNull            | Represents a blank cell. |
| CellValueType_IsNumeric         | Specifies that cell value is numeric. |
| CellValueType_IsString          | Specifies that cell value is string. |
| CellValueType_IsUnknown         | Specifies that cell value is unknown. |

You can also use the above pre‑defined cell value types to compare with the type of the data present in each cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddAndRetrieveData-1.go" >}}
{{< app/cells/assistant language="go" >}}

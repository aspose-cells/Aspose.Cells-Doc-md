---
title: Add and Retrieve Data
type: docs
weight: 20
url: /cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accessing Cells of a Worksheet](/cells/cpp/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}} 
## **Adding Data to Cells**
Aspose.Cells provides a class [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains an [IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides an [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. Each item in the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection represents an object of the [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class [PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) method. Aspose.Cells provides overloaded versions of the [PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) method, it is possible to add a Boolean, string, double, integer or date/time, etc. values to the cell.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Improving Efficiency**
If you use [PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) method to put a large amount of data into a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.
## **Retrieving Data from Cells**
Aspose.Cells provides a class [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains an [IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to worksheets in the file. A worksheet is represented by the [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides a [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. Each item in the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection represents an object of the [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class.

The [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class provides several methods that allow developers to retrieve values from the cells according to their data types. These methods include:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), returns the string value of the cell.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), returns the double value of the cell.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), returns the boolean value of the cell.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), returns the date/time value of the cell.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), returns the float value of the cell.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), returns the integer value of the cell.

When a field is not filled, cells with [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) or [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44) throws an exception.

The type of data contained in a cell can also be checked by using the [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class [GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) method. In fact, the [ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) class [GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) method is based on the [CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|CellValueType_IsBool|Specifies that cell value is Boolean.|
|CellValueType_IsDateTime|Specifies that cell value is date/time.|
|CellValueType_IsNull|Represents a blank cell.|
|CellValueType_IsNumeric|Specifies that cell value is numeric.|
|CellValueType_IsString|Specifies that cell value is string.|
|CellValueType_IsUnknown|Specifies that cell value is unknown.|
You can also use the above pre-defined cell value types to compare with the Type of the data present in each cell.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}

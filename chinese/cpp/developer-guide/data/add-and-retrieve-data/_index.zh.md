---
title: 添加和检索数据
type: docs
weight: 20
url: /zh/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

在[访问工作表的单元格](/cells/zh/cpp/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表中单元格的基本方法。本文使用这些方法之一将不同类型的数据添加到单元格。

{{% /alert %}} 
## **向单元格添加数据**
Aspose.Cells 提供了表示 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合中的每个项目都表示 [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 类的对象。

Aspose.Cells 允许开发人员通过调用 [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 类的 [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) 方法向工作表中的单元格添加数据。Aspose.Cells 提供 [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) 方法的重载版本，让开发人员向单元格添加不同类型的数据。使用 [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) 方法的这些重载版本，可以向单元格添加布尔、字符串、双精度、整数或日期/时间等数值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **提高效率**
如果您使用 [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) 方法向工作表中放入大量数据，您应该首先按行，然后按列向单元格添加值。这种方法极大地提高了应用程序的效率。
## **从单元格检索数据**
Aspose.Cells 提供了表示 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问文件中的工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合中的每个项目都表示 [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 类的对象。

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 类提供了几种方法，允许开发人员根据其数据类型从单元格检索值。这些方法包括：

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)，返回单元格的字符串值。
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)，返回单元格的双精度值。
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)，返回单元格的布尔值。
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)，返回单元格的日期/时间值。
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)，返回单元格的浮点值。
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)，返回单元格的整数值。

当字段未填充时，使用[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)或[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)会引发异常。

还可以通过使用[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法来检查单元格中包含的数据的类型。事实上，[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法是基于[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)枚举的，其预定义值如下：

|**单元格值类型**|**描述**|
| :- | :- |
|CellValueType_IsBool|指定单元格值为布尔型。
|CellValueType_IsDateTime|指定单元格值为日期/时间。
|CellValueType_IsNull|表示空单元格。
|CellValueType_IsNumeric|指定单元格值为数值。
|CellValueType_IsString|指定单元格值为字符串。
|CellValueType_IsUnknown|指定单元格值为未知。
您也可以使用上述预定义的单元格值类型与每个单元格中的数据类型进行比较。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

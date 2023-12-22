---
title: 添加和检索数据
type: docs
weight: 20
url: /zh/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

在[访问工作表的 Cells](/cells/zh/cpp/accessing-cells-of-a-worksheet/)，我们讨论了访问工作表中的单元格的基本方法。本文使用其中一种方法向单元格添加不同类型的数据。

{{% /alert %}} 
##  **添加数据至Cells**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。中的每一项[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合代表一个对象[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)班级。

 Aspose.Cells 允许开发人员通过调用向工作表中的单元格添加数据[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)班级[看跌期权](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)方法。 Aspose.Cells 提供了重载版本[看跌期权](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)允许开发人员将不同类型的数据添加到单元格的方法。使用这些重载版本[看跌期权](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)方法，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **提高效率**
如果你使用[看跌期权](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)方法将大量数据放入工作表中，您应该首先按行然后按列向单元格添加值。这种方法极大地提高了应用程序的效率。
##  **从 Cells 检索数据**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问文件中的工作表的集合。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。中的每一项[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合代表一个对象[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)班级。

这[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类提供了多种方法，允许开发人员根据单元格的数据类型检索值。这些方法包括：

- [获取字符串值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)，返回单元格的字符串值。
- [获取双倍值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)，返回单元格的双精度值。
- [获取布尔值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)，返回单元格的布尔值。
- [获取日期时间值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)，返回单元格的日期/时间值。
- [获取浮点值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)，返回单元格的浮点值。
- [获取整数值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)，返回单元格的整数值。

当字段未填充时，单元格带有[获取双倍值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)或者[获取浮点值](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)抛出异常。

还可以使用以下命令检查单元格中包含的数据类型[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)班级[获取类型](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法。事实上，[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)班级[获取类型](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法是基于[单元格值类型](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)下面列出了其预定义值的枚举：

|**Cell 值类型**|**描述**|
| :- | :- |
|CellValueType_IsBool|指定单元格值为布尔值。|
|CellValueType_IsDateTime|指定单元格值为日期/时间。|
|CellValueType_IsNull|代表一个空白单元格。|
|CellValueType_IsNumeric|指定单元格值为数字。|
|CellValueType_IsString|指定单元格值为字符串。|
|CellValueType_IsUnknown|指定单元格值未知。|
您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}

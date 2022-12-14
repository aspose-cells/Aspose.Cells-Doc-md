---
title: 添加和检索数据
type: docs
weight: 20
url: /zh/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

在[访问工作表的 Cells](/cells/zh/cpp/accessing-cells-of-a-worksheet/)，我们讨论了访问工作表中单元格的基本方法。本文使用其中一种方法将不同类型的数据添加到单元格。

{{% /alert %}} 
## **添加数据到 Cells**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了一个[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。中的每一项[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)集合代表一个对象[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)班级。

 Aspose.Cells 允许开发人员通过调用[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)班级[认沽价值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)方法。 Aspose.Cells 提供重载版本的[认沽价值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)允许开发人员向单元格添加不同类型数据的方法。使用这些重载版本的[认沽价值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)方法，可以向单元格添加布尔值、字符串、双精度值、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **提高效率**
如果你使用[认沽价值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)将大量数据放入工作表的方法，您应该向单元格添加值，首先按行，然后按列。这种方法极大地提高了应用程序的效率。
## **从 Cells 检索数据**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问文件中工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。中的每一项[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)集合代表一个对象[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)班级。

这[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)类提供了几种方法，允许开发人员根据数据类型从单元格中检索值。这些方法包括：

- [获取字符串值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3)返回单元格的字符串值。
- [获取双值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a)返回单元格的双精度值。
- [获取布尔值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741)返回单元格的布尔值。
- [获取日期时间值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61)返回单元格的日期/时间值。
- [获取浮动值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)返回单元格的浮点值。
- [获取整数值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8)返回单元格的整数值。

当字段未填充时，单元格[获取双值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a)或者[获取浮动值](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)抛出异常。

单元格中包含的数据类型也可以使用[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)班级[获取类型](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba)方法。事实上，[电池](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)班级[获取类型](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba)方法是基于[单元值类型](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)下面列出了预定义值的枚举：

|**Cell 值类型**|**描述**|
|:- |:- |
|CellValueType_IsBool|指定单元格值为布尔值。|
|CellValueType_IsDateTime|指定单元格值为日期/时间。|
|CellValueType_IsNull|代表一个空白单元格。|
|CellValueType_IsNumeric|指定单元格值为数字。|
|CellValueType_IsString|指定单元格值为字符串。|
|CellValueType_IsUnknown|指定单元格值未知。|
您还可以使用上述预定义的单元格值类型与每个单元格中存在的数据类型进行比较。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}

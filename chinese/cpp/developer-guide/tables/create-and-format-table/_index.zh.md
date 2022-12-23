---
title: 创建和格式化表格
type: docs
weight: 10
url: /zh/cpp/create-and-format-table/
---
## **创建表**
电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债。多个用户可以一起使用、创建和维护各种列表。

Aspose.Cells 支持创建和管理列表。
### **列表对象的优点**
将数据列表转换为实际列表对象时有很多优点

- 自动包含新行和新列。
- 列表底部的总计行可以轻松添加以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到 List 对象中。
- 基于行和列的图表将自动展开。
- 分配给行和列的命名范围将自动扩展。
- 该列表受到保护，不会意外删除行和列。
### **使用 Microsoft Excel 创建列表对象**

|**选择用于创建 List 对象的数据范围**|
|:- |
|![待办事项：图片_替代_文本](jHcNq4o.png)|
这将显示“创建列表”对话框。

|**创建列表对话框**|
|:- |
|![待办事项：图片_替代_文本](kJmukRF.png)|
为数据实现List对象并指定合计行（选择**数据**， 然后**列表**， 其次是**总行数**).

|**创建列表对象**|
|:- |
|![待办事项：图片_替代_文本](ECSGVdR.png)|
### **使用 Aspose.Cells API**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。创建一个[IList对象](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object)在工作表中，使用[获取列表对象](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705)的收集方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。每个 `[IListObject]` 实际上是[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection)类，它进一步提供了[添加](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)添加 `[IListObject]` 对象并为列表指定单元格范围的方法。

根据指定范围的单元格，`[IListObject]`对象由Aspose.Cells创建。使用属性（例如[显示总计](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2)和[列表列](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)等）的 `[IListObject]` 类来控制列表。

在下面给出的示例中，我们使用 Aspose.Cells API 创建了与上一节中使用 Microsoft Excel 创建的相同的 `[IListObject]`。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **格式化表格**
要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为 Excel 表格）。表是一系列行和列，其中包含独立于其他行和列中的数据管理的相关数据。默认情况下，表格中的每一列都在标题行中启用了筛选，以便您可以快速筛选或排序列表对象数据。您可以将总计行（列表中的特殊行，提供对处理数字数据有用的聚合函数选择）添加到列表对象，该列表对象为每个总计行单元格提供聚合函数的下拉列表。 Aspose.Cells 提供用于创建和管理列表（或表格）的选项。
### **格式化列表对象**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。创建一个*列表对象*在工作表中，使用 `IListObjectCollection`。每个 `[IListObject]` 实际上是 `IListObjectCollection` 类的一个对象，它进一步提供了[添加](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)添加 `[IListObject]` 对象并指定它应包含的单元格范围的方法。根据指定的单元格范围，一个*列表对象*由 Aspose.Cells 在工作表中创建。使用属性（例如，[表格样式类型](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)`[IListObject]` 类来根据您的要求格式化表格。

下面的示例将示例数据添加到工作表，添加 `[IListObject]` 并对其应用默认样式。 `[IListObject]` 样式受 Microsoft Excel 2007/2010 支持。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}

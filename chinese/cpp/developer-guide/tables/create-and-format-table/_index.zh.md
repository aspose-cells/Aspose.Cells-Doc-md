---
title: 创建表格并设置格式
type: docs
weight: 10
url: /zh/cpp/create-and-format-table/
---
##  **创建表**
电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易、资产或负债列表。多个用户可以一起使用、创建和维护各种列表。

Aspose.Cells 支持创建和管理列表。
###  **列表对象的优点**
将数据列表转换为实际的列表对象有很多优点

- 新的行和列会自动包含在内。
- 可以轻松添加列表底部的总计行来显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到 List 对象中。
- 基于行和列的图表将自动扩展。
- 分配给行和列的命名范围将自动扩展。
- 该列表受到保护，不会被意外删除行和列。
###  **使用 Microsoft Excel 创建列表对象**

|**选择创建List对象的数据范围**|
| :- |
|![待办事项：图像_替代_文本](jHcNq4o.png)|
这将显示“创建列表”对话框。

|**创建列表对话框**|
| :- |
|![待办事项：图像_替代_文本](kJmukRF.png)|
实现数据的 List 对象并指定总行数（选择 *Data**，然后选择 *List**，然后选择 *Total Row**）。

|**创建列表对象**|
| :- |
|![待办事项：图像_替代_文本](ECSGVdR.png)|
###  **使用 Aspose.Cells API**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种用于管理工作表的方法。创建一个[列表对象](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)在工作表中，使用[获取列表对象](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/)的收集方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。每个`[ListObject]`实际上是一个对象[列表对象集合](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/)类，进一步提供了[添加](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)用于添加 `[ListObject]` 对象并指定列表单元格范围的方法。

根据指定的单元格范围，Aspose.Cells创建了`[ListObject]`对象。使用属性（例如[设置显示总计](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/)和[获取列表列](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)等）的`[ListObject]`类来控制列表。

在下面给出的示例中，我们使用 Aspose.Cells API 创建了与上一节中使用 Microsoft Excel 创建的相同的 `[ListObject]`。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **设置表格格式**
要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为 Excel 表格）。表是一系列行和列，其中包含独立于其他行和列中的数据进行管理的相关数据。默认情况下，表中的每一列都在标题行中启用了过滤，以便您可以快速过滤或排序列表对象数据。您可以将总计行（列表中的特殊行，提供对处理数值数据有用的聚合函数的选择）添加到列表对象，该列表对象为每个总计行单元格提供聚合函数的下拉列表。 Aspose.Cells 提供用于创建和管理列表（或表格）的选项。
###  **格式化列表对象**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种管理工作表的方法。创建一个*列表对象*在工作表中，使用 `ListObjectCollection`。每个 `[ListObject]` 实际上是 `ListObjectCollection` 类的一个对象，该类进一步提供[添加](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)添加 `[ListObject]` 对象并指定它应包含的单元格范围的方法。根据指定的单元格范围，*列表对象*由 Aspose.Cells 在工作表中创建。使用属性（例如，[设置表格样式类型](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)）的 `[ListObject]` 类来根据您的要求格式化表格。

下面的示例将示例数据添加到工作表中，添加 `[ListObject]` 并对其应用默认样式。 `[ListObject]` 样式受 Microsoft Excel 2007/2010 支持。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}

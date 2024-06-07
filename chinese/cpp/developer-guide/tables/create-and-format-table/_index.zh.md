---
title: 创建和格式化表
type: docs
weight: 10
url: /zh/cpp/create-and-format-table/
---

## **创建表**
电子表格的优点之一是它允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。
### **列表对象的优点**
将数据列表转换为实际列表对象时有很多优点

- 新行和列会自动包含其中。
- 可轻松添加位于列表底部的总行，以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到列表对象中。
- 基于行和列的图表将自动扩展。
- 针对行和列分配的命名范围将自动扩展。
- 列表受到意外删除的保护。
### **使用Microsoft Excel创建列表对象**

|**选择创建列表对象的数据范围**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
这将显示创建列表对话框。

|**创建列表对话框**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
为数据实现列表对象并指定总行（选择**数据**，然后**列表**，紧接着 **总行**）。

|**创建列表对象**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **使用Aspose.Cells API**
Aspose.Cells提供一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了大量管理工作表的方法。要在工作表中创建一个[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)，请使用[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/)集合方法。每个`[ListObject]`实际上是[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/)类的对象，后者提供添加一个`[ListObject]`对象并指定列表的单元格范围的[Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)方法。

根据指定的单元格范围，Aspose.Cells创建了`[ListObject]`对象。使用`[ListObject]`类的属性（例如[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/)和[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)等），来控制列表。

在下面的示例中，我们使用Aspose.Cells API创建了相同的`[ListObject]`，就像在上面的Microsoft Excel中创建的那样。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **格式化表**
要管理和分析一组相关数据，可以将一系列单元格转成列表对象（也被称为Excel表格）。表格是一系列包含相关数据的行和列，与其他行和列的数据独立管理。默认情况下，表中的每个列在标题行中启用筛选，以便您可以快速筛选或排序列表对象数据。您可以为列表对象添加一个总行（列表中提供的特殊行，为每个总行单元格提供一系列有用于处理数字数据的聚合函数的下拉列表）。Aspose。Cells提供了创建和管理列表（或表）的选项。
### **格式化列表对象**
Aspose.Cells提供一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了广泛的用于管理工作表的方法。要在工作表中创建一个*ListObject*，请使用`ListObjectCollection`。每个`[ListObject]`实际上是`ListObjectCollection`类的对象，后者提供了`Add`方法用于添加一个`[ListObject]`对象并指定其所包含的单元格范围。根据指定的单元格范围，Aspose.Cells会在工作表中创建一个*ListObject*。使用`[ListObject]`类的属性（例如[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)）来根据您的需求为表格设置格式。

下面的示例代码向工作表添加样本数据，添加了一个`[ListObject]`并将默认样式应用于它。`[ListObject]`样式得到了Microsoft Excel 2007/2010的支持。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}

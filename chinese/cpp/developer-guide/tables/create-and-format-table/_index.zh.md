---
title: 创建和格式化表
type: docs
weight: 10
url: /zh/cpp/create-and-format-table/
---

## **创建表**
电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。
### **列表对象的优点**
当您将数据列表转换为实际列表对象时，会有相当多的优点

- 新行和列会自动包括在内。
- 列表底部可以轻松添加总计行来显示求和、平均、计数等信息。
- 添加在右侧的列会自动并入列表对象中。
- 基于行和列的图表会自动扩展。
- 分配给行和列的命名范围将自动扩展。
列表受到意外行和列删除的保护。
### **在 Microsoft Excel 中创建列表对象**

|**选择用于创建列表对象的数据范围**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
这会显示创建列表对话框。

|**创建列表对话框**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
为数据实现列表对象并指定总行数（选择**数据**，然后选择**列表**，然后选择**总行**）。

|**创建列表对象**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **使用 Aspose.Cells API**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了广泛的方法来管理工作表。要在工作表中创建一个[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)，请使用[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/)集合方法。 每个`[ListObject]`实际上是 [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) 类的对象，它提供了[Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)方法，用于添加`[ListObject]`对象并指定列表的单元格范围。

根据指定的单元格范围，Aspose.Cells创建了`[ListObject]`对象。使用`[ListObject]`类的属性（例如[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/)和[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)等）来控制列表。

在下面的示例中，我们使用Aspose.Cells API创建了与上一节中使用Microsoft Excel创建的相同的`[ListObject]`。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **格式化表**
要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表）。表是包含相关数据的一系列行和列，可独立于其他行和列中的数据进行管理。默认情况下，表中的每一列都在标题行中启用了筛选，因此您可以快速筛选或排序列表对象数据。您可以为列表对象添加一个总行（列表中提供一系列聚合函数的特殊行，对于处理数值数据非常有用），用于为列表对象的每个总行单元格提供聚合函数的下拉列表。Aspose.Cells提供了创建和管理列表（或表）的选项。
### **格式化列表对象**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示工作表。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了广泛的方法来管理工作表。要在工作表中创建*ListObject*，请使用`ListObjectCollection`。每个`[ListObject]`实际上是`ListObjectCollection`类的对象，它提供了[Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)方法，用于添加`[ListObject]`对象并指定其应包含的单元格范围。根据指定的单元格范围，Aspose.Cells在工作表中创建了一个*ListObject*。 使用`[ListObject]`类的属性（例如[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)）对表格进行格式化，以满足您的需求。

以下示例将示例数据添加到工作表，添加了`[ListObject]`并应用了默认样式。`[ListObject]`样式由Microsoft Excel 2007/2010支持。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

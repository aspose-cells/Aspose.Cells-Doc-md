---
title: 创建和格式化表
type: docs
weight: 10
url: /zh/go-cpp/create-and-format-table/
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

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，其包含[Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)集合，可访问Excel文件中的所有工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)类表示。它提供管理工作表的多种方法。要在工作表中创建[ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) ，使用[GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/)方法，该方法返回[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)的[ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/)，可以调用其[Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/)方法添加[ListObject]，并指定范围。

根据指定的单元格范围，Aspose.Cells会创建[ListObject]对象。可通过[ListObject]类的属性（例如[SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/)和[GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/)）控制表格。

在下面的示例中，我们使用Aspose.Cells API创建了与上一节中使用Microsoft Excel创建的相同的`[ListObject]`。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **格式化表**

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表）。表是包含相关数据的一系列行和列，可独立于其他行和列中的数据进行管理。默认情况下，表中的每一列都在标题行中启用了筛选，因此您可以快速筛选或排序列表对象数据。您可以为列表对象添加一个总行（列表中提供一系列聚合函数的特殊行，对于处理数值数据非常有用），用于为列表对象的每个总行单元格提供聚合函数的下拉列表。Aspose.Cells提供了创建和管理列表（或表）的选项。

### **格式化列表对象**

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，其包含[Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)集合，可访问Excel文件中的所有工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)类表示。它提供多种方法管理工作表。要在工作表中创建[ListObject]，使用[ListObjectCollection]。每个[ListObject]实际上是[ListObjectCollection]类的对象，可以调用其[Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/)方法，添加[ListObject]对象并指定应包含的单元格范围。根据所指定的单元格范围，Aspose.Cells 会在工作表中创建[ListObject]，并用[ListObject]类的属性（例如[SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)）来格式化表格以满足需求。

以下示例将示例数据添加到工作表，添加了`[ListObject]`并应用了默认样式。`[ListObject]`样式由Microsoft Excel 2007/2010支持。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}

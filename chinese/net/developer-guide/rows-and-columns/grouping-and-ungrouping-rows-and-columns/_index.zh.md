---
title: 行和列的分组和取消分组
type: docs
weight: 50
url: /zh/net/grouping-and-ungrouping-rows-and-columns/
---

## **介绍**

在 Microsoft Excel 文件中，您可以创建一个数据大纲，以便通过单击鼠标来显示和隐藏不同级别的细节。

单击**大纲符号**1、2、3、+和- 快速显示工作表中仅提供摘要或标题部分的行或列，或者您可使用符号查看摘要或标题下的详细信息，如下图所示:

|**分组行和列**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行和列的分组管理**

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合提供了几种管理工作表行或列的方法，以下将更详细地讨论其中的一些。

### **分组行和列**

通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)和[**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)方法，可以对行或列进行分组。这两种方法都带有以下参数:

- 第一个行/列索引，即组中的第一行或列。
- 最后一个行/列索引，即组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **分组设置**

Microsoft Excel 允许您配置用于显示的分组设置：

- 详细信息下面的摘要行。
- 详细信息右侧的摘要列。

开发者可以使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline)属性配置这些组设置。

### **将摘要行显示在详细信息下方**

可以通过将[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)类的[**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow)属性设置为**true**或**false**来控制是否在详细信息下方显示摘要行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **将摘要列显示在详细信息右侧**

开发者还可以通过将[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)类的[**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright)属性设置为**true**或**false**来控制是否在详细信息右侧显示摘要列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **取消分组行和列**

要取消任何已分组的行或列，调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)和[**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)方法。这两个方法都带有两个参数:

- 第一个行或列索引，即要取消分组的第一行/列。
- 最后一个行或列索引，即要取消分组的最后一行/列。

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)有一个额外的重载，它带有一个布尔型第三个参数。将其设置为true会移除所有分组信息。否则，只有外部的组信息会被移除。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}

---
title: 分组和取消分组行和列
type: docs
weight: 50
url: /zh/net/grouping-and-ungrouping-rows-and-columns/
---
## **介绍**

在 Microsoft Excel 文件中，您可以为数据创建一个大纲，以便通过单击鼠标来显示和隐藏详细信息级别。

点击**大纲符号**、1、2、3、+ 和 - 快速仅显示工作表中为各部分提供摘要或标题的行或列，或者您可以使用符号查看单个摘要或标题下的详细信息，如下图所示:

|**分组行和列。**|
|:- |
|![待办事项：图像_替代_文本](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行列分组管理**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)代表工作表中所有单元格的集合。

这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection 提供了多种方法来管理工作表中的行或列，下面将详细讨论其中的一些方法。

### **分组行和列**

可以通过调用[**组行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)和[**组列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。这两种方法都采用以下参数：

- 第一行/列索引，组中的第一行或第一列。
- 最后一行/列索引，组中的最后一行或最后一列。
- is hidden，布尔型参数，指定分组后是否隐藏行/列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **群组设置**

Microsoft Excel 允许您配置组设置以显示：

- 详细信息下方的摘要行。
- 详细信息右侧的摘要列。

开发人员可以使用[**大纲**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline)的财产[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

### **详细信息下方的汇总行**

可以通过设置[**大纲**](https://reference.aspose.com/cells/net/aspose.cells/outline)班级'[**汇总行下方**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow)财产给**真的**或者**错误的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **详细信息右侧的摘要列**

开发人员还可以通过设置[**摘要列右**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright)的财产[**大纲**](https://reference.aspose.com/cells/net/aspose.cells/outline)类**真的**或者**错误的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **取消分组行和列**

要取消分组任何已分组的行或列，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**解组行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)和[**取消组合列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)方法。两种方法都有两个参数：

- 第一行或第一列索引，要取消分组的第一行/列。
- 最后一行或最后一列索引，要取消分组的最后一行/列。

[**解组行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)有一个带有第三个布尔参数的重载。将其设置为**真的**删除所有分组信息。否则，仅删除外部组信息。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}

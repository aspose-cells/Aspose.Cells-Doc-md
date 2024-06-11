---
title: 对行和列进行分组和取消分组
type: docs
weight: 50
url: /zh/python-net/grouping-and-ungrouping-rows-and-columns/
description: 本文介绍了如何通过 Aspose.Cells for Python 通过 .NET API 对行和列进行分组和取消分组。
keywords: Python Excel库，Python如何对行和列进行分组，Python如何对行和列进行取消分组，Python行和列的组管理，Python如何将摘要行设置为详细信息下方，Python如何将摘要列设置为详细信息右侧。
---

## **介绍**

在 Microsoft Excel 文件中，您可以为数据创建概要，让您单击一次鼠标即可显示和隐藏详细级别。

单击**概要符号**，1、2、3、+ 和 - ，即可快速显示仅提供摘要或标题用于工作表中的节的行或列，或者您可以使用符号查看摘要或标题下的详细信息，如下图所示：

|**对行和列进行分组。**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行和列的分组管理**

Aspose.Cells for Python 通过 .NET 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供了一个 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合提供了几种方法来管理工作表中的行或列，以下是其中几种方法的详细讨论。

### **如何对行和列进行分组**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的 [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) 和 [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) 方法来对行或列进行分组。这两种方法都采用以下参数：

- 第一个行/列索引，组中的第一个行或列。
- 最后一个行/列索引，组中的最后一个行或列。
- 是否隐藏，一个布尔参数，指定在分组后是否隐藏行/列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **分组设置**

Microsoft Excel 允许您配置用于显示的组设置：

- 详细下面的摘要行。
- 摘要列放在详细信息右侧。

开发人员可以使用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) 属性配置这些组设置。

### **如何将摘要行设置为详细信息下方**

可以通过将 [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) 类的 [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) 属性设置为 **true** 或 **false** 来控制是否在详细信息下方显示摘要行。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **如何将摘要列设置为详细信息右侧**

开发人员还可以通过将[**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline)类的[**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/)属性设置为**true**或**false**来控制在详细信息右侧显示汇总列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **如何对行和列进行取消分组**

为了取消任何已分组的行或列，请调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合的[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/)和[**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int)方法。这两种方法各自接受两个参数:

- 第一行或列索引，要取消分组的第一行/列。
- 最后一行或列索引，要取消分组的最后一行/列。

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool)还包含一个采用布尔类型第三参数的重载方法。将其设置为**true**将删除所有分组信息。否则，只会删除外部分组信息。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}

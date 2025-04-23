---
title: 分组、取消分组行和列
type: docs
weight: 30
url: /zh/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **介绍**

在 Microsoft Excel 文件中，您可以创建一个数据大纲，以便通过单击鼠标来显示和隐藏不同级别的细节。

单击**大纲符号** 1、2、3、+ 和 -，快速显示工作表中提供摘要或标题的行或列，或者您可以使用这些符号来查看摘要或标题下的详细信息。

## **行和列的分组管理**

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，它包含一个[Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)集合，可以访问Excel文件中的每个工作表。

[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合提供多个方法用于管理工作表中的行和列，以下将详细介绍其中一些。

### **分组行和列**

可以调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/)和[GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/)方法，将行或列分组。这两个方法的参数如下：

- 第一个行/列索引，分组中的第一行或列。
- 最后一个行/列索引，分组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **分组设置**

Microsoft Excel 允许您配置用于显示的分组设置：

- 详细信息下面的摘要行。
- 详细信息右侧的摘要列。

## **取消行和列的分组**

要取消分组任何已分组的行或列，调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/)和[UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/)方法。两者的参数如下：

- 第一个要取消分组的行或列索引。
- 最后一个要取消分组的行或列索引。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}

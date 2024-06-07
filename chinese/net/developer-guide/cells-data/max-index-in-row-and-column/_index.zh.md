---
title: 在行中获取最大列索引，在列中获取最大行索引
type: docs
weight: 600
url: /zh/net/get-max-index-in-row-and-column/
description: 通过Aspose.Cells for .NET API学习如何在行中获取最大列索引和在列中获取最大行索引。
keywords: 在行中获取最大列索引，在列中获取最大行索引，在行中获取最大数据列索引，在列中获取最大数据行索引。 
---

## **可能的使用场景**
当您只需要处理行或列上的一些数据时，您需要了解行和列的数据范围。Aspose.Cells提供了此功能。要获取行上的最大列索引，您可以获取[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)和[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)属性，然后使用[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)属性来获取最大列索引和最大数据列索引。但是，为了获取列上的最大行索引和最大行数据索引，您需要在列上创建一个范围，然后遍历范围以找到最后一个单元格，最后获取单元格上的[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)属性。

Aspose.Cells 提供以下属性和方法，帮助您实现目标。
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **使用Aspose.Cells获取行中的最大列索引和列中的最大行索引**
此示例显示如何：

1. 加载[示例文件](sample.xlsx)。
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 获取单元格上的[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)属性。
1. 基于列创建范围。
1. 获取迭代器并遍历范围。
1. 获取单元格上的[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}

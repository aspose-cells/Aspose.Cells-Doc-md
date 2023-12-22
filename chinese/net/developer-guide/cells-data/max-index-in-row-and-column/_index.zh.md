---
title: 获取行中的最大列索引和列中的最大行索引
type: docs
weight: 600
url: /zh/net/get-max-index-in-row-and-column/
description: 了解如何通过 Aspose.Cells for .NET API 获取行中的最大列索引和列中的最大行索引。
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **可能的使用场景**
当只需要操作行或列上的一些数据时，需要知道行和列的数据范围。 Aspose.Cells 提供此功能。要获取行上的最大列索引，可以获取[行.最后一个单元格](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)和[行.最后一个数据单元格](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)属性，然后使用[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)属性获取最大列索引和最大数据列索引。但为了获取某一列上的最大行索引和最大行数据索引，需要在该列上创建一个范围，然后遍历该范围找到最后一个单元格，最后得到[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)单元格上的属性。

Aspose.Cells 提供以下属性和方法来帮助您实现目标。
- [**行.最后一个单元格**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**行.最后一个数据单元格**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **使用 Aspose.Cells 获取行中的最大列索引和列中的最大行索引**
此示例演示如何：

1. 加载[样本文件](sample.xlsx).
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 得到[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)单元格上的属性。
1. 根据列创建范围。
1. 获取迭代器和遍历范围。
1. 得到[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)单元格上的属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
---
title: 获取Cells索引
type: docs
weight: 600
url: /zh/net/get-cells-index/
description: 了解如何通过行、列或单元格的名称获取行或列。将单元格名称转换为从零开始的行和列索引。
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Excel默认的视图是A1样式参考，每一列定义为A、B、C…，单元格命名为A1、B2、C3…等。
您可能想知道该单元格位于哪一行哪一列。

{{% /alert %}}


##  **可能的使用场景**
当您只需要按行和列索引操作工作表上的特定数据时，您需要知道该特定单元格的列和列索引。
 Aspose.Cells提供了此功能，可以通过行、列和单元格的名称获取行和列索引。
Aspose.Cells 提供以下属性和方法来帮助您实现目标。
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

注意：.Net 的 Aspose.Cells 中的索引是从零开始的，但在 MS Excel 中 Row 的 id 是从一开始的。

##  **使用 Aspose.Cells 获取 Cells 索引**
此示例演示如何：

1. 创建工作簿并添加一些数据。
1. 在第一个工作表中查找特定单元格。
1. 根据单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名称获取行索引。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
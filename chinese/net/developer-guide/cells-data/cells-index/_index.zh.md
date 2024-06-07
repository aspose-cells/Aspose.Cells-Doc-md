---
title: 获取单元格索引
type: docs
weight: 600
url: /zh/net/get-cells-index/
description: 学习如何通过行、列或单元格的名称获取行或列索引。将单元格的名称转换为基于零的行和列索引。
keywords: 通过单元格的名称获取行索引和列索引，通过列名获取列索引，通过行名获取行索引，通过单元格的名称获取索引。 
---

{{% alert color="primary" %}}
Excel 的默认视图是 A1 样式引用，每个列都定义为 A、B、C...，单元格的名称为 A1、B2、C3...等。 
您可能想知道此单元格所在的行和列。

{{% /alert %}}


## **可能的使用场景**
当您只需通过行和列索引操纵工作表上的特定数据时，您需要了解该特定单元格的行和列索引。 
Aspose.Cells 提供此功能，通过行、列和单元格的名称获取行和列索引。 
Aspose.Cells 提供以下属性和方法，帮助您实现目标。
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

注意：在 Aspose.Cells for .Net 中，索引是基于零的，但在 MS Excel 中，行的 id 是基于一的。

## **使用 Aspose.Cells 获取单元格索引**
此示例显示如何：

1. 创建一个工作簿并添加一些数据。
1. 查找第一个工作表中的特定单元格。
1. 通过单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名获取行索引。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}

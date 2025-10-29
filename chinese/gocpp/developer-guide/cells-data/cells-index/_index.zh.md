---
title: 使用C++和Golang获取单元格索引
linktitle: 获取单元格索引
type: docs
weight: 600
url: /zh/go-cpp/get-cells-index/
description: 学习如何通过单元格、行或列名获取索引。使用C++和Golang将单元格名转换为以零为基准的行列索引。
keywords: 通过单元格名称获取行索引和列索引，通过列名获取列索引，通过行名获取行索引，通过单元格名称获取索引。
---

{{% alert color="primary" %}}
Excel的默认视图是A1样式引用，其中每列定义为A、B、C等等，单元格命名为A1、B2、C3……等。
你可能想知道该单元格属于哪一行和哪一列。

{{% /alert %}}

## **可能的使用场景**

当你只需要通过行和列索引操作特定数据时，你需要知道该单元格的行和列索引。
Aspose.Cells提供此功能，以通过行、列和单元格的名称获取行和列索引。
Aspose.Cells提供以下属性和方法帮助你实现目标：

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

注意：在Aspose.Cells for C++中索引从零开始，但在MS Excel中行的ID是从一开始的。

## **使用 Aspose.Cells 获取单元格索引**

此示例演示如何：

1. 创建一个工作簿并添加一些数据。
1. 在第一个工作表中查找特定单元格。
1. 通过单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名获取行索引。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}

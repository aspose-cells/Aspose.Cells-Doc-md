---
title: 名称和索引
type: docs
weight: 10
url: /zh/go-cpp/names-and-indices/
---

## **从行和列索引获取单元格名称**

可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。
Aspose.Cells提供[CellsHelper_CellIndexToName]方法（https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/），开发者可以通过提供行和列索引来获取单元格的名称。

{{% alert color="primary" %}}

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}}

以下示例代码展示如何使用[CellsHelper_CellIndexToName]（https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/）在已知行和列索引时访问单元格名称，代码生成以下输出。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **从单元格名称获取行和列索引**

可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。
Aspose.Cells提供[CellsHelper_CellNameToIndex]方法（https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/），开发者可以通过单元格名称获取行和列的索引。

{{% alert color="primary" %}}

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}}

以下示例代码展示如何使用[CellsHelper_CellNameToIndex]（https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/）根据单元格名称获取行列索引，代码生成以下输出。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}

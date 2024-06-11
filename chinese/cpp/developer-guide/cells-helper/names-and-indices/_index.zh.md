---
title: 名称和索引
type: docs
weight: 10
url: /zh/cpp/names-and-indices/
---

## **从行和列索引获取单元格名称**
可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。
Aspose.Cells提供了[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/)方法，使开发人员能够在提供行和列索引时获取单元格的名称。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码说明了如何使用[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/)来访问已知行和列索引的单元格名称。 代码生成以下输出。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **从单元格名称获取行和列索引**
可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。
Aspose.Cells提供了[CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)方法，使开发人员能够从单元格名称中获取行和列索引。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码说明了如何使用[CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)来从单元格名称中获取行和列索引。 代码生成以下输出。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}

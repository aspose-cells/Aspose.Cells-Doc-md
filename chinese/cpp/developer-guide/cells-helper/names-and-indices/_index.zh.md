---
title: 名称和索引
type: docs
weight: 10
url: /zh/cpp/names-and-indices/
---
## **从行和列索引中获取 Cell 名称**
给定行和列索引可以找到单元格的名称。这篇文章解释了如何。
Aspose.Cells 提供了 ICellsHelper.CellIndexToName_i 方法，允许开发人员在提供行和列索引的情况下获取单元格的名称。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行和列索引。

{{% /alert %}} 

以下示例代码说明如何使用 ICellsHelper.CellIndexToName_i 访问给定已知行和列索引的单元格名称。该代码生成以下输出。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **从 Cell 名称获取行和列索引**
可以从单元格的名称中找到单元格的行和列索引。这篇文章解释了如何。
Aspose.Cells 提供了 ICellsHelper.CellNameToIndex_i 方法，允许开发人员从单元格名称中获取行和列索引。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用 CellsHelper.CellNameToIndex 从单元格名称中获取行和列索引。该代码生成以下输出。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}

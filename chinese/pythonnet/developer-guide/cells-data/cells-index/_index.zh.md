---
title: 获取单元格索引
type: docs
weight: 600
url: /zh/python-net/get-cells-index/
description: 学习如何使用 Aspose.Cells for Python via .NET API 通过行的名称获取行或列，或单元格。通过 Aspose.Cells for Python via .NET API 将单元格的名称转换为基于零的行和列索引。
keywords: Python 中，使用 Python 通过单元格的名称获取行索引和列索引，使用 Python 通过列的名称获取列索引，使用 Python 通过行的名称获取行索引，使用 Python 通过单元格的名称获取索引。 
---

{{% alert color="primary" %}}
Excel 的默认视图是 A1 样式引用，每列定义为 A、B、C……，单元格命名为 A1、B2、C3……等等。
您可能想知道该单元格位于哪一行和列。

{{% /alert %}}


## **可能的使用场景**
当您只需通过行和列索引操作工作表上的特定数据时，您需要了解该特定单元格的行索引和列索引。 
Aspose.Cells for Python via .NET 提供了通过行、列和单元格的名称获取行和列索引的功能。 
Aspose.Cells for Python via .NET提供以下属性和方法，以帮助您实现您的目标。
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

注意：在Aspose.Cells for Python via .NET中，索引是以零为基础的，但是MS Excel中的行标识是以一为基础的。

## **使用Aspose.Cells for Python Excel库获取单元格索引**
此示例演示如何：

1. 创建一个工作簿并添加一些数据。
1. 在第一个工作表中查找特定单元格。
1. 通过单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名获取行索引。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}

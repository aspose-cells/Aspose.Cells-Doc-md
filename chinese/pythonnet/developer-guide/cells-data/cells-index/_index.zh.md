---
title: 获取单元格索引
type: docs
weight: 600
url: /zh/python-net/get-cells-index/
description: 了解如何通过 Aspose.Cells for Python 通过 .NET API按行的名称获取行或列，列或单元格。 通过 Aspose.Cells for Python 通过 .NET API，通过单元格名称将行和列索引转换为基于零的列和行索引，通过单元格的名称获取索引使用 Python。
keywords: Python Excel，通过 Python 获取单元格的行索引和列索引，通过单元格的名称获取单元格的列索引，通过 Python 获取行的行索引，通过 Python 获取单元格的名称获取索引。 
---

{{% alert color="primary" %}}
Excel 的默认视图是 A1 样式引用，每个列都定义为 A、B、C...，单元格的名称为 A1、B2、C3...等。 
您可能想知道此单元格所在的行和列。

{{% /alert %}}


## **可能的使用场景**
当您只需通过行和列索引操纵工作表上的特定数据时，您需要了解该特定单元格的行和列索引。 
通过 .NET 的 Aspose.Cells for Python 可以按名称获取行和列的索引，也可以获取单元格的索引。 
Aspose.Cells for Python通过.NET提供以下属性和方法，以帮助您实现目标。
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

注意：在 Aspose.Cells for Python 中，索引是以零为基础的，但在 MS Excel 中，行的 ID 是以一为基础的。

## **使用 Aspose.Cells for Python Excel 库获取单元格索引**
此示例显示如何：

1. 创建一个工作簿并添加一些数据。
1. 查找第一个工作表中的特定单元格。
1. 通过单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名获取行索引。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}

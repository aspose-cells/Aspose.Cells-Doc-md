---
title: 获取单元格索引
type: docs
weight: 600
url: /zh/nodejs-cpp/get-cells-index/
description: 学习如何通过行名、列名或单元格名获取行或列。将单元格的名称转换为从零开始的行和列索引。
keywords: 通过单元格名称获取行索引和列索引，通过列名获取列索引，通过行名获取行索引，通过单元格名称获取索引。 
---

{{% alert color="primary" %}}
Excel 的默认视图是 A1 样式引用，每列定义为 A、B、C……，单元格命名为 A1、B2、C3……等等。
您可能想知道该单元格位于哪一行和列。

{{% /alert %}}


## **可能的使用场景**
当您只需通过行和列索引操作工作表上的特定数据时，您需要了解该特定单元格的行索引和列索引。 
Aspose.Cells for Node.js via C++ 提供此功能，根据行名、列名和单元格名获取对应的行和列索引。 
Aspose.Cells for Node.js via C++提供以下属性和方法，帮助你实现目标。
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

注意：在 Aspose.Cells for Node.js via C++ 中索引从零开始，但在 MS Excel 中行的 ID 是从一开始的。

## **使用 Aspose.Cells for Node.js via C++ 获取单元格索引**
此示例演示如何：

1. 创建一个工作簿并添加一些数据。
1. 在第一个工作表中查找特定单元格。
1. 通过单元格名称获取行索引和列索引。
1. 通过列名获取列索引。
1. 通过行名获取行索引。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

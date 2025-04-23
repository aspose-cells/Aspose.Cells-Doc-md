---
title: 获取行中最大列索引和列中最大行索引
type: docs
weight: 600
url: /zh/nodejs-cpp/get-max-index-in-row-and-column/
description: 学习如何通过Aspose.Cells for Node.js via C++ API获取行中的最大列索引和列中的最大行索引。
keywords: 获取行中的最大列索引 Node.js via C++，获取列中的最大行索引 Node.js via C++，获取行中的最大数据列索引 Node.js via C++，获取列中的最大数据行索引 Node.js via C++。
---

## **可能的使用场景**
当你只需要操作某些行或列中的数据时，需要知道行和列的数据范围。Aspose.Cells for Node.js via C++提供了此功能。要获得某行的最大列索引，可以调用[**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)和[**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)方法，然后使用[**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)方法获取最大列索引和最大数据列索引。但为了获取某列的最大行索引和最大行数据索引，你需要在该列创建一个范围，然后遍历该范围找到最后一个单元格，最后调用该单元格的[**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)方法。

Aspose.Cells for Node.js via C++提供以下属性和方法，帮助你实现目标。
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **获取行中的最大列索引和列中的最大行索引**
此示例演示如何：

1. 加载[示例文件](sample.xlsx)。
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 调用单元格的[**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)方法。
1. 根据列创建一个范围。
1. 获取迭代器并遍历范围。
1. 调用单元格的[**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)方法。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}


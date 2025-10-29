---
title: 用Golang通过C++获取行中的最大列索引和列中的最大行索引
linktitle: 获取行中最大列索引和列中最大行索引
type: docs
weight: 600
url: /zh/go-cpp/get-max-index-in-row-and-column/
description: 了解如何通过Aspose.Cells for C++ API获取行中的最大列索引和列中的最大行索引。
keywords: 获取行中最大列索引，获取列中最大行索引，获取行中最大数据列索引，获取列中最大数据行索引。
---

## **可能的使用场景**
当只需要操作部分行或列的数据时，需知道数据范围。Aspose.Cells提供此功能。获取行的最大列索引，可以获取[Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)和[Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)属性，然后用[Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)属性来获得最大列索引和最大数据列索引。而要获得列中的最大行索引和最大数据行索引，还需要创建列范围，然后遍历范围找到最后一个单元格，最后获取该单元格的[Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性。

Aspose.Cells 提供以下属性和方法，帮助您实现目标。
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **使用 Aspose.Cells 获取行中的最大列索引和列中的最大行索引**
此示例演示如何：

1. 加载[示例文件](sample.xlsx)。
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 获取[Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)属性。
1. 根据列创建一个范围。
1. 获取迭代器并遍历范围。
1. 获取[Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/)属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}

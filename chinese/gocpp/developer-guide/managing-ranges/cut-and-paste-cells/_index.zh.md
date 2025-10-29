---
title: 用Golang通过C++剪切和粘贴范围
linktitle: 剪切和粘贴范围
type: docs
weight: 130
url: /zh/go-cpp/cut-and-paste-cells/
description: 学习如何使用Aspose.Cells for C++在工作表内剪切和粘贴单元格。
---

## **剪切和粘贴单元格**

Aspose.Cells允许你通过使用[**InsertCutCells**](https://reference.aspose.com/cells/go-cpp/cells/insertcutcells/)方法和[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的[**InsertCutCells**](https://reference.aspose.com/cells/go-cpp/cells/insertcutcells/)方法在工作表中剪切粘贴单元格，参数如下：

- [**Range**](https://reference.aspose.com/cells/go-cpp/range/)：要剪切的单元格范围。
- 行索引：要插入单元格的行索引。
- 列索引：要插入单元格的列索引。
- [**ShiftType**](https://reference.aspose.com/cells/go-cpp/shifttype/)：列的移动方向。

以下示例展示了如何在工作表中剪切和粘贴单元格。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CutAndPasteCells.go" >}}

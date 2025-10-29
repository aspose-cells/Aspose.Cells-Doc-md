---
title: 用Golang通过C++合并或取消合并单元格范围
linktitle: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/go-cpp/merge-or-unmerge-range-of-cells/
description: 使用Golang通过C++代码在Excel中合并和取消合并范围内的单元格。
keywords: 用C++合并和取消合并范围内的单元格，使用C++合并和取消合并范围内的单元格，使用C++合并和取消合并单元格范围，使用C++合并和取消合并单元格，使用C++在Excel中合并和取消合并单元格，使用C++在Excel中合并单元格，使用C++取消合并单元格，使用C++在范围内合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/) 和 [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

## **示例**

以下示例代码首先创建一个范围 — A1:D4 — 然后使用[**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/)方法将该范围中的单元格合并成一个单元格。类似地，你也可以通过创建范围并调用[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)方法来拆分单元格。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeOrUnmergeRangeOfCells.go" >}}

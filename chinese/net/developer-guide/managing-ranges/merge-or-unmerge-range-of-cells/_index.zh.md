---
title: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/net/merge-or-unmerge-range-of-cells/
description: 使用 C# 代码在 Excel 中合并和取消合并单元格范围。
keywords: c# 在范围内合并和取消合并单元格，c# 在范围内合并和取消合并单元格，使用 c# 在范围内合并和取消合并单元格，使用 c# 在 Excel 中合并和取消合并单元格，使用 c# 在 Excel 中合并和取消合并单元格，c# 在 Excel 中合并和取消合并单元格，c# 在 Excel 中合并单元格，c# 在 Excel 中取消合并单元格，使用 c# 在范围内合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) 和 [**Range.UnMerge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/unmerge) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

## **示例**

以下示例代码首先创建范围 - A1:D4 - 然后使用 [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) 方法将范围中的单元格合并为单个单元格。类似地，您可以通过创建范围并调用 [**Range.UnMerge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/unmerge) 方法来拆分单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-MergeUnmergeRangeOfCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

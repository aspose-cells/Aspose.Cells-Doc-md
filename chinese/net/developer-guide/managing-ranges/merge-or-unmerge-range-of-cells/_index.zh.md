---
title: 合并或拆分单元格范围
type: docs
weight: 190
url: /zh/net/merge-or-unmerge-range-of-cells/
description: 使用C#代码在Excel中合并和拆分范围中的单元格。
keywords: 在C#中合并和拆分范围中的单元格，在C#中合并和拆分范围中的单元格，使用C#合并和拆分范围中的单元格，使用C#在Excel中合并和拆分范围中的单元格，使用C#在Excel中合并和拆分范围中的单元格，C#在Excel中合并和拆分单元格，C#在Excel中合并单元格，C#在Excel中拆分单元格，使用C#合并单元格范围
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells来合并或拆分单元格范围。Aspose.Cells提供了[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)和[**Range.UnMerge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/unmerge)方法来实现这一目的。本文解释了如何将一组单元格合并为单个单元格。

{{% /alert %}}

## **例子**

下面的示例代码首先创建一个范围 - A1:D4 - 然后使用[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)方法将范围中的单元格合并为单个单元格。类似地，您可以通过创建范围并调用[**Range.UnMerge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/unmerge)方法来拆分单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-MergeUnmergeRangeOfCells-1.cs" >}}

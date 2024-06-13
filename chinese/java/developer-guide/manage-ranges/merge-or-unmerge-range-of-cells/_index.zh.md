---
title: 合并或取消合并单元格范围
type: docs
weight: 70
url: /zh/java/merge-or-unmerge-range-of-cells/
description: 使用Java代码在Excel中合并和拆分单元格范围。
keywords: java在范围内合并和拆分单元格, java在范围内合并和拆分单元格, 使用java在范围内合并和拆分单元格, 使用java在范围内合并和拆分单元格, 使用java在Excel中合并和拆分单元格, 使用java在Excel中合并和拆分单元格, java在Excel中合并和拆分单元格, java在Excel中合并单元格, java在Excel中拆分单元格, 使用java在Excel中合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge--) 和 [**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge--) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

以下示例代码首先创建一个范围 - A1:D4 - 然后使用[**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge--)方法将范围中的单元格合并为一个单元格。
类似地，可以通过创建一个范围并调用[**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge--)方法来拆分单元格。

下图显示了使用示例代码生成的输出Excel文件。如您所见，范围A1:D4已合并为单个单元格。

![todo:image_alt_text](merge-or-unmerge-range-of-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-MergeUnmergeRangeofCells-MergeUnmergeRangeofCells.java" >}}

{{% alert color="primary" %}}

## **相关文章**

- [合并和拆分单元格](/cells/zh/java/merging-and-unmerging-cells/).

{{% /alert %}}

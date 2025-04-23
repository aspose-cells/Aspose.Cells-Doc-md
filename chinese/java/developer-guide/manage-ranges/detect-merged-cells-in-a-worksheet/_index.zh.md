---
title: 检测工作表中的合并单元
type: docs
weight: 3000
url: /zh/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

在 Microsoft Excel 中，几个单元格可以合并成一个单元格。这通常用于创建复杂的表格或创建一个横跨多列的标题单元格。

Aspose.Cells 允许您识别工作表中的合并单元格区域。您也可以取消合并它们。本文提供了使用 Aspose.Cells 执行此任务的最简单代码行。

本文提供了如何在工作表中查找并取消合并合并单元格的简明说明。

{{% /alert %}}

## **演示**

此示例使用名为 MergeTrial 的模板 Microsoft Excel 文件。该文件中的工作表也称为 Merge Trial 中有一些合并的单元格区域。

模板文件

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells 提供 [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) 方法，用于获取所有合并单元格。

当执行下面的代码时，它会清除工作表的内容并在再次保存文件之前取消所有单元格区域的合并。

输出文件

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **代码示例**

请参阅以下示例代码，了解如何识别工作表中的合并单元格区域并取消合并它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **相关文章**

- [合并和拆分单元格](/cells/zh/java/merging-and-unmerging-cells/).
{{< app/cells/assistant language="java" >}}

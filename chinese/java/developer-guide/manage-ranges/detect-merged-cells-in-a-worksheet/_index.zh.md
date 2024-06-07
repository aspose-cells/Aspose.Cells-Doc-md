---
title: 检测工作表中的合并单元格
type: docs
weight: 3000
url: /zh/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

在Microsoft Excel中，可以将多个单元格合并为一个。这通常用于创建复杂的表格或创建横跨多列的标题单元格。

Aspose.Cells允许您识别工作表中合并的单元格区域。您还可以取消合并。本文提供了使用Aspose.Cells执行该任务的最简单代码行。

本文提供了在工作表中查找并取消合并的指令。

{{% /alert %}}

## **演示**

此示例使用名为**MergeTrial**的模板Microsoft Excel文件。在名为Merge Trial的工作表中有一些合并的单元格区域。

**模板文件**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells提供了[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)方法，用于获取合并单元格区域的ArrayList。

当执行下面的代码时，它会在保存文件之前清除工作表的内容并取消合并所有单元格区域。

**输出文件**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **代码示例**

请查看以下示例代码，了解如何识别工作表中的合并单元格区域并取消合并。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **相关文章**

- [合并和拆分单元格](/cells/zh/java/merging-and-unmerging-cells/)。

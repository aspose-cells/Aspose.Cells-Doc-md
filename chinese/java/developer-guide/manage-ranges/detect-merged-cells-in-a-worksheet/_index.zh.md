---
title: 在工作表中检测合并的 Cells
type: docs
weight: 3000
url: /zh/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

在 Microsoft Excel 中，可以将多个单元格合并为一个。这通常用于创建复杂的表格或创建包含跨越多列的标题的单元格。

Aspose.Cells 允许您识别工作表中的合并单元格区域。您也可以取消合并它们。本文提供了使用 Aspose.Cells 执行任务的最简单的代码行。

本文提供了有关如何在工作表中查找并取消合并合并单元格的简要说明。

{{% /alert %}}

## **示范**

此示例使用名为 Microsoft 的 Excel 文件模板**合并试验**.它在工作表中有一些合并的单元格区域，也称为合并试验。

**模板文件**

![待办事项：图片_替代_文本](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells 提供了[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)用于获取合并单元格区域的 ArrayList 的方法。

当执行下面的代码时，它会清除工作表的内容并在再次保存文件之前取消合并所有单元格区域。

**输出文件**

![待办事项：图片_替代_文本](detect-merged-cells-in-a-worksheet_2.png)

## **代码示例**

请参阅以下示例代码，了解如何识别工作表中的合并单元格区域并取消合并它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **相关文章**

- [合并和拆分单元格](/cells/zh/java/merging-and-unmerging-cells/).

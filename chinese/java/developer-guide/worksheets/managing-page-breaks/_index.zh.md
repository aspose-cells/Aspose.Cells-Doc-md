---
title: 管理分页
type: docs
weight: 30
url: /zh/java/managing-page-breaks/
---

{{% alert color="primary" %}}

分页符是文本中一页结束并开始下一页的地方。Microsoft Excel 可以在工作表中的任何选定单元格处添加分页符。
页面在添加分页符的单元格处结束，并且分页符后的所有数据将打印在下一页。简单来说，分页符将工作表分成多个页面。使用 Aspose.Cells，也可以在运行时向工作表添加分页符。Aspose.Cells 支持两种分页符：

- 水平
- 垂直。

本文描述了如何使用 Aspose.Cells 向工作表添加水平或垂直分页符。

{{% /alert %}}

## **Aspose.Cells 和分页符**

Aspose.Cells 提供一个代表 Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示，该类提供了许多用于管理工作表的属性和方法。要添加分页符，请使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) 和 [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) 属性。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) 和 [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) 属性实际上是集合，可能包含几个分页符。每个集合都包含用于管理水平和垂直分页符的几种方法。下面将讨论如何使用这些方法。

## **添加分页**

要在工作表中添加分页符，通过调用 [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) 和 [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) 集合的 **Add** 方法在指定单元格处插入垂直和水平分页符。每个 **Add** 方法都会使用要添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

## **清除所有分页符**

要清除工作表中的所有分页符，请调用 [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) 和 [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) 集合的 **Clear** 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **移除特定的分页符**

要在工作表中移除特定的分页符，请调用 [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) 和 [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) 集合的 **removeAt** 方法。每个 **removeAt** 方法将使用要移除的分页符的索引。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**重要提示**：当设置页面设置设置中的适合页面属性（即 [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) 和 [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)）时，分页符设置会受到影响，因此，如果打印工作表，则分页符设置将不会被考虑，尽管它们仍然存在于文件中。

{{% /alert %}}

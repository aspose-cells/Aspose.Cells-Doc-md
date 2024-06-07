---
title: 管理分页
type: docs
weight: 30
url: /zh/java/managing-page-breaks/
---

{{% alert color="primary" %}}

分页符是文本中一个页面结束并另一个页面开始的位置。Microsoft Excel可以在工作表中的任何选定单元格处添加分页符。
页面在添加了分页符的单元格结束，并在分页符后的所有数据都打印在下一页。简单来说，分页符将工作表分割成多个页面。还可以使用Aspose.Cells在运行时向工作表添加分页符。Aspose.Cells支持两种类型的分页符:

- 水平
- 垂直。

本文描述了如何使用Aspose.Cells向工作表添加水平或垂直分页符。

{{% /alert %}}

## **Aspose.Cells和分页符**

Aspose.Cells提供了一个代表Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个允许访问Excel文件中每张工作表的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示，它提供了广泛的属性和方法来管理工作表。要添加分页符，请使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)和[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)属性。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)和[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)属性实际上是可能包含多个分页符的集合。每个集合包含用于管理水平和垂直分页符的多个方法。下面讨论了这些方法如何使用。

## **添加分页符**

要向工作表中添加分页符，通过调用[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)集合的**Add**方法，在指定的单元格处插入垂直和水平分页符。每个**Add**方法都需要添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

在分页符预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

## **清除所有分页符**

要清除工作表中的所有分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)集合的**Clear**方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **移除特定分页符**

要移除工作表中的特定分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)集合的**removeAt**方法。每个**removeAt**方法需要移除的分页符索引。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**需要注意的是**：当设置适合页面属性（即[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)和[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)）的页面设置时，会影响分页符设置，因此，如果打印工作表，则分页符设置不会被考虑，尽管它们仍存在于文件中。

{{% /alert %}}

---
title: 管理分页符
type: docs
weight: 30
url: /zh/java/managing-page-breaks/
---
{{% alert color="primary" %}}

分页符是文本中一页结束和下一页开始的地方。 Microsoft Excel 可以在工作表中的任何选定单元格处添加分页符。
页面在添加分页符的单元格结束，分页符后的所有数据打印在下一页上。简而言之，分页符将工作表分成多个页面。也可以使用 Aspose.Cells 在运行时向工作表添加分页符。Aspose.Cells 支持两种分页符：

- 水平的
- 垂直的。

本文介绍如何使用 Aspose.Cells 在工作表中添加水平或垂直分页符。

{{% /alert %}}

## **Aspose.Cells & 分页符**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类，它提供了广泛的属性和方法来管理工作表。要添加分页符，请使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**水平分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)和[**垂直分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)特性。

这[**水平分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)和[**垂直分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)属性实际上是可能包含多个分页符的集合。每个集合都包含几种用于管理水平和垂直分页符的方法。下面将讨论如何使用这些方法。

## **添加分页符**

要在工作表中添加分页符，请通过调用[**水平分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**垂直分页符**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)收藏品'**添加**方法。每个**添加**方法采用要添加分页符的单元格名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页是如何工作的。

{{% /alert %}}

## **清除所有分页符**

要清除工作表中的所有分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)收藏品'**清除**方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **删除特定分页符**

要删除工作表中的特定分页符，请调用[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)和[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)收藏品'**移除点**方法。每个**移除点**方法将采用要删除的分页符的索引。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**重要须知**：当您设置适合页面属性时（即[**适合页面高**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)和[**适合页面宽度**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)在页面设置中，分页符设置会受到影响，因此，如果您打印工作表，则不会考虑分页符设置，尽管它们仍然存在于文件中。

{{% /alert %}}

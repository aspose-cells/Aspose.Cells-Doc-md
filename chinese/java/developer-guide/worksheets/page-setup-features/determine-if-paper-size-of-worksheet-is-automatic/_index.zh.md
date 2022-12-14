---
title: 确定工作表的纸张大小是否为自动
type: docs
weight: 20
url: /zh/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **可能的使用场景**

大多数时候，工作表的纸张大小是自动的。自动时，常设置为*信*.有时用户会根据他们的要求设置工作表的纸张大小。在这种情况下，纸张尺寸不是自动的。您可以使用[**工作表.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)方法。

## **确定工作表的纸张大小是否为自动**

下面给出的示例代码加载了以下两个 Excel 文件

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

并查看他们的第一个工作表的纸张大小是否是自动的。在 Microsoft Excel 中，您可以通过页面设置窗口检查纸张大小是否自动，如屏幕截图所示。

![待办事项：图片_替代_文本](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **控制台输出**

这是使用给定示例 Excel 文件执行时上述示例代码的控制台输出。

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}

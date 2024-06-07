---
title: 确定工作表的纸张大小是否为自动
type: docs
weight: 20
url: /zh/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **可能的使用场景**

大多数情况下，工作表的纸张大小是自动的。当纸张大小是自动设置时，通常设置为*Letter*。有时用户根据需要设置工作表的纸张大小。在这种情况下，纸张大小不是自动的。您可以使用[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) 方法查找工作表纸张大小是否为自动的。

## **确定工作表的纸张大小是否为自动**

给定以下两个Excel文件的示例代码

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

以及查找它们的第一个工作表的纸张大小是否为自动。在Microsoft Excel中，您可以通过页面设置窗口检查纸张大小是否为自动，如此屏幕截图所示。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **控制台输出**

以下是执行给定示例Excel文件时上述示例代码的控制台输出。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}

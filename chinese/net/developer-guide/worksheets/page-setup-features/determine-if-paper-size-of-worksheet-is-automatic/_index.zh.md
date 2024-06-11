---
title: 确定工作表的纸张尺寸是否为自动
type: docs
weight: 90
url: /zh/net/determine-if-paper-size-of-worksheet-is-automatic/
description: 本文解释了如何使用C# API或.NET库示例代码以编程方式确定工作表的纸张大小是否为自动。
keywords: 确定工作表纸张大小是否为自动c#
---

## **可能的使用场景**

大多数情况下，工作表的纸张大小是自动的。当它是自动的时候，通常设置为*Letter*。有时用户根据自己的需求设置工作表的纸张大小。在这种情况下，纸张大小不是自动的。您可以使用[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)属性来查看工作表纸张大小是否为自动。

## **确定工作表的纸张大小是否自动**

以下给出的示例代码加载以下两个Excel文件

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

并找到它们的第一个工作表的纸张尺寸是否为自动。在Microsoft Excel中，您可以通过页面设置窗口（如截图所示）检查纸张尺寸是否是自动的。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **控制台输出**

以下是上述示例代码在给定的示例Excel文件上执行时的控制台输出。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}

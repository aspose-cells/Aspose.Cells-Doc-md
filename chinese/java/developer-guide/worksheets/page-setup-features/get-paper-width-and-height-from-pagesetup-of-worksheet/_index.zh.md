---
title: 从工作表的页面设置获取纸张的宽度和高度
type: docs
weight: 300
url: /zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/
---

## **可能的使用场景**

有时，您需要知道工作表页面设置中设置的纸张尺寸的宽度和高度。为此，请使用[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight)属性。

## **从工作表的页面设置获取纸张的宽度和高度**

以下示例代码解释了[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight)属性的用法。首先将纸张大小更改为A2，然后找到纸张的宽度和高度，然后将其更改为A3、A4、Letter，并依次找到纸张的宽度和高度。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-GetPaperWidthHeight-GetPaperWidthHeight.java" >}}

## **控制台输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11.0

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

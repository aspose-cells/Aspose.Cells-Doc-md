---
title: 获取工作表的页面设置纸张宽度和高度
type: docs
weight: 50
url: /zh/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: 在本文中，您将了解如何使用C#代码以编程方式获取Excel工作表页面设置的纸张宽度和高度，借助.NET API或库。
keywords: excel页面设置纸张宽度 c#，excel页面设置纸张高度 c#
---

## **可能的使用场景**

有时，您需要知道工作表页面设置中纸张大小的宽度和高度。请用[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)属性来实现此目的。

## **获取工作表的页面设置纸张宽度和高度**

以下示例代码解释了如何使用[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)属性。它首先将纸张大小更改为*A2*，然后找到纸张的宽度和高度，然后将其更改为*A3*、*A4*、*Letter*，并分别找到纸张的宽度和高度。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **控制台输出**

这是上述示例代码的控制台输出。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}

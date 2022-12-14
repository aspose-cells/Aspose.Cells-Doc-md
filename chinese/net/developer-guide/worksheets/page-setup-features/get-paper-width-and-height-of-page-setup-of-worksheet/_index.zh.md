---
title: 获取工作表页面设置的纸张宽度和高度
type: docs
weight: 50
url: /zh/net/get-paper-width-and-height-of-page-setup-of-worksheet/
---
## **可能的使用场景**

有时，您需要知道纸张尺寸的宽度和高度，因为它已在工作表的页面设置中设置。请使用[**页面设置.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)用于此目的的属性。

## **获取工作表页面设置的纸张宽度和高度**

下面的示例代码解释了[**页面设置.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)和[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)特性。它首先将纸张大小更改为*A2*然后找到纸张的宽度和高度，然后将其更改为*A3*, *A4*, *信*并分别求出纸张的宽度和高度。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **控制台输出**

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}

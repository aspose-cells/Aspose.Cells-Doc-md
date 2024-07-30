---
title: 获取工作表页面设置的纸张宽度和高度
type: docs
weight: 50
url: /zh/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: 在本文中，您将发现如何使用python代码通过Aspsoe.Cells for Python via .NET API或库以程序方式获取Excel工作表页面设置的纸张宽度和纸张高度。
keywords: Python Excel库，Python设置工作表的自定义纸张宽度，Python中的Excel页面设置纸张高度。
---

## **可能的使用场景**

有时，您需要知道页面设置中纸张大小的宽度和高度。请为此目的使用[**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)和[**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)属性。

## **获取工作表页面设置的纸张宽度和高度**

以下示例代码解释了[**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)和[**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)属性的用法。它首先将纸张尺寸更改为*A2*，然后找到纸张的宽度和高度，然后将其更改为*A3*、 *A4*、 *Letter*并分别找到纸张的宽度和高度。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **控制台输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}

---
title: 获取工作表页面设置的纸张宽度和高度
type: docs
weight: 50
url: /zh/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: 本文将教你如何使用 Aspose.Cells for Python via .NET API，程序化获取 Excel 工作表页面设置中的纸宽和纸高。
keywords: Python Excel 库，Python 设置页面宽度，Excel 页面高度在 Python 中。
---

## **可能的使用场景**

有时，您需要知道页面设置中纸张大小的宽度和高度。请为此目的使用[**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)和[**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)属性。

## **获取工作表页面设置的纸张宽度和高度**

以下示例代码演示 [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) 和 [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) 属性的用法。首先将纸张大小改为 *A2*，然后获取纸张宽度和高度，接着设为 *A3*、*A4*、*Letter* 并分别找出纸张宽度和高度。

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
{{< app/cells/assistant language="python-net" >}}

---
title: 限制生成的页面数 - Excel 到 PDF 转换
type: docs
weight: 180
url: /zh/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将渲染 Excel 时生成的页面数限制为 PDF。
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

有时，您想要将一系列页面打印到输出 PDF 文件。 Aspose.Cells for Python via .NET 能够设置将 Excel 电子表格转换为 PDF 文件格式时生成的页面数量限制。

{{% /alert %}}

##  **限制生成的页面数**

以下示例演示如何将 Microsoft Excel 文件中的一系列页面（3 和 4）渲染为 PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[工作簿.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法，然后将其渲染到 PDF。这样做可确保重新计算公式相关值，并在输出文件中渲染正确的值。

{{% /alert %}}

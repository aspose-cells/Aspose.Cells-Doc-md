---
title: 限制生成的页面数量 - Excel转PDF转换
type: docs
weight: 180
url: /zh/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 学习如何在将 Excel 转换为 PDF 时限制生成的页面数，使用 Aspose.Cells for Python via .NET API。
keywords: 在将Excel渲染为PDF时限制生成的页面数量，使用Python保存Excel为PDF时限制生成的页面数量，在将Excel转换为PDF时设置生成的页面数量，在python中控制生成用于Excel为PDF的页面数量
---

{{% alert color="primary" %}}

有时，您希望将页面范围打印到PDF文件中。Aspose.Cells for Python通过.NET可以在将Excel电子表格转换为PDF文件格式时设置生成的页面数量限制。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示如何将 Microsoft Excel 文件的页面范围(第3页和第4页)渲染为PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其渲染为PDF之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样可以确保重新计算依赖于公式的值，并在输出文件中呈现正确的值。

{{% /alert %}}

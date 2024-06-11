---
title: 限制生成的页面数量 - 将Excel转换为PDF
type: docs
weight: 180
url: /zh/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 学习如何使用Aspose.Cells for Python via .NET API在渲染Excel到PDF时限制所生成的页面数量。
keywords: Python限制在将Excel转换为PDF时所生成的页面数量，在Python中保存Excel为PDF时限制生成的页面数量，Python将Excel转换为PDF时设置生成的页面数量，在Python中控制生成Excel到PDF的页面数量
---

{{% alert color="primary" %}}

有时，您希望将一系列页面打印到输出PDF文件。Aspose.Cells for Python via .NET具有在将Excel电子表格转换为PDF文件格式时设置生成的页面数量的能力。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其渲染为PDF之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样做可以确保重新计算基于公式的值，并在输出文件中呈现正确的值。

{{% /alert %}}

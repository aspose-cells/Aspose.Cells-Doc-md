---
title: 将Excel工作表渲染为一份PDF页面  Excel转PDF转换
type: docs
weight: 100
url: /zh/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: 学习如何使用Aspose.Cells for Python via .NET API将Excel工作表转换为PDF时渲染每个Excel工作表为一份PDF页面。
keywords: 使用Python将每个Excel工作表渲染为一份PDF页面，同时将Excel保存为PDF时渲染每个Excel工作表为一份PDF页面，Python在将Excel转换为PDF时显示每个工作表的一页
---

{{% alert color="primary" %}} 

当处理大型Microsoft Excel文件时（例如一个包含许多工作表的工作簿，每个工作表都有50列和300多行数据），您可能希望PDF输出每个工作表显示一页，而不管工作表的大小如何。这意味着每个页面可能具有完全不同的页面大小。可以使用Aspose.Cells for Python via .NET API来实现这一点。

{{% /alert %}} 

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

如果[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) 选项设置为**true**，则所有工作表内容将被渲染到一个PDF页面中。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格渲染为PDF之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) 方法。这可以确保重新计算基于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

---
title: 将所有工作表列放在单个 PDF 页上
type: docs
weight: 160
url: /zh/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: 了解如何使用 Aspose.Cells for Python via .NET API 在单个 PDF 页面上调整所有工作表列。
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

有时您想要生成一个 PDF 文件，将工作表的所有列放入一页。这[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property 以非常易于使用的方式提供此功能。输出 PDF 的高度和宽度等复杂计算在内部处理，并基于工作表中的数据。

{{% /alert %}}

##  **在单个 PDF 页上调整工作表列**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)确保工作表中的所有列都呈现到单个 PDF 页面，尽管行可能会根据工作表中的数据扩展到多个页面。

下面的示例代码展示了如何使用[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)属性来呈现 100 列的大型工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

当给定工作表有很多列时，呈现的 PDF 文件可能会以非常小的尺寸显示内容。当在 Acrobat Reader 等查看应用程序中放大时，它仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好致电[工作簿.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法在将电子表格渲染为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

---
title: 每个 Excel 工作表渲染一页 PDF - Excel 到 PDF 转换
type: docs
weight: 100
url: /zh/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: 了解如何渲染每个 Excel 工作表一页 PDF，同时使用 Aspose.Cells for Python via .NET API 将 Excel 转换为 PDF。
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

处理大型 Microsoft Excel 文件（例如，包含多个工作表的工作簿，每个工作表包含 50 列和 300 行或更多行数据）时，您可能希望 PDF 输出为每个工作表显示一页，无论工作表的大小如何。这意味着每个页面可能具有完全不同的页面大小。这可以通过使用 Aspose.Cells for Python via .NET API 来实现。

{{% /alert %}} 

请参阅以下示例代码，将具有多个工作表的 Excel 文件转换为 PDF。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

如果[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)选项设置为*true**，所有工作表内容将呈现到一页 PDF 页面。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，最好致电[工作簿.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法在将电子表格渲染到 PDF 之前。这可确保重新计算公式相关值，并在 PDF 中渲染正确的值。

{{% /alert %}}

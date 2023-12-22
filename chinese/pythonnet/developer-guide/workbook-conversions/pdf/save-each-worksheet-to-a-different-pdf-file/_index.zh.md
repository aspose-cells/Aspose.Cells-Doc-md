---
title: 将每个工作表保存到不同的 PDF 文件
type: docs
weight: 130
url: /zh/python-net/save-each-worksheet-to-a-different-pdf-file/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将每个工作表保存到不同的 PDF 文件。
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET 支持将 XLS 文件（包含图像、图表等）转换为 PDF 文档。 Aspose.Cells for Python via .NET 可以独立工作将电子表格转换为 PDF，并且您不需要使用 Aspose.PDF for .NET 进行转换。转换不需要软件创建或使用任何临时文件，因为整个过程可以在内存中完成。

{{% /alert %}} 
##  **将每个工作表保存到不同的 PDF 文件**
如果您需要将每个工作表保存在模板 Excel 文件中以生成不同的 PDF 文件，您可以轻松实现这一点。您可以尝试将一页索引设置为**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginationsaveoptions/sheet_set/)**一次选择渲染到 PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好致电[**工作簿.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)就在将电子表格渲染为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

---
title: 每个Excel工作表呈现为一个PDF页面 - Excel转PDF转换
type: docs
weight: 100
url: /zh/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: 学习如何在使用Aspose.Cells for Python通过.NET API将Excel转换为PDF时将每个Excel工作表呈现为一个PDF页面。
keywords: 将文件保存为PDF时使用Python将每个Excel工作表呈现为一个PDF页面，在将Excel保存为PDF时使用Python将每个Excel工作表呈现为一个PDF页面
---

{{% alert color="primary" %}} 

在处理具有多个工作表的大型Microsoft Excel文件时（例如，每个具有50列和300多行数据的工作表的工作簿），您可能希望PDF输出显示每个工作表一页，无论工作表的大小如何。这意味着每个页面可能具有截然不同的页面大小。通过使用Aspose.Cells for Python通过.NET API可以实现此目标。

{{% /alert %}} 

请参阅以下转换多个工作表的 Excel 文件为 PDF 的示例代码。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

如果将[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)选项设置为**true**，则所有工作表内容将呈现为一个PDF页面。

{{% /alert %}} {{% alert color="primary" %}} 

如果电子表格包含公式，最好在将电子表格渲染为PDF之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样可以确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

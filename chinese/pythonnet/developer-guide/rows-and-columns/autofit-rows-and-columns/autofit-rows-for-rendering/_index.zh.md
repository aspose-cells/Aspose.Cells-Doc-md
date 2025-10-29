---
title: 在渲染时自动调整列的行高
type: docs
weight: 130
url: /zh/python-net/autofit-rows-for-rendering/
description: 了解如何通过 Aspose.Cells for Python via .NET API 进行渲染时自动调整行高。
keywords: Python Excel 库，Python 渲染时自动调整行高，当打开 Excel 文件时，Python 会自动调整行高。 
---

通常，当您想要在单元格中显示所有文本时，您可以在 Microsoft Excel 的普通视图中进行行高自动调整，放大到 100%。这样可以在普通视图中完全显示文本，甚至在打印或将文件保存为 PDF 时，文本也能正确显示。

但在一些情况下，自动调整行在普通视图中效果良好，但当切换到打印视图或将文件保存为 PDF 时，文本会被截断。请查看源文件 [Book1.xlsx](Book1.xlsx) 和屏幕截图。

![打印视图中文本被截断](text_clipped_in_printview.png)

如果您想要防止在保存的 PDF 文件中文本被截断，可以使用 [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/) 选项进行自动调整行。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

现在，在输出的 PDF 文件中文本不再被截断。

![保存的 PDF 文件中文本未被截断](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}

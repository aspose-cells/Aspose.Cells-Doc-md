---
title: 渲染时自动调整行高
type: docs
weight: 130
url: /zh/python-net/autofit-rows-for-rendering/
description: 学习如何通过 Aspose.Cells for Python 的 .NET API 自动调整渲染行高。
keywords: Python Excel 库，Python 渲染自动调整行高，Python 打开 Excel 文件时自动调整行高。 
---

通常，当您想要在单元格中显示所有文本时，可以在Microsoft Excel的正常视图中以100%缩放比例自动调整行高。这样可以确保文本在正常视图中完全可见，即使在打印或保存文件为PDF时，文本也将正确显示。

然而，在某些情况下，自动调整行在正常视图中效果很好，但当切换到打印视图或将文件另存为PDF时，文本会被截断。请查看源文件[Book1.xlsx]（Book1.xlsx）和屏幕截图。

![文本在打印视图中被截断](text_clipped_in_printview.png)

如果您想在保存的 PDF 文件中防止文字被裁剪，可以使用 [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/) 选项自动调整行高。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

现在，在输出的PDF文件中，文本不会被剪切。

![文本未在保存的PDF中被剪切](text_not_clipped_in_saved_pdf.png)

---
title: 在渲染时自动调整列的行高
type: docs
weight: 130
url: /zh/java/autofit-rows-for-rendering/
---

通常，当您想要在单元格中显示所有文本时，您可以在 Microsoft Excel 的普通视图中进行行高自动调整，放大到 100%。这样可以在普通视图中完全显示文本，甚至在打印或将文件保存为 PDF 时，文本也能正确显示。

但在一些情况下，自动调整行在普通视图中效果良好，但当切换到打印视图或将文件保存为 PDF 时，文本会被截断。请查看源文件 [Book1.xlsx](Book1.xlsx) 和屏幕截图。

![打印视图中文本被截断](text_clipped_in_printview.png)

如果要防止保存的PDF文件中出现文本被裁剪，可以使用[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) 选项来自动调整行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

现在，在输出的 PDF 文件中文本不再被截断。

![保存的 PDF 文件中文本未被截断](text_not_clipped_in_saved_pdf.png)

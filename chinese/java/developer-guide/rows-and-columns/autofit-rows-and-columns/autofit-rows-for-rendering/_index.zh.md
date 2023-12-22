---
title: 用于渲染的自动调整行
type: docs
weight: 130
url: /zh/java/autofit-rows-for-rendering/
---
通常，当您想要显示单元格中的所有文本时，您可以在 Microsoft Excel 中以 100% 缩放的普通视图中自动调整行。这使得文本在普通视图中完全可见，即使您打印或将文件另存为 PDF，文本也将正确显示。

但是，在某些情况下，自动调整行在普通视图中工作正常，但当您切换到打印视图或将文件另存为 PDF 时，文本会被剪切。请检查源文件[书1.xlsx](Book1.xlsx)和屏幕截图。

![文本在打印视图中被剪裁](text_clipped_in_printview.png)

如果您想防止在保存的 PDF 文件中剪切文本，您可以使用以下命令自动调整行[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-)选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

现在，输出 PDF 文件中的文本不会被剪切。

![保存的 pdf 中的文本未被剪裁](text_not_clipped_in_saved_pdf.png)
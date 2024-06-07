---
title: 重新采样添加的图像 - Excel 转为 PDF
type: docs
weight: 150
url: /zh/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

在处理包含大量图像的大型 Microsoft Excel 文件时，您可能需要压缩已添加的图像，以减小输出 PDF 文件的大小并改善整体转换性能。Aspose.Cells 支持重新采样已添加的图像，以减小输出 PDF 文件的大小并在一定程度上提高性能。

{{% /alert %}}

请参阅以下描述如何使用 Aspose.Cells API 执行任务的示例代码。该示例将 Microsoft Excel 文件转换为 PDF 文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

使用 [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) 选项可以最小化输出 PDF 的大小，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算公式相关值，并且正确的值呈现在PDF中。

{{% /alert %}}

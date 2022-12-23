---
title: 重新采样添加的图像 - Excel 到 PDF 的转换
type: docs
weight: 150
url: /zh/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

在处理包含大量图像的大 Microsoft Excel 文件时，您可能需要压缩已添加的图像以减小输出 PDF 文件大小并提高整体转换性能。 Aspose.Cells 支持重新采样添加的图像以减少输出 PDF 文件大小并提高性能。

{{% /alert %}}

请参阅以下示例代码，它描述了如何使用 Aspose.Cells API 执行任务。该示例将 Microsoft Excel 文件转换为 PDF 文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

使用的[**设置图像重采样**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)选项最小化输出 PDF 的大小，但它可能会影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

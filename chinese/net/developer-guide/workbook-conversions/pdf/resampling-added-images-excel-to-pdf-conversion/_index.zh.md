---
title: 重新采样添加的图像-将Excel转换为PDF
type: docs
weight: 150
url: /zh/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

当处理包含大量图片的大型Microsoft Excel文件时，您可能需要压缩已添加的图片，以减小输出的PDF文件大小并提高整体转换性能。Aspose.Cells支持重新采样已添加的图像，以减小输出的PDF文件大小并稍微提高性能。

{{% /alert %}}

请参阅以下示例代码，描述如何使用Aspose.Cells API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，并压缩文件中的图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

使用 [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) 选项可使输出PDF的大小最小化，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

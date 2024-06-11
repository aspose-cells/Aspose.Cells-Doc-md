---
title: 重新采样添加的图像-将Excel转换为PDF
type: docs
weight: 150
url: /zh/python-net/resample-added-images-excel-to-pdf-conversion/
description: 学习如何使用Aspose.Cells for Python via .NET API在将Excel转换为PDF时对添加的图像进行重新采样。
keywords: Python重新采样添加的图像-将Excel转换为PDF
---

{{% alert color="primary" %}}

在处理包含大量图像的大型Microsoft Excel文件时，您可能需要压缩已添加的图像，以减小输出PDF文件的大小并改善整体转换性能。Aspose.Cells for Python via .NET支持重新采样添加的图像以减小输出PDF文件的大小并在一定程度上改善性能。

{{% /alert %}}

请参阅以下示例代码，了解如何使用Aspose.Cells for Python via .NET API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

使用 [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) 选项可使输出PDF的大小最小化，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

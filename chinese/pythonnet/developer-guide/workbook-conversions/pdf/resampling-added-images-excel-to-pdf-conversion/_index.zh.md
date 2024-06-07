---
title: 重新取样添加的图像-Excel转PDF转换
type: docs
weight: 150
url: /zh/python-net/resample-added-images-excel-to-pdf-conversion/
description: 学习如何在使用Aspose.Cells for Python通过.NET API转换时重新取样添加的图像到PDF。
keywords: 在处理具有许多图像的大型Microsoft Excel文件时，您可能需要压缩已添加的图像以减小输出PDF文件大小并提高整体转换性能。Aspose.Cells for Python通过.NET支持对添加的图像进行重新取样以减小输出PDF文件大小并在一定程度上提高性能。
---

{{% alert color="primary" %}}

在处理具有大量图像的大型 Microsoft Excel 文件时，您可能需要压缩已添加的图像，以减小输出的 PDF 文件大小并提高整体转换性能。Aspose.Cells for Python via .NET 支持对已添加的图像进行重新采样，以减小输出的 PDF 文件大小并改善性能。

{{% /alert %}}

请参阅以下示例代码，描述如何使用Aspose.Cells for Python通过.NET API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

使用 [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) 选项可以最小化输出 PDF 的大小，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样做将确保重新计算公式相关值，并且正确的值呈现在PDF中。

{{% /alert %}}

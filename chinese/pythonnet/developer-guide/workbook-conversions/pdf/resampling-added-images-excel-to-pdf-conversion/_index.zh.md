---
title: 对添加的图像重新取样 - Excel 到 PDF 转换
type: docs
weight: 150
url: /zh/python-net/resample-added-images-excel-to-pdf-conversion/
description: 了解如何在使用 Aspose.Cells for Python via .NET API 将 Excel 转换为 pdf 时对添加的图像重新采样。
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

在处理包含大量图像的大 Microsoft Excel 文件时，您可能需要压缩已添加的图像以减少输出 PDF 文件大小并提高整体转换性能。 Aspose.Cells for Python via .NET 支持对添加的图像进行重新采样，以减少输出 PDF 文件大小并在一定程度上提高性能。

{{% /alert %}}

请参阅以下示例代码，该代码描述如何使用 Aspose.Cells for Python via .NET API 执行任务。该示例将 Microsoft Excel 文件转换为 PDF 文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

使用[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)选项可最小化输出 PDF 的大小，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好致电[**工作簿.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)就在将电子表格渲染为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

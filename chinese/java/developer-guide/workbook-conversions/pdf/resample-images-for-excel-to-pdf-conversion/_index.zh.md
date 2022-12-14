---
title: 为 Excel 到 PDF 转换重新采样图像
type: docs
weight: 250
url: /zh/java/resample-images-for-excel-to-pdf-conversion/
description: 本文演示了在将 Excel 文件转换为 PDF 时减小图像大小
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

在处理包含大量图像的大型 Microsoft Excel 文件时，您可能需要压缩已添加的图像以减小输出 PDF 文件的大小并提高整体转换性能。 Aspose.Cells 支持重新采样添加的图像以减少输出 PDF 文件大小并提高性能。

{{% /alert %}}

## **为 Excel 到 PDF 转换重新采样图像**

请参阅以下示例代码，它描述了如何使用 Aspose.Cells API 执行任务。该示例将 Microsoft Excel 文件转换为 PDF 文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

使用[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) 选项可以最小化输出 PDF 的大小，但它可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用[**工作簿.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()就在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

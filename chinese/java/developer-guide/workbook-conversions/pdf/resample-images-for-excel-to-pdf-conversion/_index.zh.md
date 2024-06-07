---
title: 为 Excel 转换为 PDF 重新采样图像
type: docs
weight: 250
url: /zh/java/resample-images-for-excel-to-pdf-conversion/
description: 本文演示了在将 Excel 文件转换为 PDF 时降低图像大小的方法
keywords: Excel 转 PDF，Excel 转 PDF 期间重新采样图像，Excel 转 PDF 期间压缩图像，Excel 转 PDF 期间减小图像大小，Excel 转 PDF 以较小尺寸保存，Excel 转 PDF 以图像重新采样进行转换，Excel 转 PDF 以图像压缩进行转换，Excel 转 PDF 期间重新采样图像 Java
---

{{% alert color="primary" %}}

在处理具有大量图像的大型 Microsoft Excel 文件时，您可能需要压缩已添加的图像以减小输出 PDF 文件大小并提高整体转换性能。Aspose.Cells 支持重新采样添加的图像以减小输出 PDF 文件大小并提高性能。

{{% /alert %}}

## **为 Excel 转换为 PDF 重新采样图像**

请参阅以下描述如何使用 Aspose.Cells API 执行任务的示例代码。该示例将 Microsoft Excel 文件转换为 PDF 文件，同时压缩文件中的图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

使用 [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int) 选项可以最小化输出 PDF 大小，但可能会稍微影响图像质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，在将电子表格呈现为 PDF 格式之前，最好调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula() 方法。这样可以确保公式依赖的值重新计算，并在 PDF 中呈现正确的值。

{{% /alert %}}

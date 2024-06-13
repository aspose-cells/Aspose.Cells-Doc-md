---
title: 重新采样图像以将Excel转换为PDF
type: docs
weight: 250
url: /zh/java/resample-images-for-excel-to-pdf-conversion/
description: 本文演示了在将Excel文件转换为PDF时减小图像大小的过程
keywords: 将excel转换为pdf，在excel转换为pdf期间重新采样图像，在excel转换为pdf期间压缩图像，在excel转换为pdf期间减小图像大小，在excel转换为pdf并使用更小的大小pdf，将excel转换为pdf采样图像重新采样，将excel转换为pdf压缩图像，并在java中对excel转换为pdf进行图像重新采样。
---

{{% alert color="primary" %}}

在处理包含大量图像的大型Microsoft Excel文件时，您可能需要压缩已添加的图像以减小输出PDF文件大小并提高整体转换性能。Aspose.Cells支持重新采样添加的图像以减小输出PDF文件大小并提高性能。

{{% /alert %}}

## **重新采样图像以将Excel转换为PDF**

请参阅以下示例代码，描述如何使用Aspose.Cells API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，并压缩文件中的图像。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

使用[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int))选项可以最大限度地减小输出PDF的大小，但可能会对图像质量产生一些影响。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

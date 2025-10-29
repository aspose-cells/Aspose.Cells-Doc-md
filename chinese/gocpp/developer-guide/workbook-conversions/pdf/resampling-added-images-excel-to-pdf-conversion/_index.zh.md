---
title: 重新采样已添加的图像——使用 C++ 通过 Golang 将 Excel 转换为 PDF
linktitle: 重新采样添加的图像 将Excel转换为PDF
type: docs
weight: 150
url: /zh/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: 学习如何重新采样添加的图像以减小 PDF 大小，使用 Aspose.Cells 通过 C++ 与 Golang。
---

{{% alert color="primary" %}}

当处理包含大量图片的大型Microsoft Excel文件时，您可能需要压缩已添加的图片，以减小输出的PDF文件大小并提高整体转换性能。Aspose.Cells支持重新采样已添加的图像，以减小输出的PDF文件大小并稍微提高性能。

{{% /alert %}}

请参阅以下示例代码，描述如何使用Aspose.Cells API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，并压缩文件中的图像。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

使用[**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/)选项可以最大限度地减小输出PDF的大小，但可能会对图像质量产生一些影响。

{{% /alert %}} 

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}


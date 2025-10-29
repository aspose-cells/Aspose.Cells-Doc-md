---
title: 使用 C++ 进行重采样添加的图片  Excel 转 PDF 转换
linktitle: 重新采样添加的图像 将Excel转换为PDF
type: docs
weight: 150
url: /zh/cpp/resampling-added-images-excel-to-pdf-conversion/
description: 学习如何使用 Aspose.Cells 与 C++ 进行重采样以减少 PDF 大小。
---

{{% alert color="primary" %}}

当处理包含大量图片的大型Microsoft Excel文件时，您可能需要压缩已添加的图片，以减小输出的PDF文件大小并提高整体转换性能。Aspose.Cells支持重新采样已添加的图像，以减小输出的PDF文件大小并稍微提高性能。

{{% /alert %}}

请参阅以下示例代码，描述如何使用Aspose.Cells API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，并压缩文件中的图像。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

使用[**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/)选项可以最大限度地减小输出PDF的大小，但可能会对图像质量产生一些影响。

{{% /alert %}} 

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}

---
title: 使用 C++ 以标准或最小尺寸保存 Excel 为 PDF
linktitle: 使用标准大小或最小大小将Excel保存为PDF
type: docs
weight: 340
url: /zh/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: 了解如何使用 Aspose.Cells for C++ 将 Excel 文件保存为标准或最小尺寸的 PDF。
---

{{% alert color="primary" %}} 

 默认情况下，Aspose.Cells 将 Excel 保存为标准尺寸的 PDF。然而，您也可以使用 [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) 属性保存为最小尺寸。它接受以下值：

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **使用 Aspose.Cells 将 Excel 保存为标准或最小尺寸的 PDF**
以下示例代码展示了如何使用 [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/) 属性将 Excel 保存为标准或最小尺寸的 PDF。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"OptimizedOutput_out.pdf";

    // Load excel file into workbook object
    Workbook workbook(inputFilePath);

    // Create PDF save options
    PdfSaveOptions opts;

    // Set optimization type to minimum size
    opts.SetOptimizationType(PdfOptimizationType::MinimumSize);

    // Save the workbook to PDF with the specified options
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved to PDF with minimum size optimization!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

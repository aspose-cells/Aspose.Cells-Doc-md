---
title: 標準または最小サイズでExcelをPDFとして保存（C++）
linktitle: Excelを標準サイズまたは最小サイズのPDFに保存する
type: docs
weight: 340
url: /ja/cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aspose.Cells for C++を使用して、Excelファイルを標準または最小サイズのPDFに保存する方法を学びます。
---

{{% alert color="primary" %}} 

デフォルトでは、Aspose.CellsはExcelを標準サイズのPDFとして保存します。ただし、[PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/)プロパティを使用して最小サイズで保存することもできます。次の値を受け入れます：

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Aspose.Cellsを使用してExcelを標準サイズまたは最小サイズのPDFに保存する**
以下のサンプルコードは、[PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getoptimizationtype/)プロパティを使用してExcelを標準または最小サイズのPDFに保存する方法を示しています。

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

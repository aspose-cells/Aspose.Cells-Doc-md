---
title: 画像のリサンプリング  C++によるExcelからPDFへの変換
linktitle: 画像のリサンプリングの追加  ExcelからPDFへの変換
type: docs
weight: 150
url: /ja/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aspose.Cellsを使用して追加された画像をリサンプリングし、PDFのサイズを縮小する方法を学びます。
---

{{% alert color="primary" %}}

大量の画像を含む大きなMicrosoft Excelファイルで作業する際に、追加された画像を圧縮して出力PDFファイルサイズを減らし、全体的な変換パフォーマンスを向上させる必要がある場合があります。 Aspose.Cellsは、追加された画像をリサンプリングして出力PDFファイルサイズを減らし、パフォーマンスを改善するためのサポートを提供しています。

{{% /alert %}}

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

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

出力PDFのサイズを最小限に抑えるために[**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/)オプションを使用すると、画像の品質に若干影響を与える可能性があります。

{{% /alert %}} 

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}


---
title: ExcelをPDFにレンダリングする際にC++でスライサーを描画
linktitle: ExcelをPDFにレンダリングする際にスライサーを描画する
type: docs
weight: 60
url: /ja/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Aspose.Cellsを使用してスライサー設定付きのExcelをPDFにエクスポート（C++）
---

## **ExcelをPDFにレンダリングする際にスライサーを描画する**
スライサーが適用されたExcelファイルを持っていて、スライサーの設定とともにPDFにエクスポートしたい場合、Aspose.Cellsはこれを標準でサポートしています。スライサー付きのExcelファイルをPDFにエクスポートすると、生成されるPDFにスライサーが反映されます。

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](94044165.xlsx)を読み込みます。その後、ワークブックを[output PDFファイル](94044166.pdf)として保存します。次のスクリーンショットは、元のExcelファイルと生成されたPDFファイルを比較しています。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **サンプルコード**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

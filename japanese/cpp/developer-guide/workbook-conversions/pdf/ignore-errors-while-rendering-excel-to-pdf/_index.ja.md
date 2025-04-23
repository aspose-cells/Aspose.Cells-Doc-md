---
title: C++でExcelをPDFに変換中にエラーを無視する
linktitle: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 80
url: /ja/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for C++を使用して、ExcelからPDFへの変換時にエラーを無視する方法を学びます。
---

## **可能な使用シナリオ**

ExcelをPDFに変換する際にエラーや例外が発生し、変換処理が停止する場合があります。変換中にこれらのエラーをすべて無視するには、`PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)`を使用します。これにより、変換処理はエラーや例外を投げずにスムーズに完了しますが、データの損失が生じることがあります。そのため、データ喪失が重大でない場合にのみこのプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視**

以下のコードは、[サンプルExcelファイル](55541778.xlsx)を読み込みますが、このファイルはエラーがあり、[PDF変換](55541779.pdf)中にエラーが発生します。ですが、`PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)`プロパティを使用しているため、エラーは発生しません。ただし、このスクリーンショットのような*丸みを帯びた赤い矢印の形状*は失われます。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

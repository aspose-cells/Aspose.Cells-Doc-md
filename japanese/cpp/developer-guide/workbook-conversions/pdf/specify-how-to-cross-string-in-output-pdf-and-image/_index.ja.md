---
title: C++を使用して出力されたPDFや画像において文字の折り返し方法を指定する
linktitle: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 120
url: /ja/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aspose.Cells for C++を使用して、PDFおよび画像出力時の文字のはみ出しを制御する方法を学びます。
---

## **可能な使用シナリオ**

セルにテキストや文字列がセルの幅よりも大きい場合、次の列のセルがnullまたは空であれば、その文字列ははみ出します。ExcelファイルをPDFや画像に保存する際に、このはみ出しをコントロールしたい場合は、[**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/)列挙型を使用して交差タイプを指定します。次の値があります：

- **TextCrossType.Default**：MS Excelのように表示。次のセルに依存します。次のセルがnullの場合、文字列ははみ出すか切り捨てられます。

- **TextCrossType.CrossKeep**：MS Excelのように文字列を表示し、PDFや画像にエクスポートします。

- **TextCrossType.CrossOverride**：文字列をすべて他のセルにまたがって表示し、また交差したセルのテキストを上書きします。

- **TextCrossType.StrictInCell**: セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、サンプルのExcelファイルを読み込み、異なる[**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/)を指定してPDF／画像形式に保存します。サンプルExcelファイルと出力ファイルは以下のリンクからダウンロード可能です：

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### サンプルコード

```c++
#include <iostream>
#include <memory>
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

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```

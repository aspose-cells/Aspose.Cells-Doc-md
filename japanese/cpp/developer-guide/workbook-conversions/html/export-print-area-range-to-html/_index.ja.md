---
title: C++を使用したHTMLへの印刷領域範囲のエクスポート
linktitle: 印刷範囲をHTMLにエクスポートする
type: docs
weight: 60
url: /ja/cpp/export-print-area-range-to/
description: Aspose.Cells for C++を使用して印刷範囲をHTMLにエクスポートする方法を学びます。
---

## **可能な使用シナリオ**

これは、シート全体の代わりに印刷範囲（選択したセル範囲）のみをHTMLにエクスポートする必要がある一般的なシナリオです。この機能はすでにPDFレンダリングに対応していますが、今度はHTMLに対してもこの作業を行うことができます。まず、ワークシートのページ設定オブジェクトで印刷範囲を設定します。次に、[**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/)フラグを使用して選択された範囲のみをエクスポートします。

## **サンプルコード**

以下のサンプルコードは、ワークブックを読み込み、その後印刷範囲をHTMLにエクスポートします。この機能をテストするためのサンプルファイルは次のリンクからダウンロードできます：

[sampleInlineCharts.xlsx](79527946.xlsx)

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

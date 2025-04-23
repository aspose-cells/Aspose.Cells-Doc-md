---
title: C++を使ったExcelファイルのPDFA 1a互換のPDF形式への変換
linktitle: ExcelファイルをPDFA 1aに対応したPDF形式に変換
type: docs
weight: 130
url: /ja/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aspose.Cellsを使用してExcelファイルをPDF/A 1a準拠のPDF形式に変換する方法を学ぶ。
---

## **可能な使用シナリオ**

PDF/Aは長期保存のために設計された、PDFのユニークなフレーバーです。PDF/AはISO標準化されたポータブルドキュメントフォーマット（PDF）の版本であり、ドキュメント内で使用されているすべてのフォントをPDFファイルに埋め込むアーカイブ形式です。PDF/Aは、フォントリンク（フォント埋め込みとは異なる）や暗号化などの機能を禁止することで、通常のPDFと異なります。Aspose.Cellsを使用すると、ExcelファイルをPDF/A準拠のPDFファイル（PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3u）に保存可能です。本トピックでは、ExcelワークブックをPDF/A準拠（PDF/A-1a）PDFファイルに保存する方法について説明します。

## **ExcelファイルをPDF形式に変換して、PDF/A-1aと互換性がある形式にする方法**

開発者は[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)クラスを使用して変換のさまざまな属性を設定できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)クラスの異なるプロパティを設定することで、出力されるPDFの印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは[**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/)で、ExcelファイルをPDF/Aに準拠したPDFファイルとして保存可能です。

次のサンプルコードは、ExcelファイルをPDF/A-1aに対応する形式に変換する方法を説明しています。参照用の[outpur PDF](outputCompliancePdfA1a.pdf)およびスクリーンショットをご覧ください。

## **スクリーンショット**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

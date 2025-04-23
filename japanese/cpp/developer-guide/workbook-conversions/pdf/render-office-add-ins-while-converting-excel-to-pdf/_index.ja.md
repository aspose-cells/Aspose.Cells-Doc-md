---
title: ExcelをPDFに変換中にOfficeアドインをレンダリングする
linktitle: ExcelをPDFに変換する際のOffice Add Insのレンダリング
type: docs
weight: 100
url: /ja/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Aspose.Cells for C++を使用して、ExcelファイルをPDFに変換中にOfficeアドインをレンダリングする方法を学びます。
---

## **可能な使用シナリオ**

以前は、Aspose.CellsはExcelファイルをPDFに保存する際にOfficeアドインをレンダリングできませんでした。現在、正しくレンダリングされます。出力PDFにOfficeアドインをレンダリングするために特別な方法やプロパティを使用する必要はありません。単にExcelファイルをPDFに保存し、それが自動的にOfficeアドインをレンダリングします。

## **ExcelをPDFに変換する際のOffice Add-Insのレンダリング**

以下のサンプルコードは、Office アドインを含むサンプル Excel ファイル（60489769.xlsx）を保存します。以前のバージョン（例：17.11）で生成された出力 PDF と、新しいバージョン（例：17.12以降）で生成された出力 PDF をご覧ください。前のバージョンの出力 PDF は空白ですが、新しいバージョンは Office アドインを表示します。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

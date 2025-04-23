---
title: C++を使ってExcelファイル内の既存プリンタ設定を削除
linktitle: 既存のプリンタ設定を削除
type: docs
weight: 60
url: /ja/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Page Setupオブジェクトを使い、プログラム的にExcelファイル内のワークシートの既存プリンタ設定を削除する方法をC++のAspose.Cellsを使用して学びます。
keywords: ワークシートのプリンター設定の削除 C++、Excelワークシートのプリンター設定の削除 C++
---

## **可能な使用シナリオ**
開発者は、保存されたXLSXファイルにプリンター設定の*.bin*ファイルを含めないようにすることを望むことがあります。プリンター設定ファイルは*「[file "root"]\xl\printerSettings」*の下にあります。この文書では、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明しています。

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cellsを使用して、Excelファイルの異なるシートに指定された既存のプリンター設定を削除することができます。以下のサンプルコードは、ワークブック内のすべてのワークシートの既存のプリンター設定を削除する方法を示します。参考のために、[sample Excel file](45056020.xlsx)、[output Excel file](45056021.xlsx)、コンソール出力、およびスクリーンショットをご覧ください。

## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **コンソール出力**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}

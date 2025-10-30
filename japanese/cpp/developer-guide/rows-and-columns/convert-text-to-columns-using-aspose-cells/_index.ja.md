---
title: Aspose.Cellsを使ったC++によるテキストを列に変換
linktitle: テキストを列に変換
type: docs
weight: 30
url: /ja/cpp/convert-text-to-columns-using-aspose-cells/
description: Aspose.Cells for C++を使ったExcelファイルのテキストを列に変換方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelを使用して、テキストを列に変換することができます。この機能は、*Data*タブの*Data Tools*から利用できます。列の内容を複数の列に分割するには、Microsoft Excelがセルの内容を複数のセルに分割する基準となる、コンマ（または他の文字）などの特定の区切り文字を含むデータが必要です。Aspose.Cellsもこの機能を提供します。[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)メソッドを介して。

## **Aspose.Cellsを使用したテキストを列に変換する**

以下のサンプルコードは[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)メソッドの使い方を説明しています。最初のワークシートの列Aにいくつかの人物名を追加し、名前と苗字をスペース文字で区切っています。その後、列Aに対して[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)メソッドを適用し、出力Excelファイルとして保存します。[出力Excelファイル](25395213.xlsx)を開くと、名前は列Aに、苗字は列Bにあることがわかります。スクリーンショットのように表示されます。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **サンプルコード**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

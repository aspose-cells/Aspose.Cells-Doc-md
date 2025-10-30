---
title: Aspose.Cellsを使用したC++でのIFNA関数の計算
linktitle: IFNA関数の計算
description: Aspose.Cellsライブラリを使用してC++でIFNA関数を計算する方法。既存のExcelファイルを読み込むか、新しいExcelファイルを作成して、Aspose.Cellsのメソッドを使用してIFNA関数を計算し、結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、IFNA関数、計算、C++
type: docs
weight: 40
url: /ja/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.CellsはIFNA Excel関数の計算をサポートしています。IFNA関数は、式が#N/Aエラー値を返す場合に指定した値を返し、それ以外の場合は式の結果を返します。

{{% /alert %}} 

## **Aspose.Cellsを使用してIFNA関数を計算する**
以下のサンプルコードは、Aspose.CellsによるIFNA関数の計算を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}

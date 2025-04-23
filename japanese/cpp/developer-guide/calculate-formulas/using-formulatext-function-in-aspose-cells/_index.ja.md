---
title: Aspose.CellsでのFormulaText関数の使用例（C++）
linktitle: FormulaText関数の使用
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelで式を処理するFormulaText関数の使用方法について紹介しています。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用してセルの式テキストを取得し、結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、FormulaText 関数
type: docs
weight: 60
url: /ja/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText はExcel 2013以降の関数です。Excel 2010や2007などの以前のバージョンではサポートされていません。その名前が示すように、指定されたセルにある式のテキストを出力します。この記事では、Aspose.Cellsを使用してこの関数をどのように利用するかを示します。

{{% /alert %}} 

次のサンプルコードは、FormulaTextをAspose.Cellsで使用する方法を示しています。このコードは、まずセルA1に式を書き込み、次にFormulaTextを使用してセルA2に式のテキストを出力しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}

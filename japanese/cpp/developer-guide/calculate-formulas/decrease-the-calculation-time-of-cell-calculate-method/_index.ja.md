---
title: Cell.Calculateメソッドの計算時間をC++で短縮
linktitle: Cell.Calculateの計算時間を短縮
description: Microsoft Excelのセル計算メソッドの計算時間を削減するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してセル計算メソッドを最適化し、パフォーマンスを改善し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, セル計算メソッド、最適化、パフォーマンス、計算時間の短縮
type: docs
weight: 100
url: /ja/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能な使用シナリオ**

通常、ユーザーには[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)メソッドを一度呼び出し、その後個々のセルの計算済み値を取得することを推奨します。しかし、時にはワークブック全体を計算したくない場合もあります。特定のセルだけを計算したい場合、Aspose.Cellsは[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)プロパティを提供しており、これを false に設定すると、個々のセルの計算時間を大幅に短縮できます。再帰プロパティがtrueに設定されている場合、すべての依存セルも都度計算されますが、falseに設定すると、依存セルは一度だけ計算され、その後は再計算されません。

## **Cell.Calculate() メソッドの計算時間を短縮する**

以下のサンプルコードは、[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)プロパティの使用例を示しています。このコードを[サンプルExcelファイル](5113710.xlsx)で実行し、その結果をコンソールで確認してください。再帰プロパティをfalseに設定すると、計算時間が大幅に短縮されることがわかります。プロパティの理解のためにコメントもご参照ください。

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **コンソール出力**

このコードは、指定された[サンプルExcelファイル](5113710.xlsx)を使用して実行した場合のコンソール出力例です。出力結果は異なる場合がありますが、再帰プロパティをfalseに設定した後の経過時間は常にtrueに設定した場合より短くなります。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}

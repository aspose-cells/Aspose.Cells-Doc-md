---
title: C++で数式を計算する
linktitle: 数式の計算
description: この記事では、Aspose.Cellsライブラリを使用してC++でMicrosoft Excelの数式を計算する方法を紹介します。既存のExcelファイルを読み込むか新規作成し、Aspose.Cellsのメソッドを使用して数式を計算し、その結果を取得します。最後に、修正したExcelファイルを保存します。
keywords: Aspose.Cells、Excel、数式、計算、数式の直接計算、数式の繰り返し計算。
type: docs
weight: 125
url: /ja/cpp/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには組み込みの式計算エンジンがあります。これにより、デザイナーテンプレートからインポートした式の再計算だけでなく、ランタイムで追加された式の結果の計算もサポートしています。

Aspose.CellsはMicrosoft Excelのほとんどの数式や関数をサポートしています（サポートされている関数のリストは [こちら](/cells/ja/cpp/supported-formula-functions/) を参照）。これらの関数はAPIやデザイナースプレッドシートを通じて使用できます。Aspose.Cellsは膨大な数学、文字列、ブール値、日付/時間、統計、データベース、ルックアップ、参照の数式セットをサポートしています。

セルに式を追加するには、[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/)プロパティまたは[**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)メソッドを使用します。式を適用する際は、Microsoft Excelでの作成と同じく文字列の先頭に等号（=）を付け、関数パラメータをカンマ（,）で区切ります。

数式の結果を計算するには、ユーザーは[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)メソッドを呼び出すことができ、これによりExcelファイル内のすべての数式が処理されます。または、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)メソッドを呼び出してシート内のすべての数式を処理するか、あるいは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/)メソッドを呼び出して1つのセルの数式を処理することも可能です。

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **数式に関する重要な点**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの**GetFormula**プロパティと**SetFormula(...)**メソッドは、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)、[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの**Calculate**メソッドとは異なります。**GetFormula**プロパティと**SetFormula(...)**メソッドは単にセルに数式を追加するだけであり、実行時に結果を計算しません。数式の結果を得るには、**Calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

ときには、シートに追加せずに式の結果を直接計算する必要があります。式に使用されるセルの値はすでにシートに存在し、それらの値の結果をMicrosoft Excelの式に基づいて見つけたい場合です。

Aspose.Cellsの式計算エンジンAPIを使用して、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)から[**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)までの式の結果をシートに追加せずに計算できます。

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
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

上記のコードは次の出力を生成します：
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **繰り返し式の計算方法**

ブック内に多くの式があり、ユーザーが一部分だけを修正して繰り返し計算する必要がある場合、パフォーマンス向上のために式の計算チェーンを有効にすることが役立つかもしれません：[**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/)。

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンの作成には追加の時間が必要なため、最初の計算 ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) は、計算チェーンを作成しない場合と比較してCPU処理時間やメモリを多く消費することがあります。ユーザーが繰り返し式を計算する必要がない場合は、デフォルトの動作（直接式を計算し、計算チェーンを作成しない）を選択した方が良いでしょう。

{{% /alert %}}

## ** 高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/cpp/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell.Calculateメソッドの計算時間を短縮する](/cells/ja/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ブックの数式計算モードの設定](/cells/ja/cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.CellsでのFormulaText関数の使用](/cells/ja/cpp/using-formulatext-function-in-aspose-cells/)

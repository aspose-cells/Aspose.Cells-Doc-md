---
title: Node.jsを介したC++による式の計算
linktitle: 数式の計算
description: この記事では、Aspose.Cellsライブラリを使用して、Node.jsとC++を通じてMicrosoft Excelの式を計算する方法を紹介します。既存のExcelファイルを読み込むか新しいファイルを作成し、Aspose.Cellsのメソッドを使って式を計算し、その結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、式、計算、式の直接計算、繰り返し式の計算、Node.jsを介したC++での式の追加
type: docs
weight: 125
url: /ja/nodejs-cpp/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには組み込みの式計算エンジンがあります。これにより、デザイナーテンプレートからインポートした式の再計算だけでなく、ランタイムで追加された式の結果の計算もサポートしています。

Aspose.Cellsは、Microsoft Excelの多くの式や関数をサポートしています（[サポートされる関数のリスト](/cells/ja/nodejs-cpp/supported-formula-functions/)を参照）。これらの関数はAPIまたはデザイナースプレッドシートを通じて使用可能です。Aspose.Cellsは、大規模な数学論理、文字列、ブール値、日付/時間、統計、データベース、検索、および参照式のセットをサポートしています。

セルに式を追加するには、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)プロパティまたは[**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-)メソッドを使用します。式を適用する際は、Microsoft Excelでの作成と同じく文字列の先頭に等号（=）を付け、関数パラメータをカンマ（,）で区切ります。

式の結果を計算するには、ユーザーは[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)メソッドを呼び出してExcelファイル内のすべての式を処理させるか、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-)メソッドを呼び出してシート内のすべての式を処理させるか、または、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-)メソッドを呼び出して特定のセルの式を処理させることができます。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **数式に関する重要な点**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの**Formula**プロパティと**setFormula(...)**メソッドは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの**calculate**メソッドとは異なり、単にセルに式を追加するだけで、結果の計算は実行しません。式の結果を取得するには、**calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

ときには、シートに追加せずに式の結果を直接計算する必要があります。式に使用されるセルの値はすでにシートに存在し、それらの値の結果をMicrosoft Excelの式に基づいて見つけたい場合です。

Aspose.Cellsの式計算エンジンAPIを使用して、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)から[**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-)までの式の結果をシートに追加せずに計算できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

上記のコードは次の出力を生成します：
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **数式を繰り返し計算する方法**

ワークブックに多くの式があり、少しの変更を加えながら繰り返し計算する必要がある場合、パフォーマンス向上のために式の計算チェーンを有効にすることが役立ちます：[**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効です。チェーンの作成には追加の時間がかかるため、最初の式計算（[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)）は、チェーンを作成しない場合に比べて、より多くのCPU処理時間とメモリを消費することがあります。繰り返し式を計算しない場合は、標準的な動作（式を直接計算する）を選んだ方が良いでしょう。

{{% /alert %}}

## **高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [セルの計算時間を短縮する方法](/cells/ja/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/nodejs-cpp/detecting-circular-reference/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ブックの数式計算モードの設定](/cells/ja/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.CellsでのFormulaText関数の使用](/cells/ja/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}

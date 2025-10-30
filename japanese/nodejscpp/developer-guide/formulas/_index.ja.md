---
title: Node.js via C++ を使用したExcelファイルの数式管理
linktitle: 数式
type: docs
weight: 122
url: /ja/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for Node.js via C++を通じてExcelファイルの数式を管理する方法について学びます。Aspose.CellsはExcelファイルの数式の取得、設定、および計算を容易に行えます。
keywords: Node.js via C++で数式を計算する方法、Node.js経由の関数と数式、Node.jsを通じてC++のビルトイン関数を管理、Node.jsとC++を組み合わせたアドイン関数の使用方法、配列数式の利用方法、Node.jsでR1C1数式を使用する方法。
---

## **紹介**

Microsoft Excelの魅力的な機能の一つは、数式や関数を使ったデータ処理能力です。Excelは多くの組み込み関数と数式を提供し、複雑な計算を迅速に行えます。Aspose.Cellsもまた、値の計算を支援する多くの組み込み関数と数式を提供し、アドイン関数もサポートしています。さらに、配列やR1C1数式もサポートしています。

## **数式と関数の使用方法**

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスするための [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスは [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションを提供します。Cells コレクション内の各アイテムは、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) クラスのオブジェクトを表します。

詳細については、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) クラスが提供するプロパティとメソッドを使用してセルに数式を適用することが可能です。

- 組み込み関数の使用。
- アドイン関数の使用。
- 配列式の操作。
- R1C1 数式の作成。

## **組み込み関数の使用方法**

組み込み関数や数式は、開発者の労力と時間を削減するための既製品として提供されます。Aspose.Cellsがサポートする[組み込み関数一覧](/cells/ja/nodejs-cpp/supported-formula-functions/)をご覧ください。関数はアルファベット順にリストされており、今後さらに多くの関数がサポートされる予定です。

Aspose.CellsはMicrosoft Excelが提供するほとんどの数式や関数をサポートしています。これらの数式はAPIまたは[デザイナースプレッドシート](/cells/ja/nodejs-cpp/what-is-a-designer-spreadsheet/)を通じて利用可能です。Aspose.Cellsは、多数の数学、文字列、論理値、日付/時間、統計、データベース、検索および参照の数式をサポートしています。

セルに数式を追加するためには、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) クラスの [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) プロパティを使用します。例えば **複雑な数式** など

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cellsでは複雑な数式もサポートされています。セルに数式を適用する際は、常に文字列を等号（=）で始めてマイクロソフトExcelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用してください。

以下の例では、ワークシートの [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) コレクションの最初のセルに複雑な数式が適用されています。この数式は、Aspose.Cells が提供する組み込みの **IF** 関数を使用しています。

```javascript
const path = require("path");
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

## **アドイン関数の使用方法**

Excel アドインとして含めたいユーザー定義の数式を持つことができます。セル.Formula 関数を使用すると組み込み関数は正常に動作しますが、アドイン関数を使用してカスタム関数や数式を設定する必要があります。

Aspose.Cells は、[**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-) を使用してアドイン関数を登録する機能を提供します。その後、cell.Formula = anyFunctionFromAddIn と設定すると、出力される Excel ファイルには、アドイン関数から計算された値が含まれます。

以下のサンプルコードの中でアドイン関数を登録するために XLAM ファイルをダウンロードできます。同様に、出力ファイル "test_udf.xlsx" もダウンロードして出力を確認することができます。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **配列式の使用方法**

配列式は、数式を構成する関数に個々の数値ではなく配列を引数として取る数式です。配列式が表示されると、括弧({})で囲まれています。

いくつかのMicrosoft Excel関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列を配列引数と同じ行数および列数のセル範囲に入力してください。

配列式をセルに適用するには、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) クラスの [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) メソッドを呼び出します。[**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) メソッドは以下のパラメータを取ります:

- **配列数式**、配列数式。
- **行数**、配列数式の結果を設定する行数。
- **列数**, 配列式の結果を入力する列数。

```javascript
const path = require("path");
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

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **R1C1 数式の使用方法**

セルに **R1C1** 参照スタイルの数式を [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) クラスの [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) プロパティを使用して追加します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **高度なトピック**
- [先行および後行](/cells/ja/nodejs-cpp/precedents-and-dependents/)
- [数式で外部リンクを設定する](/cells/ja/nodejs-cpp/set-external-links-in-formulas/)
- [新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる](/cells/ja/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の式の設定](/cells/ja/nodejs-cpp/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの通知](/cells/ja/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [共有数式の設定](/cells/ja/nodejs-cpp/setting-shared-formula/)
- [共有式の最大行数を指定](/cells/ja/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [サポートされているExcel関数](/cells/ja/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}

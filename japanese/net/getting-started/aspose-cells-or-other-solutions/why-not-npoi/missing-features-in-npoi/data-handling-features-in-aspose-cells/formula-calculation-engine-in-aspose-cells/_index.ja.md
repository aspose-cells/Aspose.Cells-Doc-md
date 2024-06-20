---
title: Aspose.Cellsの数式計算エンジン
type: docs
weight: 30
url: /ja/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - 数式計算エンジン**
数式計算エンジンはAspose.Cellsに組み込まれています。設計用スプレッドシートファイルからインポートされた数式を再計算するだけでなく、ランタイムで追加された数式の結果を計算することもサポートしています。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.Worksheets.Add();

Worksheet worksheet = book.Worksheets[sheetIndex];

Cells cells = worksheet.Cells;

Cell cell = null;

//Adding a value to "A1" cell

cell = cells["A1"];

cell.Value = 1;

//Adding a value to "A2" cell

cell = cells["A2"];

cell.Value = 2;

//Adding a value to "A3" cell

cell = cells["A3"];

cell.Value = 3;

//Adding a SUM formula to "A4" cell

cell = cells["A4"];

cell.Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

book.CalculateFormula();

//Saving the Excel file

book.Save("AsposeFormulaEngine.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**数式計算エンジン**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[数式計算エンジン](/cells/ja/net/formula-calculation-engine/)をご覧ください。

{{% /alert %}}

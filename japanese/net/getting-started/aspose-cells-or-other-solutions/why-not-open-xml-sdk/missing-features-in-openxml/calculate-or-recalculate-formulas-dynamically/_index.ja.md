---
title: 動的に数式を計算または再計算する
type: docs
weight: 10
url: /ja/net/calculate-or-recalculate-formulas-dynamically/
---

**Aspose.Cells**には**数式計算**エンジンが組み込まれています。デザイナーファイルからインポートされた数式を再計算するだけでなく、ランタイムで追加された数式の結果を計算することもサポートしています。
## **数式の追加と結果の計算**
Aspose.Cellsは、Microsoft Excelの一部であるほとんどの数式や関数をサポートしています。開発者はこれらの数式をAPIまたはデザイナースプレッドシートを使用して利用することができます。Aspose.Excelは、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、参照などの強力な数式セットをサポートしています。

セルに数式を追加するには、CellクラスのFormulaプロパティを使用します。セルに数式を適用する場合は、常に等号（=）で文字列を始める必要があります。これはMicrosoft Excelで数式を作成するときと同じです。関数パラメータを区切るためにコンマ（,）を使用します。

数式の結果を計算するには、ExcelクラスのCalculateFormulaメソッドを呼び出し、Excelファイルに埋め込まれた全ての数式を処理します。[url: CalculateFormulaメソッドでサポートされる関数のリスト]（/cells/ja/net/supported-formula-functions/）を参照してください。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **一度だけ数式を計算する**
ユーザーがWorkbook.CalculateFormula（）を呼び出して、ワークブックテンプレート内の数式の値を計算すると、Aspose.Cellsは計算チェーンを作成します。これにより、2回目や3回目などの数式の計算が高速化されます。
ただし、ユーザーテンプレートにさまざまな数式が含まれている場合、数式の最初の計算には多くのCPU処理時間とメモリが必要です。

Aspose.Cellsでは、数式計算チェーンの作成を無効にすることができます。これは、ファイルの数式を1回だけ計算したい場合に役立ちます。

Aspose.Cellsの数式の計算パフォーマンスを向上させたい場合で、数式計算チェーンを作成したくない場合は、FormulaSettings.EnableCalculationChainをfalseに設定してください。デフォルトでは、trueに設定されています。

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **数式の直接計算**
数式計算エンジンはAspose.Cellsに組み込まれています。また、デザイナーファイルからインポートされた数式を再計算するだけでなく、Aspose.Cellsは数式の結果を直接計算することもサポートしています。
時には、ワークシートに実際に追加せずに数式の結果を直接計算する必要があります。数式で使用されるセルの値はすでにワークシートに存在し、Ms-Excelの数式に基づいてこれらの値の結果を見つける必要がある場合、Aspose.CellsのFormula Calculation Engine APIであるworksheet.Calculate（string formula）を使用できます。

サンプルコードのダウンロード

{{< highlight csharp >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)

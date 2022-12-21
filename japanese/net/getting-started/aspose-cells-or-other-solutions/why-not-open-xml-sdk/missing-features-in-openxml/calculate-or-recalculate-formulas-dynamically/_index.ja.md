---
title: 数式を動的に計算または再計算する
type: docs
weight: 10
url: /ja/net/calculate-or-recalculate-formulas-dynamically/
---
**公式計算**エンジンが組み込まれている**Aspose.Cells**.デザイナ ファイルからインポートした式を再計算できるだけでなく、実行時に追加された式の結果を計算することもサポートします。
## **式の追加と結果の計算**
Aspose.Cells は、Microsoft Excel の一部である数式または関数のほとんどをサポートしています。開発者は、API またはデザイナー スプレッドシートを使用してこれらの数式を使用できます。 Aspose.Excel は、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、参照式の膨大なセットをサポートしています。

セルに数式を追加するには、Cell クラスの Formula プロパティを使用します。数式をセルに適用するときは、Microsoft Excel で数式を作成するときと同じように、文字列を常に等号 (=) で始めます。関数のパラメーターを区切るには、コンマ (,) を使用します。

数式の結果を計算するには、Excel ファイルに埋め込まれたすべての数式を処理する Excel クラスの CalculateFormula メソッドを呼び出します。読む[url:CalculateFormula メソッドでサポートされている関数のリスト](/cells/ja/net/supported-formula-functions/).

{{< highlight "csharp" >}}

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
## **数式を一度だけ計算する**
ユーザーが Workbook.CalculateFormula() を呼び出してブック テンプレート内の数式の値を計算すると、Aspose.Cells によって計算チェーンが作成されます。数式が 2 回目または 3 回目の計算などでパフォーマンスが向上します。
ただし、ユーザー テンプレートに多様な数式が多数含まれている場合、最初の数式計算で CPU の処理時間とメモリが大量に消費される可能性があります。

Aspose.Cells を使用すると、計算チェーンの作成をオフにすることができます。これは、ファイルの数式を 1 回だけ計算する場合に役立ちます。

 Aspose.Cells までに数式計算のパフォーマンスを向上させたいが、数式計算チェーンを作成したくない場合は、次のように設定してください。**FormulaSettings.EnableCalculationChain**なので**間違い** .デフォルトでは、次のように設定されています。**真実**.

{{< highlight "csharp" >}}

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
Aspose.Cells には数式計算エンジンが組み込まれています。また、Aspose.Cells は、デザイナー ファイルからインポートされた数式を再計算するだけでなく、数式の結果を直接計算することもサポートしています。
場合によっては、実際にワークシートに数式を追加せずに、数式の結果を直接計算する必要があります。数式で使用されるセルの値は既にワークシートに存在しており、ワークシートに数式を追加せずに、いくつかの Ms-Excel 数式に基づいてこれらの値の結果を見つけるだけで済みます。

 Aspose.Cells 数式計算エンジン API を使用できます。**worksheet.Calculate(文字列式)**実際にワークシートに追加せずに、そのような数式の結果を計算します。

{{< highlight "csharp" >}}

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
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)

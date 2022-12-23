---
title: パブリック API Aspose.Cells 8.8.1 の変更点
type: docs
weight: 270
url: /ja/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.0 から 8.8.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **ロードするデータをフィルタリングする**
Aspose.Cells for .NET 8.8.1 は、LoadOptions.LoadDataFilterOptions プロパティと共に LoadDataFilterOptions 列挙を公開しました。これを使用して、テンプレート ファイルからワークブックを作成するときにロードするデータ型を指定できます。ロードされたデータをフィルタリングすると、特に LightCells API を使用する場合に、特別な目的でパフォーマンスを向上させることができます。

LoadDataFilterOptions 列挙体は、次の選択肢を提供します。

1. スプレッドシートからすべてをロードします。
1. スプレッドシートから何もロードしない場合は None。
1. CellBlank は、値が空白のセルを読み込みます。
1. CellBool は、値が Boolean であるセルを読み込みます。
1. CellData は、値、数式、書式設定を含むセル データを読み込みます。
1. CellError は、値がエラーであるセルを読み込みます。
1. CellNumeric は、値が数値 (日付と時刻を含む) であるセルを読み込みます。
1. CellString は、値がテキスト/文字列であるセルをロードします。
1. CellValue は、セル値 (すべての型) のみを読み込みます。
1. Chart はチャートのみを読み込みます。
1. ConditionalFormatting は、条件付き書式ルールのみを読み込みます。
1. DataValidation は、データ検証ルールのみを読み込みます。
1. DocumentProperties は、ドキュメント プロパティのみを読み込みます。
1. Formula は、定義された名前を含む式をロードします。
1. MergedArea は、結合されたセルのみを読み込みます。
1. PivotTable は、ピボット テーブルを読み込みます。
1. 設定は、ワークブックとワークシートの設定のみを読み込みます。
1. Shape は形状のみを読み込みます。
1. スタイルは、セルの書式設定を読み込みます。
1. テーブルは、Excel テーブル/リスト オブジェクトを読み込みます。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[ロードするデータのフィルタリング](/cells/ja/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **チャートをPDFに直接変換**
Aspose.Cells API は、Chart.ToPdf メソッドを使用して PDF にグラフをレンダリングする機能を既に提供しています。このリリースでは、API は、Stream のインスタンスを受け入れることができる、前述のメソッドの別のオーバーロードされたバージョンを公開し、ユーザーがチャートの PDF を MemoryStream のインスタンスに保存できるようにしました。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **WorkbookSettings.PaperSize プロパティを追加**
Aspose.Cells for .NET 8.8.1 は、スプレッドシート全体のデフォルトの印刷用紙サイズを設定するために WorkbookSettings.PaperSize プロパティを公開しました。 WorkbookSettings.PaperSize プロパティは、最も広く使用されている印刷用紙の種類の定義済みサイズを含む PaperSizeType 列挙からの値を受け入れます。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Shape.TextBody プロパティを追加**
Aspose.Cells for .NET API のこのリリースでは、シェイプ内のテキストの側面を操作するために、Shape.TextBody が公開されています。次のスニペットは、前述のプロパティを使用して、TextBox 内のテキストの影の効果を設定します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[テキストの影効果を設定する](/cells/ja/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

// Workbook のインスタンスを作成します

var book = new Workbook();

//ワークブックの最初のワークシートにアクセス

var シート = book.Worksheets[0];

//ShapeCollection に TextBox を追加します

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

// TextBox のテキストを設定します

textBox.Text = "このテキストには次の設定があります。\n\nテキスト効果 > 影 > オフセット下";

//テキストの影効果を設定

for (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Worksheet.CalculateFormula(string formula, CalculationOptions opts) メソッドを追加**
Aspose.Cells for .NET 8.8.1 では、CalculateFormula メソッドの別のオーバーロードが公開されており、カスタム オプションを使用して特定の数式を直接計算する機能が提供されています。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[カスタム関数の直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.CreateValidation メソッドを追加**
Aspose.Cells.GridWeb は、GridCell.CreateValidation メソッドを使用して、検証ルールを単一のセルに直接追加する機能を提供しました。上記のメソッドには 2 つのパラメーターが必要です。最初のパラメーターは検証タイプを決定する GridValidationType 型で、2 番目のパラメーター (isRequied) は Boolean 型です。



**C#**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **GridCell.RemoveValidation メソッドを追加**
Aspose.Cells.GridWeb は、GridCell.RemoveValidation メソッドを使用して、GridCell からデータ検証ルールを削除する機能も提供しています。
## **廃止された API**
### **廃止された Shape.TextFrame プロパティ**
代わりに Shape.TextBody.TextAlignment プロパティを使用することをお勧めします。

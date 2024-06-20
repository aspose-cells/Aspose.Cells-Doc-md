---
title: Aspose.Cells 8.8.1でのパブリックAPIの変更
type: docs
weight: 270
url: /ja/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

このドキュメントは、バージョン8.8.0から8.8.1へのAspose.Cells APIの変更についてで、モジュール/アプリケーション開発者に関心があるかもしれないものです。

{{% /alert %}} 
## **APIの追加**
### **ロードするデータをフィルタリング**
Aspose.Cells for .NET 8.8.1では、テンプレートファイルからワークブックを構築する際にロードされるべきデータ型を指定するためにLoadDataFilterOptions列挙型とLoadOptions.LoadDataFilterOptionsプロパティを公開しました。ロードされたデータをフィルタリングすることで、特にLightCells APIを使用する場合など、特別な目的のパフォーマンスを向上させることができます。

LoadDataFilterOptions 列挙型は以下の選択肢を提供します。

1. スプレッドシートからすべてをロードするためのAll。
1. スプレッドシートから何もロードしないためのNone。
1. 値が空白のセルをロードするためのCellBlank。
1. ブール値のセルをロードするためのCellBool。
1. 値、数式、書式を含むセルデータをロードするためのCellData。
1. エラー値のセルをロードするためのCellError。
1. 数値（日付や時間を含む）のセルをロードするためのCellNumeric。
1. テキスト/文字列のセルをロードするためのCellString。
1. CellValueはセルの値のみをロードします（すべてのタイプ）。
1. Chartはグラフのみをロードします。
1. ConditionalFormattingは条件付き書式をロードします。
1. DataValidationはデータの検証規則のみをロードします。
1. DocumentPropertiesは文書のプロパティのみをロードします。
1. Formulaは定義名を含む数式をロードします。
1. MergedAreaはマージされたセルのみをロードします。
1. PivotTableはピボットテーブルのみをロードします。
1. Settingsはブックおよびシートの設定のみをロードします。
1. Shapeは図形のみをロードします。
1. Styleはセルの書式のみをロードします。
1. TableはExcelテーブル/リストオブジェクトのみをロードします。

{{% alert color="primary" %}} 

この機能の詳細については、[テンプレートファイルからワークブックをロードするときのデータのフィルタリング](/cells/ja/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **チャートを直接 PDF に変換**
Aspose.CellsのAPIはすでにChart.ToPdfメソッドを使用してグラフをPDFにレンダリングする機能を提供しています。このリリースでは、APIはそのメソッドの別のオーバーロードバージョンを公開し、Streamのインスタンスを受け入れ、ユーザーがチャートのPDFをMemoryStreamのインスタンスに保存できるようにしました。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.8.1では、WorkbookSettings.PaperSizeプロパティが公開され、スプレッドシート全体のデフォルトの印刷用紙サイズを設定するために使用されます。WorkbookSettings.PaperSizeプロパティは、PaperSizeType列挙型の値を受け入れることができ、最も一般的に使用される印刷用紙タイプの事前定義されたサイズが含まれています。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Shape.TextBody プロパティを追加**
このAspose.Cells for .NET APIのリリースでは、Shape.TextBodyが公開され、図形内のテキストの側面を操作するために使用されます。次のスニペットでは、このプロパティを使用してテキストボックス内のテキストの影響を設定しています。

{{% alert color="primary" %}} 

この機能の詳細については、[テキストの影響の設定](/cells/ja/net/setting-shadow-of-text-effects-of-shape-or-textbox/)の詳細な記事を参照してください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Worksheet.CalculateFormula(string formula, CalculationOptions opts)メソッドを追加**
Aspose.Cells for .NET 8.8.1では、CalculateFormulaメソッドの別のオーバーロードが公開され、カスタムオプションを使用して指定された数式を直接計算する機能が提供されます。

{{% alert color="primary" %}} 

この機能の詳細については、[カスタム関数の直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)の詳細な記事を参照してください。

{{% /alert %}} 
### **GridCell.CreateValidationメソッドを追加**
Aspose.Cells.GridWebは、GridCell.CreateValidationメソッドを使用して単一セルに検証規則を直接追加する機能を提供しています。このメソッドには2つのパラメータが必要です。最初のパラメータはGridValidationTypeの型で、検証のタイプを決定し、2番目のパラメータ（isRequied）はブール型です。



**C#**

{{< highlight csharp >}}

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


### **GridCell.RemoveValidationメソッドを追加**
Aspose.Cells.GridWebは、GridCell.RemoveValidationメソッドを使用して、GridCellからデータ検証規則を削除する機能を提供しています。
## **非推奨API**
### **廃止されたShape.TextFrameプロパティ**
Shape.TextBody.TextAlignmentプロパティを使用することをお勧めします。

---
title: Aspose.Cells 8.8.1でのパブリックAPIの変更
type: docs
weight: 280
url: /ja/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

このドキュメントは、バージョン8.8.0から8.8.1へのAspose.Cells APIの変更についてで、モジュール/アプリケーション開発者に関心があるかもしれないものです。

{{% /alert %}} 
## **APIの追加**
### **ロードするデータをフィルタリング**
Aspose.Cells for Java 8.8.1 では、LoadDataFilterOptions 列挙型と LoadOptions.LoadDataFilterOptions プロパティが公開され、テンプレートファイルからワークブックを構築する際にロードされるべきデータ型を指定するために使用できます。ロードされるデータをフィルタリングすることで、特に LightCells API を使用する場合など、特殊な目的に対してパフォーマンスを向上させることができます。

LoadDataFilterOptions 列挙型は以下の選択肢を提供します。

1. スプレッドシートからすべてをロードする ALL。
1. スプレッドシートから何もロードしない NONE。
1. 値がブランクのセルをロードする CELL_BLANK。
1. 値がブール型のセルをロードする CELL_BOOL。
1. 値、数式、書式を含むセルデータをロードする CELL_DATA。
1. 値がエラーのセルをロードする CELL_ERROR。
1. 数値（日付と時刻を含む）の値を持つセルをロードする CELL_NUMERIC。
1. テキスト/文字列の値を持つセルをロードする CELL_STRING。
1. セルの値だけをロードする CELL_VALUE。
1. チャートだけをロードする CHART。
1. 条件付き書式だけをロードする CONDITIONAL_FORMATTING。
1. データの妥当性を確認する規則だけをロードする DATA_VALIDATION。
1. ドキュメントのプロパティだけをロードする DOCUMENT_PROPERTIES。
1. 定義名を含む数式をロードする FORMULA。
1. 結合されたセルだけをロードする MERGED_AREA。
1. ピボットテーブルだけをロードする PIVOT_TABLE。
1. ワークブックとワークシートの設定だけをロードする SETTINGS。
1. 形状だけをロードする SHAPE。
1. セルの書式だけをロードする STYLE。
1. Excel テーブル/List オブジェクトだけをロードする TABLE。

{{% alert color="primary" %}} 

この機能の詳細については、[ロード時のデータのフィルタリング](/cells/ja/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)の詳細記事をご覧ください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **チャートを直接 PDF に変換**
Aspose.Cells API では、Chart.toPdf メソッドを使用してチャートを PDF にレンダリングする機能がすでに提供されています。このリリースでは、API が言及されたメソッドのオーバーロードバージョンをさらに公開し、OutputStream のインスタンスを受け入れることができるようになりました。これにより、ユーザーはチャートの PDF を ByteArrayOutputStream のインスタンスに保存することができます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **WorkbookSettings.PaperSize プロパティを追加**
Aspose.Cells for Java 8.8.1 では、WorkbookSettings.PaperSize プロパティが公開され、スプレッドシート全体に対してデフォルトの印刷用紙サイズを設定するために使用できます。WorkbookSettings.PaperSize プロパティは、最も一般的に使用される印刷用紙タイプの事前定義サイズを含む PaperSizeType 列挙型から値を受け入れます。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Shape.TextBody プロパティを追加**
Aspose.Cells for Java APIのこのリリースでは、Shape.TextBodyを公開して、図形内のテキストの側面を操作することができるようになりました。次のスニペットでは、このプロパティを使用して、テキストボックス内のテキストの影響を設定しています。

{{% alert color="primary" %}} 

この機能の詳細については、[テキストの影響を設定](/cells/ja/java/setting-shadow-of-text-effects-of-shape-or-textbox/)の詳細な記事を参照してください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Worksheet.calculateFormula(string formula, CalculationOptions opts) メソッドを追加しました**
Aspose.Cells for Java 8.8.1では、Worksheet.calculateFormulaメソッドの別のオーバーロードが公開され、カスタムオプションを使用して直接指定された式を計算する機能が提供されました。

{{% alert color="primary" %}} 

この機能の詳細については、[カスタム関数の直接計算](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)の詳細な記事を参照してください。

{{% /alert %}} 
### **GridCell.createValidationメソッドを追加しました**
Aspose.Cells.GridWebでは、GridCell.createValidationメソッドを使用して、個々のセルに検証ルールを直接追加する機能が提供されました。このメソッドは2つのパラメーターが必要です。1つ目は検証の種類を決定するGridValidationType型で、2つ目はBoolean型のisRequiedです。

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **GridCell.removeValidationメソッドを追加しました**
Aspose.Cells.GridWebでは、GridCell.removeValidationメソッドを使用して、GridCellからデータ検証ルールを削除する機能が提供されました。
## **非推奨API**
### **廃止されたShape.TextFrameプロパティ**
Shape.TextBody.TextAlignmentプロパティを使用することをお勧めします。

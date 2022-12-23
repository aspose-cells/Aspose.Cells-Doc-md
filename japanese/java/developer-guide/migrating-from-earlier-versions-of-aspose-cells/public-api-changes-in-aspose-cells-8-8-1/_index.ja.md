---
title: パブリック API Aspose.Cells 8.8.1 の変更点
type: docs
weight: 280
url: /ja/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.0 から 8.8.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **ロードするデータをフィルタリングする**
Aspose.Cells for Java 8.8.1 は、LoadOptions.LoadDataFilterOptions プロパティと共に LoadDataFilterOptions 列挙を公開しました。これを使用して、テンプレート ファイルからワークブックを作成するときにロードするデータ型を指定できます。ロードされたデータをフィルタリングすると、特に LightCells API を使用する場合に、特別な目的でパフォーマンスを向上させることができます。

LoadDataFilterOptions 列挙体は、次の選択肢を提供します。

1. ALL : スプレッドシートからすべてをロードします。
1. スプレッドシートから何もロードしない場合は NONE。
1. CELL_BLANK は、値が空白のセルをロードします。
1. CELL_BOOL は、値がブール値のセルをロードします。
1. CELL_DATA は、値、数式、フォーマットを含むセル データを読み込みます。
1. CELL_ERROR は、値がエラーであるセルをロードします。
1. CELL_NUMERIC は、値が数値 (日付と時刻を含む) であるセルを読み込みます。
1. CELL_STRING は、値がテキスト/文字列であるセルをロードします。
1. CELL_VALUE は、セル値 (すべての型) のみをロードします。
1. CHART はチャートのみをロードします。
1. CONDITIONAL_FORMATTING は、条件付き書式ルールのみをロードします。
1. DATA_VALIDATION は、データ検証ルールのみをロードします。
1. DOCUMENT_PROPERTIES は、ドキュメント プロパティのみを読み込みます。
1. FORMULA は、定義された名前を含む式をロードします。
1. MERGED_AREA は、結合されたセルのみをロードします。
1. PIVOT_TABLE は、ピボット テーブルを読み込みます。
1. SETTINGS は、ワークブックとワークシートの設定のみを読み込みます。
1. SHAPE は形状のみをロードします。
1. STYLE は、セルの書式設定を読み込みます。
1. TABLE は、Excel テーブル/リスト オブジェクトを読み込みます。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[ロードするデータのフィルタリング](/cells/ja/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **チャートをPDFに直接変換**
Aspose.Cells API は、Chart.toPdf メソッドを使用して PDF にグラフをレンダリングする機能を既に提供しています。このリリースでは、API は、OutputStream のインスタンスを受け入れることができる、前述のメソッドの別のオーバーロードされたバージョンを公開し、ユーザーがチャートの PDF を ByteArrayOutputStream のインスタンスに保存できるようにしました。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.8.1 は、スプレッドシート全体のデフォルトの印刷用紙サイズを設定するために WorkbookSettings.PaperSize プロパティを公開しました。 WorkbookSettings.PaperSize プロパティは、最も広く使用されている印刷用紙の種類の定義済みサイズを含む PaperSizeType 列挙からの値を受け入れます。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Shape.TextBody プロパティを追加**
Aspose.Cells for Java API のこのリリースでは、シェイプ内のテキストの側面を操作するために、Shape.TextBody が公開されています。次のスニペットは、前述のプロパティを使用して、TextBox 内のテキストの影の効果を設定します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[テキストの影効果を設定する](/cells/ja/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

// Workbook のインスタンスを作成します

ワークブック book = new Workbook();

//ワークブックの最初のワークシートにアクセス

ワークシート シート = book.getWorksheets().get(0);

//ShapeCollection に TextBox を追加します

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

// TextBox のテキストを設定します

textBox.setText("このテキストには次の設定があります。\n\nテキスト効果 > 影 > オフセット下");

//テキストの影効果を設定

for (int i = 0; i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Worksheet.calculateFormula(string formula, CalculationOptions opts) メソッドを追加**
Aspose.Cells for Java 8.8.1 では、Worksheet.calculateFormula メソッドの別のオーバーロードが公開されました。このメソッドは、カスタム オプションを使用して特定の数式を直接計算する機能を提供します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[カスタム関数の直接計算](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.createValidation メソッドを追加**
Aspose.Cells.GridWeb は、GridCell.createValidation メソッドを使用して、検証ルールを単一のセルに直接追加する機能を提供しました。上記のメソッドには 2 つのパラメーターが必要です。最初のパラメーターは検証タイプを決定する GridValidationType 型で、2 番目のパラメーター (isRequied) は Boolean 型です。

**Java**

{{< highlight "csharp" >}}

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
### **GridCell.removeValidation メソッドを追加**
Aspose.Cells.GridWeb は、GridCell.removeValidation メソッドを使用して、GridCell からデータ検証ルールを削除する機能も提供しています。
## **廃止された API**
### **廃止された Shape.TextFrame プロパティ**
代わりに Shape.TextBody.TextAlignment プロパティを使用することをお勧めします。

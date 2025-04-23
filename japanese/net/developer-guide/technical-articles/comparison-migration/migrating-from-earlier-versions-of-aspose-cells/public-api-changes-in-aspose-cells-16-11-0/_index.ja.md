---
title: Aspose.Cells 16.11.0 での Public API 変更
type: docs
weight: 350
url: /ja/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者に関連がある可能性のある Aspose.Cells API のバージョン 16.10.0 から 16.11.0 への変更について説明しています。新しいおよび更新された public メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **グローバリゼーション設定のサポート**
Aspose.Cells 16.11.0 は、Subtotals にカスタム ラベルを使用するように Aspose.Cells API を強制するために GlobalizationSettings クラスと WorkbookSettings.GlobalizationSettings プロパティを公開しました。GlobalizationSettings クラスには、カスタム実装で望ましい名前を指定するためにオーバーライドできる次のメソッドがあります **Total** と **Grand Total**。

- GlobalizationSettings.GetTotalName：関数の合計名を取得します。
- GlobalizationSettings.GetGrandTotalName：関数のグランド合計名を取得します。

GlobalizationSettings クラスを拡張し、前述のメソッドをオーバーライドしてコンソリデーション関数 Average のカスタム ラベルを返す単純なカスタムクラスは次のとおりです。

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



次のスニペットは、Pieチャートの「その他」のラベルの名前を取得する便利なGlobalizationSettings.GetOtherNameメソッドの使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



次のスニペットは、上記で作成したCustomSettingsクラスを使用して、ピースプレッドシートをロードし、チャートを画像にレンダリングするシナリオです。

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



次のコード片は、Pie チャートを含む既存のスプレッドシートを読み込み、上記で作成した CustomSettings クラスを利用しながらチャートを画像にレンダリングします。

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **CellsFactory クラスを追加しました**
Aspose.Cells 16.11.0では、CellsFactoryクラスが公開され、現在はCreateStyleという1つのメソッドがあります。CellsFactory.CreateStyleメソッドを使用して、ワークブックスタイルのプールに追加することなくStyleクラスのインスタンスを作成できます。

CellsFactory.CreateStyleメソッドの単純な使用シナリオは以下の通りです。

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Workbook.AbsolutePath プロパティを追加しました**
Aspose.Cells 16.11.0 は、workbook.xml ファイルに保存された絶対ワークブック パスを取得または設定するための Workbook.AbsolutePath プロパティを公開しました。このプロパティは、外部リンクの更新時に便利です。
### **Aspose.Cells.GridWeb 16.11.0では、GridHyperlinkCollectionクラスにGetHyperlinkメソッドが公開されました。**
GridHyperlinkCollectionクラスのGetHyperlinkメソッドの使用シナリオの簡単な例です。

{{% alert color="primary" %}} 

指定されたセルにハイパーリンクが見つからない場合、GetHyperlinkメソッドはnullを返します。

{{% /alert %}} 

GetHyperlinkメソッドの単純な使用シナリオは以下の通りです。

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **非推奨API**
### **廃止された Style コンストラクタ**
代わりに、cellsFactory.CreateStyleメソッドを使用してください。
## **削除されたAPI**
### **Deleted Cell.GetConditionalStyle Method**
代わりに、Cell.GetConditionalFormattingResultメソッドを使用してください。
### **削除されたCells.MaxDataRowInColumn(int column) Method**
代わりに、Cells.GetLastDataRow(int)メソッドを使用してください。
### **PageSetup.Draft プロパティが削除されました**
代わりに PageSetup.PrintDraft プロパティを使用することをお勧めします
### **AutoFilter.FilterColumnCollection プロパティが削除されました**
同じ目標を達成するためには AutoFilter.FilterColumns プロパティを考慮してください
### **TickLabels.Rotation プロパティが削除されました**
代わりに TickLabels.RotationAngle プロパティを使用してください
{{< app/cells/assistant language="csharp" >}}

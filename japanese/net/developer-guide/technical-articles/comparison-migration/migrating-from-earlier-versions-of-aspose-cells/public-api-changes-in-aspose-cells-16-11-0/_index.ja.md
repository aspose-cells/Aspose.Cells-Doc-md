---
title: パブリック API Aspose.Cells 16.11.0 の変更点
type: docs
weight: 350
url: /ja/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.10.0 から 16.11.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **グローバリゼーション設定のサポート**
Aspose.Cells 16.11.0 は、WorkbookSettings.GlobalizationSettings プロパティと共に GlobalizationSettings クラスを公開し、Aspose.Cells API で小計にカスタム ラベルを使用するように強制しました。 GlobalizationSettings クラスには次のメソッドがあり、カスタム実装でオーバーライドしてラベルに目的の名前を付けることができます**合計** & **総計**.

- GlobalizationSettings.GetTotalName: 関数の完全な名前を取得します。
- GlobalizationSettings.GetGrandTotalName: 関数の総計名を取得します。

以下は、GlobalizationSettings クラスを拡張し、前述のメソッドをオーバーライドして統合関数 Average のカスタム ラベルを返す単純なカスタム クラスです。

**C#**

{{< highlight "csharp" >}}

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



次のスニペットは、既存のスプレッドシートを読み込み、ワークシートで既に使用可能なデータにタイプ Average の小計を追加します。 CustomSettings クラスとその GetTotalName および GetGrandTotalName メソッドは、小計をワークシートに追加するときに呼び出されます。

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



GlobalizationSettings クラスは、円グラフの「その他」ラベルの名前を取得するのに役立つ GetOtherName メソッドも提供します。これは、GlobalizationSettings.GetOtherName メソッドの簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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



次のスニペットは、円グラフを含む既存のスプレッドシートを読み込み、上で作成した CustomSettings クラスを利用しながら、グラフを画像にレンダリングします。

**C#**

{{< highlight "csharp" >}}

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


### **CellsFactory クラスを追加**
Aspose.Cells 16.11.0 は、現在 1 つのメソッドを持つ CellsFactory クラスを公開しました。スタイルを作成します。 CellsFactory.CreateStyle メソッドを使用すると、ブック スタイルのプールに追加せずに Style クラスのインスタンスを作成できます。

CellsFactory.CreateStyle メソッドの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Workbook.AbsolutePath プロパティを追加**
Aspose.Cells 16.11.0 では、workbook.xml ファイルに格納されているブックの絶対パスを取得または設定できる Workbook.AbsolutePath プロパティが公開されました。このプロパティは、外部リンクのみを更新する場合に役立ちます。
### **GridHyperlinkCollection.GetHyperlink メソッドを追加**
Aspose.Cells.GridWeb 16.11.0 は、GridHyperlinkCollection クラスに GetHyperlink メソッドを公開しました。これにより、インスタンス GridCell または行の列インデックスに対応する整数のペアを渡すことによって、GridHyperlink のインスタンスを取得できます。

{{% alert color="primary" %}} 

指定されたセルにハイパーリンクが見つからない場合、GetHyperlink メソッドは null を返します。

{{% /alert %}} 

GetHyperlink メソッドの簡単な使用シナリオを次に示します。

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **廃止された API**
### **廃止されたスタイル コンストラクター**
代わりに、cellsFactory.CreateStyle メソッドを使用してください。
## **削除された API**
### **Cell.GetConditionalStyle メソッドを削除**
代わりに Cell.GetConditionalFormattingResult メソッドを使用してください。
### **Cells.MaxDataRowInColumn(int column) メソッドを削除**
代わりに Cells.GetLastDataRow(int) メソッドを使用してください。
### **削除された PageSetup.Draft プロパティ**
代わりに PageSetup.PrintDraft プロパティを使用することをお勧めします。
### **AutoFilter.FilterColumnCollection プロパティの削除**
同じ目標を達成するために AutoFilter.FilterColumns プロパティの使用を検討してください。
### **削除された TickLabels.Rotation プロパティ**
代わりに TickLabels.RotationAngle プロパティを使用してください。

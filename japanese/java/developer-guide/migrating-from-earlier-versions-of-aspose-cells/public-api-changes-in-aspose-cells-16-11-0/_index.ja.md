---
title: Aspose.Cells 16.11.0 での Public API 変更
type: docs
weight: 360
url: /ja/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者に関連がある可能性のある Aspose.Cells API のバージョン 16.10.0 から 16.11.0 への変更について説明しています。新しいおよび更新された public メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **グローバリゼーション設定のサポート**
Aspose.Cells 16.11.0 は、Subtotals にカスタム ラベルを使用するように Aspose.Cells API を強制するために GlobalizationSettings クラスと WorkbookSettings.GlobalizationSettings プロパティを公開しました。GlobalizationSettings クラスには、カスタム実装で望ましい名前を指定するためにオーバーライドできる次のメソッドがあります **Total** と **Grand Total**。

- GlobalizationSettings.getTotalName: 関数の合計名を取得します。
- GlobalizationSettings.getGrandTotalName: 関数の合計名を取得します。

GlobalizationSettings クラスを拡張し、前述のメソッドをオーバーライドしてコンソリデーション関数 Average のカスタム ラベルを返す単純なカスタムクラスは次のとおりです。

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

次のコード片は既存のスプレッドシートを読み込み、ワークシートにすでにあるデータに平均の Subtotal を追加します。追加時に CustomSettings クラスとその getTotalName、getGrandTotalName メソッドが呼び出されます。

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings クラスは Pie チャートの "Other" ラベルの名前を取得するのに役立つ getOtherName メソッドも提供しています。GlobalizationSettings.getOtherName メソッドの簡単な使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

次のコード片は、Pie チャートを含む既存のスプレッドシートを読み込み、上記で作成した CustomSettings クラスを利用しながらチャートを画像にレンダリングします。

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **CellsFactory クラスを追加しました**
Aspose.Cells 16.11.0 は、現在 createStyle という1つのメソッドを持つ CellsFactory クラスを公開しました。CellsFactory.createStyle メソッドは、ワークブックのスタイルのプールに追加せずに Style クラスのインスタンスを作成するために使用できます。

CellsFactory.createStyle メソッドの簡単な使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Workbook.AbsolutePath プロパティを追加しました**
Aspose.Cells 16.11.0 は、workbook.xml ファイルに保存された絶対ワークブック パスを取得または設定するための Workbook.AbsolutePath プロパティを公開しました。このプロパティは、外部リンクの更新時に便利です。
### **GridHyperlinkCollection.getHyperlink メソッドを追加しました**
Aspose.Cells.GridWeb 16.11.0 では、GridHyperlinkCollection クラスに getHyperlink メソッドが公開され、GridCell のインスタンスまたは行列インデックスのペアを渡すことで GridHyperlink のインスタンスを取得することができます。

{{% alert color="primary" %}} 

指定したセルにハイパーリンクが見つからない場合、getHyperlink メソッドは null を返します。

{{% /alert %}} 

getHyperlink メソッドの簡単な使用シナリオは次のとおりです。

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **非推奨API**
### **廃止された Style コンストラクタ**
代わりに cellsFactory.createStyle メソッドを使用してください。
## **削除されたAPI**
### **Cell.getConditionalStyle メソッドが削除されました**
代わりに Cell.getConditionalFormattingResult メソッドを使用してください
### **Cells.getMaxDataRowInColumn(int column) メソッドが削除されました**
代替として Cells.getLastDataRow(int) メソッドを使用してください
### **PageSetup.Draft プロパティが削除されました**
代わりに PageSetup.PrintDraft プロパティを使用することをお勧めします
### **AutoFilter.FilterColumnCollection プロパティが削除されました**
同じ目標を達成するためには AutoFilter.FilterColumns プロパティを考慮してください
### **TickLabels.Rotation プロパティが削除されました**
代わりに TickLabels.RotationAngle プロパティを使用してください
{{< app/cells/assistant language="java" >}}

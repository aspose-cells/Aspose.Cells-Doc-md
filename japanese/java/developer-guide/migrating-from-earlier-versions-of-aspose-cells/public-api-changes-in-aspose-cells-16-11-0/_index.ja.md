---
title: パブリック API Aspose.Cells 16.11.0 の変更点
type: docs
weight: 360
url: /ja/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.10.0 から 16.11.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **グローバリゼーション設定のサポート**
Aspose.Cells 16.11.0 は、WorkbookSettings.GlobalizationSettings プロパティと共に GlobalizationSettings クラスを公開し、Aspose.Cells API で小計にカスタム ラベルを使用するように強制しました。 GlobalizationSettings クラスには次のメソッドがあり、カスタム実装でオーバーライドしてラベルに目的の名前を付けることができます**合計** & **総計**.

- GlobalizationSettings.getTotalName: 関数の完全な名前を取得します。
- GlobalizationSettings.getGrandTotalName: 関数の総計名を取得します。

以下は、GlobalizationSettings クラスを拡張し、前述のメソッドをオーバーライドして統合関数 Average のカスタム ラベルを返す単純なカスタム クラスです。

**Java**

{{< highlight "csharp" >}}

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

次のスニペットは、既存のスプレッドシートを読み込み、ワークシートで既に使用可能なデータにタイプ Average の小計を追加します。 CustomSettings クラスとその getTotalName および getGrandTotalName メソッドは、小計をワークシートに追加するときに呼び出されます。

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings クラスは、円グラフの「その他」ラベルの名前を取得するのに役立つ getOtherName メソッドも提供します。以下は、GlobalizationSettings.getOtherName メソッドの簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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

次のスニペットは、円グラフを含む既存のスプレッドシートを読み込み、上で作成した CustomSettings クラスを利用しながら、グラフを画像にレンダリングします。

**Java**

{{< highlight "csharp" >}}

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
### **CellsFactory クラスを追加**
Aspose.Cells 16.11.0 は、現在 1 つのメソッドを持つ CellsFactory クラスを公開しました。スタイルを作成します。 CellsFactory.createStyle メソッドを使用すると、ワークブック スタイルのプールに追加せずに Style クラスのインスタンスを作成できます。

CellsFactory.createStyle メソッドの簡単な使用シナリオを次に示します。

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Workbook.AbsolutePath プロパティを追加**
Aspose.Cells 16.11.0 では、workbook.xml ファイルに格納されているブックの絶対パスを取得または設定できる Workbook.AbsolutePath プロパティが公開されました。このプロパティは、外部リンクのみを更新する場合に役立ちます。
### **GridHyperlinkCollection.getHyperlink メソッドを追加**
Aspose.Cells.GridWeb 16.11.0 は、インスタンス GridCell または行の列インデックスに対応する整数のペアを渡すことによって GridHyperlink のインスタンスを取得できる GridHyperlinkCollection クラスに getHyperlink メソッドを公開しました。

{{% alert color="primary" %}} 

指定されたセルにハイパーリンクが見つからない場合、getHyperlink メソッドは null を返します。

{{% /alert %}} 

getHyperlink メソッドの簡単な使用シナリオを次に示します。

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **廃止された API**
### **廃止されたスタイル コンストラクター**
代わりに、cellsFactory.createStyle メソッドを使用してください。
## **削除された API**
### **Cell.getConditionalStyle メソッドを削除**
代わりに Cell.getConditionalFormattingResult メソッドを使用してください。
### **Cells.getMaxDataRowInColumn(int column) メソッドを削除**
代わりに Cells.getLastDataRow(int) メソッドを使用してください。
### **削除された PageSetup.Draft プロパティ**
代わりに PageSetup.PrintDraft プロパティを使用することをお勧めします。
### **AutoFilter.FilterColumnCollection プロパティの削除**
同じ目標を達成するために AutoFilter.FilterColumns プロパティの使用を検討してください。
### **削除された TickLabels.Rotation プロパティ**
代わりに TickLabels.RotationAngle プロパティを使用してください。

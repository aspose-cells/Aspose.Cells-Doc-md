---
title: パブリック API Aspose.Cells 17.1.0 の変更点
type: docs
weight: 380
url: /ja/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.12.0 から 17.1.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **Excel 2016 グラフのサポート**
Aspose.Cells API は、ChartType 列挙を拡張することにより、いくつかの Excel 2016 グラフのサポートを追加しました。 Aspose.Cells 17.1.0 のリリースで、次の新しいフィールドが追加されました。

- ChartType.BOX_WHISKER: シリーズはボックスとウィスカーとして配置されます。
- ChartType.FUNNEL: シリーズはじょうごとしてレイアウトされます。
- ChartType.PARETO_LINE: シリーズはパレート線としてレイアウトされます。
- ChartType.SUNBURST: シリーズはサンバーストとして配置されます。
- ChartType.TREEMAP: シリーズはツリーマップとしてレイアウトされます。
- ChartType.WATERFALL: シリーズはウォーターフォールとしてレイアウトされます。
- ChartType.HISTOGRAM: シリーズはヒストグラムとしてレイアウトされます。

{{% alert color="primary" %}} 

の詳細記事をチェック[Excel 2016 グラフの種類の読み取り](/cells/ja/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions プロパティのセッターを追加**
Aspose.Cells 17.1.0 では、LoadFilter.LoadDataFilterOptions プロパティのセッターが追加され、m_LoadDataFilterOptions インスタンス変数が置き換えられました。ユーザーは、LoadFilter クラスの独自の実装で LoadDataFilterOptions プロパティを変更して、テンプレート ファイルの読み込み動作を変更できます。

簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[カスタム テンプレート フィルタリング](/cells/ja/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **CellsHelper.SignificantDigits プロパティを追加**
Aspose.Cells 17.1.0 は、スプレッドシートの数値の有効桁数を取得または設定できる CellsHelper クラスから SignificantDigits プロパティを公開しました。 CellsHelper.SignificantDigits プロパティのデフォルト値は 17 ですが、結果を XLSX ファイル形式で保存する必要がある場合にのみ適用されます。

CellsHelper.SignificantDigits プロパティの使用法を示す簡単なシナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[有効桁数の設定](/cells/ja/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **GlowEffect.Color プロパティを追加**
Aspose.Cells 17.1.0 では、グロー効果の色を取得するために使用できる GlowEffect.Color プロパティが追加されました。

次のスニペットでは、GlowEffect.Color プロパティを使用しています。

{{% alert color="primary" %}} 

の詳細記事をチェック[シェイプのグロー カラーの読み取り](/cells/ja/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **PageSetup.PaperWidth & PaperHeight プロパティを追加**
Aspose.Cells 17.1.0 では、PageSetup クラスの PaperWidth および PaperHeight プロパティが公開されました。 PageSetup.PaperWidth および PageSetup.PaperHeight プロパティは double 型で、ページの向きを考慮して用紙の幅と高さをインチ単位で表します。

{{% alert color="primary" %}} 

の詳細記事をチェック[ワークシートの用紙サイズの取得](/cells/ja/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat プロパティを追加**
Aspose.Cells 17.1.0 では、CheckCustomNumberFormat プロパティが WorkbookSettings クラスに追加されました。 CheckCustomNumberFormat は、Style.Custom プロパティが適切に設定されているかどうかを確認するのに役立ちます。 Style.Custom プロパティが不適切に設定されている場合、つまり、値が有効なパターンに対応していない場合、Aspose.Cells API は適切なメッセージとともに CellsException をスローします。

{{% alert color="primary" %}} 

の詳細記事をチェック[カスタム フォーマットの検証](/cells/ja/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **DisplayUnitType.PERCENTAGE フィールドを追加**
Aspose.Cells 17.1.0 では、PERCENTAGE フィールドも DisplayUnitType 列挙に公開されました。 DisplayUnitType.PERCENTAGE フィールドは、グラフの値が 0.01 で除算されることを示します。
## **削除された API**
### **インスタンス変数 m_LoadDataFilterOptions が削除されました**
このリリースでは、m_LoadDataFilterOptions インスタンス変数が削除されました。代わりに LoadFilter.LoadDataFilterOptions プロパティを使用することをお勧めします。

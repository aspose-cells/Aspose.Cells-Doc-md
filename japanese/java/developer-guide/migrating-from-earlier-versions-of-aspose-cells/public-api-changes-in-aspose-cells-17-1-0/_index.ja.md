---
title: Aspose.Cells 17.1.0 の公開API変更
type: docs
weight: 380
url: /ja/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

この文書は、バージョン16.12.0から17.1.0へのAspose.Cells APIの変更について、モジュール/アプリケーション開発者に興味を持たれる可能性のあるものを記載しています。新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Excel 2016 チャートのサポート**
Aspose.CellsのAPIは、ChartType列挙型を拡張していくつかのExcel 2016 チャートのサポートを追加しました。Aspose.Cells17.1.0のリリースと共に、以下の新しいフィールドが追加されています。

ChartType.BOX_WHISKER: シリーズは箱ひげ図として配置されます
ChartType.FUNNEL: シリーズはじょうごとして配置されます
ChartType.PARETO_LINE: シリーズはパレート線として配置されます
ChartType.SUNBURST: シリーズはサンバーストとして配置されます
ChartType.TREEMAP: シリーズはツリーマップとして配置されます
ChartType.WATERFALL: シリーズはウォーターフォールとして配置されます
ChartType.HISTOGRAM: シリーズはヒストグラムとして配置されます

{{% alert color="primary" %}} 

[Excel 2016 チャートタイプの読み取り](/cells/ja/java/read-and-manipulate-excel-2016-charts/)の詳細な記事を確認してください

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions プロパティのセッターが追加されました**
Aspose.Cells17.1.0では、LoadFilter.LoadDataFilterOptions プロパティのセッターが追加され、m_LoadDataFilterOptions インスタンス変数を置き換えるためにLoadFilterクラスのユーザーは自分の実装でLoadDataFilterOptionsプロパティを変更できます

以下は単純な使用シナリオです。

{{% alert color="primary" %}} 

詳細な記事は[カスタムテンプレートフィルタリング](/cells/ja/java/filter-objects-while-loading-workbook-or-worksheet/)を参照してください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **CellsHelper.SignificantDigits プロパティが追加されました。**
Aspose.Cells 17.1.0 では，CellsHelper クラスから SignificantDigits プロパティが公開され，スプレッドシート内の数値の有効桁数を取得または設定できます。CellsHelper.SignificantDigits プロパティのデフォルト値は17であり，結果をXLSXファイル形式で保存する場合のみ適用されます。

CellsHelper.SignificantDigits プロパティの使用法をデモンストレーションするシンプルなシナリオです。

{{% alert color="primary" %}} 

詳細な記事は[有効桁数の設定](/cells/ja/java/specifying-significant-digits-to-be-stored-in-excel-file/)を参照してください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **GlowEffect.Color プロパティが追加されました。**
Aspose.Cells 17.1.0 に GlowEffect.Color プロパティが追加され，グローエフェクトの色を取得するのに使用できます。

以下のコードは GlowEffect.Color プロパティを使用しています。

{{% alert color="primary" %}} 

詳細な記事は[シェイプのグローカラーの読み取り](/cells/ja/java/read-color-of-the-shape-s-glow-effect/)を参照してください。
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **PageSetup.PaperWidth 及び PaperHeight プロパティが追加されました。**
Aspose.Cells 17.1.0 では，PageSetup クラスに PaperWidth 及び PaperHeight プロパティが公開されました。PageSetup.PaperWidth 及び PageSetup.PaperHeight プロパティは，インチ単位でペーパーの幅と高さを表す double 型です。

{{% alert color="primary" %}} 

詳細な記事は[ワークシートのペーパーサイズを取得](/cells/ja/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)を参照してください。

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat プロパティが追加されました。**
Aspose.Cells 17.1.0 に WorkbookSettings クラスに CheckCustomNumberFormat プロパティが追加されました。CheckCustomNumberFormat は Style.Custom プロパティが適切に設定されているかどうかを確認するのに役立ちます。Style.Custom プロパティが適切に設定されていない場合，つまり，値が有効なパターンに対応していないと，Aspose.Cells API は適切なメッセージとともに CellsException をスローします。

{{% alert color="primary" %}} 

詳細な記事は[カスタムフォーマットの検証](/cells/ja/java/check-custom-number-format-when-setting-style-custom-property/)を参照してください。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **DisplayUnitType.PERCENTAGE フィールドが追加されました。**
Aspose.Cells 17.1.0 では，DisplayUnitType 列挙型に PERCENTAGE フィールドも公開されました。DisplayUnitType.PERCENTAGE フィールドは，チャート上の値が0.01で除算されることを示します。
## **API が削除されました**
### **Instance Variable m_LoadDataFilterOptions が削除されました。**
このリリースでは，m_LoadDataFilterOptions インスタンス変数が削除されました。LoadFilter.LoadDataFilterOptions プロパティを使用することを推奨します。

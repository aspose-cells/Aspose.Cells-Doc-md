---
title: Aspose.Cells 17.1.0 の公開API変更
type: docs
weight: 370
url: /ja/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

この文書は、バージョン16.12.0から17.1.0へのAspose.Cells APIの変更について、モジュール/アプリケーション開発者に興味を持たれる可能性のあるものを記載しています。新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Excel 2016 チャートのサポート**
Aspose.CellsのAPIは、ChartType列挙型を拡張していくつかのExcel 2016 チャートのサポートを追加しました。Aspose.Cells17.1.0のリリースと共に、以下の新しいフィールドが追加されています。

- ChartType.BoxWhisker: シリーズは箱ひげとして配置されます。
- ChartType.Funnel: シリーズはファンネルとして配置されます。
- ChartType.ParetoLine: シリーズはパレートラインとして配置されます。
- ChartType.Sunburst: シリーズはサンバーストとして配置されます。
- ChartType.Treemap: シリーズはツリーマップとしてレイアウトされます。
- ChartType.Waterfall: シリーズはウォーターフォールとして配置されます。
- ChartType.Histogram: シリーズはヒストグラムとして配置されます。

{{% alert color="primary" %}} 

[Excel 2016 チャートタイプの読み取り](/cells/ja/net/read-and-manipulate-excel-2016-charts/)に関する詳細な記事を確認してください。

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions プロパティのセッターが追加されました**
Aspose.Cells17.1.0では、LoadFilter.LoadDataFilterOptions プロパティのセッターが追加され、m_LoadDataFilterOptions インスタンス変数を置き換えるためにLoadFilterクラスのユーザーは自分の実装でLoadDataFilterOptionsプロパティを変更できます

以下は単純な使用シナリオです。

{{% alert color="primary" %}} 

[カスタムテンプレートフィルタリング](/cells/ja/net/filter-objects-while-loading-workbook-or-worksheet/)に関する詳細な記事を確認してください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **CellsHelper.SignificantDigits プロパティが追加されました。**
Aspose.Cells 17.1.0 では，CellsHelper クラスから SignificantDigits プロパティが公開され，スプレッドシート内の数値の有効桁数を取得または設定できます。CellsHelper.SignificantDigits プロパティのデフォルト値は17であり，結果をXLSXファイル形式で保存する場合のみ適用されます。

CellsHelper.SignificantDigits プロパティの使用法をデモンストレーションするシンプルなシナリオです。

{{% alert color="primary" %}} 

[Excel ファイルに格納される有効桁数の指定](/cells/ja/net/specifying-significant-digits-to-be-stored-in-excel-file/)に関する詳細な記事を確認してください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **GlowEffect.Color プロパティが追加されました。**
Aspose.Cells 17.1.0 に GlowEffect.Color プロパティが追加され，グローエフェクトの色を取得するのに使用できます。

以下のコードは GlowEffect.Color プロパティを使用しています。

{{% alert color="primary" %}} 

「形状の発光色」の詳細な記事は[こちら](/cells/ja/net/read-color-of-shape-s-glow-effect/)をご確認ください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **PageSetup.PaperWidth 及び PaperHeight プロパティが追加されました。**
Aspose.Cells 17.1.0 では，PageSetup クラスに PaperWidth 及び PaperHeight プロパティが公開されました。PageSetup.PaperWidth 及び PageSetup.PaperHeight プロパティは，インチ単位でペーパーの幅と高さを表す double 型です。

{{% alert color="primary" %}} 

ワークシートの用紙サイズの詳細な記事は[こちら](/cells/ja/net/get-paper-width-and-height-of-page-setup-of-worksheet/)をご確認ください

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat プロパティが追加されました。**
Aspose.Cells 17.1.0 に WorkbookSettings クラスに CheckCustomNumberFormat プロパティが追加されました。CheckCustomNumberFormat は Style.Custom プロパティが適切に設定されているかどうかを確認するのに役立ちます。Style.Custom プロパティが適切に設定されていない場合，つまり，値が有効なパターンに対応していないと，Aspose.Cells API は適切なメッセージとともに CellsException をスローします。

{{% alert color="primary" %}} 

カスタムフォーマットの詳細な記事は[こちら](/cells/ja/net/check-custom-number-format-when-setting-style-custom-property/)をご確認ください

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **DisplayUnitType.Percentageフィールドを追加しました**
Aspose.Cells 17.1.0では、DisplayUnitType列挙体にPercentageフィールドも公開されました。DisplayUnitType.Percentageフィールドは、チャート上の値を0.01で除算することを示します。
## **API が削除されました**
### **Instance Variable m_LoadDataFilterOptions が削除されました。**
このリリースでは，m_LoadDataFilterOptions インスタンス変数が削除されました。LoadFilter.LoadDataFilterOptions プロパティを使用することを推奨します。
{{< app/cells/assistant language="csharp" >}}

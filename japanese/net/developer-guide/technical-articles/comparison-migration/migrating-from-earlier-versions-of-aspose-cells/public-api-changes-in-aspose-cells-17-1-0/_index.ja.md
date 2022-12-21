---
title: パブリック API Aspose.Cells 17.1.0 の変更点
type: docs
weight: 370
url: /ja/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.12.0 から 17.1.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **Excel 2016 グラフのサポート**
Aspose.Cells API は、ChartType 列挙を拡張することにより、いくつかの Excel 2016 グラフのサポートを追加しました。 Aspose.Cells 17.1.0 のリリースで、次の新しいフィールドが追加されました。

- ChartType.BoxWhisker: シリーズはボックスとウィスカーとして配置されます。
- ChartType.Funnel: シリーズはじょうごとしてレイアウトされます。
- ChartType.ParetoLine: シリーズはパレート線としてレイアウトされます。
- ChartType.Sunburst: シリーズはサンバーストとして配置されます。
- ChartType.Treemap: シリーズはツリーマップとして配置されます。
- ChartType.Waterfall: シリーズはウォーターフォールとしてレイアウトされます。
- ChartType.Histogram: シリーズはヒストグラムとして配置されます。

{{% alert color="primary" %}} 

の詳細記事をチェック[Excel 2016 グラフの種類の読み取り](/cells/ja/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions プロパティのセッターを追加**
Aspose.Cells 17.1.0 では、LoadFilter.LoadDataFilterOptions プロパティのセッターが追加され、m_LoadDataFilterOptions インスタンス変数が置き換えられました。ユーザーは、LoadFilter クラスの独自の実装で LoadDataFilterOptions プロパティを変更して、テンプレート ファイルの読み込み動作を変更できます。

簡単な使用シナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[カスタム テンプレート フィルタリング](/cells/ja/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **CellsHelper.SignificantDigits プロパティを追加**
Aspose.Cells 17.1.0 は、スプレッドシートの数値の有効桁数を取得または設定できる CellsHelper クラスから SignificantDigits プロパティを公開しました。 CellsHelper.SignificantDigits プロパティのデフォルト値は 17 ですが、結果を XLSX ファイル形式で保存する必要がある場合にのみ適用されます。

CellsHelper.SignificantDigits プロパティの使用法を示す簡単なシナリオを次に示します。

{{% alert color="primary" %}} 

の詳細記事をチェック[有効桁数の設定](/cells/ja/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **GlowEffect.Color プロパティを追加**
Aspose.Cells 17.1.0 では、グロー効果の色を取得するために使用できる GlowEffect.Color プロパティが追加されました。

次のスニペットでは、GlowEffect.Color プロパティを使用しています。

{{% alert color="primary" %}} 

の詳細記事をチェック[シェイプのグロー カラーの読み取り](/cells/ja/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **PageSetup.PaperWidth & PaperHeight プロパティを追加**
Aspose.Cells 17.1.0 では、PageSetup クラスの PaperWidth および PaperHeight プロパティが公開されました。 PageSetup.PaperWidth および PageSetup.PaperHeight プロパティは double 型で、ページの向きを考慮して用紙の幅と高さをインチ単位で表します。

{{% alert color="primary" %}} 

の詳細記事をチェック[ワークシートの用紙サイズの取得](/cells/ja/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat プロパティを追加**
Aspose.Cells 17.1.0 では、CheckCustomNumberFormat プロパティが WorkbookSettings クラスに追加されました。 CheckCustomNumberFormat は、Style.Custom プロパティが適切に設定されているかどうかを確認するのに役立ちます。 Style.Custom プロパティが不適切に設定されている場合、つまり、値が有効なパターンに対応していない場合、Aspose.Cells API は適切なメッセージとともに CellsException をスローします。

{{% alert color="primary" %}} 

の詳細記事をチェック[カスタム形式の確認](/cells/ja/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **DisplayUnitType.Percentage フィールドを追加**
Aspose.Cells 17.1.0 では、Percentage フィールドも DisplayUnitType 列挙に公開されています。 DisplayUnitType.Percentage フィールドは、グラフの値が 0.01 で除算されることを示します。
## **削除された API**
### **インスタンス変数 m_LoadDataFilterOptions が削除されました**
このリリースでは、m_LoadDataFilterOptions インスタンス変数が削除されました。代わりに LoadFilter.LoadDataFilterOptions プロパティを使用することをお勧めします。

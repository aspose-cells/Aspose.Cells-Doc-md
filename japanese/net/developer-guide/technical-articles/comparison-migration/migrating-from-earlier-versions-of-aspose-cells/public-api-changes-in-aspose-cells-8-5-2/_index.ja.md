---
title: パブリック API Aspose.Cells の変更点 8.5.2
type: docs
weight: 180
url: /ja/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.5.1 から 8.5.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-5-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **ワークシートをグラフィック コンテキストにレンダリング**
 Aspose.Cells for .NET API のこのリリースでは、System.Drawing.Graphics クラスのインスタンスを受け入れることができる SheetRender.ToImage メソッドの 2 つの新しいオーバーロードが公開されました。[グラフィックス コンテキストでレンダリングする](/cells/ja/net/render-worksheet-to-graphic-context/).新しく追加されたメソッドのシグネチャは次のとおりです。

1. SheetRender.ToImage(int pageIndex、Graphics g、float x、float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **メソッド PivoTable.GetCellByDisplayName が追加されました**
Aspose.Cells for .NET 8.5.2 で使用できる PivotTable.GetCellByDisplayName メソッドが公開されました。[PivotField の名前で Cell オブジェクトを取得します](/cells/ja/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/).このメソッドは、ピボットフィールド ヘッダーを強調表示または書式設定する場合に役立ちます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **プロパティ SaveOptions.MergeAreas が追加されました**
Aspose.Cells for .NET 8.5.2 では、ブール型の値を受け入れることができる SaveOptions.MergeAreas プロパティが公開されました。デフォルト値は false ですが、true に設定すると、Aspose.Cells for .NET API はファイルを保存する前に個々の CellArea をマージしようとします。

{{% alert color="primary" %}} 

スプレッドシートに検証が適用された個々のセルが多すぎる場合、結果のスプレッドシートが破損する可能性があります。考えられる解決策の 1 つは、同一の検証規則でセルを結合することです。または、SaveOptions.MergeAreas プロパティを使用して、保存操作の前に CellAreas を自動結合するように API に指示できます。

{{% /alert %}} 
### **プロパティ Shape.Geometry.ShapeAdjustValues が追加されました**
v8.5.2 のリリースにより、Aspose.Cells API は、使用できる Shape.Geometry.ShapeAdjustValues プロパティを公開しました。[さまざまな形状の調整ポイントを変更する](/cells/ja/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel インターフェイスでは、調整ポイントは黄色のひし形ノードとして表示されます。

{{% /alert %}} 

例えば、

1. 角丸長方形には、円弧を変更するための調整があります
1. 三角形には、ポイントの位置を変更するための調整があります
1. 台形は、トップの幅を変更する調整があります
1. 矢印には、頭と尾の形状を変更するための 2 つの調整があります。

これが最も単純な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **列挙型フィールド ConsolidationFunction.DistinctCount が追加されました**
Aspose.Cells for .NET 8.5.2 で ConsolidationFunction.DistinctCount フィールドが公開されました。[Distinct Count 連結関数を適用する](/cells/ja/net/consolidation-function/)ピボットテーブルのデータ フィールド。

{{% alert color="primary" %}} 

Distinct Count 連結機能は、Microsoft Excel 2013 のみでサポートされています。

{{% /alert %}} 
### **GridDesktop のイベント処理の改善**
Aspose.Cells.GridDesktop の今回のリリースでは、4 つの新しいイベントが公開されました。これらのイベントのうち 2 つは、GridDesktop でスプレッドシート ファイルをロードするさまざまな状態でトリガーされますが、他の 2 つは数式の計算時にトリガーされます。

イベントは次のとおりです。

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate

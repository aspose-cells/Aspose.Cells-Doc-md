---
title: Aspose.Cells 8.5.2のPublic APIの変更
type: docs
weight: 180
url: /ja/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.5.1 から 8.5.2 への変更点をモジュール/アプリケーション開発者に関連する可能性があるものとして説明しています。新しいおよび更新された公開メソッド、追加されたクラスなどだけでなく、Aspose.Cells の裏側での動作の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **ワークシートをグラフィックコンテキストにレンダリング**
このリリースの Aspose.Cells for .NET API は、SheetRender.ToImage メソッドの新しいオーバーロードを公開し、System.Drawing.Graphics クラスのインスタンスを受け入れて [グラフィックコンテキストでのレンダリング](/cells/ja/net/render-worksheet-to-graphic-context/) を可能にしました。新しく追加されたメソッドのシグネチャは次のとおりです。

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **PivotTable.GetCellByDisplayName メソッドが追加されました**
Aspose.Cells for .NET 8.5.2 は PivotTable.GetCellByDisplayName メソッドを公開し、[PivotTable の PivotField 名で Cell オブジェクトを取得](/cells/ja/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/) するために使用できます。このメソッドは、PivotField ヘッダーを強調表示または書式設定したいシナリオで有用です。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **SaveOptions.MergeAreasプロパティを追加**
Aspose.Cells for .NET 8.5.2 では、SaveOptions.MergeAreas プロパティが公開され、Boolean 型の値を受け入れるようになりました。デフォルト値は false ですが、true に設定すると、Aspose.Cells for .NET API はファイルを保存する前に個々の CellArea をマージしようとします。

{{% alert color="primary" %}} 

スプレッドシートに検証が適用された個々のセルが多すぎる場合、生成されるスプレッドシートが壊れる可能性があります。類似する検証ルールを持つセルをマージする一つの解決策、またはSaveOptions.MergeAreasプロパティを使用して、APIに保存操作前に自動でCellAreasをマージするよう指示することができます。

{{% /alert %}} 
### **Shape.Geometry.ShapeAdjustValues プロパティが追加されました**
v8.5.2 のリリースでは、Aspose.Cells API は Shape.Geometry.ShapeAdjustValues プロパティを公開し、さまざまな形状の調整ポイントを[変更するために使用できるようにしました](/cells/ja/net/change-adjustment-values-of-the-shape/)。

{{% alert color="primary" %}} 

Microsoft Excel インタフェースでは、調整ポイントが黄色のダイヤモンドノードとして表示されます。

{{% /alert %}} 

たとえば、

1. 丸角長方形には、角を変更するための調整があります
2. 三角形には、ポイントの位置を変更するための調整があります
3. 台形には、上部の幅を変更するための調整があります
4. 矢印には、ヘッドとテールの形状を変更するための2つの調整があります

以下は最もシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **列挙型 ConsolidationFunction.DistinctCount が追加されました**
Aspose.Cells for .NET 8.5.2 は ConsolidationFunction.DistinctCount フィールドを公開し、PivotTable の DataField に [重複のないカウントの結合関数を適用](/cells/ja/net/consolidation-function/) するために使用できます。

{{% alert color="primary" %}} 

Distinct Count 結合関数は、Microsoft Excel 2013 でのみサポートされています。

{{% /alert %}} 
### **GridDesktop のイベントハンドリングの改善**
この Aspose.Cells.GridDesktop のリリースでは、4 つの新しいイベントが公開されました。これらのイベントの 2 つは、GridDesktop でスプレッドシートファイルをロードする異なる状態でトリガーされ、残りの 2 つは数式の計算時にトリガーされます。

以下のようにイベントがリストされています。

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate

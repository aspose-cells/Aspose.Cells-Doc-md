---
title: パブリック API Aspose.Cells の変更点 8.5.2
type: docs
weight: 190
url: /ja/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.5.1 から 8.5.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **ワークシートをグラフィック コンテキストにレンダリング**
Aspose.Cells for Java API のこのリリースでは、Graphics2D クラスのインスタンスを受け入れることができる SheetRender.toImage メソッドの別のオーバーロードが公開されました。[ワークシートをグラフィック コンテキストでレンダリングする](/cells/ja/java/render-worksheet-to-graphic-context/).新しく追加されたメソッドのシグネチャは次のとおりです。

- SheetRender.toImage(int pageIndex, Graphics2D グラフィック)

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **メソッド PivoTable.getCellByDisplayName が追加されました**
Aspose.Cells for Java 8.5.2 は PivotTable.getCellByDisplayName メソッドを公開しました。[PivotField の名前で Cell オブジェクトを取得します](/cells/ja/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/).このメソッドは、ピボットフィールド ヘッダーを強調表示または書式設定する場合に役立ちます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **プロパティ SaveOptions.MergeAreas が追加されました**
Aspose.Cells for Java 8.5.2 では、ブール型の値を受け入れることができる SaveOptions.MergeAreas プロパティが公開されました。デフォルト値は false ですが、true に設定すると、Aspose.Cells for Java API はファイルを保存する前に個々の CellArea をマージしようとします。

{{% alert color="primary" %}} 

スプレッドシートに検証が適用された個々のセルが多すぎる場合、結果のスプレッドシートが破損する可能性があります。考えられる解決策の 1 つは、同一の検証規則でセルを結合することです。または、SaveOptions.MergeAreas プロパティを使用して、保存操作の前に CellAreas を自動結合するように API に指示できます。

{{% /alert %}} 
### **プロパティ Geometry.ShapeAdjustValues が追加されました**
v8.5.2 のリリースにより、Aspose.Cells API は Geometry.getShapeAdjustValues メソッドを公開しました。[さまざまな形状の調整ポイントにアクセスして変更する](/cells/ja/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel インターフェイスでは、調整ポイントが黄色のひし形ノードとして表示されます。

{{% /alert %}} 

例えば、

1. 角丸長方形には、円弧を変更するための調整があります
1. 三角形には、ポイントの位置を変更するための調整があります
1. 台形は、トップの幅を変更する調整があります
1. 矢印には、頭と尾の形状を変更するための 2 つの調整があります。

これが最も単純な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **列挙型フィールド ConsolidationFunction.DISTINCT_COUNT が追加されました**
Aspose.Cells for Java 8.5.2 では、ピボットテーブルの DataField に Distinct Count 統合関数を適用するために使用できる ConsolidationFunction.DISTINCT_COUNT フィールドが公開されました。

{{% alert color="primary" %}} 

Distinct Count 連結機能は、Microsoft Excel 2013 のみでサポートされています。

{{% /alert %}}

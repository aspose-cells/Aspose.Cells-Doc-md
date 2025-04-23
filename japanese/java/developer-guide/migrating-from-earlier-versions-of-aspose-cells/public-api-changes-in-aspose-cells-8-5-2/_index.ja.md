---
title: Aspose.Cells 8.5.2のPublic APIの変更
type: docs
weight: 190
url: /ja/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

このドキュメントには、バージョン8.5.1から8.5.2へのAspose.Cells APIの変更が含まれており、モジュール/アプリケーション開発者に興味を持たれる可能性があるものです。新しいメソッドや更新されたpublicメソッド,[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-2/)だけでなく、Aspose.Cellsの背後での挙動に変更がある場合についての説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **ワークシートをグラフィックコンテキストにレンダリング**
このAspose.Cells for Java APIのリリースでは、SheetRender.toImageメソッドの別のオーバーロードが公開され、現在はGraphics2Dクラスのインスタンスを受け入れて、[ワークシートをグラフィックコンテキストにレンダリング](/cells/ja/java/render-worksheet-to-graphic-context/)することができます。新しく追加されたメソッドのシグネチャは次のとおりです。

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
### **PivotTable.getCellByDisplayNameメソッドを追加**
Aspose.Cells for Java 8.5.2では、PivotTable.getCellByDisplayNameメソッドが公開され、[PivotFieldの名前によってCellオブジェクトを取得](/cells/ja/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/)することができます。このメソッドは、PivotFieldヘッダーの強調表示や書式設定を行いたい場合に役立ちます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
### **SaveOptions.MergeAreasプロパティを追加**
Aspose.Cells for Java 8.5.2では、SaveOptions.MergeAreasプロパティが公開され、Boolean型の値を受け入れるようになりました。デフォルト値はfalseですが、trueに設定すると、Aspose.Cells for Java APIはファイルを保存する前に個々のCellAreaをマージしようとします。

{{% alert color="primary" %}} 

スプレッドシートに検証が適用された個々のセルが多すぎる場合、生成されるスプレッドシートが壊れる可能性があります。類似する検証ルールを持つセルをマージする一つの解決策、またはSaveOptions.MergeAreasプロパティを使用して、APIに保存操作前に自動でCellAreasをマージするよう指示することができます。

{{% /alert %}} 
### **Geometry.ShapeAdjustValuesプロパティを追加**
v8.5.2のリリースに伴い、Aspose.Cells APIはGeometry.getShapeAdjustValuesメソッドを公開し、[異なる形状の調整ポイントにアクセスして変更を加える](/cells/ja/java/change-adjustment-values-of-the-shape/)ことができるようになりました。

{{% alert color="primary" %}} 

Microsoft Excelのインターフェイスでは、調整ポイントが黄色のダイヤモンドノードとして表示されます。

{{% /alert %}} 

たとえば、 

1. 丸角長方形には、角を変更するための調整があります
2. 三角形には、ポイントの位置を変更するための調整があります
3. 台形には、上部の幅を変更するための調整があります
4. 矢印には、ヘッドとテールの形状を変更するための2つの調整があります

以下は最もシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
### **列挙フィールド ConsolidationFunction.DISTINCT_COUNT が追加されました**
Aspose.Cells for Java 8.5.2 では、ConsolidationFunction.DISTINCT_COUNT フィールドが公開されており、PivotTable の DataField に対して Distinct Count 結合関数を適用できます。

{{% alert color="primary" %}} 

Distinct Count 結合関数は、Microsoft Excel 2013 でのみサポートされています。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

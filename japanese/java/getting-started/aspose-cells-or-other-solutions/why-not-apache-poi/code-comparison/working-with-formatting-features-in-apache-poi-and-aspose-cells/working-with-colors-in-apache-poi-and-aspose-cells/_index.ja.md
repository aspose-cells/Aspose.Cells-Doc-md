---
title: Apache POI および Aspose.Cells での色の操作
type: docs
weight: 20
url: /ja/java/working-with-colors-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 色を扱う**
Aspose.Cells はクラスを提供し、[ワークブック](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは、[ワークシート](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)クラス。 Worksheet クラスは Cellscollection を提供します。 Cells コレクションの各アイテムは、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)クラス。

Aspose.Cells は、セルの書式設定に使用される Cell クラスの setStyle メソッドを提供します。また、Style クラスの Style オブジェクトを使用して、フォント設定を構成できます。

**Java**

{{< highlight "java" >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 色の操作**
CellStyle クラスを使用して、背景と塗りつぶしの設定を設定できます。

**Java**

{{< highlight "java" >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[色と背景パターン](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}

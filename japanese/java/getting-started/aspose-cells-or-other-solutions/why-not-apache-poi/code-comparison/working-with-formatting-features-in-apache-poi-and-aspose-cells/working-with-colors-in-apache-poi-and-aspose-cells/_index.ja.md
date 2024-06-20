---
title: Apache POI および Aspose.Cells で色の扱い
type: docs
weight: 20
url: /ja/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 色の操作**
Aspose.Cells は、Microsoft Excel ファイルを表す[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) クラスを提供します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスが許可される[WorksheetCollection](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) を含んでいます。ワークシートは[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) クラスによって表されます。Worksheet クラスは、Cellscollection を提供します。Cells コレクション内の各アイテムは、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) クラスのオブジェクトを表します。

Aspose.Cells は、Cell クラスのsetStyle メソッドを提供し、セルのフォーマットを設定するために使用されます。また、Style クラスの Style オブジェクトを使用してフォント設定を構成できます。

**Java**

{{< highlight java >}}

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
## **Apache POI SS - HSSF XSSF - 色の扱い**
CellStyle クラスは、背景色と塗りつぶしパターンの設定を行うために利用できます。

**Java**

{{< highlight java >}}

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

[カラーと背景パターン](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns)をご覧ください。

{{% /alert %}}

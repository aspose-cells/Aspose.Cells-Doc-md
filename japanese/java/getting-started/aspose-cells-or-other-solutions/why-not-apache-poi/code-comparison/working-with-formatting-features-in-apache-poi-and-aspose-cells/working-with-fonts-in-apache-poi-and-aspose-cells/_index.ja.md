---
title: Apache POI および Aspose.Cells でのフォントの操作
type: docs
weight: 30
url: /ja/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - フォントの操作**
Aspose.Cells はクラスを提供し、[ワークブック](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection が含まれています。ワークシートは、[ワークシート](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)クラス。 Worksheet クラスは Cells コレクションを提供します。 Cells コレクションの各アイテムは、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)クラス。

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - フォントの操作**
Apache POI SS は、さまざまなフォント設定を設定するための Font クラスを提供します。

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[フォント設定の扱い](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}

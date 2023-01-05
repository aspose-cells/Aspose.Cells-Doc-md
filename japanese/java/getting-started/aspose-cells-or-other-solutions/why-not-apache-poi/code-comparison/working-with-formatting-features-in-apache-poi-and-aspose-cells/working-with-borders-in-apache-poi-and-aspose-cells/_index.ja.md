---
title: Apache POI および Aspose.Cells での境界線の操作
type: docs
weight: 10
url: /ja/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - ボーダーの操作**
Aspose.Cells はクラスを提供し、[ワークブック](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは、[ワークシート](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)クラス。 Worksheet クラスは Cellscollection を提供します。 Cells コレクションの各アイテムは、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)クラス。

Aspose.Cells は、setStyle メソッドを[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)セルのフォーマット スタイルを設定するために使用されるクラス。また、の Style オブジェクト[スタイル](http://docs.aspose.com:8082/docs/display/cellsjava/Style)クラスが使用され、フォント設定を構成するためのプロパティを提供します。

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - ボーダーの操作**
CellStyle クラスは、Apache POI SS - HSSF および XSSF を使用してボーダー設定を設定する機能を提供します。

**Java**

{{< highlight "java" >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[Cells に罫線を追加する](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}

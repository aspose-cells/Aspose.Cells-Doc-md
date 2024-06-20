---
title: Apache POI および Aspose.Cells で境界線を扱う
type: docs
weight: 10
url: /ja/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 境界線の操作**
Aspose.Cells は、Microsoft Excel ファイルを表す[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) クラスを提供します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスが許可される[WorksheetCollection](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) を含んでいます。ワークシートは[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) クラスによって表されます。Worksheet クラスは、Cellscollection を提供します。Cells コレクション内の各アイテムは、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) クラスのオブジェクトを表します。

Aspose.Cells は、[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) クラスのsetStyle メソッドを提供し、セルの書式設定を行うために使用されます。また、フォント設定を構成するための[Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) クラスの Style オブジェクトを使用できます。

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 色の扱い**
CellStyle クラスは、Apache POI SS - HSSF および XSSF を使用して境界線の設定を提供します。

**Java**

{{< highlight java >}}

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

詳細については、[セルに境界線を追加する](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells) を参照してください。

{{% /alert %}}

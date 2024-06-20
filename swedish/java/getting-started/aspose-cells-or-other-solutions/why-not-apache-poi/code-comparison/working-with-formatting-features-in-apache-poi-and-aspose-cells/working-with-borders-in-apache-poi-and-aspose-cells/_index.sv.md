---
title: Arbeta med ramar i Apache POI och Aspose.Cells
type: docs
weight: 10
url: /sv/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Arbeta med ramar**
Aspose.Cells tillhandahåller en klass, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). Klassen Worksheet tillhandahåller en Cells-samling. Varje objekt i Cells-samlingen representerar ett objekt av klassen [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells tillhandahåller metoden setStyle i klassen [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) som används för att ange en cells formateringsstil. Dessutom används Style-objektet i klassen [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) och tillhandahåller egenskaper för att konfigurera teckensnittsinställningar.

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
## **Apache POI SS - HSSF XSSF - Arbeta med ramar**
CellStyle-klassen tillhandahåller funktioner för att ange ramsinställningar med Apache POI SS - HSSF och XSSF.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

För mer information, besök [Lägga till ramar till celler](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}

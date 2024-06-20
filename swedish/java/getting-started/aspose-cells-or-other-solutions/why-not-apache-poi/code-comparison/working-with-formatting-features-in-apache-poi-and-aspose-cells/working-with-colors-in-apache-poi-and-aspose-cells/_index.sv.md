---
title: Arbeta med färger i Apache POI och Aspose.Cells
type: docs
weight: 20
url: /sv/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Arbeta med färger**
Aspose.Cells tillhandahåller en klass, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). Klassen Worksheet tillhandahåller en Cells-samling. Varje objekt i Cells-samlingen representerar ett objekt av klassen [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells tillhandahåller metoden setStyle i klassen Cell som används för att ange en cells formatering. Dessutom kan objektet Style i klassen Style användas för att konfigurera teckensnittsinställningar.

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
## **Apache POI SS - HSSF XSSF - Arbeta med färger**
CellStyle-klassen är tillgänglig för att ange bakgrund och fillpattern-inställningar.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

För mer information, besök [Färger och bakgrundsmönster](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}

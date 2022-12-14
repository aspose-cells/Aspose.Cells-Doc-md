---
title: Arbeta med teckensnitt i Apache POI och Aspose.Cells
type: docs
weight: 30
url: /sv/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Arbeta med teckensnitt**
Aspose.Cells tillhandahåller en klass,[Arbetsbok](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)klass. Kalkylbladsklassen tillhandahåller en Cells-samling. Varje föremål i Cells-samlingen representerar ett objekt av[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)klass.

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
## **Apache POI SS - HSSF XSSF - Arbeta med teckensnitt**
Apache POI SS tillhandahåller teckensnittsklass för att ställa in olika teckensnittsinställningar.

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 För mer information, besök[Hantera teckensnittsinställningar](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}

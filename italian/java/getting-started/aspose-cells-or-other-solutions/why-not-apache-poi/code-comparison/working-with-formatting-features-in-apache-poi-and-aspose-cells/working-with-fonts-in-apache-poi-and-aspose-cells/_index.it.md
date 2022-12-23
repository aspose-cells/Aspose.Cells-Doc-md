---
title: Lavorare con i caratteri in Apache POI e Aspose.Cells
type: docs
weight: 30
url: /it/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Lavorare con i caratteri**
Aspose.Cells offre un corso,[Cartella di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classe. La classe del foglio di lavoro fornisce una raccolta Cells. Ogni articolo della collezione Cells rappresenta un oggetto della[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe.

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
## **Apache POI SS - HSSF XSSF - Lavorare con i caratteri**
Apache POI SS fornisce la classe Font per configurare varie impostazioni dei caratteri.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Gestione delle impostazioni dei caratteri](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}

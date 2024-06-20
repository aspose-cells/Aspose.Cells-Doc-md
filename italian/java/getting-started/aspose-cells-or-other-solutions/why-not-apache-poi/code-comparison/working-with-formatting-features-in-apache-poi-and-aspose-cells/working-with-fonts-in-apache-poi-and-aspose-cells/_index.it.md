---
title: Lavorare con i Caratteri in Apache POI e Aspose.Cells
type: docs
weight: 30
url: /it/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Lavorare con i Caratteri**
Aspose.Cells fornisce una classe, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La classe Worksheet fornisce una raccolta di celle. Ogni elemento nella raccolta di celle rappresenta un oggetto della classe [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

**Java**

{{< highlight java >}}

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
## **Apache POI SS - HSSF XSSF - Lavorare con i Caratteri**
Apache POI SS fornisce la classe Font per impostare diverse impostazioni del carattere.

**Java**

{{< highlight java >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Gestione delle Impostazioni del Carattere](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}

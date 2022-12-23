---
title: Lavorare con i colori in Apache POI e Aspose.Cells
type: docs
weight: 20
url: /it/java/working-with-colors-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Lavorare con i colori**
Aspose.Cells offre un corso,[Cartella di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classe. La classe Worksheet fornisce una raccolta Cells. Ogni articolo della collezione Cells rappresenta un oggetto della[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe.

Aspose.Cells fornisce il metodo setStyle nella classe Cell utilizzata per impostare la formattazione di una cella. Inoltre, l'oggetto Style della classe Style può essere utilizzato per configurare le impostazioni dei caratteri.

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
## **Apache POI SS - HSSF XSSF - Lavorare con i colori**
La classe CellStyle è disponibile per impostare le impostazioni di background e fillpattern.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Colori e motivi di sfondo](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}

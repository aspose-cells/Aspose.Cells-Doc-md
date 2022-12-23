---
title: Lavorare con i bordi in Apache POI e Aspose.Cells
type: docs
weight: 10
url: /it/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Lavorare con i confini**
Aspose.Cells offre un corso,[Cartella di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classe. La classe Worksheet fornisce una raccolta Cells. Ogni articolo della collezione Cells rappresenta un oggetto della[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe.

Aspose.Cells fornisce il metodo setStyle nel file[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe utilizzata per impostare lo stile di formattazione di una cella. Inoltre, l'oggetto Style di[Stile](http://docs.aspose.com:8082/docs/display/cellsjava/Style)viene utilizzata la classe e fornisce le proprietà per la configurazione delle impostazioni dei caratteri.

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
## **Apache POI SS - HSSF XSSF - Lavorare con i bordi**
La classe CellStyle fornisce funzionalità per impostare le impostazioni dei bordi utilizzando Apache POI SS - HSSF e XSSF.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Aggiunta di bordi a Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}

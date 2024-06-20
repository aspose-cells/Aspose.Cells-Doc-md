---
title: Lavorare con i bordi in Apache POI e Aspose.Cells
type: docs
weight: 10
url: /it/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Lavorare con i bordi**
Aspose.Cells fornisce una classe, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La classe Worksheet fornisce una raccolta di celle. Ogni elemento nella raccolta Cells rappresenta un oggetto della classe [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells fornisce il metodo setStyle nella classe [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) utilizzato per impostare lo stile di formattazione di una cella. Inoltre, viene utilizzato l'oggetto Style della classe [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) che fornisce proprietà per configurare le impostazioni del font.

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
## **Apache POI SS - HSSF XSSF - Lavorare con i bordi**
La classe CellStyle fornisce funzionalità per impostare le impostazioni dei bordi utilizzando Apache POI SS - HSSF e XSSF.

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
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Aggiunta di bordi alle celle](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}

---
title: Nuova Linea nelle Celle
type: docs
weight: 30
url: /it/java/new-line-in-cells/
---

## **Aspose.Cells - Nuova Linea nelle Celle**
Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

Per far andare a capo il testo in una cella, utilizzare il metodo Style.setTextWrapped.

**Java**

{{< highlight java >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Nuova riga in celle**
CellStyle.setWrapText dovrebbe essere vero per il testo a capo automatico.

**Java**

{{< highlight java >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Interruzioni di linea e testo a capo](/java/line-breaks-and-text-wrapping).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

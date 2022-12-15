---
title: Nuova Linea allo Cells
type: docs
weight: 30
url: /it/java/new-line-in-cells/
---
## **Aspose.Cells - Nuova Linea Cells**
Per garantire che il testo in una cella possa essere letto, è possibile applicare interruzioni di riga esplicite e ritorno a capo automatico. Il ritorno a capo trasforma una riga in più righe in una cella, che le interruzioni di riga esplicite inseriscono nelle interruzioni esattamente dove le desideri.

Per disporre il testo in una cella, utilizzare il metodo Style.setTextWrapped.

**Giava**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Nuova linea in Cells**
CellStyle.setWrapText dovrebbe essere vero per il testo a capo.

**Giava**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Interruzioni di riga e ritorno a capo del testo](/java/line-breaks-and-text-wrapping).

{{% /alert %}}

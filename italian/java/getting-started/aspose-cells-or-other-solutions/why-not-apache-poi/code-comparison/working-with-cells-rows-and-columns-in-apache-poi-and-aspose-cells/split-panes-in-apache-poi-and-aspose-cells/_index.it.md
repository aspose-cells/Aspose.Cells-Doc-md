---
title: Dividere riquadri in Apache POI e Aspose.Cells
type: docs
weight: 70
url: /it/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Dividi riquadri**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Microsoft Excel. La classe Workbook fornisce una vasta gamma di proprietà e metodi per la gestione dei file Excel. Per implementare le visualizzazioni suddivise, utilizza il metodo split della classe Worksheet. Per rimuovere riquadri suddivisi, utilizza il metodo removeSplit.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Riquadri suddivisi**
La funzionalità dei riquadri suddivisi può essere ottenuta mediante il metodo createSplitPane utilizzando l'API Apache POI SS (HSSF & XSSF).

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

Per maggiori dettagli, visita [Riquadri suddivisi](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

---
title: Fattore di Zoom utilizzando Apache POI e Aspose.Cells
type: docs
weight: 70
url: /it/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Fattore di zoom**
Microsoft Excel offre una funzione che consente agli utenti di impostare il fattore di zoom o di scala di un foglio di lavoro. Questa funzione aiuta gli utenti a visualizzare i contenuti del foglio di lavoro in visualizzazioni più piccole o più grandi.

Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente l'accesso ad ogni foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il metodo setZoom della classe Worksheet.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Fattore di Zoom**
Apache POI fornisce il metodo Sheet.setZoom() per fornire la funzione di zoom.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)

---
title: Zoom Factor utilizzando Apache POI e Aspose.Cells
type: docs
weight: 70
url: /it/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Fattore di ingrandimento**
Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare lo zoom o il fattore di ridimensionamento di un foglio di lavoro. Questa funzione aiuta gli utenti a vedere i contenuti del foglio di lavoro in viste più piccole o più grandi.

Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare il metodo setZoom della classe Worksheet.

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Fattore di zoom**
Apache POI fornisce la funzione di zoom dell'avail del metodo Sheet.setZoom().

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)

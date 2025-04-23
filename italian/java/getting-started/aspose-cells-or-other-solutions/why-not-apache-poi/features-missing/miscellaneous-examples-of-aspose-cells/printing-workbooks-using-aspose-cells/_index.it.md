---
title: Stampare Cartelle di Lavoro utilizzando Aspose.Cells
type: docs
weight: 20
url: /it/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - Stampa dei workbook**
Dopo aver terminato la creazione del foglio di lavoro, probabilmente vorrai stampare una copia cartacea del foglio per le tue esigenze. Durante la stampa, MS Excel presume che si voglia stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione.

Stampa del foglio di lavoro

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

Stampare Cartella di Lavoro

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Per maggiori dettagli, visita [Stampa dei Quaderni](/cells/it/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

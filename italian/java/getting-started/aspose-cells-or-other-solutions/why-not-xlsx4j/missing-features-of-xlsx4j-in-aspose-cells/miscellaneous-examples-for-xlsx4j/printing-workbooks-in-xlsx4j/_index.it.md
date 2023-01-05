---
title: Stampa di cartelle di lavoro in xlsx4j
type: docs
weight: 30
url: /it/java/printing-workbooks-in-xlsx4j/
---
## **Aspose.Cells - Stampa Quaderni**
Dopo aver finito di creare il tuo foglio di calcolo, probabilmente vorrai stampare una copia cartacea del foglio per le tue necessità. Quando si stampa, MS Excel presuppone che si desideri stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione.

**Foglio di lavoro per la stampa**

**Java**

{{< highlight "java" >}}

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

**Cartella di lavoro di stampa**

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[ Stampa di cartelle di lavoro](/cells/it/java/printing-workbooks).

{{% /alert %}}

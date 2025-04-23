---
title: Stampa dei fogli di lavoro in xlsx4j
type: docs
weight: 30
url: /it/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Stampa dei workbook**
Dopo aver terminato la creazione del foglio di lavoro, probabilmente vorrai stampare una copia cartacea del foglio per le tue esigenze. Durante la stampa, MS Excel presume che si voglia stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione.

**Stampa del foglio di lavoro**

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

**Stampa della cartellina di lavoro**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Stampa dei fogli di lavoro](/cells/it/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

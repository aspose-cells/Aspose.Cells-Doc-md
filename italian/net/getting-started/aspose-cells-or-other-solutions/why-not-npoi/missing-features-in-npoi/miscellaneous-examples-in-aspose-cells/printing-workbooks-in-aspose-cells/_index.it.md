---
title: Stampa di cartelle di lavoro in Aspose.Cells
type: docs
weight: 20
url: /it/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - Stampa Quaderni**
Dopo aver finito di creare il tuo foglio di calcolo, probabilmente vorrai stampare una copia cartacea del foglio per le tue necessità. Quando si stampa, MS Excel presuppone che si desideri stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione.

Foglio di lavoro per la stampa

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Stampa di cartelle di lavoro** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Stampa di cartelle di lavoro](/cells/it/net/printing-workbooks/).

{{% /alert %}}

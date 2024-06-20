---
title: Stampa i workbook in Aspose.Cells
type: docs
weight: 20
url: /it/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Stampa dei workbook**
Dopo aver terminato la creazione del foglio di lavoro, probabilmente vorrai stampare una copia cartacea del foglio per le tue esigenze. Durante la stampa, MS Excel presume che si voglia stampare l'intera area del foglio di lavoro a meno che non si specifichi la selezione.

Stampa del foglio di lavoro

**C#**

{{< highlight cs >}}

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
Scarica **Stampa dei workbook** da uno qualsiasi dei seguenti siti di codice sociale:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Stampa dei workbook](/cells/it/net/printing-workbooks/)

{{% /alert %}}

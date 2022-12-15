---
title: Calcola sub totali
type: docs
weight: 10
url: /it/net/calculate-sub-totals/
---
## **Aspose.Cells - Calcola sub totali**
Puoi creare automaticamente subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells fornisce funzionalità API che consentono di aggiungere subtotali ai fogli di calcolo in modo programmatico.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[]{ 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Calcola sub totali** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Creazione di subtotali](/cells/it/net/creating-subtotals/).

{{% /alert %}}

---
title: Trova valore in Cells
type: docs
weight: 20
url: /it/net/find-value-in-cells/
---
## **Aspose.Cells - Trova valore in Cells**
In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic**Modificare**poi**Trova**apre la finestra di dialogo Cerca. Gli utenti immettono un valore e fanno clic**OK**per cercarlo. Excel evidenzia i campi corrispondenti.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Trova valore in Cells** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Trova o cerca dati](/cells/it/net/find-or-search-data/).

{{% /alert %}}

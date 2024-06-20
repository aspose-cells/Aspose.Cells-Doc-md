---
title: Trova il valore nelle celle
type: docs
weight: 20
url: /it/net/find-value-in-cells/
---

## **Aspose.Cells - Trova il valore nelle celle**
In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic su **Modifica** e quindi su **Trova** si apre il dialogo di ricerca. Gli utenti inseriscono un valore e fanno clic su **OK** per cercarlo. Excel evidenzia i campi corrispondenti.

**C#**

{{< highlight cs >}}

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
Scarica **Trova il valore nelle celle** da uno qualsiasi dei seguenti siti di codice sociale:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Trova o ricerca dati](/cells/it/net/find-or-search-data/).

{{% /alert %}}

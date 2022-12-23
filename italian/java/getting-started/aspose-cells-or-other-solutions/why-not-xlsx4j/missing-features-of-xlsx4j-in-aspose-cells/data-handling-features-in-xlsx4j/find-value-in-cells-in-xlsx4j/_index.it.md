---
title: Trova valore in Cells in xlsx4j
type: docs
weight: 30
url: /it/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - Trova valore in Cells**
In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic**Modificare**e poi**Trova**apre la finestra di dialogo Cerca. Gli utenti immettono un valore e fanno clic**OK**per cercarlo. Excel evidenzia i campi corrispondenti.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Trova o cerca dati](/cells/it/java/find-or-search-data).

{{% /alert %}}

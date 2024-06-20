---
title: Trova il Valore nelle Celle in xlsx4j
type: docs
weight: 30
url: /it/java/find-value-in-cells-in-xlsx4j/
---

## **Aspose.Cells - Trova il valore nelle celle**
In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic su **Modifica** e quindi su **Trova** si apre il dialogo di ricerca. Gli utenti inseriscono un valore e fanno clic su **OK** per cercarlo. Excel evidenzia i campi corrispondenti.

**Java**

{{< highlight java >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Trova o Cerca Dati](/cells/it/java/find-or-search-data).

{{% /alert %}}

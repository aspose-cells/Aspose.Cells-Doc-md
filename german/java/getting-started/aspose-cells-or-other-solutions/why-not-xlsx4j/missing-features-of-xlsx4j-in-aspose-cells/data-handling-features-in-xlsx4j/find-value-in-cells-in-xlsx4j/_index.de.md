---
title: Wert in Zellen in xlsx4j finden
type: docs
weight: 30
url: /de/java/find-value-in-cells-in-xlsx4j/
---

## **Aspose.Cells - Wert in Zellen finden**
In Microsoft Excel können Benutzer nach Zellen suchen, die bestimmte Daten enthalten. Beispielsweise öffnet das Klicken auf **Bearbeiten** und dann auf **Suchen** den Suchdialog. Benutzer geben einen Wert ein und klicken auf **OK**, um danach zu suchen. Excel markiert übereinstimmende Felder.

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

Für weitere Details, besuchen Sie [Daten suchen](/cells/de/java/find-or-search-data).

{{% /alert %}}

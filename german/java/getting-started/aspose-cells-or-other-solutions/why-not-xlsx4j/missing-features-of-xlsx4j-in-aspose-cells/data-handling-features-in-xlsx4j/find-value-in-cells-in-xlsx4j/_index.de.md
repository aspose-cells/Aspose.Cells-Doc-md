---
title: Finden Sie den Wert in Cells in xlsx4j
type: docs
weight: 30
url: /de/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - Wert finden in Cells**
In Microsoft Excel können Benutzer nach Zellen suchen, die bestimmte Daten enthalten. Klicken zum Beispiel**Bearbeiten**und dann**Finden**öffnet den Suchdialog. Der Benutzer gibt einen Wert ein und klickt**OK**danach zu suchen. Excel hebt übereinstimmende Felder hervor.

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Daten finden oder suchen](/cells/de/java/find-or-search-data).

{{% /alert %}}

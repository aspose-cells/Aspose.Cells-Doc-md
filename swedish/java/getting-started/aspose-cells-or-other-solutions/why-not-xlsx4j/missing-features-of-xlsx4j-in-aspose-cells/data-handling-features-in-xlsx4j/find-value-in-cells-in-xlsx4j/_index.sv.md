---
title: Hitta värde i Cells i xlsx4j
type: docs
weight: 30
url: /sv/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - Hitta värde i Cells**
I Microsoft Excel kan användare söka efter celler som innehåller specifika data. Till exempel att klicka**Redigera**och då**Hitta**öppnar dialogrutan Sök. Användare anger ett värde och klickar**OK**att söka efter det. Excel markerar matchande fält.

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 För mer information, besök[Hitta eller sök data](/cells/sv/java/find-or-search-data).

{{% /alert %}}

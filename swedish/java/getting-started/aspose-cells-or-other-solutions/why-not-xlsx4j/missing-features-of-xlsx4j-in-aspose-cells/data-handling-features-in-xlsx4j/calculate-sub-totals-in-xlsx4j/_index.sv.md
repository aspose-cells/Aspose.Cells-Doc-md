---
title: Beräkna delsummor i xlsx4j
type: docs
weight: 10
url: /sv/java/calculate-sub-totals-in-xlsx4j/
---

## **Aspose.Cells - Beräkna delsummor**
Du kan automatiskt skapa delsummer för vilka återkommande värden som helst i en kalkyl. Aspose.Cells tillhandahåller API-funktioner som hjälper dig att lägga till delsummer till kalkylblad programmatiskt.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook workbook = new Workbook("book1.xls");

//Get the Cells collection in the first worksheet

Cells cells = workbook.getWorksheets().get(0).getCells();

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn =1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.subtotal(ca, 0, ConsolidationFunction.SUM, new int[] { 1 });

//Save the excel file

workbook.save(dataDir + "AsposeTotal.xls");

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/calculatesubtotals/AsposeCalculateSubTotals.java)

{{% alert color="primary" %}} 

För mer detaljer, besök [Skapa delsummering](/cells/sv/java/skapa-delsummering).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: Beräkna delsummor
type: docs
weight: 10
url: /sv/net/calculate-sub-totals/
---
## **Aspose.Cells - Beräkna delsummor**
Du kan automatiskt skapa delsummor för alla återkommande värden i ett kalkylblad. Aspose.Cells tillhandahåller API-funktioner som hjälper dig att lägga till delsummor till kalkylark programmatiskt.

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
## **Ladda ner Running Code**
 Ladda ner**Beräkna delsummor** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Skapa delsummor](/cells/sv/net/creating-subtotals/).

{{% /alert %}}

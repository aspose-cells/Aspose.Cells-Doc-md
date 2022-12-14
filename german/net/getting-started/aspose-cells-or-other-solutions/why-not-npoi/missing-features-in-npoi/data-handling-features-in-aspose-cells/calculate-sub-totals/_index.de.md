---
title: Zwischensummen berechnen
type: docs
weight: 10
url: /de/net/calculate-sub-totals/
---
## **Aspose.Cells - Zwischensummen berechnen**
Sie können automatisch Zwischensummen für sich wiederholende Werte in einer Tabelle erstellen. Aspose.Cells bietet API-Funktionen, mit denen Sie programmgesteuert Zwischensummen zu Tabellenkalkulationen hinzufügen können.

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
## **Laufcode herunterladen**
 Download**Zwischensummen berechnen** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Erstellen von Zwischensummen](/cells/de/net/creating-subtotals/).

{{% /alert %}}

---
title: Berechnen Sie die Teilsummen
type: docs
weight: 10
url: /de/net/calculate-sub-totals/
---

## **Aspose.Cells - Teilsummenberechnung**
Sie können automatisch Teilergebnisse für beliebige wiederholende Werte in einem Tabellenblatt erstellen. Aspose.Cells bietet API-Funktionen, die Ihnen helfen, Teilergebnisse programmgesteuert zu Tabellenblättern hinzuzufügen.

**C#**

{{< highlight cs >}}

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

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Berechnen von Teilsummen** von einer der unten aufgeführten sozialen Code-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Erstellen von Teilsummen](/cells/de/net/creating-subtotals/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

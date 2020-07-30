---
title : "Calculate Sub Totals" 
description : "" 
weight : 20941 
toc : false
type: docs
url: /net/plugins/npoi/missingfeaturesinnpoi/datahandling/calculate+sub+totals/
---

# Aspose.Cells for .NET : Calculate Sub Totals


## Aspose.Cells - Calculate Sub Totals

You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.

**C#**

{{< code lang="c#" >}}
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
{{< /code >}}

## Download Running Code

Download **Calculate Sub Totals** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1482187)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

For more details, visit [Creating Subtotals](http://www.aspose.com/docs/display/cellsnet/Creating+Subtotals).


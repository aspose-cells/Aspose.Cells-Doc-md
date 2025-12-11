---
title: Calculate Sub Totals
type: docs
weight: 10
url: /net/calculate-sub-totals/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Calculate Sub Totals**
You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

// Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

// Create a cell area, i.e., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

// Apply subtotal; the consolidation function is Sum and it will be applied to

// the second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

// Save the Excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Download Running Code**
Download **Calculate Sub Totals** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

For more details, visit [Creating Subtotals](/cells/net/creating-subtotals/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

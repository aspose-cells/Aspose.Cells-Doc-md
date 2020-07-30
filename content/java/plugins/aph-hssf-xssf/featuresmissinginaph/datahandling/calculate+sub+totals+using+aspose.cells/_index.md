---
title : "Calculate Sub Totals using Aspose.Cells" 
description : "" 
weight : 20629 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/datahandling/calculate+sub+totals+using+aspose.cells/
---

# Aspose.Cells for Java : Calculate Sub Totals using Aspose.Cells


## Aspose.Cells - Calculate Sub Totals

You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.

**Java**

{{< code lang="java" >}}
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
workbook.save("AsposeTotal.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)

For more details, visit [Creating Subtotals](http://docs.aspose.com:8082/docs/display/cellsjava/Creating+Subtotals).


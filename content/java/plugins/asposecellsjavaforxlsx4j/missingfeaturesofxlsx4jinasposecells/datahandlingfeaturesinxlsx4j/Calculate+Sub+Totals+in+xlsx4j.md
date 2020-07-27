+++
title = "Calculate Sub Totals in xlsx4j" 
description = "" 
weight = 20664 
+++

Aspose.Cells for Java : Calculate Sub Totals in xlsx4j  

# Aspose.Cells for Java : Calculate Sub Totals in xlsx4j


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
workbook.save(dataDir + "AsposeTotal.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/calculatesubtotals/AsposeCalculateSubTotals.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/calculatesubtotals/AsposeCalculateSubTotals.java)

For more details, visit [Creating Subtotals](http://docs.aspose.com:8082/docs/display/cellsjava/Creating+Subtotals).


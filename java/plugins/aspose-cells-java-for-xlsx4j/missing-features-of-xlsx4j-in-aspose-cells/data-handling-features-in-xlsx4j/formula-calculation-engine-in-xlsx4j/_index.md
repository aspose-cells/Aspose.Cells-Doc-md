---
title: Formula Calculation Engine in xlsx4j
type: docs
weight: 40
url: /java/formula-calculation-engine-in-xlsx4j/
---

## **Aspose.Cells - Formula Calculation Engine**
The formula calculation engine is embedded in Aspose.Cells. It can not only re-calculate the formula imported from a designer spreadsheet file but also supports to calculate the results of formulas added at runtime.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.getWorksheets().add();

Worksheet worksheet = book.getWorksheets().get(sheetIndex);

Cells cells = worksheet.getCells();

Cell cell = null;

//Adding a value to "A1" cell

cell = cells.get("A1");

cell.setValue(1);

//Adding a value to "A2" cell

cell = cells.get("A2");

cell.setValue(2);

//Adding a value to "A3" cell

cell = cells.get("A3");

cell.setValue(3);

//Adding a SUM formula to "A4" cell

cell = cells.get("A4");

cell.setFormula("=SUM(A1:A3)");

//Calculating the results of formulas

book.calculateFormula();

//Saving the Excel file

book.save(dataDir + "AsposeFormulaEngine.xls");

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/formulacalculationengine/AsposeFormulaCalculationEngine.java)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/formulacalculationengine/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

For more details, visit [Formula Calculation Engine](http://docs.aspose.com:8082/docs/display/cellsjava/Formula+Calculation+Engine).

{{% /alert %}}

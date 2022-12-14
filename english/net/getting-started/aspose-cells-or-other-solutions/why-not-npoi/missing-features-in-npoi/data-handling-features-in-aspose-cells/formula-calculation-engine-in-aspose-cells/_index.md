---
title: Formula Calculation Engine in Aspose.Cells
type: docs
weight: 30
url: /net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Formula Calculation Engine**
The formula calculation engine is embedded in Aspose.Cells. It can not only re-calculate the formula imported from a designer spreadsheet file but also supports to calculate the results of formulas added at runtime.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.Worksheets.Add();

Worksheet worksheet = book.Worksheets[sheetIndex];

Cells cells = worksheet.Cells;

Cell cell = null;

//Adding a value to "A1" cell

cell = cells["A1"];

cell.Value = 1;

//Adding a value to "A2" cell

cell = cells["A2"];

cell.Value = 2;

//Adding a value to "A3" cell

cell = cells["A3"];

cell.Value = 3;

//Adding a SUM formula to "A4" cell

cell = cells["A4"];

cell.Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

book.CalculateFormula();

//Saving the Excel file

book.Save("AsposeFormulaEngine.xls");

{{< /highlight >}}
## **Download Running Code**
Download **Formula Calculation Engine** form any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

For more details, visit [Formula Calculation Engine](/cells/net/formula-calculation-engine/).

{{% /alert %}}

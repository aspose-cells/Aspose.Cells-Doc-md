---
title: Formelberäkningsmotor i Aspose.Cells
type: docs
weight: 30
url: /sv/net/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Formelberäkningsmotor**
Formelberäkningsmotorn är inbäddad i Aspose.Cells. Den kan inte bara räkna om formeln som importerats från en designerkalkylarksfil utan stöder även beräkning av resultaten av formler som läggs till under körning.

**C#**

{{< highlight "cs" >}}

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
## **Ladda ner Running Code**
 Ladda ner**Formelberäkningsmotor** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Formelberäkningsmotor](/cells/sv/net/formula-calculation-engine/).

{{% /alert %}}

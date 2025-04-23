---
title: Motore di calcolo delle formule in Aspose.Cells
type: docs
weight: 30
url: /it/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Motore di calcolo delle formule**
Il motore di calcolo delle formule è incorporato in Aspose.Cells. Può non solo ricalcolare la formula importata da un file di foglio di lavoro del progettista ma supporta anche il calcolo dei risultati delle formule aggiunte durante l'esecuzione.

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
## **Scarica il codice in esecuzione**
Scarica **Motore di calcolo delle formule** da uno qualsiasi dei seguenti siti di codice sociale:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Motore di calcolo delle formule](/cells/it/net/formula-calculation-engine/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

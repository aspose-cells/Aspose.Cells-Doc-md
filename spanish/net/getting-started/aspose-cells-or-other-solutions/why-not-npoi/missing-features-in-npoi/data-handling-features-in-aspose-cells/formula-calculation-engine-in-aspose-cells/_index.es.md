---
title: Motor de cálculo de fórmulas en Aspose.Cells
type: docs
weight: 30
url: /es/net/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Motor de cálculo de fórmulas**
El motor de cálculo de fórmulas está integrado en Aspose.Cells. No solo puede volver a calcular la fórmula importada desde un archivo de hoja de cálculo del diseñador, sino que también permite calcular los resultados de las fórmulas agregadas en tiempo de ejecución.

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
## **Descargar código de ejecución**
 Descargar**Motor de cálculo de fórmulas** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Motor de cálculo de fórmulas](/cells/es/net/formula-calculation-engine/).

{{% /alert %}}

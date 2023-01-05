---
title: Formelberechnungsmodul in Aspose.Cells
type: docs
weight: 30
url: /de/net/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Formelberechnungsmodul**
Die Formelberechnungs-Engine ist in Aspose.Cells eingebettet. Sie kann nicht nur die aus einer Designer-Tabellendatei importierte Formel neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.

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
## **Laufcode herunterladen**
 Download**Formel-Berechnungs-Engine** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Formel-Berechnungs-Engine](/cells/de/net/formula-calculation-engine/).

{{% /alert %}}

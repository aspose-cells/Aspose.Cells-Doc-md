---
title: Moteur de calcul de formules dans Aspose.Cells
type: docs
weight: 30
url: /fr/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Moteur de calcul de formules**
Le moteur de calcul de formules est intégré dans Aspose.Cells. Il peut non seulement recalculer la formule importée à partir d'un fichier de feuille de calcul conçu, mais prend également en charge le calcul des résultats des formules ajoutées à l'exécution.

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Moteur de calcul de formules** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Moteur de calcul de formules](/cells/fr/net/formula-calculation-engine/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

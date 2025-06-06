---
title: Moteur de calcul de formules dans Aspose.Cells
type: docs
weight: 50
url: /fr/java/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Moteur de calcul de formules**
Le moteur de calcul de formules est intégré dans Aspose.Cells. Il peut non seulement recalculer la formule importée à partir d'un fichier de feuille de calcul conçu, mais prend également en charge le calcul des résultats des formules ajoutées à l'exécution.

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
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Moteur de calcul de formules](/cells/fr/java/aspose-cells-formula-calculation-engine).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

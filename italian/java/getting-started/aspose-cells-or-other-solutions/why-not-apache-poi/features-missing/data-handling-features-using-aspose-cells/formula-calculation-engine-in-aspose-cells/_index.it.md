---
title: Motore di calcolo delle formule in Aspose.Cells
type: docs
weight: 50
url: /it/java/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Motore di calcolo delle formule**
Il motore di calcolo delle formule è incorporato in Aspose.Cells. Non solo può ricalcolare la formula importata da un file di foglio di calcolo del designer, ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.

**Giava**

{{< highlight "java" >}}

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
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Motore di calcolo delle formule](/cells/it/java/aspose-cells-formula-calculation-engine).

{{% /alert %}}

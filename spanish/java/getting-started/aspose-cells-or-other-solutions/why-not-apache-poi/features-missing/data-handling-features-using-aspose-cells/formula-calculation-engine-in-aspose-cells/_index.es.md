---
title: Motor de cálculo de fórmulas en Aspose.Cells
type: docs
weight: 50
url: /es/java/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Motor de cálculo de fórmulas**
El motor de cálculo de fórmulas está integrado en Aspose.Cells. No solo puede volver a calcular la fórmula importada desde un archivo de hoja de cálculo del diseñador, sino que también permite calcular los resultados de las fórmulas agregadas en tiempo de ejecución.

**Java**

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
## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Motor de cálculo de fórmulas](/cells/es/java/aspose-cells-formula-calculation-engine).

{{% /alert %}}

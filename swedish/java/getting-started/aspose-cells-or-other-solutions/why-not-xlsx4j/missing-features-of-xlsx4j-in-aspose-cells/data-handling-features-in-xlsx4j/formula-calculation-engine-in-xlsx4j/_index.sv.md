---
title: Formelberäkningsmotor i xlsx4j
type: docs
weight: 40
url: /sv/java/formula-calculation-engine-in-xlsx4j/
---

## **Aspose.Cells - Formelberäkningsmotorn**
Formelberäkningsmotorn är inbäddad i Aspose.Cells. Den kan inte bara omberäkna formeln som importerats från en designerkalkylbladsfil utan också stödjer att beräkna resultatet av formler som läggs till vid körning.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/formulacalculationengine/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

För mer detaljer, besök [Formelberäkningsmotor](/cells/sv/java/formelberakningsmotor-i-aspose-cells).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

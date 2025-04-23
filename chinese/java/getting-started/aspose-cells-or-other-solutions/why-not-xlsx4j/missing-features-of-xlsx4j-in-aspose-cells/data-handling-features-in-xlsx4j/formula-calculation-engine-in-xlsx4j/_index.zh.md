---
title: 在xlsx4j中的公式计算引擎
type: docs
weight: 40
url: /zh/java/formula-calculation-engine-in-xlsx4j/
---

## **Aspose.Cells - 公式计算引擎**
公式计算引擎嵌入在Aspose.Cells中。它不仅可以重新计算从设计者电子表格文件导入的公式，还支持计算运行时添加的公式结果。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/formulacalculationengine/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

更多详情，请访问[公式计算引擎](/cells/zh/java/formula-calculation-engine-in-aspose-cells)。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: Aspose.Cells中的公式计算引擎
type: docs
weight: 30
url: /zh/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - 公式计算引擎**
公式计算引擎嵌入在 Aspose.Cells 中。它不仅可以重新计算从设计师电子表格文件中导入的公式，还支持计算在运行时添加的公式的结果。

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
## **下载运行代码**
从以下任何社交编码网站下载**公式计算引擎**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关详细信息，请访问[公式计算引擎](/cells/zh/net/formula-calculation-engine/)

{{% /alert %}}

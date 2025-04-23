---
title: 通过Node.js用C++追踪前置单元格和依赖单元格
linktitle: 先例和从属
type: docs
weight: 230
url: /zh/nodejs-cpp/precedents-and-dependents/
description: 学习如何在电子表格中追踪前置和依赖单元格，使用代码Aspose.Cells for Node.js via C++。了解如何识别复杂财务工作表中的关联单元格。
---

{{% alert color="primary" %}} 

复杂的财务工作表，尤其是合作开发的工作表，可能隐藏最令人尴尬的错误。当公式使用先例单元格和从属单元格时，检查公式的准确性并找到错误的来源可能很困难。

{{% /alert %}} 
## **介绍**
- **前代单元格** 是由另一个单元格的公式引用的单元格。例如，如果单元格D10包含公式=B5，则单元格B5是单元格D10的前代。
- **依赖单元格**包含引用其他单元格的公式。例如，若单元格D10包含公式 =B5，D10依赖于B5单元格。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格中用于公式的单元格。同样，您可能需要提取其他单元格的依赖单元格。

Aspose.Cells 允许您跟踪单元格并找出哪些是相互关联的。
## **跟踪先例和依赖单元格：Microsoft Excel**
公式可能会根据客户做出的修改而改变。例如，如果单元格 C1 依赖于包含公式的 C3 和 C4，并且更改了 C1（使公式被覆盖），则根据业务规则需要更改 C3 和 C4，或其他单元格，以使电子表格保持平衡。

类似地，假设 C1 包含公式"=(B1*22)/(M2*N32)"。我想找到 C1 依赖的单元格，即先例单元格 B1、M2 和 N32。

您可能需要跟踪特定单元格到其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系，并根据此执行一些规则。同样，如果特定单元格的值被修改，那么工作表中哪些单元格受到此变化的影响？

Microsoft Excel 允许用户跟踪先例和依赖。

1. 在**查看工具栏**上选择**公式审计**。将显示公式审计对话框。
1. 跟踪先例：
   1. 选择包含您想要查找先例单元格的公式的单元格。
   1. 要向每个直接提供数据给活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪先例**。
1. 跟踪引用特定单元格的公式（依赖项）
   1. 选择要识别其依赖单元格的单元格。
   1. 若要在依赖于活动单元格的每个单元格上显示追踪箭头，请点击公式审计工具栏上的**追踪依赖项**。
## **跟踪先例和依赖单元格：Aspose.Cells**
### **跟踪先例**
Aspose.Cells 使得获取先例单元格变得容易。它不仅可以检索为简单公式先例提供数据的单元格，还可以找到为具有命名范围的复杂公式先例提供数据的单元格。

在下面的示例中，使用了模板Excel文件《Book1.xls》。电子表格在第一个工作表上包含数据和公式。

Aspose.Cells 提供 [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的 [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) 方法，用于追踪单元格的前置项。它返回一个引用区域的集合。如上所示，在 Book1.xls 中，单元格 B7 包含公式 "=SUM(A1:A3)"，因此 A1:A3 是单元格 B7 的前置单元格。以下示例展示了使用模板文件 Book1.xls 进行追踪前置项的功能。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **跟踪依赖项**
Aspose.Cells 让你能够获取电子表格中的依赖单元格。Aspose.Cells 不仅可以检索提供简单公式数据的单元格，还能找到为复杂公式依赖项提供数据的带有命名范围的单元格。

Aspose.Cells 提供 [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的 [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) 方法，用于追踪单元格的依赖项。例如，在 Book1.xlsx 中，B2 和 C2 单元格中分别包含公式 "=A1+20" 和 "=A1+30"。以下示例演示了如何使用模板文件 Book1.xlsx 追踪 A1 单元格的依赖项。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **根据计算链跟踪先行单元格和依赖单元格**
上述追踪前置项和依赖项的 API 是根据公式表达式本身设计的。它们仅为用户提供追踪少数公式间相互依赖的方便方式。如果工作簿中有大量公式，用户需要追踪每个单元格的前置项和依赖项，性能将会变差。对于这种情况，用户应考虑使用 [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) 和 [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) 方法。这两个方法根据计算链追踪依赖关系。使用前，首先需要通过 [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--) 方法启用计算链，然后对工作簿执行全量计算 [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。之后，就可以为所有这些单元格追踪前置项或依赖项。

某些公式的前置项可能在 getPrecedents 和 getPrecedentsInCalculation 中不同，依赖项在 getDependents 和 getDependentsInCalculation 中也可能不同。例如，如果单元格 A1 的公式是 "=IF(TRUE,B2,C3)"，则 getPrecedents 会将 B2 和 C3 作为 A1 的前置项。而在检查依赖项时，B2 和 C3 都会显示有依赖 A1。然而在这个公式的计算中，显然只有 B2 会影响结果，因此 getPrecedentsInCalculation 不会为 A1 提供 C3，而 getDependentsInCalculation 不会为 C3 提供 A1。有时候，用户只需要追踪实际上会影响公式计算结果的相互依赖关系，基于当前工作簿数据，此时应使用 getDependentsInCalculation 和 getPrecedentsInCalculation，而非 getDependents 和 getPrecedents。

以下示例演示如何根据计算链追踪单元格的前置项和依赖项：


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```

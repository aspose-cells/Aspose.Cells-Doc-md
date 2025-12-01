---
title: Precedents and Dependents with Node.js via C++
linktitle: Precedents and Dependents
type: docs
weight: 230
url: /nodejs-cpp/precedents-and-dependents/
description: Learn to trace precedent and dependent cells in spreadsheets using Aspose.Cells for Node.js via C++. Understand how to identify linked cells in complex financial worksheets.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

{{% /alert %}} 
## **Introduction**
- **Precedent cells** are cells that are referred to by a formula in another Cell. For example, if cell D10 contains the formula =B5, cell B5 is a precedent to cell D10.
- **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula =B5, cell D10 is dependent on cell B5.

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.
## **Tracing Precedent and Dependent Cells: Microsoft Excel**
Formulas may change based on modifications made by a client. For example, if cell C1 is dependent on C3 and C4 containing a formula, and C1 is changed (so the formula is overridden), C3 and C4, or other cells, need to change to balance the spreadsheet based on business rules.

Similarly, suppose C1 contains the formula "=(B1*22)/(M2*N32)". I want to find the cells that C1 depends on, that is the precedent cells B1, M2, and N32.

You might need to trace the dependency of a particular cell to other cells. If business rules are embedded in formulas, we would like to find out the dependency and execute some rules based on it. Similarly, if the value of a particular cell is modified, which cells in the worksheet are impacted by that change?

Microsoft Excel allows users to trace precedents and dependents.

1. On the **View Toolbar**, select **Formula Auditing**. The Formula Auditing dialog will be displayed.
1. Trace Precedents:
   1. Select the cell that contains the formula for which you want to find precedent cells.
   1. To display a tracer arrow to each cell that directly provides data to the active cell, click **Trace Precedents** on the **Formula Auditing** toolbar.
1. Trace formulas that reference a particular cell (dependents)
   1. Select the cell for which you want to identify the dependent cells.
   1. To display a tracer arrow to each cell that is dependent on the active cell, click **Trace Dependents** on the Formula Auditing toolbar.
## **Tracing Precedent and Dependent Cells: Aspose.Cells**
### **Tracing Precedents**
Aspose.Cells makes it easy to get precedent cells. Not only can it retrieve cells that provide data to simple formula precedents but also find cells that provide data to complex formula precedents with named ranges.

In the example below, a template excel file, Book1.xls, is used. The spreadsheet has data and formulas on the first Worksheet.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) method used to trace a cell's precedents. It returns a collection of referred areas. As you can see above, in Book1.xls, cell B7 contains a formula "=SUM(A1:A3)". So cells A1:A3 are the precedent cells to cell B7. The following example demonstrates the tracing precedents feature using the template file Book1.xls.


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
### **Tracing Dependents**
Aspose.Cells lets you get dependent cells in spreadsheets. Aspose.Cells not only can retrieve cells that provide data regarding a simple formula but also find cells that provide data to complex formula dependents with named ranges.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) method used to trace a cell's dependents. For example, in Book1.xlsx there are formulas: "=A1+20" and "=A1+30" in the B2 and C2 cells respectively. The following example demonstrates how to trace the dependents for the A1 cell using the template file Book1.xlsx.


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
### **Tracing Precedent and Dependent cells according to calculation chain**
The above APIs of tracing precedents and dependents are according to the formula expression itself. They simply provide a convenient way for users to trace interdependencies for a few formulas. If there are a large number of formulas in the workbook and the user needs to trace precedents and dependents for every cell, they will give poor performance. For such a situation, the user should consider using [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) and [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) methods. These two methods trace dependencies according to the calculation chain. So, to use them, firstly you need to enable the calculation chain by [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). Then you should perform full calculation for the Workbook by [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). After that, you can trace precedents or dependents for all those cells you need.

For some formulas, the resultant precedents may be different for getPrecedents and getPrecedentsInCalculation, and the resultant dependents may be different for getDependents and getDependentsInCalculation. For example, if cell A1's formula is "=IF(TRUE,B2,C3)", getPrecedents will provide B2 and C3 as A1's precedent. Accordingly, B2 and C3 both have the dependent A1 when checking by getDependents. However, for the calculation of this formula, it is obvious that only B2 can affect the calculated result. So getPrecedentsInCalculation will not provide C3 for A1, and getDependentsInCalculation will not provide A1 for C3. Sometimes users may just have the requirement of tracing those interdependencies that actually affect the calculated result of formulas based on the current data of the Workbook, then they also need to use getDependentsInCalculation/getPrecedentsInCalculation instead of getDependents/getPrecedents.

The following example demonstrates how to trace the precedents and dependents according to the calculation chain for cells:


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
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal with Node.js via C++
linktitle: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Learn how to implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal using Aspose.Cells for Node.js via C++. 
---

## **Possible Usage Scenarios**

Microsoft Excel Formulas may have different names in different locales or regions or languages. For example, **SUM** function is called **SUMME** in German. Aspose.Cells cannot work with non-English function names. In Microsoft Excel VBA, there is **Range.FormulaLocal** property that returns the name of the function as per its language or region. Aspose.Cells for Node.js via C++ also provides [**Cell.FormulaLocal**](https://reference.aspose.com/cells/nodejs-cpp/cell/#formulalocal) property for this purpose. However, this property will only work when you implement [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) method.

## **Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal**

The following sample code explains how to implement [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) method. The method returns the local name of the standard function. If the standard function name is **SUM**, it returns **UserFormulaLocal_SUM**. You can change the code as per your needs and return the correct local function names e.g. **SUM** is **SUMME** in German and **TEXT** is **ТЕКСТ** in Russian. Please also see the console output of the sample code given below for reference.

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");

class GS extends AsposeCells.GlobalizationSettings {
getLocalFunctionName(standardName) {
// Change the SUM function name as per your needs.
if (standardName === "SUM") {
return "UserFormulaLocal_SUM";
}

// Change the AVERAGE function name as per your needs.
if (standardName === "AVERAGE") {
return "UserFormulaLocal_AVERAGE";
}

return "";
}
}

function run() {
// Create workbook
const wb = new AsposeCells.Workbook();

// Assign GlobalizationSettings implementation class
wb.getSettings().setGlobalizationSettings(new GS());

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access some cell
const cell = ws.getCells().get("C4");

// Assign SUM formula and print its FormulaLocal
cell.setFormula("SUM(A1:A2)");
console.log("Formula Local: " + cell.getFormulaLocal());

// Assign AVERAGE formula and print its FormulaLocal
cell.setFormula("=AVERAGE(B1:B2, B5)");
console.log("Formula Local: " + cell.getFormulaLocal());
}

// Call the run function
run();
```

## **Console Output**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}

---
title: 实现类似 Excel VBA Range.FormulaLocal 的 Cell.FormulaLocal，通过 Node.js 及 C++
linktitle: 实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal
type: docs
weight: 30
url: /zh/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: 学习如何用 Aspose.Cells for Node.js via C++ 实现类似 Excel VBA Range.FormulaLocal 的 Cell.FormulaLocal。 
---

## **可能的使用场景**

 Microsoft Excel 公式在不同地区或语言中可能有不同的名称。例如，**SUM** 函数在德语中叫做 **SUMME**。Aspose.Cells 不能处理非英语的函数名称。在 Microsoft Excel VBA 中，有 **Range.FormulaLocal** 属性根据语言或地区返回函数的名称。Aspose.Cells for Node.js via C++ 也提供此目的的 [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) 属性，但只有在实现 [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) 方法时才会工作。

## **实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal**

 以下示例代码说明如何实现 [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) 方法。该方法返回标准函数的本地名称。如果标准函数名为 **SUM** ，它返回 **UserFormulaLocal_SUM**。你可以根据自己的需要修改代码，并返回正确的本地函数名，例如在德语中 **SUM** 为 **SUMME**，俄语中 **TEXT** 为 **ТЕКСТ**。请同时参考下面的示例代码输出。

## **示例代码**

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

## **控制台输出**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}

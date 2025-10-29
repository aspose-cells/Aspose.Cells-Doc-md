---
title: Реализуйте Cell.FormulaLocal, аналогично Range.FormulaLocal в Excel VBA, с помощью Node.js через C++
linktitle: Реализуйте свойство Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ru/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Узнайте, как реализовать Cell.FormulaLocal, подобно Range.FormulaLocal в Excel VBA, используя Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

 Формулы Microsoft Excel могут иметь разные имена в разных локализациях, регионах или языках. Например, функция **SUM** называется **SUMME** на немецком языке. Aspose.Cells не поддерживает работу с функциями на неанглийских языках. В Microsoft Excel VBA есть свойство **Range.FormulaLocal**, которое возвращает название функции согласно ее языке или региону. Aspose.Cells for Node.js via C++ также предоставляет свойство [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) для этой цели. Однако это свойство работает только при реализации метода [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-).

## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**

Следующий пример объясняет, как реализовать метод [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-). Метод возвращает локальное имя стандартной функции. Если имя функции **SUM**, он возвращает **UserFormulaLocal_SUM**. Вы можете изменить код по своему усмотрению и возвращать правильные локальные имена функций, например, **SUM** — это **SUMME** на немецком, а **TEXT** — это **ТЕКСТ** на русском. Также обратитесь к выводу консоли приведенного ниже образца кода для справки.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

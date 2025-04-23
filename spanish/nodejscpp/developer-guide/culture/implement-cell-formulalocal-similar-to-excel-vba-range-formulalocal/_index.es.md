---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal con Node.js a través de C++
linktitle: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /es/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aprende cómo implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Las fórmulas de Microsoft Excel pueden tener diferentes nombres en diferentes regiones o idiomas. Por ejemplo, la función **SUM** se llama **SUMME** en alemán. Aspose.Cells no puede trabajar con nombres de funciones que no estén en inglés. En Microsoft Excel VBA, existe la propiedad **Range.FormulaLocal** que devuelve el nombre de la función en su idioma o región. Aspose.Cells for Node.js via C++ también proporciona la propiedad [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implementes el método [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-).

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

El siguiente ejemplo de código explica cómo implementar el método [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es **SUM**, devuelve **UserFormulaLocal_SUM**. Puedes modificar el código según tus necesidades y devolver los nombres correctos de las funciones locales, por ejemplo, **SUM** es **SUMME** en alemán y **TEXT** es **ТЕКСТ** en ruso. También ve la salida en consola del ejemplo de código a continuación como referencia.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}

---
title: Returnering av ett intervall av värden med AbstractCalculationEngine med Node.js via C++
linktitle: Returnera ett område av värden med hjälp av AbstractCalculationEngine
description: Denna artikel introducerar en abstrakt beräkningsmotor som returnerar ett intervall av värden i Excel med Aspose.Cells för Node.js via C++. Lär dig att ladda eller skapa en Excel fil och spara den modifierade filen till disk.
keywords: Aspose.Cells, Excel, abstrakt beräkningsmotor som returnerar värden Node.js via C++, anpassade funktioner
type: docs
weight: 55
url: /sv/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) klass som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

Den här artikeln kommer att förklara hur man returnerar en serie värden från [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

Följande kod visar användningen av [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) klassen och returnerar värdeintervallet via dess metod.

Skapa en klass med en funktion *calculateCustomFunction*. Denna klass implementerar [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

Använd nu ovanstående funktion i ditt program

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}

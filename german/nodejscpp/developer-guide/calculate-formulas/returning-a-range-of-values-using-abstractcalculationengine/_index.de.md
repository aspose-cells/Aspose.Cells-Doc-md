---
title: Rückgabe eines Wertebereichs mit AbstractCalculationEngine, verwendet in Node.js über C++
linktitle: Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors
description: Dieser Artikel stellt eine abstrakte Berechnungs Engine vor, die in Excel einen Wertebereich mit der Aspose.Cells Bibliothek für Node.js über C++ zurückgibt. Lernen Sie, eine Excel Datei zu laden oder zu erstellen und die modifizierte Datei auf Festplatte zu speichern.
keywords: Aspose.Cells, Excel, abstrakte Berechnungs Engine, Werte zurückgeben, Node.js über C++, benutzerdefinierte Funktionen
type: docs
weight: 55
url: /de/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

In diesem Artikel wird erläutert, wie der Wertebereich von [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) zurückgegeben wird.

{{% /alert %}}

 Der folgende Code zeigt die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) und gibt den Wertebereich über ihre Methode zurück.

Erstellen Sie eine Klasse mit einer Funktion *calculateCustomFunction*. Diese Klasse implementiert [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

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

Verwenden Sie die oben erwähnte Funktion jetzt in Ihrem Programm

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

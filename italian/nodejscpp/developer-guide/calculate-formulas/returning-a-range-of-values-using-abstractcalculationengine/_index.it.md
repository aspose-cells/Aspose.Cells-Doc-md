---
title: Restituire un intervallo di valori utilizzando AbstractCalculationEngine con Node.js via C++
linktitle: Restituzione di un Intervallo di Valori utilizzando l AbstractCalculationEngine
description: Questo articolo introduce un motore di calcolo astratto che restituisce un intervallo di valori in Excel utilizzando la libreria Aspose.Cells per Node.js via C++. Imparare a caricare o creare un file Excel e salvare il file modificato su disco.
keywords: Aspose.Cells, Excel, motore di calcolo astratto che restituisce valori Node.js via C++, funzioni personalizzate
type: docs
weight: 55
url: /it/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) che viene utilizzata per implementare funzioni utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Questo articolo spiegherà come restituire l'intervallo di valori da [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

Il seguente esempio mostra l'uso della classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) e restituisce l'intervallo di valori tramite il suo metodo.

Creare una classe con una funzione *calculateCustomFunction*. Questa classe implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

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

Ora utilizzare la funzione sopra nel programma

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

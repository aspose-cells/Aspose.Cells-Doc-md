---
title: Calcolo diretto di funzione personalizzata senza scriverla in un foglio di lavoro con Node.js via C++
linktitle: Calcolo diretto di una funzione personalizzata senza scriverla in un foglio di lavoro
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare direttamente funzioni personalizzate in Microsoft Excel senza scriverle in un foglio di lavoro utilizzando Node.js via C++. Caricare un file Excel esistente o crearne uno nuovo, calcolare la funzione personalizzata e salvare il file modificato.
keywords: Aspose.Cells, Excel, funzioni personalizzate, calcoli diretti, Node.js via C++, senza scrivere in fogli di lavoro
type: docs
weight: 90
url: /it/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

Questo argomento spiega come calcolare direttamente le proprie funzioni personalizzate senza prima scriverle in un foglio di lavoro. Utilizzare il metodo [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) a questo scopo.

Si prega di vedere il seguente codice di esempio che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata MyCompany.CustomFunction() e ne calcoliamo il valore come "Aspose.Cells." e questo valore viene automaticamente concatenato con il valore della cella A1 che è "Benvenuto in " dall'interprete di calcolo e il valore calcolato finale ritorna come "Benvenuto in Aspose.Cells.".". Come si può vedere dal codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **Output della console**

Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}

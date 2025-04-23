---
title: Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells con Node.js via C++
linktitle: Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
description: Questo articolo descrive come estendere il motore di calcolo predefinito in Node.js implementando un motore di calcolo personalizzato utilizzando la libreria Aspose.Cells per Node.js via C++. Caricare un file Excel esistente o crearne uno nuovo, utilizzare i metodi forniti e salvare il file Excel modificato.
keywords: Aspose.Cells, Excel, motore di calcolo personalizzato, Node.js via C++
type: docs
weight: 80
url: /it/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementare un Motore di Calcolo Personalizzato**

Aspose.Cells ha un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti permette anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Il seguente codice implementa il motore di calcolo personalizzato. Implementa l'interfaccia [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) che ha un metodo [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-). Questo metodo viene chiamato su tutte le formule. All'interno di questo metodo, catturiamo la funzione **TODAY** e aggiungiamo un giorno alla data di sistema. Quindi, se la data corrente è 27/07/2023, il motore personalizzato calcolerà TODAY() come 28/07/2023.

### **Esempio di programmazione**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **Risultato**

Verificare l'output della console del codice di esempio sopra; il valore (data e ora) di A1 con il motore personalizzato dovrebbe essere di un giorno più tardi rispetto al risultato senza il motore personalizzato.

### **Articolo correlato**

{{% alert color="primary" %}}

[Calcolo diretto di funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}

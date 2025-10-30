---
title: Implementieren Sie eine benutzerdefinierte Berechnungs Engine, um die Standard Berechnungs Engine von Aspose.Cells mit Node.js über C++ zu erweitern
linktitle: Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des standardmäßigen Berechnungsmotors von Aspose.Cells
description: Dieser Artikel beschreibt, wie die Standard Berechnungs Engine in Node.js durch die Implementierung einer benutzerdefinierten Berechnungs Engine mit der Aspose.Cells Bibliothek für Node.js über C++ erweitert werden kann. Laden Sie eine vorhandene Excel Datei oder erstellen Sie eine neue, verwenden Sie die bereitgestellten Methoden und speichern Sie die modifizierte Excel Datei.
keywords: Aspose.Cells, Excel, benutzerdefinierte Berechnungs Engine, Node.js über C++
type: docs
weight: 80
url: /de/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Der folgende Code implementiert die benutzerdefinierte Berechnungs-Engine. Er implementiert die Schnittstelle [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine), die eine [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-) Methode hat. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **HEUTE** und addieren einen Tag zum Systemdatum. Wenn das aktuelle Datum 27.07.2023 ist, berechnet die benutzerdefinierte Engine **HEUTE()** als 28.07.2023.

### **Programmierbeispiel**

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

### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes; der Wert (Datum und Uhrzeit) von A1 mit der benutzerdefinierten Engine sollte einen Tag später sein als das Ergebnis ohne die benutzerdefinierte Engine.

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt zu schreiben](/cells/de/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

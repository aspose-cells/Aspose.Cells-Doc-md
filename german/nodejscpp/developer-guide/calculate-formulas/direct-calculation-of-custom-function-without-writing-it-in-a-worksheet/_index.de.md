---
title: Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt mit Node.js über C++ zu schreiben
linktitle: Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben
description: Dieser Artikel zeigt, wie die Aspose.Cells Bibliothek verwendet werden kann, um benutzerdefinierte Funktionen in Microsoft Excel direkt zu berechnen, ohne die Funktion in einem Arbeitsblatt zu schreiben, mithilfe von Node.js über C++. Laden Sie eine vorhandene Excel Datei oder erstellen Sie eine neue, berechnen Sie die benutzerdefinierte Funktion und speichern Sie die modifizierte Datei.
keywords: Aspose.Cells, Excel, benutzerdefinierte Funktionen, direkte Berechnungen, Node.js über C++, kein Schreiben erforderlich, Arbeitsblätter
type: docs
weight: 90
url: /de/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt**

Dieses Thema erklärt, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in einem Arbeitsblatt zu schreiben. Bitte verwenden Sie dafür die [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-)-Methode.

Bitte beachten Sie den folgenden Beispielcode, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany.CustomFunction() verwendet und ihren Wert als "Aspose.Cells." selbst berechnet. Dieser Wert wird dann automatisch mit dem Wert der Zelle A1, der "Willkommen bei " durch den Berechnungsmotor, konkateniert und der endgültig berechnete Wert als "Willkommen bei Aspose.Cells." zurückgegeben. Wie Sie im Code sehen können, haben wir unsere benutzerdefinierte Funktion nirgendwo in einem Arbeitsblatt geschrieben und sie wird direkt durch unsere eigene benutzerdefinierte Logik berechnet.

### **Programmierbeispiel**

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

### **Konsolenausgabe**

Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}

---
title: Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad med Node.js via C++
linktitle: Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att direkt beräkna anpassade funktioner i Microsoft Excel utan att skriva funktionen i ett kalkylblad med Node.js via C++. Ladda en befintlig Excel fil eller skapa en ny, beräkna den anpassade funktionen och spara den modifierade filen.
keywords: Aspose.Cells, Excel, anpassade funktioner, direktberäkning, Node.js via C++, behöver inte skriva, kalkylblad
type: docs
weight: 90
url: /sv/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad**

Denna artikel förklarar hur du kan direkt beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Använd metod [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) för detta ändamål.

Se följande exempelkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany.CustomFunction() och beräknar dess värde som "Aspose.Cells." på egen hand och sedan konkateneras detta värde automatiskt med värdet för cell A1, vilket är "Välkommen till " av beräkningsmotorn och det slutliga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i en arbetsbok och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

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

### **Konsoloutput**

Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Implementera anpassad beräkningsmotor för att utöka standardberäkningsmotorn i Aspose.Cells]( /cells/sv/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/ )

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

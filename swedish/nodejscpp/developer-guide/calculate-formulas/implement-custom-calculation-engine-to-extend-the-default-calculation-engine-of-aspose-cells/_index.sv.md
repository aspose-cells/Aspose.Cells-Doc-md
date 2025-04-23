---
title: Implementera anpassad beräkningsmotor för att utöka standardberäkningsmotorn i Aspose.Cells med Node.js via C++
linktitle: Implementera anpassad beräkningsmotor för att utöka Aspose.Cells standardberäkningsmotor
description: Denna artikel beskriver hur man utökar standardberäkningsmotorn i Node.js genom att implementera en anpassad beräkningsmotor med Aspose.Cells för Node.js via C++. Ladda en befintlig Excel fil eller skapa en ny för att använda de metodiker som tillhandahålls och spara den modifierade Excel filen.
keywords: Aspose.Cells, Excel, anpassad beräkningsmotor, Node.js via C++
type: docs
weight: 80
url: /sv/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) som har en [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-) metod. Denna metod anropas för alla dina formler. Inuti denna metod fångar vi **TODAY**-funktionen och lägger till en dag till systemdatumet. Så om dagens datum är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

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

### **Resultat**

Vänligen kontrollera konsolutmatningen för ovanstående exempel; värdet (datum/tid) för A1 med den anpassade motorn bör vara en dag senare än resultatet utan den anpassade motorn.

### **Relaterad artikel**

{{% alert color="primary" %}}

[Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad](/cells/sv/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}

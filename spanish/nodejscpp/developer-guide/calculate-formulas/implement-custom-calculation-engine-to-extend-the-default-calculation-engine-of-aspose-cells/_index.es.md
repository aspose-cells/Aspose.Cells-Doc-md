---
title: Implementar motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells con Node.js vía C++
linktitle: Implementar un Motor de Cálculo Personalizado para extender el Motor de Cálculo Predeterminado de Aspose.Cells
description: Este artículo describe cómo extender el motor de cálculo predeterminado en Node.js implementando un motor de cálculo personalizado usando la biblioteca Aspose.Cells para Node.js vía C++. Carga un archivo de Excel existente o crea uno nuevo para usar los métodos proporcionados y guarda el archivo de Excel modificado.
keywords: Aspose.Cells, Excel, Motor de cálculo personalizado, Node.js vía C++
type: docs
weight: 80
url: /es/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te brinda mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

El siguiente código implementa el Motor de cálculo personalizado. Implementa la interfaz [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) que tiene un método [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-). Este método se llama para todas tus fórmulas. Dentro de este método, capturamos la función **TODAY** y añadimos un día a la fecha del sistema. Entonces, si la fecha actual es 27/07/2023, el motor personalizado calculará TODAY() como 28/07/2023.

### **Ejemplo de Programación**

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

### **Resultado**

Por favor, verifica la salida en consola del código de muestra anterior; el valor (fecha y hora) de A1 con el motor personalizado debería ser un día más tarde que el resultado sin el motor personalizado.

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Cálculo directo de función personalizada sin escribirla en una hoja de cálculo]( /cells/es/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/ )

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

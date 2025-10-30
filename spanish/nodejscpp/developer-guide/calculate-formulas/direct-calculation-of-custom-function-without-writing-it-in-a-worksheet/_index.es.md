---
title: Cálculo directo de función personalizada sin escribirla en una hoja de cálculo con Node.js vía C++
linktitle: Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para calcular directamente funciones personalizadas en Microsoft Excel sin escribir la función en una hoja de cálculo usando Node.js vía C++. Carga un archivo de Excel existente o crea uno nuevo, calcula la función personalizada y guarda el archivo modificado.
keywords: Aspose.Cells, Excel, funciones personalizadas, cálculos directos, Node.js vía C++, sin necesidad de escribir, hojas de cálculo
type: docs
weight: 90
url: /es/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo**

Este tema explica cómo puedes calcular directamente tus funciones personalizadas sin escribirlas primero en una hoja de cálculo. Por favor, usa el método [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) para este propósito.

Por favor, consulta el siguiente código de muestra que ilustra el uso de este método. Hemos utilizado una función personalizada llamada MyCompany.CustomFunction() y calculamos su valor como "Aspose.Cells." por nosotros mismos y luego este valor se concatena automáticamente con el valor de la celda A1 que es "Bienvenido a " por el motor de cálculo y el valor calculado final retorna como "Bienvenido a Aspose.Cells.". Como se puede ver en un código, no hemos escrito nuestra función personalizada en ninguna hoja de cálculo y se calcula directamente por nuestra lógica personalizada.

### **Ejemplo de Programación**

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

### **Salida de la consola**

A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Implementar motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells]( /cells/es/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/ )

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}

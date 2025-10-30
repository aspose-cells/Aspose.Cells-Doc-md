---
title: Usando la clase GlobalizationSettings para etiquetas personalizadas de subtotal y otras etiquetas de gráficos de pastel con Node.js a través de C++
linktitle: Usar la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores
type: docs
weight: 70
url: /es/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Aprende cómo personalizar las etiquetas de subtotal y otras etiquetas en gráficos de pastel usando la clase GlobalizationSettings en Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Las APIs de Aspose.Cells han expuesto la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) para tratar escenarios donde el usuario desea usar etiquetas personalizadas para subtotales en una hoja de cálculo. Además, la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) también puede usarse para modificar la etiqueta **Other** en gráficos circulares al renderizar la hoja o gráfico.

## **Introducción a la Clase Configuración Global**

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) ofrece actualmente los siguientes 3 métodos que pueden ser sobreescritos en una clase personalizada para obtener las etiquetas deseadas para los subtotales o para renderizar texto personalizado en la etiqueta **Other** de un gráfico circular.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Obtiene el nombre total de la función.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Obtiene el nombre del total general de la función.


### **Etiquetas Personalizadas para Subtotales**

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) puede usarse para personalizar las etiquetas de subtotal sobrescribiendo los métodos [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) y [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) como se demuestra a continuación.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

Para inyectar etiquetas personalizadas, es necesario asignar la propiedad [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) a una instancia de la clase **CustomSettings** definida anteriormente antes de agregar los subtotales a la hoja.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

La clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) solo funciona para agregar nuevos subtotales. Si una hoja ya contiene subtotales, sus etiquetas no pueden modificarse.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}

---  
title: Implementar etiquetas de subtotal o total general en otros idiomas con Node.js a través de C++  
linktitle: Implementar etiquetas de subtotal o total general en otros idiomas  
type: docs  
weight: 50  
url: /es/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Escenarios de uso posibles**  

A veces, quieres mostrar etiquetas de subtotal y total general en idiomas no ingleses como chino, japonés, árabe, hindi, etc. Aspose.Cells for Node.js via C++ permite hacer esto usando la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) y la propiedad [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/). Por favor, consulta este artículo sobre cómo usar la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).  

- [Usando la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores](/cells/es/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementar etiquetas de subtotal o total general en otros idiomas**  

El siguiente ejemplo de código carga el [archivo Excel de muestra](5115151.xlsx) e implementa nombres de subtotal y total general en idioma chino. Por favor, revisa el [archivo Excel resultante](5115152.xlsx) generado por este código como referencia. Primero creamos una clase de [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) y luego la usamos en nuestro código.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

Ahora usa la clase creada anteriormente en el código como sigue:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

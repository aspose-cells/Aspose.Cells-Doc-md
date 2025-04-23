---  
title: Configuración del modo de cálculo de fórmulas del libro de trabajo con Node.js vía C++  
linktitle: Configuración del modo de cálculo de fórmulas del libro de trabajo  
description: Este artículo introduce cómo configurar el modo de cálculo de fórmulas en un libro de Microsoft Excel con Aspose.Cells for Node.js via C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar el método proporcionado por Aspose.Cells para establecer el modo de cálculo de fórmulas y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en disco.  
keywords: Aspose.Cells, Excel, libro de trabajo, modo de cálculo de fórmulas, configuraciones, Node.js vía C++  
type: docs  
weight: 110  
url: /es/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excel te permite establecer el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:  

- Automático: recalcula cada vez que algo cambia, y cada vez que se abre un libro.  
- Automático excepto para tablas de datos: recalcula cada vez que algo cambia, pero deja fuera las tablas de datos.  
- Manual: recalcula solo cuando el usuario lo solicita explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarda el libro.  
{{% /alert %}}  

Para establecer el modo de cálculo de fórmulas en Microsoft Excel:  

1. Selecciona **Fórmulas** y luego **Opciones de cálculo**.  
1. Selecciona una de las opciones.  

Aspose.Cells for Node.js via C++ también permite establecer el **Modo de Cálculo de Fórmulas** usando la propiedad [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--) mode. Puedes asignarle la enumeración [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) que tiene uno de los siguientes valores:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


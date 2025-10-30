---  
title: Usa la opción de comprobación de errores con Node.js a través de C++  
linktitle: Usar opciones de verificación de errores  
type: docs  
weight: 140  
url: /es/nodejs-cpp/use-error-checking-options/  
description: Aprende cómo usar las opciones de comprobación de errores en las hojas de cálculo de Excel programáticamente usando Aspose.Cells for Node.js via C++.  
keywords: almacenar número como texto en Excel usando Node.js a través de C++, opción de comprobación de errores en Excel Node.js a través de C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios definir opciones y reglas de verificación de errores. Los usuarios a menudo ven verificaciones de errores al crear fórmulas, un pequeño triángulo en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.  
{{% /alert %}}  

## **Tipos de Errores**  

Los errores que indican que la fórmula no puede devolver un resultado, como dividir un número por cero, requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde, aparece un signo de exclamación; hacer clic en esto abre una lista de opciones.  

El error puede ser resuelto usando las opciones o ser ignorado. Ignorar un error significa que ese error no aparecerá en controles de errores futuros.  

Aspose.Cells proporciona funciones de opción de comprobación de errores. La clase [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) gestiona diferentes tipos de comprobaciones de errores, por ejemplo, números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Use la enumeración [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) para establecer la comprobación de errores deseada.  

## **Números Almacenados como Texto**  

Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con cálculos o producir órdenes de clasificación confusos. Los números formateados como texto están alineados a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en celdas no devuelve un valor, verifica la alineación en las celdas a las que hace referencia la fórmula; algunas o todas esas celdas pueden ser números formateados como texto.  

Puedes usar las opciones de verificación de errores para convertir rápidamente los números almacenados como texto en números reales. En Microsoft Excel 2003:  

1. En el menú **Herramientas**, haz clic en **Opciones**.  
1. Selecciona la pestaña de Verificación de Errores.  
   La opción de **Número almacenado como texto** está marcada por defecto.  
1. Desactívala.  

El siguiente código de muestra muestra cómo deshabilitar la opción de verificación de errores de números almacenados como texto para una hoja de cálculo en el archivo XLS de plantilla utilizando las APIs de Aspose.Cells.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}

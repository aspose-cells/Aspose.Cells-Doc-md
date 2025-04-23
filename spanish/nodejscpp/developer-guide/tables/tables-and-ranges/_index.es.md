---  
title: Tablas y Rangos con Node.js a través de C++  
linktitle: Tablas y Rangos  
type: docs  
weight: 50  
url: /es/nodejs-cpp/tables-and-ranges/  
---  

## **Introducción**  

A veces crea una tabla en Microsoft Excel y no desea seguir trabajando con la funcionalidad de la tabla con la que viene. En su lugar, desea algo que se vea como una tabla. Para mantener los datos en una tabla sin perder el formato, convierta la tabla a un rango normal de datos.  
Aspose.Cells es compatible con esta función de Microsoft Excel para tablas y objetos de lista.  

## **Usar Microsoft Excel**  

Utiliza la función **Convertir en rango** para convertir rápidamente una tabla en un rango sin perder el formato. En Microsoft Excel 2007/2010:  

1. Haz clic en cualquier lugar de la tabla para asegurarte de que la celda activa esté en una columna de la tabla.  
1. En la pestaña **Diseño**, en el grupo **Herramientas**, haz clic en **Convertir en rango**.  

## **Usar Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Las características de la tabla ya no están disponibles después de que la tabla ha sido convertida en un rango. Por ejemplo, los encabezados de fila ya no incluyen las flechas para ordenar y filtrar, y las referencias estructuradas (referencias que usan nombres de tablas) que se usaban en fórmulas se convierten en referencias de celda regulares.  

{{% /alert %}}  

## **Convertir Tabla a Rango con Opciones**  

Aspose.Cells proporciona opciones adicionales al convertir una Tabla en un Rango a través de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). La clase [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) proporciona la propiedad [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) que le permite establecer el último índice de la fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.  

El código de ejemplo a continuación demuestra el uso de la clase [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  


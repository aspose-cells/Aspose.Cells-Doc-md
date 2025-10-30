---  
title: Optimización del uso de memoria al trabajar con archivos grandes con grandes conjuntos de datos con Node.js a través de C++  
linktitle: Optimización del uso de memoria al trabajar con archivos grandes que contienen conjuntos de datos extensos  
type: docs  
weight: 180  
url: /es/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

Cuando se crea un libro de trabajo con grandes conjuntos de datos o se lee un archivo de Microsoft Excel grande, la cantidad total de RAM que la operación requerirá siempre es una preocupación. Hay medidas que se pueden adaptar para afrontar el desafío. Aspose.Cells for Node.js via C++ ofrece algunas opciones relevantes y llamadas a la API para reducir, disminuir y optimizar el uso de memoria. Además, puede ayudar a que la operación funcione de manera más eficiente y rápido.  

Utilice la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) para optimizar el uso de memoria para los datos de las celdas y disminuir el costo total de memoria. Al construir un conjunto de datos grande para las celdas, se puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Optimización de memoria**  

### **Lectura de archivos Excel grandes**  

El siguiente ejemplo muestra cómo leer un archivo grande de Microsoft Excel en modo optimizado.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Escribiendo Archivos de Excel Grandes**  

El siguiente ejemplo muestra cómo escribir un conjunto de datos grande en una hoja de trabajo en modo optimizado.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Precaución**  

La opción predeterminada, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), se aplica para todas las versiones. Para algunas situaciones, como construir un libro con un conjunto de datos grande para celdas, la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) puede optimizar el uso de memoria y disminuir el costo de memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales, como se indica a continuación.  

1. **Acceder a las celdas aleatoriamente y de forma repetida**: La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila, y luego fila por fila. Especialmente, si accede a filas/celdas mediante el enumerador obtenido de [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection), y [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), el rendimiento se maximizará con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Insertar y eliminar celdas y filas**: Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para celdas/filas, el deterioro del rendimiento será notable en modo *MemoryPreference* en comparación con el modo *Normal*.  
3. **Operar en diferentes tipos de celda**: Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será igual al modo *Normal*, pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos y otros, la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) dará mejor rendimiento.  

{{< app/cells/assistant language="nodejs-cpp" >}}

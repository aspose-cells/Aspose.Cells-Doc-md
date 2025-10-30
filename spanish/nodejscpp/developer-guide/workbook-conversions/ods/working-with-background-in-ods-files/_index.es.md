---  
title: Trabajar con fondo en archivos ODS con Node.js a través de C++  
linktitle: Trabajar con fondo en archivos ODS  
type: docs  
weight: 150  
url: /es/nodejs-cpp/working-with-background-in-ods-files/  
description: Aprende cómo gestionar fondos en archivos ODS usando Aspose.Cells for Node.js via C++.  
---  

## **Fondo en archivos ODS**  

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el cuadro de diálogo de vista previa de impresión.  

Aspose.Cells for Node.js via C++ ofrece la habilidad de leer la información de fondo y agregar el fondo en archivos ODS.  

## **Leer información de fondo de archivo ODS**  

Aspose.Cells for Node.js via C++ proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la clase [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) cargando el archivo [source ODS](90112030.ods) y leyendo la información de fondo. Por favor, consulte la salida de consola generada por el código como referencia.  

### **Código de muestra**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **Salida de la consola**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Agregar fondo de color al archivo ODS**  

Aspose.Cells for Node.js via C++ proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) para agregar un fondo de color al archivo ODS. Por favor, vea el archivo [output ODS](90112031.ods) generado por el código como referencia.  

### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **Agregar fondo gráfico al archivo ODS**  

Aspose.Cells for Node.js via C++ ofrece la clase [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código muestra el uso de la propiedad [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) para agregar un fondo gráfico al archivo ODS. Por favor, consulte el archivo [output ODS](90112030.ods) generado por el código como referencia.  

### **Código de muestra**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

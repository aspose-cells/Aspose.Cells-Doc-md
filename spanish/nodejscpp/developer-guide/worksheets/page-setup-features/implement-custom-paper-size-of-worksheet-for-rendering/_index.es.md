---  
title: Implementar tamaño de papel personalizado de la hoja de trabajo para renderizado con Node.js usando C++  
linktitle: Implementar tamaño de papel personalizado de la hoja de cálculo para la representación  
type: docs  
weight: 70  
url: /es/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Este artículo explica cómo usar la API de Node.js a través de C++ para establecer un tamaño de papel personalizado para tus hojas de trabajo deseadas al renderizar un archivo de Excel en formato PDF de forma programática.  
keywords: Establecer tamaño de papel personalizado al renderizar Excel a PDF usando Node.js con C++  
---  

## **Escenarios de uso posibles**  

No hay opción disponible directamente para crear tamaños de papel personalizados en MS Excel, sin embargo, puedes establecer un tamaño de papel personalizado en las hojas de trabajo deseadas al renderizar un archivo de Excel en formato PDF. Este documento explica cómo configurar un tamaño de papel personalizado en una hoja de trabajo usando las API de Aspose.Cells.  

## **Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado**  

 Aspose.Cells te permite implementar el tamaño de papel deseado de la hoja de trabajo. Puedes usar el método [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) de la clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) para especificar un tamaño de página personalizado. El siguiente código de ejemplo ilustra cómo especificar un tamaño de papel personalizado para la primera hoja del libro. También mira el [PDF de salida](45056028.pdf) generado con el siguiente código como referencia.  

## **Captura de pantalla**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  


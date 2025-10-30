---  
title: Convertir hoja de cálculo en imagen usando las opciones ImageOrPrint con Node.js a través de C++  
linktitle: Conversión de Hoja de Cálculo a Imagen usando Opciones de Imagen o Impresión  
type: docs  
weight: 90  
url: /es/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Aprende cómo convertir una hoja de cálculo en un archivo de imagen y aplicar varias opciones de imagen e impresión usando Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.  
{{% /alert %}}  

## **Guardar hojas de cálculo en imágenes - Diferentes enfoques**  

A veces, es posible que desee presentar sus hojas de cálculo como representación pictórica. Es posible que necesite presentar las imágenes de las hojas de cálculo en sus aplicaciones o páginas web. Es posible que necesite insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint o usarlas en algún otro escenario. Simplemente desea que una hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de cálculo en archivos de Excel a imágenes. Además, Aspose.Cells admite configurar diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.  

Podrías intentar la Automatización de Office, pero esta tiene sus propias desventajas. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad, precio y funciones. En resumen, hay muchas razones, siendo la principal que Microsoft mismo recomienda encarecidamente evitar la automatización de Office desde soluciones de software.  

Este artículo muestra cómo crear una aplicación de consola en Visual Studio .NET, realizar la conversión de una hoja de cálculo a imagen utilizando diferentes opciones de imagen e impresión con unas pocas y simples líneas de código utilizando la API de Aspose.Cells.  

La clase [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) representa una hoja de trabajo para renderizar imágenes de la hoja de trabajo, tiene un método sobrecargado [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) que puede convertir directamente una hoja de trabajo en archivos de imagen especificados con los atributos u opciones deseados. Puede devolver un objeto en el que puede Guardar un archivo de imagen en el disco/transmisión. Se admiten varios formatos de imagen, como BMP, PNG, GIFF, JPEG, TIFF, EMF y otros.  

## **Usar Aspose.Cells para convertir hoja de cálculo a imagen utilizando opciones de imagen o impresión.**  

### **Creación de un libro de trabajo de plantilla en Microsoft Excel**  

Creé un nuevo libro de trabajo en MS Excel y agregué algunos datos en la primera hoja de cálculo. Ahora, convertiré la hoja de trabajo del archivo de plantilla 'Sheet1' a un archivo de imagen 'SheetImage.tiff' y aplicaré diferentes opciones de imagen como resoluciones horizontal y vertical, Compresión Tiff, etc.  

### **Descargar e instalar Aspose.Cells**  

Primero, necesita [descargar](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Instálelo en su computadora de desarrollo. Todos los componentes de [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.  

### **Crear un proyecto**  

Inicie su entorno de desarrollo preferido (por ejemplo, Visual Studio). Cree una nueva aplicación de consola.  

### **Agregar referencias**  

Este proyecto utilizará Aspose.Cells. Por lo tanto, debe agregar una referencia al componente Aspose.Cells en su proyecto. Por ejemplo, agregue una referencia a ….\Archivos de programa\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **Convertir hoja de cálculo a un archivo de imagen**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Opciones de conversión**  

Es posible guardar páginas específicas como imágenes. El siguiente código convierte las primeras y segundas hojas de cálculo en un libro de trabajo a imágenes JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Conversión de imagen usando WorkbookRender**  

Una imagen TIFF puede contener más de un cuadro. Puede guardar toda la hoja de trabajo en una sola imagen TIFF con múltiples cuadros o páginas:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


{{< app/cells/assistant language="nodejs-cpp" >}}

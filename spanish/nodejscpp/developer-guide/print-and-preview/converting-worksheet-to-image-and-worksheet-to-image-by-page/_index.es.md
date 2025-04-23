---  
title: Convertir Hoja de Cálculo en Imagen y Hoja de Cálculo por Página con Node.js a través de C++  
linktitle: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página  
type: docs  
weight: 80  
url: /es/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y hojas con múltiples páginas en archivos de imagen por página.  

A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Puedes necesitar insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, o utilizarlas en otro escenario. Básicamente, quieres renderizar la hoja de cálculo como una imagen. Aspose.Cells admite la conversión de hojas de cálculo en archivos de imagen de Excel. Además, Aspose.Cells admite la conversión de un libro de trabajo a múltiples archivos de imagen, uno por página.  

Podrías utilizar la Automatización de Office para lograr esto, pero la Automatización de Office tiene sus propias desventajas. Hay varias razones y problemas implicados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft en sí mismo recomienda firmemente en contra de la Automatización de Office.  
{{% /alert %}}  

## **Usar Aspose.Cells for Node.js via C++ para convertir hoja de cálculo en archivo de imagen**  

Este artículo muestra cómo crear una aplicación de consola, convertir una hoja de cálculo en una imagen y convertir una hoja en una imagen única para cada hoja con unas pocas y sencillas líneas de código utilizando la API de Aspose.Cells.  

Debes importar varias clases valiosas relacionadas con las funcionalidades de renderizado en tu programa o proyecto, como [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/), y otras. La clase [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) representa una hoja de cálculo para renderizar en imágenes de la hoja y tiene un método [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) sobrecargado que puede convertir una hoja de cálculo en archivos de imagen directamente con cualquier atributo u opción establecidos. Puede devolver un objeto de imagen y también guardar un archivo de imagen en el disco/flujo. Varias formatos de imagen son soportados, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF y otros.  

Este artículo explica cómo:  

- Convertir una hoja de cálculo a una imagen  
- Convertir cada página en una hoja de cálculo a una imagen  

Esta tarea muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo de plantilla a un archivo de imagen.  

### **Configurar Proyecto**  

1. Primero, [descarga Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Instálalo en tu computadora de desarrollo. Todos los componentes [Aspose](http://www.aspose.com/), al ser instalados, funcionan en modo evaluación. El modo evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Ahora inicia tu entorno de desarrollo y crea una nueva aplicación de consola. Este ejemplo usa una aplicación de consola en Node.js, pero puedes usar cualquier configuración que se integre con Node.js. Agrega una referencia a Aspose.Cells en tu proyecto.  

### **Convertir Hoja de Cálculo a Archivo de Imagen**  

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook.xlsx** (1 hoja de cálculo). A continuación, convierte la hoja de cálculo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.  

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en **Testbook.xlsx** a un archivo de imagen para explicar lo sencilla que es esta conversión.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Usar Aspose.Cells for Node.js via C++ para convertir hoja de cálculo en archivo de imagen por página**  

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo que tiene varias páginas a un archivo de imagen por página.  

### **Convertir hoja de cálculo en imagen por página**  

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook2.xlsx** (1 hoja de cálculo).  

Ahora, convierte la hoja de cálculo del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de cálculo.  

El siguiente es el código utilizado por el componente para realizar la tarea. Convierte la hoja Sheet1 en Testbook2.xlsx en archivos de imagen por página.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  



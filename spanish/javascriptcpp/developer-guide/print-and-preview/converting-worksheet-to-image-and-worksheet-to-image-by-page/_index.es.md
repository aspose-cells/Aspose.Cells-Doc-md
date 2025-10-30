---
title: Convertir Hoja de Cálculo a Imagen y Hoja de Cálculo a Imagen por Página con JavaScript a través de C++
linktitle: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página
type: docs
weight: 80
url: /es/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y hojas con múltiples páginas en archivos de imagen por página.

A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Puedes necesitar insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, o utilizarlas en otro escenario. Básicamente, quieres renderizar la hoja de cálculo como una imagen. Aspose.Cells admite la conversión de hojas de cálculo en archivos de imagen de Excel. Además, Aspose.Cells admite la conversión de un libro de trabajo a múltiples archivos de imagen, uno por página.

Podrías utilizar la Automatización de Office para lograr esto, pero la Automatización de Office tiene sus propias desventajas. Hay varias razones y problemas implicados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft en sí mismo recomienda firmemente en contra de la Automatización de Office.
{{% /alert %}}

## **Usando Aspose.Cells for JavaScript a través de C++ para convertir hoja de cálculo a archivo de imagen**

Este artículo muestra cómo crear una aplicación de consola, convertir una hoja de cálculo en una imagen y convertir una hoja en una imagen única para cada hoja con unas pocas y sencillas líneas de código utilizando la API de Aspose.Cells.

Necesitas importar varias clases valiosas relacionadas con funcionalidades de renderizado en tu programa o proyecto, como [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/), y otros. La clase [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) representa una hoja de cálculo para renderizar imágenes y tiene un método sobrecargado [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) que puede convertir una hoja de cálculo en archivos de imagen directamente con atributos u opciones establecidas. Puede devolver un objeto de imagen y guardar un archivo de imagen en disco/transmisión. Se soportan varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, y otros.

Este artículo explica cómo:

- Convertir una hoja de cálculo a una imagen
- Convertir cada página en una hoja de cálculo a una imagen

Esta tarea muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo de plantilla a un archivo de imagen.

### **Configurar Proyecto**

1. Primero, [descarga Aspose.Cells for JavaScript a través de C++](https://downloads.aspose.com/cells/javascript-cpp).
1. Instálalo en tu computadora de desarrollo. Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo evaluación. El modo evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Ahora inicia tu entorno de desarrollo y crea una nueva aplicación de consola. Este ejemplo usa una aplicación de consola en JavaScript, pero puedes usar cualquier configuración que integre con JavaScript. Añade referencia a Aspose.Cells en el proyecto creado.

### **Convertir Hoja de Cálculo a Archivo de Imagen**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook.xlsx** (1 hoja de cálculo). A continuación, convierte la hoja de cálculo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en **Testbook.xlsx** a un archivo de imagen para explicar lo sencilla que es esta conversión.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **Usando Aspose.Cells for JavaScript a través de C++ para convertir hoja de cálculo en archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo que tiene varias páginas a un archivo de imagen por página.

### **Convertir hoja de cálculo en imagen por página**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook2.xlsx** (1 hoja de cálculo).

Ahora, convierte la hoja de cálculo del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de cálculo.

El siguiente es el código utilizado por el componente para realizar la tarea. Convierte la hoja Sheet1 en Testbook2.xlsx en archivos de imagen por página.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```

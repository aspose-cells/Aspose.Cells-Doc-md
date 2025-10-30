---
title: Convertir hoja de cálculo a imagen usando Opciones de ImagenoImpresión con JavaScript a través de C++
linktitle: Conversión de Hoja de Cálculo a Imagen usando Opciones de Imagen o Impresión
type: docs
weight: 90
url: /es/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Aprende cómo convertir una hoja de cálculo en un archivo de imagen y aplicar varias opciones de imagen e impresión usando Aspose.Cells for JavaScript a través de C++.   
---

{{% alert color="primary" %}}  
Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.  
{{% /alert %}}  

## **Guardar hojas de cálculo en imágenes - Diferentes enfoques**  

A veces, es posible que desee presentar sus hojas de cálculo como representación pictórica. Es posible que necesite presentar las imágenes de las hojas de cálculo en sus aplicaciones o páginas web. Es posible que necesite insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint o usarlas en algún otro escenario. Simplemente desea que una hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells admite la conversión de hojas de cálculo en archivos de Excel a imágenes. Además, Aspose.Cells admite configurar diferentes opciones como formato de imagen, resolución (tanto vertical como horizontal), calidad de imagen y otras opciones de imagen e impresión.  

Podrías intentar la Automatización de Office, pero esta tiene sus propias desventajas. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad, precio y funciones. En resumen, hay muchas razones, siendo la principal que Microsoft mismo recomienda encarecidamente evitar la automatización de Office desde soluciones de software.  

Este artículo muestra cómo crear una aplicación de consola en Visual Studio .NET, realizar la conversión de una hoja de cálculo a imagen utilizando diferentes opciones de imagen e impresión con unas pocas y simples líneas de código utilizando la API de Aspose.Cells.  

La clase [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) representa una hoja de trabajo para renderizar imágenes de la hoja de trabajo, tiene un método sobrecargado [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) que puede convertir directamente una hoja de trabajo en archivos de imagen especificados con los atributos u opciones deseados. Puede devolver un objeto en el que puede Guardar un archivo de imagen en el disco/transmisión. Se admiten varios formatos de imagen, como BMP, PNG, GIFF, JPEG, TIFF, EMF y otros.  

## **Usar Aspose.Cells para convertir hoja de cálculo a imagen utilizando opciones de imagen o impresión.**  

### **Creación de un libro de trabajo de plantilla en Microsoft Excel**  

Creé un nuevo libro de trabajo en MS Excel y agregué algunos datos en la primera hoja de cálculo. Ahora, convertiré la hoja de trabajo del archivo de plantilla 'Sheet1' a un archivo de imagen 'SheetImage.tiff' y aplicaré diferentes opciones de imagen como resoluciones horizontal y vertical, Compresión Tiff, etc.  

### **Descargar e instalar Aspose.Cells**  

Primero, necesitas [descargar](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript a través de C++. Instálalo en tu computadora de desarrollo. Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, trabajan en modo evaluación. El modo evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.  

### **Crear un proyecto**  

Inicie su entorno de desarrollo preferido (por ejemplo, Visual Studio). Cree una nueva aplicación de consola.  

### **Agregar referencias**  

Este proyecto usará Aspose.Cells. Por lo tanto, debes añadir una referencia al componente Aspose.Cells en tu proyecto. Por ejemplo, añade una referencia a ….\Program Files\Aspose\Aspose.Cells for JavaScript a través de C++\Bin\Aspose.Cells.node  

### **Convertir hoja de cálculo a un archivo de imagen**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **Opciones de conversión**  

Es posible guardar páginas específicas como imágenes. El siguiente código convierte las primeras y segundas hojas de cálculo en un libro de trabajo a imágenes JPG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **Conversión de imagen usando WorkbookRender**  

Una imagen TIFF puede contener más de un cuadro. Puede guardar toda la hoja de trabajo en una sola imagen TIFF con múltiples cuadros o páginas:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

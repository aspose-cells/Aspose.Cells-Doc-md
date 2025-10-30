---
title: Trabajando con Fondo en archivos ODS con JavaScript vía C++
linktitle: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/javascript-cpp/working-with-background-in-ods-files/
description: Aprenda cómo gestionar fondos en archivos ODS usando Aspose.Cells for JavaScript vía C++.
---

## **Fondo en archivos ODS**  

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el cuadro de diálogo de vista previa de impresión.  

Aspose.Cells for JavaScript vía C++ proporciona la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.  

## **Leer información de fondo de archivo ODS**  

Aspose.Cells for JavaScript vía C++ proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la clase [**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground) cargando el archivo [archivo ODS fuente](90112030.ods) y leyendo la información del fondo. Por favor, consulte la salida del Consola generada por el código para referencia.  

### **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>ODS Background Extraction Example</title>
    </head>
    <body>
        <h1>ODS Background Extraction Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
        <button id="runExample">Extract Background</button>
        <a id="downloadLink" style="display: none;">Download Background Image</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS/Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access ODS page background from the worksheet's page setup
            const background = worksheet.pageSetup.odsPageBackground;

            // Read background properties
            const backgroundType = background.type.toString();
            const backgroundPosition = background.graphicPositionType.toString();

            document.getElementById('result').innerHTML = `<p>Background Type: ${backgroundType}</p><p>Background Position: ${backgroundPosition}</p>`;

            // Get graphic data and prepare download link
            const graphicData = background.graphicData;
            const blob = new Blob([graphicData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'background.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Background Image';
        });
    </script>
</html>
```  

### **Salida de la consola**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Agregar fondo de color al archivo ODS**  

Aspose.Cells for JavaScript vía C++ proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.color**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground/#color--) para agregar un fondo de color al archivo ODS. Por favor, consulte el archivo [salida ODS](90112031.ods) generado por el código para referencia.  

### **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Colored ODS Background</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate a new workbook. If a file is provided, open it; otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Populate cells (converted to property-style assignments)
            worksheet.cells.get(0, 0).value = 1;
            worksheet.cells.get(1, 0).value = 2;
            worksheet.cells.get(2, 0).value = 3;
            worksheet.cells.get(3, 0).value = 4;
            worksheet.cells.get(4, 0).value = 5;
            worksheet.cells.get(5, 0).value = 6;
            worksheet.cells.get(0, 1).value = 7;
            worksheet.cells.get(1, 1).value = 8;
            worksheet.cells.get(2, 1).value = 9;
            worksheet.cells.get(3, 1).value = 10;
            worksheet.cells.get(4, 1).value = 11;
            worksheet.cells.get(5, 1).value = 12;

            // Configure ODS page background (converted getters/setters to properties)
            const background = worksheet.pageSetup.odsPageBackground;
            background.color = AsposeCells.Color.Azure;
            background.type = AsposeCells.OdsPageBackgroundType.Color;

            // Save the workbook as ODS and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColoredBackground.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ColoredBackground.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Agregar fondo gráfico al archivo ODS**  

Aspose.Cells for JavaScript vía C++ proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.graphicData**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground/#graphicData--) para agregar fondos gráficos al archivo ODS. Por favor, consulte el archivo [salida ODS](90112030.ods) generado por el código para referencia.  

### **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Graphic Background Example</h1>
        <p>Select a background image to embed into a new workbook as an ODS page background.</p>
        <input type="file" id="imageInput" accept="image/*" />
        <button id="runExample">Create Workbook with Graphic Background</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OdsPageBackgroundType, OdsPageBackgroundGraphicType } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            // Read selected image file
            const file = imageInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Populate some cells
            worksheet.cells.get(0, 0).value = 1;
            worksheet.cells.get(1, 0).value = 2;
            worksheet.cells.get(2, 0).value = 3;
            worksheet.cells.get(3, 0).value = 4;
            worksheet.cells.get(4, 0).value = 5;
            worksheet.cells.get(5, 0).value = 6;
            worksheet.cells.get(0, 1).value = 7;
            worksheet.cells.get(1, 1).value = 8;
            worksheet.cells.get(2, 1).value = 9;
            worksheet.cells.get(3, 1).value = 10;
            worksheet.cells.get(4, 1).value = 11;
            worksheet.cells.get(5, 1).value = 12;

            // Access ODS page background via pageSetup property
            const background = worksheet.pageSetup.oDSPageBackground;
            background.type = OdsPageBackgroundType.Graphic;
            background.graphicData = imageBytes;
            background.graphicType = OdsPageBackgroundGraphicType.Area;

            // Save the workbook as ODS and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'GraphicBackground.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ODS File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```

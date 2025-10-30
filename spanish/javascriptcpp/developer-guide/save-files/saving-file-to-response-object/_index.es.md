---
title: Guardar archivo en el objeto de respuesta con JavaScript vía C++
linktitle: Guardando archivo en objeto de respuesta
type: docs
weight: 50
url: /es/javascript-cpp/saving-file-to-response-object/
description: Aprende cómo generar archivos dinámicamente y enviarlos directamente al navegador del cliente usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}  

Aspose.Cells hace posible manipular archivos. Este artículo explica las diferentes formas en las que los archivos se pueden guardar en un objeto de respuesta.  

{{% /alert %}}  

## **Guardando archivo en objeto de respuesta**  

También es posible generar un archivo dinámicamente y enviarlo directamente a un navegador cliente. Para hacerlo, usa una versión especial sobrecargada del método [**Save**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) que acepta los siguientes parámetros:  

- Objeto de respuesta de JavaScript.  
- Nombre de archivo.  
- [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/), el tipo de disposición de contenido del archivo de salida.  
- [**SaveOptions**](https://reference.aspose.com/cells/javascript-cpp/saveoptions/), el tipo de formato de archivo  

La enumeración [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/) determina si el archivo enviado al navegador ofrece la opción de abrirse por sí mismo directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.  

La enumeración contiene los siguientes tipos de guardado predefinidos:  

|**Tipo**|**Descripción**|  
| :- | :- |  
|Archivo adjunto|Envía la hoja de cálculo al navegador y se abre en una aplicación como un archivo adjunto asociado con .xls/.xlsx u otras extensiones|  
|En línea|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrir dentro del navegador|  

### **Archivos XLS**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Save XLS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions, Utils } = AsposeCells;

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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Simulate the JavaScript "response" which is null in this example
            let response = null;

            if (response != null) {
                // Server-side streaming scenario (not used in browser example)
                // Save in Excel2003 XLS format to response stream with options
                const options = new XlsSaveOptions();
                workbook.save(response, "output.xls", AsposeCells.ContentDisposition.Inline, options);
                response.end();
                document.getElementById('result').innerHTML = '<p style="color: green;">File written to response stream.</p>';
            } else {
                // Browser: save workbook and provide download link
                const options = new XlsSaveOptions();
                const outputData = workbook.save(SaveFormat.Excel97To2003, options);
                const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';
                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved. Click the download link to get the file.</p>';
            }
        });
    </script>
</html>
```  

### **Archivos XLSX**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an Excel file to load or leave empty to create a new workbook. Click "Save as XLSX" to generate and download output.xlsx.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions, Utils } = AsposeCells;

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

            // Load workbook from selected file or create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Save the workbook in XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook generated successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```  

### **Archivos PDF**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Prepare PDF save options
            const pdfOptions = new PdfSaveOptions();

            // Save workbook as PDF and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, pdfOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **Nota**  

Debido a la ausencia de un objeto de respuesta estándar en JavaScript, esta funcionalidad no existe en Aspose.Cells for JavaScript vía C++. Puedes consultar el siguiente código para guardar el archivo en el stream y luego realizar operaciones en el stream.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a memory buffer in XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">File is ready. Click the download link to save the workbook.</p>';
        });
    </script>
</html>
```

---
title: Salvataggio del file nell’oggetto Response con JavaScript tramite C++
linktitle: Salvataggio File in un Oggetto di Risposta
type: docs
weight: 50
url: /it/javascript-cpp/saving-file-to-response-object/
description: Impara come generare dinamicamente file e inviarli direttamente a un browser cliente usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  

Aspose.Cells rende possibile manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto di risposta.  

{{% /alert %}}  

## **Salvataggio del file nell'oggetto di risposta**  

È anche possibile generare un file dinamicamente e inviarlo direttamente a un browser client. Per farlo, utilizza una versione sovraccaricata speciale del metodo [**Save**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) che accetta i seguenti parametri:  

- Oggetto di risposta JavaScript.  
- Nome file.  
- [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/), il tipo di content-disposition del file di output.  
- [**SaveOptions**](https://reference.aspose.com/cells/javascript-cpp/saveoptions/), il tipo di formato file.  

L'enumerazione [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/) determina se il file inviato al browser offre l'opzione di aprirlo direttamente nel browser stesso o in un'applicazione associata a .xls/.xlsx o altra estensione.  

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:  

|**Tipo**|**Descrizione**|  
| :- | :- |  
|Allegato|Invia il foglio di calcolo al browser e apre un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|  
|Inline|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo sul disco o aprirlo all'interno del browser|  

### **File XLS**  

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

### **File XLSX**  

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

### **File PDF**  

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

 A causa dell’assenza di un oggetto di risposta standard in JavaScript, questa funzionalità non esiste in Aspose.Cells for JavaScript tramite C++. Puoi fare riferimento al seguente codice per salvare il file nello stream, quindi eseguire operazioni sullo stream.  

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

---
title: Renderizzare il Modello di Formato Data Personalizzato g e ge mm dd
linktitle: Renderizzare il Modello di Formato Data Personalizzato g e ge mm dd  
description: Scopri come rappresentare modelli di formattazione data personalizzati g e ge in Aspose.Cells for JavaScript via C++ per controllare la visualizzazione delle date nei fogli di calcolo.  
keywords: Aspose.Cells, libreria JavaScript, foglio elettronico, formato data personalizzato, rendering, pattern g , pattern ge , controllo visualizzazione    
type: docs  
weight: 160  
url: /it/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells è ora in grado di renderizzare i modelli di formato data personalizzati come g, ge.mm.dd e simili. Si prega di controllare il file Excel di origine allegato (5112361.xlsx) e il PDF convertito (5112360.pdf) da Aspose.Cells per il tuo riferimento.

{{% /alert %}}  

Il seguente codice di esempio converte il file Excel di origine (5112361.xlsx) che contiene valori di data con modelli di formato personalizzati come g e ge.mm.dd in un PDF di output (5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

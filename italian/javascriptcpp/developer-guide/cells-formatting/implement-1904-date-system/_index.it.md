---
title: Implementa il sistema di data 1904 con JavaScript tramite C++
description: Aspose.Cells è una libreria JavaScript per lavorare con file di fogli di calcolo. Supporta la realizzazione del sistema di data 1904, consentendo agli utenti di calcolare e formattare in base al sistema di data 1 gennaio 1904. Questo articolo descrive come implementare il sistema di data 1904 utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, sistema di data 1904, foglio di calcolo, calcolo, formattazione, JavaScript tramite C++
type: docs
weight: 7000
url: /it/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supporta due sistemi di data: sistema di data 1900 (il sistema di data predefinito implementato in Excel per Windows) e sistema di data 1904. Il sistema di data 1904 è normalmente usato per garantire compatibilità con i file di Excel per Macintosh ed è il sistema predefinito se si utilizza Excel per Macintosh. Puoi impostare il sistema di data 1904 per i file Excel usando Aspose.Cells for JavaScript tramite C++. 

{{% /alert %}} 

Per implementare il sistema di data 1904 in Microsoft Excel (ad esempio, Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e selezionare la scheda **Calcolo**.
1. Selezionare l'opzione **sistema di data del 1904**.
1. Fai clic su **OK**.

|**Selezione del sistema di data del 1904 in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Vedere il seguente codice di esempio su come realizzare questo utilizzando le API di Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

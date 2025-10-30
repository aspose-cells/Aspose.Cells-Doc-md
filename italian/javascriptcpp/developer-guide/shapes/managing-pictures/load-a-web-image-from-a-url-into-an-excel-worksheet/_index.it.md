---
title: Carica un immagine web da un URL in un foglio di Excel con JavaScript tramite C++
linktitle: Carica un immagine web da un URL in un foglio di calcolo di Excel
type: docs
weight: 30
url: /it/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Come convertire un immagine da URL in immagine Excel reale usando Aspose.Cells for JavaScript tramite C++.
keywords: excel mostra immagine da URL, url in immagine excel, mostra immagine in excel da url, inserisci immagine da url in excel, converti url in immagine in excel, immagine excel da url, carica immagine da url in excel, JavaScript, Excel
---

## Caricare un'immagine da un URL in un foglio di lavoro di Excel

Aspose.Cells for JavaScript tramite C++ fornisce un metodo semplice e facile per caricare immagini da URL nei fogli di lavoro Excel. Questo articolo spiega come scaricare i dati dell'immagine in un flusso e quindi inserirli nel foglio di lavoro utilizzando l'API Aspose.Cells. Usando questo metodo, le immagini diventano parte del file Excel e non vengono scaricate ogni volta che si apre il foglio di lavoro.

## Codice di esempio

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Potrebbero esserci casi in cui si desidera sempre l'immagine aggiornata da un URL. Per ottenere ciò, si può seguire le istruzioni fornite nell'articolo [Inserisci un'immagine collegata da indirizzo web](/cells/it/javascript-cpp/insert-a-linked-picture-from-web-address/). Seguendo questo metodo, l'immagine viene caricata dall'URL ogni volta che si apre il foglio di lavoro.
{{% /alert %}}

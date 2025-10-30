---
title: Adattare automaticamente l altezza della riga quando si carica un file con JavaScript tramite C++
linktitle: Adattamento automatico dell altezza della riga in modo automatico durante il caricamento del file
type: docs
weight: 120
url: /it/javascript-cpp/autofit-row-height/
description: Impara come adattare le righe non personalizzate automaticamente quando si carica un file usando Aspose.Cells for JavaScript via C++.
keywords: Adattamento automatico dell altezza della riga durante il caricamento del file JavaScript tramite C++, regolando automaticamente l altezza della riga all apertura del file Excel JavaScript via C++ 
---

## **Possibili Scenari di Utilizzo**
L'altezza della riga si adatta automaticamente al carattere del contenuto, ma quando l'altezza della riga memorizzata non corrisponde all'altezza del contenuto nel file, MS Excel adatterà automaticamente l'altezza della riga al caricamento del file, mentre Aspose.Cells for JavaScript via C++ non lo regolerà automaticamente per migliorare le prestazioni. Se hai bisogno di usare il programma Aspose.Cells per adattare automaticamente le altezze delle righe al caricamento dei file, puoi ottenere questo attraverso il parametro [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) nel tuo codice.

Puoi fare riferimento ai seguenti dati immagine. Possiamo osservare che l’altezza della riga memorizzata alla linea 11 è 15, ma Excel ha regolato automaticamente l’altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

## **Regolare l'altezza della riga usando Aspose.Cells for JavaScript via C++**
Se carichi direttamente il file e lo salvi in PDF, i dati non saranno completamente visualizzati in PDF perché la sua altezza della linea memorizzata è di soli 15.
<br>
<img src="2.png" width=70% />
<br>
Se imposti il parametro [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) su true quando carichi il file, allora Aspose.Cells adatterà automaticamente l'altezza della riga. L'altezza modificata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

## **Codice di esempio JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```

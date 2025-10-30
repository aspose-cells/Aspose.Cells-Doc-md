---
title: Leggere fogli di calcolo Numbers sviluppati da Apple Inc. usando Aspose.Cells for JavaScript tramite C++
linktitle: Leggi il foglio elettronico Numbers sviluppato da Apple Inc. utilizzando Aspose.Cells
type: docs
weight: 140
url: /it/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Impara come leggere fogli di calcolo Numbers sviluppati da Apple Inc. usando Aspose.Cells for JavaScript tramite C++. 
---

## **Possibili Scenari di Utilizzo**

Numbers è un'applicazione di fogli di calcolo sviluppata da Apple Inc. Aspose.Cells può leggere i fogli di calcolo Numbers, ma non supporta la scrittura su di essi. Può leggere i dati, lo stile e le formule dei fogli di calcolo Numbers.

## **Leggere fogli di calcolo Numbers sviluppati da Apple Inc. usando Aspose.Cells for JavaScript tramite C++**

Il seguente esempio di codice carica l'[Esempio di Foglio di Calcolo Numbers](sampleNumbersByAppleInc.numbers) e lo converte in [Formato PDF di Output](outputNumbersByAppleInc.pdf). Dovrai utilizzare la classe [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) e specificare [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) come parametro nel suo costruttore per caricarlo correttamente. Scarica entrambi dai link forniti. Puoi provare il codice con qualsiasi foglio di calcolo Numbers. Leggi anche i commenti del codice per ulteriori aiuti.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

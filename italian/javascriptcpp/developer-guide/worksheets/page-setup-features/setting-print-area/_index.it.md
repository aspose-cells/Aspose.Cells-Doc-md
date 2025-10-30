---
title: Come impostare l’area di stampa con JavaScript tramite C++
linktitle: Come impostare l area di stampa
type: docs
weight: 200
url: /it/javascript-cpp/how-to-set-print-area/
description: Questo articolo mostra codice che spiega come impostare l area di stampa usando la libreria Aspose.Cells per JavaScript via C++.
keywords: Limitare l intervallo di stampa, impostare l intervallo di stampa, cancellare l intervallo di stampa, impostare e cancellare l’intervallo di stampa usando JavaScript via C++, JavaScript via C++ Come impostare l’area di stampa, impostare e cancellare l’area di stampa usando JavaScript via C++, Come cancellare l’area di stampa in JavaScript via C++, Come aggiungere area di stampa usando JavaScript via C++, Come rimuovere area di stampa usando JavaScript via C++, Come impostare l’area di stampa in Excel, Come cancellare l’area di stampa in Excel.
---

## **Possibili Scenari di Utilizzo**

Impostare un'area di stampa in un documento, come un foglio di calcolo Excel, aiuta a controllare quali contenuti vengono inclusi durante la stampa. Ecco alcuni motivi per impostare un'area di stampa:

1. Concentrarsi su dati specifici: puoi stampare solo le sezioni più rilevanti, evitando contenuti non necessari.
1. Layout migliorato: aiuta a organizzare e adattare i contenuti ordinatamente sulle pagine di stampa, evitando interruzioni o salti di pagina indesiderati.
1. Risparmiare risorse: limitando l'area di stampa, puoi ridurre l'uso di carta e inchiostro.
1. Presentazione professionale: garantisce che vengano stampate solo le versioni rifinite e finali dei dati, importante particolarmente per report o presentazioni.
1. Coerenza: quando si stampa lo stesso documento più volte, avere un'area di stampa impostata garantisce coerenza nell'output.

<br>
Impostare un'area di stampa è particolarmente utile in documenti più grandi dove solo una porzione deve essere condivisa o revisionata in forma stampata.

## **Come impostare l'area di stampa in Excel**

Per impostare un'area di stampa in Excel, segui questi passaggi:

1. Seleziona le celle: clicca e trascina per selezionare l'intervallo di celle che desideri impostare come area di stampa.
1. Apri la scheda Layout di pagina: vai alla scheda "Layout di pagina" nella barra multifunzione nella parte superiore della finestra di Excel.
1. Imposta l'area di stampa: nel gruppo "Imposta pagina", clicca su "Area di stampa". Dal menu a discesa, seleziona "Imposta area di stampa".
<br>
<img src="3.png" width=60% />

1. Aggiungi all'area di stampa: se desideri aggiungere ulteriori celle all'area di stampa esistente, seleziona le celle aggiuntive, vai su "Area di stampa" nella scheda "Layout di pagina" e scegli "Aggiungi all'area di stampa".

<br>
Questa azione definirà le celle selezionate come area di stampa. Quando stamperai il foglio di lavoro, verrà stampata solo questa area definita.

## **Come eliminare l'area di stampa in Excel**

Per eliminare l'area di stampa in Excel, segui questi passaggi:

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.
1. Elimina l'area di stampa: nel gruppo "Impostazione pagina", clicca su "Area di stampa". Dal menu a tendina, seleziona "Elimina area di stampa".
<br>
<img src="4.png" width=60% />

<br>
Questa azione rimuoverà qualsiasi area di stampa precedentemente impostata, consentendo di stampare l'intero foglio di lavoro.

## **Cosa succede dopo aver eliminato l'area di stampa**

Eliminando l'area di stampa in un'applicazione come Excel usando Aspose.Cells, l'intero foglio di lavoro verrà incluso nella stampa del documento. Se è impostata un'area di stampa, verrà stampato solo l'intervallo di celle specificato. Eliminando l'area di stampa, si garantisce che nessun intervallo specifico sia definito, e il comportamento di stampa predefinito, che include l'intero foglio, verrà applicato.

1. Comportamento di stampa predefinito: l'intero foglio di lavoro sarà considerato per la stampa. Ciò significa che tutte le celle con dati o formattazioni verranno stampate.
1. Nessun limite di area di stampa: i limiti dell'area di stampa precedentemente definiti verranno rimossi. Se c'erano righe e colonne specifiche destinate alla stampa, non saranno più vincolate a quei limiti.
1. Stampa di tutto il contenuto: tutto il contenuto, inclusi intestazioni, piè di pagina e altri dati all'interno del foglio di lavoro, sarà incluso nel lavoro di stampa.

## **Come impostare l’area di stampa usando Aspose.Cells for JavaScript via C++**

Per impostare l'area di stampa in un foglio di lavoro specificato: Prima, carica il [file di esempio](input.xlsx), quindi devi modificare la proprietà [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per il foglio di lavoro desiderato. Impostando questa proprietà a una stringa di intervallo verrà impostata l'area di stampa.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Il risultato dell'output:
<br>
<img src="1.png" width=60% />

## **Come Cancellare l'Area di Stampa Usando Aspose.Cells for JavaScript tramite C++**

Per eliminare l'area di stampa in un foglio di lavoro specificato: Innanzitutto, carica il [file di esempio](input.xlsx), e poi devi modificare la proprietà [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per il foglio desiderato. Impostare questa proprietà a una stringa vuota eliminerà l'area di stampa.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Il risultato dell'output:
<br>
<img src="2.png" width=60% />

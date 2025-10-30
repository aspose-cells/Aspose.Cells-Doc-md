---
title: Come scalare un Foglio di Lavoro con JavaScript tramite C++
linktitle: Come ridimensionare un foglio di lavoro
type: docs
weight: 130
url: /it/javascript-cpp/how-to-scale-a-worksheet/
description: Questo articolo ti mostra come scalare un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++.
keywords: Scala un foglio di lavoro con JavaScript, Come scalare un foglio di lavoro usando JavaScript tramite C++, Scala un foglio di lavoro in JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**
Ridimensionare un foglio di lavoro può essere utile per vari motivi, a seconda del contesto in cui si lavora. Ecco alcuni motivi comuni per ridimensionare un foglio di lavoro:
1. Adatta a pagina: assicurarsi che tutto il contenuto stia su una singola pagina o un numero specifico di pagine durante la stampa, rendendo più facile la lettura e la gestione senza dover sfogliare più pagine.

1. Presentazione: Per rendere il foglio di lavoro più organizzato e professionale, in particolare quando viene condiviso con altri in riunioni o report.

1. Leggibilità: Per regolare la dimensione del testo e degli altri elementi per una migliore leggibilità, soprattutto per le persone che potrebbero avere difficoltà a leggere caratteri più piccoli.

1. Gestione dello Spazio: Per ottimizzare l'uso dello spazio su un foglio di lavoro, assicurando che non ci siano spazi bianchi inutili e che tutte le informazioni importanti siano visibili senza scorrimenti eccessivi.

1. Visualizzazione dei Dati: Nel caso di grafici e diagrammi, la scala può aiutare a renderli più comprensibili regolando la dimensione per adattarsi correttamente allo spazio disponibile.

1. Coerenza: Per mantenere un aspetto uniforme in più fogli di lavoro o documenti, cosa particolarmente importante in ambienti professionali ed educativi.

## **Come scalare un foglio di lavoro in Excel**
La scalatura di un foglio di lavoro in Excel può aiutarti ad adattare i contenuti su una singola pagina o su un numero specificato di pagine durante la stampa. Ecco i passaggi per scalare un foglio di lavoro:

1. Apri il Tuo Foglio di Lavoro: Apri il foglio di lavoro Excel che desideri scalare.

1. Vai alla scheda Layout di Pagina: Clicca sulla scheda Layout di Pagina nella Barra multifunzione.

1. Gruppo Scala per Adatta: Nella scheda Layout di Pagina, trova il gruppo Scala per Adatta. Qui hai opzioni per regolare la scala. Larghezza: Questa opzione permette di specificare quante pagine di larghezza avrà il foglio stampato. Altezza: Questa opzione permette di specificare quante pagine di altezza avrà il foglio stampato. Scala: Puoi anche impostare una percentuale personalizzata di scalatura.
<br>
<img src="1.png" width=60% />

1. Regola Larghezza e Altezza: Imposta la Larghezza e l'Altezza al numero desiderato di pagine. Ad esempio, imposta entrambi a 1 pagina se vuoi che il foglio di lavoro si adatti su una pagina sola.

1. Regola la Percentuale di Scalatura (se necessario): Se preferisci impostare una percentuale di scalatura specifica, regola la casella Scala. Ad esempio, impostarla al 50% farà tutto la metà delle dimensioni originali.


## **Come scalare un foglio di lavoro usando JavaScript tramite C++**
Aspose.Cells for JavaScript via C++ è una libreria potente per lavorare con i file Excel programmaticamente. Per scalare un foglio di lavoro usando Aspose.Cells, devi seguire questi passaggi: carica [file di esempio](sample.xlsx) e regola le impostazioni di stampa in modo che il contenuto si adatti al numero desiderato di pagine o a una percentuale specifica delle dimensioni originali.

### **Esempio: Adatta a una Pagina**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Esempio: Scala alla Percentuale**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />

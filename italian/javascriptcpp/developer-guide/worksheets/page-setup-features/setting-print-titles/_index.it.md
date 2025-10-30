---
title: Come impostare i Titoli di Stampa con JavaScript tramite C++
linktitle: Come impostare i titoli di stampa
type: docs
weight: 200
url: /it/javascript-cpp/how-to-set-print-titles/
description: Questo articolo ti mostra come impostare i titoli di stampa utilizzando la libreria Aspose.Cells per JavaScript tramite C++.
keywords: Stampa di righe e colonne ripetutamente, Come impostare i Titoli di Stampa con JavaScript, Imposta e Cancella i Titoli di Stampa con JavaScript, Come cancellare i Titoli di Stampa in JavaScript, Come aggiungere titoli di stampa con JavaScript, Come rimuovere titoli di stampa con JavaScript, Come impostare i Titoli di Stampa in Excel, Come cancellare i Titoli di Stampa in Excel.  
---

## **Possibili Scenari di Utilizzo**  

Impostare i titoli di stampa in Excel assicura che righe o colonne specifiche siano ripetute su ogni pagina stampata, molto utile per grandi fogli di calcolo che si estendono su più pagine. Ecco alcune ragioni per cui potresti impostarli:  

1. Migliore leggibilità: i titoli di stampa aiutano i lettori a comprendere i dati mantenendo visibili le intestazioni su tutte le pagine, rendendo più facile interpretare le informazioni di ogni pagina senza dover tornare indietro alla prima.  

1. Presentazione professionale: mostrare costantemente intestazioni o etichette su ogni pagina crea un aspetto più curato e professionale per i documenti stampati.  

1. Navigazione migliorata: per documenti con dati estesi, ripetere le intestazioni su ogni pagina consente una navigazione e un riferimento più rapidi, riducendo la necessità di sfogliare avanti e indietro tra le pagine.  

1. Minori errori: quando le intestazioni sono presenti su ogni pagina, si riducono le possibilità di malintesi o errori di inserimento dati, poiché gli utenti possono facilmente vedere il contesto dei dati.  

1. Coerenza: garantire che le informazioni importanti, come intestazioni di colonne o etichette di riga, siano sempre visibili mantiene coerenza e chiarezza nel documento.  

## **Come impostare i titoli di stampa in Excel**  

Per impostare i titoli di stampa in Excel, segui questi passaggi:  

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.  
1. Accedi ai Titoli di Stampa: Nel gruppo "Imposta Pagina", clicca su "Titoli di Stampa".  
1. Imposta le righe da ripetere: nella finestra di dialogo "Impostazione pagina", vai alla scheda "Foglio". Nella sezione "Titoli di stampa", specifica le righe da ripetere in alto cliccando sulla casella accanto a "Righe da ripetere in alto" e selezionando le righe desiderate.  
1. Imposta le colonne da ripetere (se necessario): allo stesso modo, puoi specificare le colonne da ripetere a sinistra cliccando sulla casella accanto a "Colonne da ripetere a sinistra" e selezionando la colonna o le colonne desiderate.  
<br>  
<img src="3.png" width=60% />  

1. Conferma e Stampa: Clicca su "OK" per applicare le impostazioni. Quando stampi il foglio di lavoro, le righe o colonne specificate appariranno su ogni pagina stampata.  

## **Come Rimuovere i Titoli di Stampa in Excel**  

Per rimuovere i titoli di stampa in Excel, devi eliminare le righe o colonne impostate per ripetersi in ogni pagina stampata. Ecco come fare:  

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.  
1. Accedi ai Titoli di Stampa: Nel gruppo "Imposta Pagina", clicca su "Titoli di Stampa".  
1. Rimuovi i Titoli di Stampa: Nella finestra di dialogo "Imposta Pagina", vai alla scheda "Foglio". Cancella i campi di testo per "Righe da ripetere in alto" e "Colonne da ripetere a sinistra" eliminando qualsiasi contenuto.  
<br>  
<img src="4.png" width=60% />  

1. Conferma e Chiudi: Clicca su "OK" per applicare le modifiche.  

## **Come impostare i Titoli di Stampa usando Aspose.Cells for JavaScript tramite C++**  

Per impostare i titoli di stampa in un foglio di lavoro specificato: Prima, carica il [file di esempio](input.xlsx), e poi devi modificare le proprietà [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) e [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per il foglio di lavoro desiderato. Impostando queste proprietà a una stringa di intervallo, si impostano i titoli di stampa.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Il risultato dell'output:  
<br>  
<img src="1.png" width=60% />  

## **Come cancellare i Titoli di Stampa usando Aspose.Cells for JavaScript tramite C++**  

Per cancellare i titoli di stampa in un foglio di lavoro specificato: Prima, carica il [file di esempio](input.xlsx), e poi devi modificare le proprietà [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) e [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per il foglio desiderato. Impostando queste proprietà a una stringa vuota, si rimuovono i titoli di stampa.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Il risultato dell'output:  
<br>  
<img src="2.png" width=60% />

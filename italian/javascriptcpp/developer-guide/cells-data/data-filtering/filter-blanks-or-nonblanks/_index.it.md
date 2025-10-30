---
title: Come Filtrare Spazi Vuoti o Non Spazi Vuoti
type: docs
weight: 85
url: /it/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Impara come filtrare i vuoti e i non vuoti usando lo script Aspose.Cells for Java tramite API C++.
keywords: Filtra Celle Vuote, Filtra Celle Non Vuote, Filtra Celle Vuote nel foglio di lavoro, Filtra Celle Non Vuote nel foglio di lavoro, Filtra Celle Vuote in excel, Filtra Celle Non Vuote in excel, Filtra Celle Vuote e Non Vuote in excel
---

## **Possibili Scenari di Utilizzo**
Filtrare i dati in Excel è uno strumento prezioso che migliora l'analisi, l'esplorazione e la presentazione dei dati consentendo agli utenti di concentrarsi su sottoinsiemi specifici di dati in base ai loro criteri, rendendo il processo generale di manipolazione e interpretazione dei dati più efficiente ed efficace.

## **Come Filtrare Spazi Vuoti o Non Spazi Vuoti in Excel**
In Excel, è possibile filtrare facilmente gli spazi vuoti o non spazi vuoti utilizzando le opzioni di filtraggio. Ecco come puoi farlo:

### **Come Filtrare Spazi Vuoti in Excel**
1. Seleziona l'Intervallo: Fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare gli spazi vuoti.
1. Apri il Menu Filtro: Vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni di Filtro: Fai clic sul pulsante "Filtro". Questo aggiungerà delle freccette di filtro all'intervallo selezionato.
1. Filtra Spazi Vuoti: Fai clic sulla freccia di filtro nella colonna in cui desideri filtrare gli spazi vuoti. Deseleziona tutte le opzioni tranne "Spazi vuoti" e fai clic su OK. Questo mostrerà solo le celle vuote in quella colonna.
<br>
<image src="2.png" width="70%" />
1. Il risultato è il seguente:
<br>
<image src="3.png" width="70%" />

### **Come Filtrare Non Spazi Vuoti in Excel**
1. Seleziona l'Intervallo: Fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare non spazi vuoti.
1. Apri il Menu Filtro: Vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni di Filtro: Fai clic sul pulsante "Filtro". Questo aggiungerà delle freccette di filtro all'intervallo selezionato.
1. Filtra Non Spazi Vuoti: Fai clic sulla freccia di filtro nella colonna in cui desideri filtrare non spazi vuoti. Deseleziona tutte le opzioni tranne "Non spazi vuoti" o "Personalizzato" e imposta le condizioni di conseguenza. Fai clic su OK. Questo mostrerà solo le celle che non sono vuote in quella colonna.
<br>
<image src="4.png" width="70%" />
1. Il risultato è il seguente:
<br>
<image src="5.png" width="70%" />

## **Come filtrare i vuoti usando lo script Aspose.Cells for Java tramite C++**
Se una colonna contiene testo tale che alcune celle sono vuote, e si desidera filtrare per selezionare solo le righe con celle vuote, le funzioni [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) e [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) possono essere usate come mostrato di seguito. 

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Il codice di esempio utilizza tre metodi per filtrare le celle vuote. Poi salva il workbook come [file Excel di output](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **Come filtrare i non vuoti usando lo script Aspose.Cells for Java tramite C++**

Vivi di seguito un esempio di codice che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati fittizi. Dopo aver caricato il file, chiama la funzione [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) per filtrare i dati non vuoti, e infine salva il libro di lavoro come [file Excel di output](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

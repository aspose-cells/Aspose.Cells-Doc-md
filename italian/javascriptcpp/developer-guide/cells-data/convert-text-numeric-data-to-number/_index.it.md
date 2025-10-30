---
title: Converti dati numerici testuali in numeri
type: docs
weight: 900
url: /it/javascript-cpp/convert-text-numeric-data-to-number/
description: Scopri come convertire i numeri memorizzati come testo in Excel in numeri utilizzando l API Aspose.Cells for JavaScript attraverso C++.
keywords: excel converti testo in numero, excel converti testo in numero codice JavaScript, excel converti dati numerici testuali in numero, excel converti dati numerici testuali in numero codice JavaScript, excel converti testo numerico in numero, excel converti testo numerico in numero codice JavaScript, excel converti testo numerico in numero con codice JavaScript, converti testo numerico in numero in excel con codice JavaScript, converti testo numerico in numero in excel con codice JavaScript, converti stringa numerica in numero in excel con codice JavaScript, excel converti dati numerici testuali in numero codice JavaScript, excel converti stringa numerica in numero JavaScript
---

## **Possibili Scenari di Utilizzo**
A volte, vuoi convertire i dati numerici inseriti come testo in numeri. Puoi inserire numeri come testo in Microsoft Excel mettendo un apostrofo prima di un numero, ad esempio **'12345**. Excel tratta quindi il numero come stringa. Aspose.Cells for JavaScript attraverso C++ ti permette di convertire le stringhe in numeri.


## Come Convertire i numeri memorizzati come testo in numeri in Excel
Puoi convertire i numeri memorizzati come testo in numeri seguendo alcuni semplici passaggi.
1. Seleziona una singola cella o un intervallo di celle che ha un indicatore di errore nell'angolo in alto a sinistra.
1. Accanto alla cella o all'intervallo di celle selezionato, fai clic sul pulsante di errore che appare. Nel menu, fai clic su Converti in numero. 
<br>
<img src="4.png" width=70% />
1. Se il pulsante di avviso non è disponibile, seleziona una colonna con questo problema. Se non vuoi convertire l'intera colonna, puoi selezionare una o più celle invece. Assicurati solo che le celle che selezioni siano nella stessa colonna, altrimenti questo processo non funzionerà. Il pulsante Testo in colonne viene generalmente utilizzato per dividere una colonna, ma può anche essere utilizzato per convertire una singola colonna di testo in numeri. Sulla scheda Dati, fai clic su Testo in colonne.
<br>
<img src="1.png" width=70% />
1. Fai clic sul pulsante Fine nella finestra di dialogo.
<br>
<img src="2.png" width=70% />
1. I numeri memorizzati come testo vengono trasformati in numeri.
<br>
<img src="3.png" width=70% />

## Come Convertire numeri memorizzati come testo in numeri usando Aspose.Cells for JavaScript attraverso C++
Aspose.Cells for JavaScript attraverso C++ fornisce il metodo [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) che può essere utilizzato per convertire tutti i dati numerici in stringa o testo in numeri.

La seguente immagine mostra numeri di stringa nelle celle **A1:A17**. I numeri di stringa sono allineati a sinistra.
<br>
<img src="5.png" width=70% />

Questi numeri di stringa sono stati convertiti in numeri utilizzando [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) nella schermata seguente. Come puoi vedere, ora sono allineati a destra.
<br>
<img src="6.png" width=70% />

## Codice JavaScript per convertire dati numerici stringa in numeri effettivi

Il seguente codice di esempio illustra come convertire tutti i dati numerici di stringa in numeri effettivi in tutte le schede.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

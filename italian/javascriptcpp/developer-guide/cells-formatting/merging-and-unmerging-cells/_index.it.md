---
title: Unisci e Disunisci Celle con JavaScript tramite C++
linktitle: Unione e separazione di celle
description: Aspose.Cells è una libreria JavaScript per lavorare con file di fogli di calcolo, che supporta l unione e la disunione delle celle. Questo articolo introdurrà come unire e disunire le celle usando la libreria Aspose.Cells, con opzioni per personalizzare lo stile della cella unita.
keywords: Aspose.Cells, libreria JavaScript, foglio di calcolo, unire celle, disunire celle, impostazioni di stile, stili personalizzati
type: docs
weight: 190
url: /it/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta questa funzionalità e può anche unire celle in un foglio di lavoro. È possibile anche separare o dividere le celle unite. Il riferimento della cella unita è il riferimento per la cella in alto a sinistra nell'intervallo selezionato originale.

{{% /alert %}} 
## **Introduzione**
Non si desidera sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, si potrebbe voler inserire un titolo in una cella che si estende su diverse colonne. Oppure, se si crea una fattura, potrebbe essere necessario meno colonne per il totale. Per rendere una cella da due o più celle, unirle. Microsoft Excel consente agli utenti di selezionare i file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Nota che quando le celle sono unite, vengono conservati solo i dati nella cella in alto a sinistra. Se ci sono dati nelle altre celle dell'intervallo, questi dati vengono eliminati. La formattazione, allo stesso modo, si basa sulla cella di riferimento in modo che, quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate sulla cella unita. Quando la cella viene divisa, le nuove celle mantengono le impostazioni di formattazione originali.

{{% /alert %}} 
## **Unione di celle in un foglio di lavoro**
### **Unione di celle in Microsoft Excel**
I seguenti passaggi descrivono come unire celle nel foglio di lavoro utilizzando MS Excel.

1. Copiare i dati che si desidera nella cella in alto a sinistra nell'intervallo.
1. Selezionare le celle che si desidera unire.
1. Per unire le celle in una riga o colonna e centrare i contenuti della cella, fare clic sull'icona **Unisci e centrato** sulla barra degli strumenti **Formattazione**.

### **Unione di celle con Aspose.Cells**
La classe Aspose.Cells.Cells dispone di alcuni metodi utili per il compito. Ad esempio, il metodo `merge()` unisce le celle in una singola cella all'interno di un intervallo specificato.

Nell'esempio seguente viene mostrato come unire le celle (C6:E7) in un foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Dividere (Separare) celle unite**
### **Utilizzando Microsoft Excel**
I seguenti passaggi descrivono come dividere le celle unite usando Microsoft Excel.

1. Seleziona la cella unita.
   Quando le celle sono state unite, **Unisci e centra** è selezionato sulla barra degli strumenti **Formattazione**.
1. Fai clic su **Unisci e centra** sulla barra degli strumenti **Formattazione**.

### **Usare Aspose.Cells**
La classe Aspose.Cells.Cells ha un metodo chiamato `unmerge()` che divide le celle nel loro stato originale. Il metodo divide le celle utilizzando il riferimento della cella all'interno dell'intervallo di celle unito.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nel precedente esempio e divide le celle unite.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Rileva le celle unite in un foglio di lavoro](/cells/it/javascript-cpp/detect-merged-cells-in-a-worksheet/)

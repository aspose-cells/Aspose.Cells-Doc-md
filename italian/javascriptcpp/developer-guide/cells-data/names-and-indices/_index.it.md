---
title: Conversione tra nome della cella e indice riga/colonna
linktitle: Nome della Cella e Conversione Indice
type: docs
weight: 10
url: /it/javascript-cpp/names-and-indices/
description: Impara come ottenere la conversione tra nome della cella e indice riga/colonna tramite lo Script Aspose.Cells for Java tramite API C++.
keywords: JavaScript tramite C++ Ottieni il nome della cella dagli indici di riga e colonna, ottieni gli indici di riga e colonna dal nome della cella, crea nomi di fogli di lavoro sicuri, aggiungi nomi di fogli di lavoro sicuri
---

## **Ottieni il Nome della Cella dagli Indici di Riga e Colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.
Aspose.Cells for JavaScript in C++ fornisce il metodo CellsHelper.cellIndexToName che consente agli sviluppatori di ottenere il nome della cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells for JavaScript in C++ inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.cellIndexToName per accedere al nome della cella dato un noto indice di riga e colonna. Il codice genera il seguente output.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Ottieni Gli Indici di Riga e Colonna dal Nome della Cella**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells for JavaScript in C++ fornisce il metodo CellsHelper.cellNameToIndex che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells for JavaScript in C++ inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.cellNameToIndex per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Crea nomi di foglio sicuri**
A volte è necessario assegnare il nome del foglio durante l'esecuzione. In questo scenario, potrebbero esserci nomi di fogli contenenti caratteri aggiuntivi come <>+(?”. È necessario sostituire qualsiasi carattere non consentito come nome di foglio con un carattere predefinito fornito dall'utente. Similarly, la lunghezza può aumentare oltre i 31 caratteri, che devono essere troncati. Apache POI offre alcune funzionalità per creare nomi sicuri, quindi una funzione analoga è disponibile in Aspose.Cells for JavaScript in C++ per gestire tutte queste problematiche. Il seguente esempio di codice dimostra questa funzione:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Output:

questo è il primo nome che viene cre

` `<> + (adj.Private _ " Privato"

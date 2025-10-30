---
title: Accesso alle celle di un foglio di lavoro
type: docs
weight: 10
url: /it/javascript-cpp/accessing-cells-of-a-worksheet/
description: Questo articolo mostra come ottenere il massimo intervallo di visualizzazione del foglio di lavoro e accedere alle celle tramite l API Aspose.Cells for JavaScript tramite C++.
keywords: Ottieni l oggetto Cell, accedi alle celle, ottieni l intervallo di visualizzazione massimo del foglio di calcolo. 
---

{{% alert color="primary" %}}

 Sappiamo che tutti i fogli di lavoro possono contenere dati che vengono memorizzati essenzialmente nelle celle (con cui è costituito un foglio di lavoro). Una cella è una parte base di un foglio di lavoro usata per costruire l'intero foglio come una sequenza di righe e colonne. Prima di cercare di accedere ai dati di un foglio di lavoro, dobbiamo ottenere l'accesso alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in runtime usando Aspose.Cells for JavaScript tramite C++.

{{% /alert %}}

## **Come accedere alle celle**

Aspose.Cells for JavaScript tramite C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre una collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) che rappresenta tutte le celle nel foglio di lavoro.

Possiamo usare la collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) per accedere alle celle di un foglio di lavoro. Aspose.Cells for JavaScript tramite C++ fornisce tre approcci di base per l'accesso alle celle di un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1. Usando un indice di cella nella collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)

 Abbiamo menzionato che il 3° approccio è il più veloce e il 1° approccio è il più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti della degradazione delle prestazioni, qualunque sia l'approccio che usi.

### **Come ottenere l'oggetto cella per nome della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando il suo nome di cella alla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) come indice.

Se crei un foglio di lavoro vuoto all'inizio, il conteggio della collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) è zero. Quando usi questo approccio per accedere a una cella, verificherà se questa cella esiste nella collezione o meno. Se sì, restituisce l'oggetto cella nella collezione, altrimenti crea un nuovo oggetto [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), aggiunge l'oggetto alla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) e poi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se sei familiare con Microsoft Excel, ma è il più lento rispetto agli altri approcci.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Come ottenere l'oggetto cella per indice di riga e colonna della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della riga e della colonna alla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Questo approccio funziona allo stesso modo del primo approccio.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Come ottenere l'oggetto cella per indice cella nella collezione celle**

Una cella può anche essere accessata passando l'indice numerico della cella alla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

Se utilizzi questo metodo per accedere alle celle, potrebbe essere sollevata un'eccezione se l'indice numerico della cella è fuori dal range. Questo metodo è il più rapido per accedere alle celle, ma è importante sapere che se usi questo metodo, l'indice numerico potrebbe cambiare dopo che nuove celle sono state aggiunte alla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Le oggetti cella nella collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sono ordinati internamente per indici di riga e colonna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Come ottenere l'intervallo di visualizzazione massimo del foglio di lavoro**

Aspose.Cells for JavaScript tramite C++ permette agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo - l'intervallo di celle tra la prima e l'ultima con contenuto - è utile quando devi copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

Puoi accedere all'intervallo di visualizzazione massimo di un foglio di lavoro usando [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). Il seguente esempio di codice illustra come accedere alla proprietà [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```

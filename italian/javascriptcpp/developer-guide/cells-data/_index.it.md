---
title: Gestire i dati dei file di Excel
linktitle: Dati delle celle
type: docs
weight: 110
url: /it/javascript-cpp/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file Excel con la libreria Aspose.Cells per JavaScript tramite C++.
keywords: Aspose.Cells JavaScript tramite C++, gestire i dati di un file Excel, aggiungere dati al file Excel, ottenere dati dal file Excel, come migliorare l efficienza dell aggiunta di dati, gestire i dati delle celle, aggiornare i dati delle celle, ottenere i dati delle celle, inserire dati nelle celle
---

{{% alert color="primary" %}}

In [Accesso alle Celle di un Foglio di Lavoro](/cells/it/javascript-cpp/accessing-cells-of-a-worksheet/), abbiamo discusso le modalità di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

## **Come aggiungere dati alle celle**

Aspose.Cells for JavaScript tramite C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione di [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre una collezione di [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento della collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Aspose.Cells offre versioni sovrapposte del metodo [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) che permettono di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovrapposte del metodo [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-), è possibile aggiungere valori booleani, stringhe, double, interi o data/ora, ecc. alle celle.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Come migliorare l'efficienza**

Se si utilizza il metodo [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) per inserire una grande quantità di dati in un foglio di lavoro, si dovrebbe prima aggiungere i valori alle celle riga per riga e poi colonna per colonna. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

## **Come recuperare i dati dalle celle**

Aspose.Cells for JavaScript via C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che permette di accedere ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento nella raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) fornisce diverse proprietà che permettono agli sviluppatori di recuperare valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): restituisce il valore stringa della cella.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): restituisce il valore double della cella.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): restituisce il valore booleano della cella.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): restituisce il valore data/ora della cella.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): restituisce il valore float della cella.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) o [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) lanciano un'eccezione.

Il tipo di dati contenuti in una cella può essere verificato anche utilizzando il metodo [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). In realtà, il metodo [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) si basa sull'enumerazione [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype) i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|IsBool| Specifica che il valore della cella è booleano.
|IsDateTime| Specifica che il valore della cella è data/ora.
|IsNull| Rappresenta una cella vuota.
|IsNumeric| Specifica che il valore della cella è numerico.
|IsString| Specifica che il valore della cella è una stringa.
|IsUnknown| Specifica che il valore della cella è sconosciuto.

Puoi anche usare i tipi di valori di cella predefiniti sopra per confrontarli con il tipo di dati presente in ogni cella.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Durante il lavoro sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi tipi di dati possono includere valori booleani, interi, in virgola mobile, testo o dati data/ora. Con Aspose.Cells, puoi ottenere i valori appropriati dalle celle in base ai loro tipi di dati.

{{% /alert %}}

## **Argomenti avanzati**
- [Accesso alle celle di un foglio di lavoro](/cells/it/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Converti Dati Numerici Testuali in Numero](/cells/it/javascript-cpp/convert-text-numeric-data-to-number/)
- [Creare i Subtotali](/cells/it/javascript-cpp/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/javascript-cpp/data-filtering/)
- [Ordinamento dati](/cells/it/javascript-cpp/sort-data-of-excel/)
- [Convalida Dati](/cells/it/javascript-cpp/data-validation/)
- [Trova o cerca dati](/cells/it/javascript-cpp/find-or-search-data/)
- [Ottieni il valore stringa della cella con e senza formattazione](/cells/it/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Aggiunta di testo ricco in formato HTML all'interno della cella](/cells/it/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Inserimento di collegamenti ipertestuali in Excel o OpenOffice](/cells/it/javascript-cpp/insert-hyperlinks-to-excel/)
- [Come e dove utilizzare gli enumeratori](/cells/it/javascript-cpp/how-and-where-to-use-enumerators/)
- [Misurare la larghezza e l'altezza del valore della cella in unità di pixel](/cells/it/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lettura dei valori della cella in più thread contemporaneamente](/cells/it/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversione tra nome della cella e indice riga/colonna](/cells/it/javascript-cpp/names-and-indices/)
- [Popolare prima i dati per riga e poi per colonna](/cells/it/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedere e aggiornare le porzioni di testo arricchito della cella](/cells/it/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)

---
title: Gestire le formule dei file Excel con JavaScript tramite C++
linktitle: Formule
type: docs
weight: 122
url: /it/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Impara come Gestire le formule dei file Excel tramite Aspose.Cells for JavaScript tramite C++. Aspose.Cells può semplicemente ottenere, impostare e calcolare le formule dei file Excel.
keywords: Come calcolare le formule in JavaScript tramite C++, Formule e Funzioni usando JavaScript tramite C++, JavaScript tramite C++ Gestisce le Funzioni incorporate, Come usare le Funzioni add in con JavaScript tramite C++, Come usare le formule array con via JavaScript tramite C++, Come usare la formula R1C1 in JavaScript tramite C++.
---

## **Introduzione**

Una delle caratteristiche più affascinanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce un set di funzioni e formule incorporate che aiutano gli utenti a eseguire calcoli complessi rapidamente. Aspose.Cells offre anche un enorme insieme di funzioni e formule integrate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells supporta inoltre funzioni add-in. Inoltre, Aspose.Cells supporta formule di array e R1C1.

## **Come utilizzare formule e funzioni**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento nella raccolta Cells rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

È possibile applicare formule alle celle utilizzando le proprietà e i metodi offerti dalla classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), discussi in dettaglio di seguito.

- Utilizzo di funzioni incorporate.
- Utilizzo di funzioni add-in.
- Lavorare con formule matriciali.
- Creazione di una formula R1C1.

## **Come utilizzare le funzioni incorporate**

Le funzioni o formule incorporate sono fornite come funzioni pronte per ridurre gli sforzi e il tempo degli sviluppatori. Vedi [elenco delle funzioni incorporate](/cells/it/javascript-cpp/supported-formula-functions/) supportate da Aspose.Cells. Le funzioni sono elencate in ordine alfabetico. Più funzioni saranno supportate in futuro.

Aspose.Cells supporta la maggior parte delle formule o funzioni offerte da Microsoft Excel. Gli sviluppatori possono usare queste formule tramite l'API o [spreadsheet designer](/cells/it/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto set di formule matematiche, di stringa, Boolean, data/ora, statistica, database, ricerca e riferimenti.

Utilizza la proprietà [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) per aggiungere una formula a una cella. **Formule complesse**, per esempio

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportate anche in Aspose.Cells. Quando si applica una formula a una cella, inizia sempre la stringa con un segno uguale (=) come fai quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Nell'esempio seguente, viene applicata una formula complessa alla prima cella di una raccolta di [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) fogli di lavoro. La formula utilizza una funzione built-in **IF** fornita da Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Come utilizzare le funzioni aggiuntive**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come componente aggiuntivo di Excel. Durante l'impostazione della funzione cell.formula, le funzioni incorporate funzionano correttamente, tuttavia è necessario impostare le funzioni o formule personalizzate usando le funzioni add-in.

Aspose.Cells fornisce funzioni per registrare funzioni add-in usando [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Successivamente, quando impostiamo cell.formula = qualsiasiFunzioneDaAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il seguente file XLAM deve essere scaricato per registrare la funzione add-in nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per controllare i risultati.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Come utilizzare la formula matriciale**

Le formule matriciali sono formule che prendono array, invece di numeri singoli, come argomenti delle funzioni che compongono la formula. Quando una formula matriciale viene visualizzata, è racchiusa da parentesi graffe ({}).

Alcune funzioni di Microsoft Excel restituiscono array di valori. Per calcolare più risultati con una formula matriciale, inserisci l'array in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti dell'array.

È possibile applicare una formula matriciale a una cella chiamando il metodo [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Il metodo [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) richiede i seguenti parametri:

- **Formula Matriciale**, la formula matriciale.
- **Numero di righe**, il numero di righe per popolare il risultato della formula matriciale.
- **Numero di colonne**, il numero di colonne per popolare il risultato della formula matriciale.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Come utilizzare la formula R1C1**

Aggiungi una formula di stile di riferimento **R1C1** a una cella con la proprietà [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Predecessori e Dipendenti](/cells/it/javascript-cpp/precedents-and-dependents/)
- [Imposta i collegamenti esterni nelle formule](/cells/it/javascript-cpp/set-external-links-in-formulas/)
- [Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe](/cells/it/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Impostazione della formula per il intervallo nominato](/cells/it/javascript-cpp/setting-formula-for-named-range/)
- [Impostazione della formula - Avviso per gli utenti non anglofoni](/cells/it/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Impostazione della formula condivisa](/cells/it/javascript-cpp/setting-shared-formula/)
- [Specificare il numero massimo di righe della formula condivisa](/cells/it/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Funzioni Excel supportate](/cells/it/javascript-cpp/supported-formula-functions/)

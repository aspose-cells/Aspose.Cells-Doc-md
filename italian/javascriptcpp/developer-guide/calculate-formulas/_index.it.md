---
title: Calcolare formule con JavaScript tramite C++
linktitle: Calcola le formule
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare formule in Microsoft Excel usando JavaScript tramite C++. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo usare i metodi forniti da Aspose.Cells per calcolare la formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, formule, calcoli, Calcolo Diretto della Formula, Calcolare le Formule ripetutamente, aggiungi formule JavaScript tramite C++
type: docs
weight: 125
url: /it/javascript-cpp/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells ha un motore di calcolo formule integrato. Non solo può ricalcolare le formule importate da modelli di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in runtime.

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel (Leggi [una lista delle funzioni supportate dal motore di calcolo](/cells/it/javascript-cpp/supported-formula-functions/)). Queste funzioni possono essere usate tramite API o fogli di calcolo progettati. Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimenti.

Usa la proprietà [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) o i metodi [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) per aggiungere una formula a una cella. Quando applichi una formula, inizia sempre la stringa con un segno di uguale (=) come quando crei una formula in Microsoft Excel e usa una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) della classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che elabora tutte le formule incorporate in un file Excel. Oppure, l'utente può chiamare il metodo [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) della classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) che elabora tutte le formule di un foglio. O, l'utente può anche chiamare il metodo [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) che processa la formula di una cella:

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Importante da Sapere per le Formule**

{{% alert color="primary" %}}

Le proprietà **Formula** e i metodi **formula(...)** della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) funzionano in modo diverso dai metodi **calculate** delle classi [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) e [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Le proprietà **Formula** e i metodi **formula(...)** semplicemente aggiungono la formula a una cella, ma non calcolano il risultato in fase di esecuzione. Per ottenere il risultato delle formule, si prega di chiamare i metodi **calculate**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte, hai bisogno di calcolare i risultati delle formule direttamente senza aggiungerle a un foglio di calcolo. I valori delle celle usate nella formula esistono già in un foglio di calcolo, e tutto ciò che devi fare è trovare il risultato di quei valori in base a una formula di Microsoft Excel senza aggiungere la formula in un foglio.

Puoi usare le API del motore di calcolo formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) a [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) calcolare i risultati di tali formule senza aggiungerle al foglio:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Il codice sopra produce il seguente output:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Come Calcolare le Formule ripetutamente**

Quando ci sono molte formule nel file di lavoro, e l'utente ha bisogno di calcolarle ripetutamente mentre modifica solo una piccola parte di esse, può essere utile per la performance abilitare la catena di calcolo delle formule: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita, la catena di calcolo è disattivata. Poiché creare la catena richiede anche tempo extra, la prima volta che si calcolano le formule ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) potrebbe consumare più tempo di CPU e memoria rispetto al calcolo delle formule senza una catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolare direttamente la formula senza creare una catena di calcolo) dovrebbe essere l'opzione migliore.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il Tempo di Calcolo del metodo Cell.calculate](/cells/it/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Individuazione di riferimento circolare](/cells/it/javascript-cpp/detecting-circular-reference/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompere o annullare il calcolo della formula del foglio di lavoro](/cells/it/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Impostare la modalità di calcolo della formula del foglio di lavoro](/cells/it/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilizzo della funzione FormulaText in Aspose.Cells](/cells/it/javascript-cpp/using-formulatext-function-in-aspose-cells/)

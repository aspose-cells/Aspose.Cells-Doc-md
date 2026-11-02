---
title: Trasporre Intervallo
description: Questo articolo spiega come trasporre o ruotare i dati da righe a colonne o viceversa nei file Excel utilizzando Aspose.Cells for JavaScript via C++ con tre approcci diversi.
linktitle: Transpose Range
url: /it/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, JavaScript via C++, foglio di calcolo, trasposizione intervallo, ruotare dati, funzione TRASPONI, formula array dinamica, formula array, Excel TRANSPOSE, Righe in Colonne
type: docs
weight: 80
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo in‑place `range.transpose()` e funziona su tutte le versioni di Excel, mentre il secondo usa `cell.setDynamicArrayFormula()` per scrivere una moderna formula di array dinamico `=TRANSPOSE(...)` che si espande automaticamente su Excel 365 o Excel 2021. Il terzo approccio utilizza `cell.setArrayFormula()` per scrivere una classica formula CSE (Ctrl+Shift+Enter) compatibile con le versioni più vecchie di Excel. Questo articolo illustra ciascun approccio con istruzioni passo‑a‑passo e esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo effettivamente i dati rispetto alla sua diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione, e il riferimento concettuale è documentato su [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Questo concetto può essere applicato programmaticamente a un intervallo di celle, risultato utile in molti scenari aziendali e di reporting.
- Riorientare report trimestrali o annuali in cui i trimestri normalmente scorrono orizzontalmente e le regioni verticalmente, o viceversa.  
- Scambiare l’orientamento degli assi in dashboard o grafici affinché una serie temporale scorra verticalmente anziché orizzontalmente.  
- Rimodellare dati importati da sistemi esterni per farli corrispondere al layout atteso da modelli di analisi o reportistica a valle.
Per rendere concreto il resto dell’articolo, tutti gli esempi utilizzano la seguente piccola tabella vendite‑per‑regione‑per‑trimestre. Nel workbook di esempio la tabella occupa l’intervallo **A1:D5**, con **A1** lasciato vuoto come angolo superiore sinistro, **B1:D1** contenenti le intestazioni delle regioni e **A2:A5** contenenti le intestazioni dei trimestri.
| Regione          | Europa    | Asia      | America del Nord |
|------------------|-----------|-----------|-------------------|
| Trimestre 1      | 21704714  | 8774099   | 12094215          |
| Trimestre 2      | 17987034  | 12214447  | 10873099          |
| Trimestre 3      | 19485029  | 14356879  | 15689543          |
| Trimestre 4      | 22567894  | 15763492  | 17456723          |
L’articolo quindi presenta tre modi diversi per trasporre questi dati usando Aspose.Cells for JavaScript via C++, ciascuno adatto a una diversa versione di Excel e caso d’uso.

## **Approccio 1 — Trasporre Intervallo in Situ (Range.transpose)**
Utilizzare questo approccio quando si desidera trasporre i dati senza coinvolgere la funzione foglio di lavoro `TRANSPOSE`. Funziona su **tutte le versioni di Excel** e non dipende dagli array dinamici, rendendolo l’opzione più sicura compatibile tra versioni. È ideale quando serve solo il risultato trasposto finale e non è necessario mantenere la formula `TRANSPOSE` nel workbook.

### **API utilizzata**
`Range.transpose()` è un metodo di istanza della classe `Aspose.Cells.Range`. Chiamandolo l’intervallo viene capovolto in sede scambiando righe e colonne, quindi ciò che era una riga diventa una colonna e viceversa. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire il workbook di origine con `LoadOptions` impostato al formato `.xlsx` mediante `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Recuperare il primo foglio di lavoro dal workbook usando `workbook.getWorksheets().get(0)`.  
3. Accedere alla collezione di celle del foglio tramite `worksheet.getCells()`.  
4. Creare l’intervallo di origine che copre **A1:D5** con `cells.createRange("A1:D5")`.  
5. Chiamare `source.transpose()` per ruotare l’intervallo in situ, scambiando righe e colonne.  
6. Salvare il workbook con `workbook.save(outputFile)`.
Dopo la trasposizione questo intervallo di ancoraggio contiene i dati ruotati. La prima riga legge (vuota, **Europa**, **Asia**, **America del Nord**) e la prima colonna legge (vuota, **Trimestre 1**, **Trimestre 2**, **Trimestre 3**, **Trimestre 4**). Ogni colonna originale di vendite diventa una riga nell’intervallo trasposto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Approccio 2 — Trasporre con una Formula di Array Dinamico (Excel 365 / 2021)**
Utilizzare questo approccio quando si vuole conservare la formula `=TRANSPOSE(A1:D5)` come formula viva nel workbook di output, così il risultato si aggiorna automaticamente se i dati di origine cambiano, e il file Excel di destinazione sarà aperto in **Excel 365 / Excel 2021 o versioni successive** dove gli array dinamici e l’operatore spill sono supportati.

### **API utilizzata**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` è un metodo della classe `Aspose.Cells.Cell` che imposta la formula della cella come **formula di array dinamico**. Excel valuta la formula una sola volta e “spilla” automaticamente il risultato nelle celle circostanti. Il terzo parametro, impostato a `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare il workbook di origine con `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Recuperare il primo foglio di lavoro e accedere alla sua collezione di celle.  
3. Posizionare la formula di array dinamico nella cella **A6**, subito sotto l’intervallo di origine, chiamando `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.  
4. L’argomento `new FormulaParseOptions()` utilizza le impostazioni predefinite, e il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come array dinamico e di valutarla così i valori “spilled” vengano scritti nel workbook.  
5. Salvare il workbook con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` e Excel distribuisce automaticamente il risultato nell’intervallo **A6:E9**, un blocco di 4 righe per 5 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni di Excel più vecchie non espanderanno correttamente le formule di array dinamico.
{{% /alert %}}

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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Approccio 3 — Trasporre con una Formula di Array Classica (CSE)**
Utilizzare questo approccio quando si desidera una formula `TRANSPOSE` conservata nel workbook ma il file Excel di destinazione potrebbe essere aperto in **versioni più vecchie di Excel (pre‑2021, incluse 2019, 2016, 2013, ecc.)** dove lo spilling di array dinamici non è supportato. La formula di array classica CSE (Ctrl+Shift+Enter) è l’alternativa legacy compatibile con tutte le versioni di Excel.

### **API utilizzata**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` è un metodo della classe `Aspose.Cells.Cell` che assegna una **formula di array classica (CSE)** alla cella di ancoraggio e dichiara le dimensioni dell’array risultante. Aspose.Cells scrive il marcatore di formula multi‑cella così che Excel valuti la formula come un’unica espressione di array che riempie l’intervallo dichiarato.

### **Passaggi**
1. Caricare il workbook di origine come descritto negli approcci precedenti.  
2. Recuperare il primo foglio di lavoro e accedere alla sua collezione di celle.  
3. Chiamare `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe dell’array di destinazione e il terzo argomento `5` è il numero di colonne.  
4. Salvare il workbook con `workbook.save(outputFile)`.
La cella **A6** è l’ancora della formula di array e l’array valutato si estende per 4 righe per 5 colonne a partire da A6, corrispondente alle dimensioni trasposte della sorgente A1:D5. Excel scrive un singolo marcatore di formula di array sull’intervallo risultante, così le versioni più vecchie di Excel la valutano correttamente.

{{% alert color="primary" %}}
Le formule di array CSE sono il metodo classico di Excel per valutare un’espressione `TRANSPOSE` e questo approccio è universalmente compatibile con tutte le versioni di Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Carica il workbook di origine con le LoadOptions per xlsx
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Accedi al primo foglio di lavoro e alla sua collezione Cells
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Imposta la classica formula CSE array sulla cella A6.
                // La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe per 4 colonne
                // in un array di 4 righe per 5 colonne. Il secondo argomento (4) è il numero di righe
                // e il terzo argomento (5) è il numero di colonne dell'array risultante.
                // Aspose.Cells scrive il marcatore della formula array CSE in modo che Excel la valuti
                // come una singola formula array multi-cella, compatibile con le versioni più vecchie di Excel
                // (2019, 2016, 2013, ecc.) che non supportano il versamento dinamico degli array.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Salva il workbook affinché il marcatore della formula array sia memorizzato
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Confronto — Quando Utilizzare Ogni Approccio**
| Approccio | API / Metodo | Versione Excel | Formula di origine preservata? | Intervallo di output |
|-----------|--------------|----------------|--------------------------------|----------------------|
| Approccio 1 — Trasposizione in situ | `range.transpose()` | Tutte le versioni | No (solo valori) | Intervallo di ancoraggio originale, 5×4 |
| Approccio 2 — Formula di array dinamico | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Sì (spilla dinamicamente) | Spill dall’ancora |
| Approccio 3 — Formula di array classica (CSE) | `cell.setArrayFormula()` | Tutte le versioni | Sì (formula di array multi‑cella) | Dimensione esplicita, 4×5 |
Utilizzare **l’Approccio 1** quando serve una trasformazione rapida, cross‑versione, e sono necessari solo i valori trasposti scritti nel file. Utilizzare **l’Approccio 2** quando è garantito l’uso di Excel moderno e si vuole mantenere la formula viva e aggiornata se la sorgente cambia. Utilizzare **l’Approccio 3** quando è necessaria la massima compatibilità con una formula preservata su ogni versione di Excel, incluse le versioni più datate che non supportano gli array dinamici.

{{< app/cells/assistant language="javascript-cpp" >}}
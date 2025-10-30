---
title: Utilizzo dell API LightCells con JavaScript tramite C++
linktitle: Utilizzo dell API LightCells
type: docs
weight: 160
url: /it/javascript-cpp/using-lightcells-api/
description: Impara come leggere e scrivere grandi file Excel usando l API LightCells in JavaScript tramite C++. Migliora le prestazioni e l efficienza con meno consumo di memoria.
---

{{% alert color="primary" %}}  

A volte è necessario leggere e scrivere file Microsoft Excel di grandi dimensioni con un enorme elenco di dati o contenuti nel foglio di lavoro. La LightCells API è utile per la creazione di enormi fogli di calcolo Excel: con essa, è necessaria una quantità di memoria inferiore e si ottiene una migliore performance ed efficienza.  

{{% /alert %}}  
# Architettura basata su eventi  
Aspose.Cells fornisce la LightCells API, progettata principalmente per manipolare i dati delle celle uno per uno senza costruire un blocco di modello di dati completo (utilizzando la collezione di celle ecc.) in memoria. Funziona in modalità basata su eventi.  

Per salvare i workbook, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.  

Quando si leggono file di template, il componente analizza ogni cella e fornisce il loro valore uno per uno.  

In entrambe le procedure, un oggetto Cell viene elaborato e poi scartato; l'oggetto Workbook non mantiene la collezione. In questa modalità, quindi, la memoria viene risparmiata quando si importano ed esportano file Microsoft Excel con grandi dataset che altrimenti consumeranno molta memoria.  

Anche se la LightCells API elabora le celle allo stesso modo per i file XLSX e XLS (non carica effettivamente tutte le celle in memoria ma elabora una cella e poi la scarta), salva la memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa dei diversi modelli di dati e delle strutture dei due formati.  

Tuttavia, **per i file XLS**, per risparmiare più memoria, gli sviluppatori possono specificare una posizione temporanea per salvare i dati temporanei generati durante il processo di salvataggio. Comunemente, **usare l'API LightCells per salvare file XLSX può risparmiare il 50% o più di memoria** rispetto al metodo comune; **salvare XLS può risparmiare circa il 20-40% di memoria**.  

## Scrittura di un ampio file Excel  
Aspose.Cells fornisce un'interfaccia, `LightCellsDataProvider`, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il fornitore di dati per il salvataggio di grandi file di fogli di calcolo in modalità leggera.  

Quando si salva un workbook usando questa modalità, `StartSheet(int)` viene verificato quando si salva ogni foglio di lavoro nel workbook. Per un foglio, se `StartSheet(int)` è vero, allora tutti i dati e le proprietà di righe e celle di questo foglio da salvare sono forniti da questa implementazione. Innanzitutto, `NextRow()` viene chiamato per ottenere il prossimo indice di riga da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente per le righe da salvare), allora un oggetto Row che rappresenta questa riga viene fornito all'implementazione per impostare le sue proprietà tramite `StartRow(Row)`.  

Per una riga, `NextCell()` viene verificato prima. Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per tutte le celle di una riga da salvare), allora un oggetto Cell che rappresenta quella cella viene fornito all'implementazione per impostare i suoi dati e proprietà tramite `StartCell(Cell)`. Dopo aver impostato i dati della cella, la cella viene salvata direttamente nel file di foglio di calcolo generato e si verifica e si processa la cella successiva.  
### Scrivere un grande file Excel: Esempio  
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.  

Il programma crea un file enorme con **10.000 (matrice 10000x30) record** in un foglio di lavoro e li riempie con dati fittizi. Puoi specificare la tua matrice modificando le variabili `rowsCount` e `colsCount` nel metodo `Main()`.  

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
        const { Workbook, SaveFormat, OoxmlSaveOptions } = AsposeCells;

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

        class TestDataProvider {
            constructor(workbook, maxRows, maxColumns) {
                this._workbook = workbook;
                this.maxRows = maxRows;
                this.maxColumns = maxColumns;
                this._row = -1;
                this._column = -1;
            }

            isGatherString() {
                return false;
            }

            nextCell() {
                this._column++;
                if (this._column < this.maxColumns) {
                    return this._column;
                } else {
                    this._column = -1;
                    return -1;
                }
            }

            nextRow() {
                this._row++;
                if (this._row < this.maxRows) {
                    this._column = -1;
                    return this._row;
                } else {
                    return -1;
                }
            }

            startCell(cell) {
                cell.value = this._row + this._column;
                if (this._row !== 1) {
                    cell.formula = "=Rand() + A2";
                }
            }

            startRow(row) {
            }

            startSheet(sheetIndex) {
                return sheetIndex === 0;
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            // The example does not require an input file; file input is optional.
            const rowsCount = 10000;
            const colsCount = 30;

            const workbook = new Workbook();
            const ooxmlSaveOptions = new OoxmlSaveOptions();

            ooxmlSaveOptions.lightCellsDataProvider = new TestDataProvider(workbook, rowsCount, colsCount);

            const outputData = workbook.save(SaveFormat.Xlsx, ooxmlSaveOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the generated file.</p>';
        });
    </script>
</html>
```  

## Lettura di grandi file Excel  
Aspose.Cells fornisce un'interfaccia, `LightCellsDataHandler`, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il fornitore di dati per la lettura di grandi file di fogli di calcolo in modalità leggera.  

Quando si legge un workbook in questa modalità, `StartSheet` viene verificato durante la lettura di ogni foglio di lavoro. Per un foglio, se `StartSheet` restituisce vero, allora tutti i dati e le proprietà delle celle in righe e colonne del foglio vengono verificati e processati dall'implementazione di questa interfaccia. Per ogni riga, viene chiamato `StartRow` per verificare se deve essere processata. Se una riga deve essere processata, le sue proprietà vengono lette prima, e lo sviluppatore può accedere alle sue proprietà con `ProcessRow`. Se anche le celle della riga devono essere processate, allora `ProcessRow` dovrebbe restituire vero, e quindi `StartCell` viene chiamato per ogni cella esistente nella riga per verificare se una cella deve essere processata. Se una cella deve essere processata, allora `ProcessCell` viene chiamato per processarla tramite l'implementazione di questa interfaccia.  
### Lettura di grandi file Excel: Esempio  
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.  

Il programma legge un file enorme con milioni di record in un foglio di calcolo. Impiega poco tempo per leggere ogni foglio nel workbook. Il codice di esempio legge il file e recupera il numero totale di celle, il conteggio delle stringhe e il conteggio delle formule in ogni foglio.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>LightCells Data Handler Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, CellValueType, Utils } = AsposeCells;

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

        class LightCellsDataHandlerVisitCells {
            constructor() {
                this.cellCount = 0;
                this.formulaCount = 0;
                this.stringCount = 0;
            }

            get CellCount() {
                return this.cellCount;
            }

            get FormulaCount() {
                return this.formulaCount;
            }

            get StringCount() {
                return this.stringCount;
            }

            StartSheet(sheet) {
                console.log("Processing sheet[" + sheet.name + "]");
                return true;
            }

            StartRow(rowIndex) {
                return true;
            }

            ProcessRow(row) {
                return true;
            }

            StartCell(column) {
                return true;
            }

            ProcessCell(cell) {
                this.cellCount++;
                if (cell.isFormula()) {
                    this.formulaCount++;
                } else if (cell.type === CellValueType.IsString) {
                    this.stringCount++;
                }
                return false;
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const opts = new LoadOptions();
            const v = new LightCellsDataHandlerVisitCells();
            opts.lightCellsDataHandler = v;
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);
            const sheetCount = wb.worksheets.count;

            resultDiv.innerHTML = '<p style="color: green;">Total sheets: ' + sheetCount + ', cells: ' + v.CellCount
                + ', strings: ' + v.StringCount + ', formulas: ' + v.FormulaCount + '</p>';
        });
    </script>
</html>
```

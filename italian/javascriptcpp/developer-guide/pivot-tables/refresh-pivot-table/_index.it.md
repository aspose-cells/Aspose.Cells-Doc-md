---
title: Aggiornamento delle Tabelle Pivot e delle cache Pivot in Aspose.Cells for JavaScript via C++
description: Scopri come aggiornare le Tabelle Pivot in Aspose.Cells for JavaScript via C++ utilizzando l'API di aggiornamento v26.7+. Questo articolo illustra workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData e pivotCache.getPivotTables con esempi di codice pratici.
linktitle: Aggiorna le Tabelle Pivot
keywords: Aspose.Cells, JavaScript via C++, tabella pivot, aggiornamento, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /it/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento stratificata che consente di ricaricare i dati delle Tabelle Pivot a quattro livelli di granularità diversi, dall'intera cartella di lavoro fino a una singola Tabella Pivot. A partire da **Aspose.Cells for JavaScript via C++ v26.7**, il metodo precedente `pivotTable.refreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e basate sulla cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
L'aggiornamento di una Tabella Pivot raramente consiste in una singola operazione. Internamente, Aspose.Cells mantiene una catena di dati stratificata che collega i dati di origine iniziali ai valori visualizzati nel foglio di lavoro. Comprendere questa catena è essenziale per scegliere l'API di aggiornamento più appropriata in ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dei dati** — gli intervalli originari dei fogli di lavoro, l'interrogazione del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — la copia istantanea in memoria dei dati di origine. Ogni Tabella Pivot è costruita su un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto di visualizzazione che definisce i campi di riga, colonna, valore e filtro. Un `PivotTable` legge *esclusivamente* dal proprio `PivotCache`, mai direttamente dall'origine dei dati.
4. **Cells** — le celle del foglio di lavoro restituite da `getCells()`, in cui il `PivotTable` rende i valori calcolati e gli stili.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (enumerazione `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `pivotCache.refresh()` supporta esclusivamente i tipi di origine **`SHEET`** e **`CONSOLIDATION`**, ovvero i dati contenuti in intervalli di fogli di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
A causa di questa catena, in Aspose.Cells esistono due percorsi fondamentali di aggiornamento:
- **`pivotTable.calculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` utilizzando i dati già presenti nella cache, senza tornare all'origine dei dati.
Tutti gli scenari di questo articolo utilizzano dati di origine costituiti da celle del foglio di lavoro; pertanto, il tipo di origine è `SHEET` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Avvio rapido
Se devi soltanto utilizzare il codice più breve possibile per aggiornare tutte le Tabelle Pivot della cartella di lavoro, è sufficiente una singola chiamata:

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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Tutto il resto di questo articolo spiega quando scegliere invece un'API con un ambito più ristretto.

## Import richiesti
Tutti gli esempi JavaScript di questo articolo iniziano con la seguente importazione del modulo, poiché i tipi relativi alle Tabelle Pivot sono esposti tramite il namespace `Aspose.Cells.Pivot`:
- `const Aspose = require('aspose.cells');`

## Aggiornamento di tutte le Tabelle Pivot nella cartella di lavoro
Quando devi assicurarti che ogni cache delle Tabelle Pivot e ogni Tabella Pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `workbook.refreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali dell'intero documento quando le prestazioni non costituiscono un fattore critico.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine `Fruit`/`Year`/`Amount`, crea una singola Tabella Pivot, modifica alcuni valori di origine e quindi utilizza `refreshAll()` per aggiornare tutto con una singola chiamata.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Crea una nuova cartella di lavoro
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Scrivi la riga di intestazione nelle celle A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Scrivi le righe di dati nelle celle A2:C9 (8 righe di dati sui frutti per il 2020 e il 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Aggiungi una tabella pivot: intervallo di origine "A1:C9", cella di destinazione "E3"
            const pivotTableIndex = worksheet.pivotTables.add(
                "=A1:C9",
                "E3",
                "PivotTable1"
            );
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Assegna i campi pivot: Fruit a Righe, Year a Colonne, Amount a Dati
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Modifica diversi valori Amount nei dati di origine per simulare cambiamenti
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Aggiorna tutte le tabelle pivot / le cache pivot nella cartella di lavoro
            workbook.refreshAll();
            // Salva la cartella di lavoro
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Aggiornamento di tutte le Tabelle Pivot in un singolo foglio di lavoro
Talvolta devi aggiornare soltanto le Tabelle Pivot presenti in un foglio di lavoro specifico, ad esempio quando le Tabelle Pivot in altri fogli di lavoro sono note come non correlate e non devono essere modificate. In questo caso, Aspose.Cells fornisce `worksheet.refreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTableIndex = worksheet.pivotTables.add("=A1:C9", "E3", "PivotTable1");
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Aggiornamento di una singola Tabella Pivot
Quando desideri esercitare un controllo dettagliato su una singola Tabella Pivot, l'API basata sulla cache offre due opzioni. La scelta dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di visualizzazione o disposizione della Tabella Pivot stessa.

### I dati di origine sono cambiati — Usa `pivotCache.refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di accesso corretto è `pivotTable.getPivotCache().refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da essa.

### Sono cambiati solo la visualizzazione o la disposizione — Usa `pivotTable.calculateData()`
Se i dati di origine non sono cambiati, ma sono state modificate soltanto le impostazioni di visualizzazione o disposizione della Tabella Pivot (ad esempio, un campo è stato spostato in un'area diversa oppure è stata attivata o disattivata un'impostazione di aggiornamento all'apertura), non è necessario tornare all'origine dei dati. La cache contiene già i dati corretti; è sufficiente ricalcolare il `PivotTable` visualizzato. In questo caso, `pivotTable.calculateData()` è la scelta corretta.
L'esempio seguente modifica una proprietà della Tabella Pivot che non riguarda i dati di origine e quindi chiama `calculateData()` per ridisegnarla usando la cache esistente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Scrivi la riga di intestazione Frutto / Anno / Importo
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Scrivi 8 righe di dati (righe 2-9, corrispondenti all'intervallo di origine A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Aggiungi una tabella pivot posizionata nella cella di destinazione E3, usando A1:C9 come origine
                const pivotTableIndex = worksheet.pivotTables.add(
                    "=A1:C9",
                    "E3",
                    "PivotTable1"
                );
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                // Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Modifica una proprietà di visualizzazione/layout: questa è una modifica solo di presentazione,
                // quindi NON richiede la rilettura dei dati di origine tramite PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // calculateData() aggiorna nuovamente la visualizzazione di QUESTA tabella pivot (dati + stile) dai
                // dati già contenuti in PivotCache. Poiché i dati di origine non sono cambiati,
                // non viene eseguito alcun ritorno ai dati di origine: vengono ricalcolati solo i valori memorizzati
                // nelle celle del foglio.
                pivotTable.calculateData();
                // Salva la cartella di lavoro su disco
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Una cartella di lavoro contiene spesso molte Tabelle Pivot basate su una singola cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento per gruppi o per analizzare l'impatto della cache condivisa, usa `pivotCache.getPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrazione dal metodo obsoleto `pivotTable.refreshData()`
Prima di Aspose.Cells for JavaScript via C++ v26.7, il metodo standard per aggiornare una Tabella Pivot era chiamare `pivotTable.refreshData()` singolarmente per ciascuna Tabella Pivot. A partire dalla v26.7, il metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API basate sulla cache descritte in precedenza.
Due motivi rendono problematico l'approccio con `refreshData()` per singola tabella nelle cartelle di lavoro utilizzate in contesti reali:
- Ricarica i dati dall'origine *a ogni chiamata*, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente illustra il nuovo modello efficiente per cartelle di lavoro con più Tabelle Pivot che condividono una singola cache.

## Quale API di aggiornamento devo usare?
La tabella seguente riepiloga le API di aggiornamento disponibili e i casi in cui scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `workbook.refreshAll()` | Una chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le Tabelle Pivot di un singolo foglio | `worksheet.refreshPivotTables()` | Limitata a un foglio di lavoro. |
| I dati di origine di una cache sono cambiati | `pivotTable.getPivotCache().refresh()` | Aggiorna TUTTE le Tabelle Pivot basate sulla cache condivisa. |
| Sono cambiate solo le impostazioni di visualizzazione o disposizione | `pivotTable.calculateData()` | Evita un inutile ritorno all'origine dei dati. |
| Elencare tutte le Tabelle Pivot basate su una cache condivisa | `pivotCache.getPivotTables()` | Usare per enumerarle prima di un aggiornamento per gruppi. |
Nella pratica, preferisci le API basate sulla cache rispetto all'obsoleto `refreshData()` per singola tabella. Sono in grado di riconoscere le cache condivise, evitano il recupero ridondante dei dati di origine e consentono di scegliere l'ambito più ristretto che soddisfa il requisito di aggiornamento.

## Errori comuni
- **Dimenticare di aggiornare prima di salvare.** Una Tabella Pivot scrive i suoi valori visualizzati nel foglio di lavoro soltanto quando la catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `pivotCache.refresh()` (oppure `workbook.refreshAll()`) prima di `workbook.save()`; in caso contrario, il file salvato continuerà a contenere i vecchi valori aggregati.
- **Chiamare l'obsoleto `refreshData()` per ogni tabella.** Nella v26.7, `pivotTable.refreshData()` è contrassegnato come obsoleto e ricarica i dati di origine a ogni chiamata. Con più Tabelle Pivot che condividono una cache, ciò comporta N recuperi ridondanti dei dati di origine. Sostituiscilo con una singola chiamata a `pivotCache.refresh()` seguita da `pivotTable.calculateData()` per ogni tabella.
- **Aggiornare quando è cambiata soltanto la disposizione.** Se hai modificato solo la visualizzazione di una Tabella Pivot (ordine delle colonne, `getConsolidationFunction()`, ecc.) senza intervenire sui dati di origine, `pivotCache.refresh()` è inutile e lenta. Chiama `pivotTable.calculateData()` per ridisegnarla usando la cache esistente.
- **Origine esterna non supportata da `pivotCache.refresh()`.** Se l'origine della Tabella Pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `pivotCache.refresh()` non può aggiornarla nella v26.7, poiché attualmente supporta solo i tipi di origine `SHEET` e `CONSOLIDATION`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

{{< app/cells/assistant language="javascript-cpp" >}}
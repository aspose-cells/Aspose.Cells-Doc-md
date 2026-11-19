---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for JavaScript via C++ supporta un ampio set di funzionalità di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri top 10 e come nascondere o mostrare gli elementi pivot.
keywords: Aspose.Cells, libreria JavaScript via C++, foglio di lavoro, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro top 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna contenenti testo, utilizzare filtri per data quando il campo contiene solo celle con data e ora oppure celle vuote, applicare filtri per valore ai numeri aggregati, utilizzare i filtri top 10 per classificare gli elementi in base a un campo di valore oppure nascondere e mostrare manualmente singoli elementi pivot mediante la proprietà `isHidden`. Ogni strategia è disponibile tramite API dedicate nelle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi iniziali spesso contengono molte più informazioni di quelle necessarie per la presentazione. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori rilevanti per un report specifico. Aspose.Cells for JavaScript via C++ offre le stesse funzionalità di filtraggio disponibili in Microsoft Excel e le rende disponibili a livello programmatico, consentendo di automatizzare completamente la generazione dei report.
Le seguenti strategie di filtraggio sono illustrate in questo articolo:
1. **Filtro per etichetta** — filtra gli elementi di un campo di riga o colonna in base alle relative etichette testuali.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data e ora (o celle vuote).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro top 10** — mostra solo i N elementi con i valori più alti o più bassi, classificati in base a un campo di valore.
5. **Nascondere / mostrare gli elementi pivot** — controlla manualmente la visibilità di ciascun singolo elemento di un campo.
Ogni approccio utilizza un metodo diverso della classe `PivotField` o una proprietà della classe `PivotItem`. Dopo aver applicato un filtro, è necessario chiamare `pivotCache.refresh()` sulla tabella pivot, in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie testuali con un modello. È utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o corrispondono a un altro criterio basato sulle didascalie.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. L'argomento `filterType` seleziona la modalità di confronto (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via). Gli argomenti `label1` e `label2` forniscono il testo da confrontare: passare `""` per `label2` quando è necessario confrontare un solo valore, ad esempio per i filtri «inizia con» o «contiene».
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che rimangano visibili solo gli elementi le cui didascalie iniziano con un prefisso specificato, aggiorna la tabella pivot e salva il risultato.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulle date, come oggi, la settimana scorsa, il mese corrente, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che operano esclusivamente su campi che memorizzano informazioni relative a data e ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle con data e ora oppure celle vuote. Se il campo sottostante contiene altri tipi di dati, come numeri o testo, il filtro per data non produrrà il risultato atteso. Prima di applicare il filtro, assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure corrispondano a celle vuote.
Aspose.Cells espone il filtraggio per data tramite il metodo `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori specifici per il filtraggio per data, come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro selezionato, si passano uno o due valori `DateTime`; per `Between`, si passano la data di inizio e quella di fine.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un intervallo di date specifico, aggiorna la tabella pivot e salva la cartella di lavoro.
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
        const { Workbook } = AsposeCells;
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di corrispondere alle didascalie testuali, confrontano i totali numerici con una soglia. I casi d'uso più comuni includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo obiettivo, oppure delle sole regioni il cui numero di transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Il parametro `valueFieldIndex` specifica quale campo dati deve essere valutato (utilizzare `pivotTable.getDataFields().indexOf(dataField)` oppure scorrere la raccolta per individuare la posizione). Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. I due argomenti `double` forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi per i quali le vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

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
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Filtro top 10**
Il filtro top 10 è una variante specializzata del filtro per valore che conserva esclusivamente i N elementi con i valori più alti o più bassi in base al campo di valore selezionato. È comunemente utilizzato per report di classifica come "i 10 prodotti con il fatturato più alto" o "le 5 regioni con il numero di vendite più basso".

{{% alert color="primary" %}}
Il filtro top 10 è efficace solo quando la tabella pivot dispone di uno o più campi pivot di valore nell'area dati. Senza almeno un campo di valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtraggio top 10 tramite il metodo `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati determinano la classificazione degli elementi, `filterType` seleziona l'unità di misura di `itemCount` (`Count` conserva un numero fisso di elementi, mentre `Percent` conserva una percentuale di elementi e, in questo caso, `itemCount` rappresenta la percentuale stessa), `isTop` indica se conservare gli elementi con i valori più alti (true) o più bassi (false), mentre `itemCount` definisce quanti elementi o quale percentuale conservare.
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo di valore, applica un filtro top 10 per mantenere solo i 10 elementi con il valore più alto della somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Filtrare nascondendo o mostrando gli elementi pivot**
Oltre alle API di filtraggio strutturato, Aspose.Cells consente di controllare direttamente la visibilità di ciascun singolo elemento pivot. Iterando la raccolta `pivotField.getPivotItems()` di un `PivotField` e impostando la proprietà `isHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. L'impostazione di `pivotItem.isHidden = true` nasconde l'elemento dalla tabella pivot; l'impostazione di `pivotItem.isHidden = false` lo mostra e lo rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per un singolo elemento, ad esempio per nascondere un piccolo numero di categorie che non devono comparire in un determinato report. L'esempio seguente carica una cartella di lavoro contenente una tabella pivot, nasconde un elemento specifico in base al nome, mostra come riportarlo alla vista, aggiorna la tabella pivot e salva la cartella di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Riepilogo**
Aspose.Cells for JavaScript via C++ offre un insieme completo di funzionalità di filtraggio delle tabelle pivot, corrispondenti a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro top 10 gestisce i report che richiedono classificazioni. Quando la regola di filtraggio è irregolare, la proprietà `pivotItem.isHidden` offre un'alternativa flessibile a livello di singolo elemento. La combinazione di queste strategie — ad esempio, l'applicazione di un filtro per etichetta seguita dalla nascita di elementi specifici — consente di creare, interamente tramite codice, report sulle tabelle pivot precisamente mirati.

{{< app/cells/assistant language="javascript-cpp" >}}
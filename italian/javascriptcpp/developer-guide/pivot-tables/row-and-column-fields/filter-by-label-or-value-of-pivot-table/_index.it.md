---
title: Filtro delle Tabelle Pivot per etichetta o valore
description: Aspose.Cells for JavaScript via C++ supporta funzionalità complete di filtraggio delle Tabelle Pivot. Questo articolo spiega come filtrare i dati delle Tabelle Pivot utilizzando filtri per etichetta, filtri per data, filtri di valore, filtri dei primi 10 e nascondendo o mostrando gli elementi pivot.
linktitle: Filtro per etichetta o valore
keywords: Aspose.Cells, libreria JavaScript via C++, foglio di calcolo, Tabella Pivot, filtro, filtro per etichetta, filtro di valore, filtro per data, filtro dei primi 10, elemento pivot, nascondere un elemento pivot
type: docs
weight: 10
url: /it/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce cinque strategie pratiche per filtrare i dati visualizzati in una Tabella Pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati sul testo, utilizzare filtri per data quando il campo contiene solo celle con data e ora oppure celle vuote, applicare filtri di valore rispetto ai numeri aggregati, utilizzare filtri dei primi 10 per classificare in base a un campo di valore oppure nascondere e mostrare manualmente singoli elementi pivot mediante la proprietà `isHidden`. Ogni strategia è disponibile tramite API dedicate offerte dalle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le Tabelle Pivot sono potenti strumenti analitici, ma i riepiloghi non elaborati spesso contengono molte più informazioni di quanti si desideri presentare. Il filtraggio è il meccanismo principale per restringere una Tabella Pivot alle righe, alle colonne o ai valori pertinenti a un report specifico. Aspose.Cells for JavaScript via C++ replica le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello programmatico in modo che la generazione dei report possa essere completamente automatizzata.
In questo articolo vengono illustrate le seguenti strategie di filtraggio:
1. **Filtro per etichetta** — filtra gli elementi di un campo di riga o colonna in base alle rispettive etichette testuali.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori di data e ora (o valori vuoti).
3. **Filtro di valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro dei primi 10** — mostra solo i N elementi con i valori più alti o più bassi, classificati in base a un campo di valore.
5. **Nascondere / mostrare gli elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento di un campo.
Ogni approccio utilizza un metodo diverso della classe `PivotField` o una proprietà della classe `PivotItem`. Dopo aver applicato un filtro, è necessario chiamare `pivotCache.refresh()` sulla Tabella Pivot, in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le rispettive etichette testuali con un modello. Questo è utile quando si desidera mostrare solo prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano un altro criterio basato sulle etichette.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. L'argomento `filterType` seleziona la modalità di confronto (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via). Gli argomenti `label1` e `label2` forniscono il testo da confrontare; passare `""` per `label2` quando è necessario un confronto con un solo valore, ad esempio per i filtri «inizia con» o «contiene».
L'esempio seguente carica una cartella di lavoro contenente una Tabella Pivot esistente, applica un filtro per etichetta in modo che restino visibili solo gli elementi le cui etichette iniziano con un prefisso specificato, aggiorna la Tabella Pivot e salva il risultato.

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
                    // Carica la cartella di lavoro esistente contenente una tabella pivot
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
                    const worksheet = workbook.worksheets.get(0);
                    // Accedi alla tabella pivot tramite indice
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Ottieni il primo PivotField di riga
                    const rowField = pivotTable.rowFields.get(0);
                    // Applica il filtro delle etichette — mostra solo gli elementi di riga le cui etichette iniziano con il prefisso specificato
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Aggiorna e ricalcola i dati della tabella pivot in modo che il filtro venga applicato
                    pivotTable.refreshData();
                    // Salva la cartella di lavoro su disco
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
I filtri per data consentono di restringere una Tabella Pivot in base a criteri temporali, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati applicabili esclusivamente a campi che memorizzano informazioni di data e ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle con data e ora oppure valori vuoti. Se il campo sottostante contiene altri tipi di dati, come numeri o testo, il filtro per data non produrrà il risultato previsto. Prima di applicare il filtro, assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze `DateTime` valide o celle vuote.
Aspose.Cells espone il filtraggio per data tramite il metodo `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date, quali `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro selezionato, è necessario passare uno o due valori `DateTime` (per `Between`, passare la data di inizio e quella di fine).
L'esempio seguente carica una cartella di lavoro con una Tabella Pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un intervallo di date specifico, aggiorna la Tabella Pivot e salva la cartella di lavoro.
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
                // Carica la cartella di lavoro esistente che contiene la tabella pivot
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
                const worksheet = workbook.worksheets.get(0);
                // Accedi alla tabella pivot tramite indice
                const pivotTable = worksheet.pivotTables.get(0);
                // Recupera il campo pivot della data dall'area delle righe
                // (Il filtro data funziona solo quando l'area righe/colonne contiene solo celle con data e ora o vuote)
                const dateField = pivotTable.rowFields.get(0);
                // Definisci il criterio di data per il filtro Tra
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Applica il filtro data al campo pivot
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Aggiorna e ricalcola la tabella pivot affinché il filtro venga applicato
                pivotTable.refreshData();
                // Salva la cartella di lavoro
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

## **Filtro di valore**
I filtri di valore operano sui valori aggregati che una Tabella Pivot calcola nella propria area dati. Invece di confrontare etichette testuali, confrontano i totali numerici con una soglia. I casi d'uso tipici includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo obiettivo oppure delle sole regioni il cui numero di transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Il parametro `valueFieldIndex` specifica quale campo dati deve essere valutato (usare `pivotTable.getDataFields().indexOf(dataField)` oppure scorrere la raccolta per individuare la posizione). Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. I due argomenti `double` forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una Tabella Pivot, applica un filtro di valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la Tabella Pivot e salva la cartella di lavoro.

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
                // Trova manualmente l'indice del campo dati poiché PivotFieldCollection non ha IndexOf
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
                pivotTable.refreshData();
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

## **Filtro dei primi 10**
Il filtro dei primi 10 è una forma specializzata di filtro di valore che mantiene solo i N elementi con i valori più alti o più bassi, in base a un campo di valore scelto. È comunemente utilizzato per report di classifica come «i 10 prodotti principali per ricavi» o «le 5 regioni con il minor numero di vendite».

{{% alert color="primary" %}}
Il filtro dei primi 10 è efficace solo quando la Tabella Pivot contiene uno o più campi pivot di valore nell'area dati. Senza almeno un campo di valore, non esiste una misura aggregata con cui classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtraggio dei primi 10 tramite il metodo `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati determinano la classifica degli elementi, `filterType` seleziona l'unità di `itemCount` (`Count` mantiene un numero prefissato di elementi, mentre `Percent` mantiene una percentuale degli elementi e in questo caso `itemCount` è il valore percentuale stesso), `isTop` indica se mantenere gli elementi con i valori più alti (true) o più bassi (false) e `itemCount` definisce quanti elementi, oppure quale percentuale, mantenere.
L'esempio seguente carica una cartella di lavoro con una Tabella Pivot che contiene un campo di valore, applica un filtro dei primi 10 per mantenere solo i 10 elementi con la somma delle vendite più alta, aggiorna la Tabella Pivot e salva la cartella di lavoro.
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
                // Carica il workbook esistente che contiene la tabella pivot
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
                const worksheet = workbook.worksheets.get(0);
                // Accedi alla tabella pivot tramite indice
                const pivotTable = worksheet.pivotTables.get(0);
                // Conferma che nell'area dati sia presente almeno un PivotField di valore
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Ottieni il PivotField di riga target (il campo a cui vogliamo applicare Top 10)
                const rowField = pivotTable.rowFields.get(0);
                // Il primo (e unico) campo dati si trova all'indice 0; Top 10 classifica in base a esso.
                const valueFieldIndex = 0;
                // Applica il filtro Top 10 al campo di riga:
                //   - valueFieldIndex = 0 — il campo dati utilizzato per classificare gli elementi
                //   - filterType  = PivotFilterType.Count (mantiene un numero fisso di elementi;
                //     PivotFilterType.Percent interpreterebbe 10 come "top 10 percent")
                //   - isTop       = true (top N; false significherebbe bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Aggiorna i dati della tabella pivot e ricalcolala affinché il filtro venga applicato
                pivotTable.refreshData();
                // Salva il workbook
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

## **Filtro tramite la nascita o la visualizzazione di elementi pivot**
Oltre alle API di filtraggio strutturato, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Scorrendo la raccolta `pivotField.getPivotItems()` di un `PivotField` e commutando la proprietà `isHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. L'impostazione `pivotItem.isHidden = true` nasconde l'elemento dalla Tabella Pivot; l'impostazione `pivotItem.isHidden = false` lo rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per un elemento, ad esempio per nascondere un piccolo numero di categorie note che non devono comparire in un report specifico. L'esempio seguente carica una Tabella Pivot, nasconde un elemento specifico in base al nome, illustra come renderlo nuovamente visibile, aggiorna la Tabella Pivot e salva la cartella di lavoro.

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
                // Carica una cartella di lavoro esistente contenente una tabella pivot
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accedi al primo foglio di lavoro che contiene la tabella pivot
                const sheet = workbook.worksheets.get(0);
                // Accedi alla tabella pivot tramite l'indice (la prima tabella pivot nel foglio)
                const pivotTable = sheet.pivotTables.get(0);
                // Recupera il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
                const pivotField = pivotTable.rowFields.get(0);
                // Itera nella raccolta PivotItems del PivotField selezionato
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Dimostra come mostrare nuovamente un elemento pivot precedentemente nascosto
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
                pivotTable.refreshData();
                // Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
                // ma sono esclusi dall'output visualizzato della tabella pivot
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
Aspose.Cells for JavaScript via C++ offre una serie completa di funzionalità di filtraggio delle Tabelle Pivot, corrispondenti a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e di valore coprono gli scenari analitici più comuni, mentre il filtro dei primi 10 gestisce i report di classifica. Quando la regola di filtraggio è irregolare, la proprietà `pivotItem.isHidden` offre un'alternativa flessibile a livello di singolo elemento. Combinando queste strategie, ad esempio applicando un filtro per etichetta e quindi nascondendo elementi specifici, è possibile creare report di Tabelle Pivot precisamente mirati interamente mediante codice.

{{< app/cells/assistant language="javascript-cpp" >}}
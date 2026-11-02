---
title: Mostrare o filtrare i primi 10 nella tabella pivot
linktitle: Mostrare o filtrare i primi 10 nella tabella pivot
description: Scopri come applicare a un campo di una tabella pivot un filtro che mostri solo gli elementi con il migliore o il peggiore posizionamento in classifica in Aspose.Cells for JavaScript via C++. Questo articolo descrive le proprietà AutoShow di Excel 97-2003 (isAutoShow e proprietà analoghe), come rileggere le opzioni correnti e come utilizzare il filtro Primi 10 di Excel 2007-365 tramite filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tabella pivot, primi 10, visualizzazione automatica, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /it/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può risultare difficile da leggere quando il campo contiene decine di membri. Un report sui primi 10 conserva soltanto gli elementi con il migliore o il peggiore posizionamento in classifica. Si tratta di una funzionalità essenziale per report di classifica come "i 5 prodotti principali in base al fatturato" o "le 3 regioni meno performanti in base al numero di vendite". Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **Excel 97-2003 AutoShow** — le quattro proprietà di `PivotField`: `isAutoShow`, `isAscendShow`, `autoShowCount` e `autoShowField`. Corrisponde all'impostazione classica "Mostra i primi/ultimi N elementi", memorizzata direttamente sul campo della tabella pivot. Funziona in tutte le versioni di Excel, poiché fa parte del formato originale della tabella pivot.
- **Filtro Primi 10 di Excel 2007-365** — il metodo `PivotField.filterTop10()`. È il filtro moderno relativo ai primi 10, disponibile nel menu del campo nella sezione Filtri valore. Viene memorizzato come oggetto `PivotFilter` associato al campo e consente classifiche basate sul numero di elementi o sulla percentuale.

## **Visualizzazione dei primi 10 in Excel 97-2003 (AutoShow)**
L'AutoShow classico viene configurato assegnando quattro proprietà all'oggetto `PivotField`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isAscendShow` — `false` mantiene gli elementi con il migliore posizionamento in classifica (Primi), `true` mantiene quelli con il posizionamento peggiore (Ultimi).
- `autoShowCount` — il numero di elementi da mantenere, ad esempio 10 per un report classico dei primi 10.
- `autoShowField` — l'indice a base zero del **campo dati** i cui valori determinano l'ordine degli elementi in classifica. Passare -1 per ordinare gli elementi in base al campo stesso.
La classifica può essere basata su un campo valore o sul campo stesso. Le due varianti disponibili sono illustrate di seguito.

### **Classifica in base a un campo valore**
Classificare gli elementi del campo di riga in base a un campo valore, ad esempio Sum of Sales. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i 2 sport con le vendite più elevate. `rankBy` è 0 perché "Sum of Sales" è il campo dati all'indice 0.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Mostra i primi 2 elementi classificati in base a "Sum of Sales" (indice del campo dati 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Classifica in base al campo stesso**
Un campo può essere classificato in base a sé stesso: in questo caso, passare il valore -1 a `autoShowField`. Per questa variante non è necessario alcun campo dati aggiuntivo; basta che il campo sia collocato nell'area delle righe (o delle colonne). L'esempio seguente mostra gli ultimi 3 sport in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dal XML della tabella pivot, poiché -1 è il valore predefinito del formato e il valore di `autoShowField` riletto è -1.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Mostra i 3 elementi inferiori classificati in base al campo stesso (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Lettura delle opzioni AutoShow correnti**
Le proprietà `isAutoShow`, `isAscendShow`, `autoShowCount` e `autoShowField` di `PivotField` forniscono accesso alle opzioni AutoShow attualmente memorizzate sul campo. Utilizzatele per controllare come verranno visualizzati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata. Sono valide anche per le cartelle di lavoro caricate da file.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Le quattro proprietà corrispondono agli attributi AutoShow classici scritti nel XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), pertanto i valori letti sono quelli che verranno interpretati da tutte le versioni di Excel.

## **Nota**

{{% alert color="primary" %}}
- Dopo aver modificato una qualsiasi proprietà AutoShow, chiamare di nuovo `pivotTable.calculateData()` — le impostazioni vengono applicate al layout visualizzato soltanto al ricalcolo successivo.
- Le impostazioni AutoShow si applicano ai campi di riga e di colonna. Un campo presente soltanto nell'area dei filtri non può essere classificato in questo modo, poiché i suoi elementi non vengono visualizzati nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro dei primi 10 (filterTop10)**
Le versioni moderne di Excel espongono l'opzione Primi 10 come filtro valore nel menu del campo (Filtri valore, Primi 10...). Aspose.Cells rappresenta questa funzionalità mediante il metodo `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — l'indice a base zero del campo dati i cui valori aggregati determinano la classifica degli elementi.
- `type` — specifica il significato di `itemCount`. `PivotFilterType.Count` mantiene un numero fisso di elementi (l'opzione Elementi della finestra di dialogo). `PivotFilterType.Percent` mantiene una percentuale degli elementi; pertanto `itemCount` è la percentuale stessa: con il valore 30, viene mantenuto il 30% superiore della classifica. `PivotFilterType.Sum` classifica gli elementi in base alla copertura cumulativa dei valori.
- `isTop` — `true` per Primi, `false` per Ultimi.
- `itemCount` — il valore N dell'opzione Primi N; l'unità dipende da `type`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Le proprietà AutoShow e `filterTop10` sono due funzionalità distinte. AutoShow scrive sul campo della tabella pivot l'attributo classico `autoShow` e le relative impostazioni. Questo meccanismo è supportato da tutte le versioni di Excel a partire da Excel 97. `filterTop10` scrive una voce `PivotFilter` moderna, che richiede Excel 2007 o versione successiva. Quando una cartella di lavoro che utilizza il filtro moderno viene aperta in una versione precedente di Excel, la tabella pivot torna a visualizzare tutti gli elementi. Per i documenti che devono essere elaborati anche da strumenti di versioni precedenti, preferire le proprietà AutoShow; per le cartelle di lavoro moderne, preferire `filterTop10`, perché si integra con gli altri filtri valore.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi della tabella pivot nella tabella pivot](/cells/it/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
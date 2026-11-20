---
title: Raggruppare i campi Pivot nella Tabella Pivot
linktitle: Raggruppare i Campi Pivot
type: docs
weight: 80
url: /it/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Scopri come raggruppare i campi pivot di riga e colonna in una tabella pivot in periodi di data come mesi e trimestri e intervalli numerici usando PivotField.group e PivotFieldGroupOptions in Aspose.Cells per JavaScript tramite C++.
keywords: Aspose.Cells, tabella pivot, raggruppare campo pivot, PivotField.group, PivotFieldGroupOptions, raggruppamento per data, raggruppamento per numero, mesi, trimestri, intervallo numerico, JavaScript via C++
---

## **Possibili scenari di utilizzo**
- Raggruppare i campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento comprime questi elementi in sezioni significative: date in mesi, trimestri e anni, e numeri in intervalli come 0-1, 2-3, 4-5. Ciò rende una grande tabella pivot più compatta e più facile da analizzare. Aspose.Cells fornisce questa funzionalità tramite il metodo `PivotField.group()` (raggruppamento automatico per tipo di dati) e `PivotField.group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per data aggrega le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e crea una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Le tendenze nel tempo diventano visibili a colpo d'occhio, e ogni livello di periodo diventa un proprio campo pivot nell'area di riga o colonna della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGA o COLONNA di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare tale campo è necessario prima aggiungerlo all'area di riga o colonna della tabella pivot.

## **Raggruppare i Campi Pivot Automaticamente**
La sovraccarico senza parametri di `PivotField.group()` esamina il tipo di dati del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e celle vuote) viene raggruppato per mesi. Un campo che contiene solo numeri (e celle vuote) viene raggruppato in intervalli numerici usando un intervallo automatico.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Raggruppare i Campi Pivot con Opzioni Personalizzate**
La classe `PivotFieldGroupOptions` fornisce la configurazione per il raggruppamento personalizzato. Per i campi data, impostare `startDate`, `endDate` e `groupTypes`. Per i campi numerici, impostare `startNumber`, `endNumber` e `interval`. La proprietà `newPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto a quello originale (vedere la sezione Nota alla fine di questo articolo).

### **Raggruppare un Campo Data per Mesi e Trimestri**
L'esempio seguente raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Nota che l'ordine dei valori in `options.groupTypes` è ignorato. Indipendentemente dall'ordine in cui i tipi di gruppo sono elencati, i campi raggruppati vengono sempre visualizzati dal periodo più grande al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.groupTypes`, tuttavia i trimestri vengono mostrati come livello esterno e i mesi come livello interno.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Pivot table grouped by months and quarters](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppare un Campo Numerico in Intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché è possibile raggruppare solo i campi di riga o colonna, il codice chiama prima `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` per spostare `FieldTwo` nell'area di riga, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 usando `startNumber = 0`, `endNumber = 5` e `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Nota**

{{% alert color="primary" %}}
- I sovraccarichi del metodo `PivotField.groupBy()` sono deprecati e rimossi dall'interfaccia API. `PivotField.group()` e `PivotField.group(PivotFieldGroupOptions)` sono i sostituti.
- In Microsoft Excel, il raggruppamento di un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre il raggruppamento di un campo data crea NUOVI campi pivot (uno per livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `PivotField.group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.newPivotField` esiste per compatibilità con versioni precedenti: è impostata su false per il raggruppamento numerico e su true per il raggruppamento data‑ora; impostala su false se desideri che il raggruppamento delle date sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento delle date per giorni (ad esempio, raggruppare le date in periodi di 7 giorni); viene ignorata quando le date sono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungere campi di riga e colonna nella Tabella Pivot](/cells/it/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere campo pagina nella Tabella Pivot](/cells/it/javascript-cpp/add-page-field-in-pivot-table/)
- [Applicare stile alla Tabella Pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Aggiornare la Tabella Pivot](/cells/it/javascript-cpp/refresh-pivot-table/)
- [Raggruppamento discreto degli elementi dei campi pivot](/cells/it/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}
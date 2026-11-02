---
title: Modificare il layout dei campi pagina nella Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una Tabella Pivot utilizzando Aspose.Cells for JavaScript via C++, inclusa l'impostazione dell'ordine di visualizzazione, del numero di campi pagina per riga o colonna e dell'ordine dei campi pagina nella parte superiore della Tabella Pivot.
linktitle: Modificare il layout dei campi pagina nella Tabella Pivot
keywords: Aspose.Cells for JavaScript via C++, foglio di calcolo, Tabella Pivot, campo pagina, ordine dei campi pagina, numero di campi pagina per riga o colonna, spostamento di un campo pagina
type: docs
weight: 191
url: /it/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Questo articolo prosegue l'argomento **Aggiungere un campo pagina alla Tabella Pivot**. Dimostra come controllare il layout dell'area dei campi pagina — la barra dei controlli di filtro nella parte superiore di una Tabella Pivot — tra cui l'ordine di visualizzazione, il numero di campi pagina per riga o colonna e il riordinamento dei campi.
{{% /alert %}}

## **Introduzione**
Una Tabella Pivot in Microsoft Excel dispone di un'**area dei campi pagina** dedicata che si trova sopra il corpo di righe, colonne e dati della tabella. Questa area viene visualizzata come una barra di menu a discesa per il filtro (uno per ogni campo pagina) ed è l'area su cui gli utenti finali fanno clic per filtrare la Tabella Pivot in base a criteri come l'anno o la regione. Aspose.Cells modella questa area tramite la raccolta `pivotTable.pageFields` ed espone tre proprietà che controllano la disposizione visiva della barra:
- `pivotTable.pageFieldOrder` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono disposti *accanto* a quelli esistenti o *sotto* di essi.
- `pivotTable.pageFieldWrapCount` imposta quanti campi pagina vengono disposti per riga o colonna prima del ritorno a capo.
- `pivotTable.pageFields.move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordinamento.
Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un set di dati condiviso, consentendo di confrontare i layout risultanti.

## **Dati di origine**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Mela   | 2022 | Nord   | 150    |
| Mela   | 2023 | Nord   | 180    |
| Banana | 2022 | Sud    | 120    |
| Banana | 2023 | Sud    | 140    |
| Ciliegia | 2022 | Est  | 200    |
| Ciliegia | 2023 | Est  | 220    |
| Uva    | 2022 | Ovest  | 90     |
| Uva    | 2023 | Ovest  | 110    |
Tutte le otto righe contengono dati in ogni esempio di codice, nello stesso ordine, in modo che i dati di origine non cambino mai tra uno scenario e l'altro — cambiano soltanto le proprietà relative al layout dei campi pagina.

## **Esempio 1: Orizzontale poi verticale**
Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) in modo che vengano visualizzati **uno accanto all'altro in una sola riga** nella parte superiore della Tabella Pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse dei campi pagina (l'ordine delle chiamate a `addFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati e quindi impostiamo `pivotTable.pageFieldOrder` su `PrintOrderType.OverThenDown` con `pivotTable.pageFieldWrapCount = 2`. Con `OverThenDown` e un numero di campi pagina per riga o colonna pari a 2, i due campi pagina vengono disposti in orizzontale, uno accanto all'altro, in una sola riga nella parte superiore della Tabella Pivot; la barra occupa quindi una riga con due campi affiancati.

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
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Intestazioni (riga 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Riga 1: Apple, 2022, North, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Riga 2: Apple, 2023, North, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Riga 3: Banana, 2022, South, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Riga 4: Banana, 2023, South, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Riga 5: Cherry, 2022, East, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Riga 6: Cherry, 2023, East, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Riga 7: Grape, 2022, West, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Riga 8: Grape, 2023, West, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Aggiungi il foglio PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Crea una tabella pivot con origine in PivotData!A1:D9, posizionata in A1 su PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Aggiungi i campi
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Configura il layout dell'area dei campi pagina: disponi i campi pagina prima orizzontalmente, poi verticalmente, andando a capo ogni 2 campi
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Aggiorna e calcola
            pivotTable.calculateData();
            // Salva
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Esempio 2: Verticalmente poi orizzontalmente**
In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse dei campi pagina (con `Year` per primo) e `Amount` (Sum) come campo dati, esattamente come nell'Esempio 1. Impostiamo quindi `pivotTable.pageFieldOrder` su `PrintOrderType.DownThenOver` e `pivotTable.pageFieldWrapCount` su `2`. Con `DownThenOver` e un numero di campi pagina per riga o colonna pari a 2, i due campi pagina vengono impilati in verticale — `Year` in alto, `Region` immediatamente sotto — formando una singola colonna nella parte superiore della Tabella Pivot. La barra occupa quindi due righe con un solo campo ciascuna, in contrasto con l'Esempio 1.

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
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Esempio 3: Spostare un campo pagina**
Nel terzo scenario manteniamo questo set di dati e questa assegnazione dei campi, impostiamo un layout neutro (`OverThenDown` con un valore di `2` per il numero di campi pagina per riga o colonna) e quindi dimostriamo l'operazione `pivotTable.pageFields.move`. La chiamata `move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, mentre il campo pagina che si trovava alla posizione 1 (`Region`) passa alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. Il numero di campi per riga e la modalità di ordinamento restano invariati, quindi la barra viene ancora visualizzata in orizzontale, con i campi uno accanto all'altro; cambia soltanto l'ordine dei due menu a discesa.

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
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Articoli correlati**
- [Aggiungere un campo pagina alla Tabella Pivot](/cells/it/javascript-cpp/add-page-field-in-pivot-table/) — la pagina padre che introduce l'aggiunta dei campi pagina a una Tabella Pivot.
- [Gestire i campi valore nella Tabella Pivot](/cells/it/javascript-cpp/manage-value-fields/) — descrive come configurare l'area dei dati (valori), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Applicare uno stile alla Tabella Pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/) — mostra come formattare la Tabella Pivot visualizzata dopo la disposizione della barra dei campi pagina.

{{< app/cells/assistant language="javascript-cpp" >}}
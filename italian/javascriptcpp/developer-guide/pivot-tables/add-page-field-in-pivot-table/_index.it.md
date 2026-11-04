---
title: Aggiungere campi filtro a una tabella pivot tramite Aspose.Cells for JavaScript via C++
linktitle: Aggiungere campi filtro a una tabella pivot tramite Aspose.Cells for JavaScript via C++
description: Scopri come aggiungere e configurare campi filtro nelle tabelle pivot utilizzando Aspose.Cells for JavaScript via C++, inclusi l’aggiunta di campi filtro, il filtro con selezione singola e quello con selezione multipla.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l’intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un’API di alto livello e di semplice utilizzo oppure mediante la raccolta a basso livello `getPageFields()`, quindi gestire il filtro in modalità di selezione singola, cancellarlo per mostrare tutti gli elementi di filtro o impostare il campo in modalità di selezione multipla, consentendo agli utenti di scegliere contemporaneamente più elementi di filtro tramite l’interfaccia utente con caselle di controllo di Excel.
{{% /alert %}}

## **Introduzione**
Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della tabella pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una tabella pivot visualizzata in Excel; selezionare uno degli elementi di filtro disponibili ricostruisce il corpo della tabella pivot, in modo che vengano riepilogati solo i record appartenenti all’elemento selezionato. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché come `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Aggiunta di un campo filtro**

### Aggiunta di un campo filtro con `addFieldToArea`
L’esempio seguente crea un piccolo set di dati `Fruit` / `Year` / `Amount`, colloca una tabella pivot nella cella E3 con `Fruit` nell’area righe, `Amount` nell’area dati e `Year` nell’area filtro, aggiorna la tabella pivot e salva la cartella di lavoro.

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
            // Crea un nuovo workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // Imposta la riga di intestazione
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Popola 9 righe di dati di esempio: Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Aggiungi una tabella pivot ancorata alla cella E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Aggiungi i campi alle rispettive aree: Fruit come riga, Amount come dati, Year come campo di pagina
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Aggiorna e calcola i dati della tabella pivot
            pivotTable.calculateData();
            // Salva il workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Aggiunta di un campo filtro con `getPageFields().add`
Quando si lavora già con un’istanza di `PivotField`, è possibile passarla direttamente a `pivotTable.getPageFields().add(pivotField)`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell’area filtro viene sostituita da una chiamata API di basso livello.

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
            // — La tabella pivot e il campo di pagina sono costruiti esattamente come nello
            //   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Riga,
            //   Amount→Dati). Di seguito otteniamo il campo pivot Year dalla
            //   raccolta BaseFields e lo passiamo a PageFields.Add — l'alternativa
            //   di basso livello a AddFieldToArea. Il risultato è
            //   funzionalmente identico allo Scenario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Intestazioni
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Dati di esempio (9 righe)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Aggiungi la tabella pivot in E3 che copre A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Fruit → Riga, Amount → Dati (Year verrà aggiunto alla pagina qui sotto)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Approccio di basso livello: prendiamo il campo pivot Year esistente da BaseFields
            // e lo registriamo nell'area Page tramite PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Aggiorna in modo che il nuovo campo di pagina venga riflesso nel workbook salvato
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Filtro con selezione singola (visualizzazione di un solo elemento di filtro)**
Con il comportamento predefinito della selezione singola, il campo filtro viene visualizzato come un unico menu a discesa e la proprietà `pivotField.currentPageItem`, di tipo intero, determina quale elemento di filtro controlla il corpo della tabella pivot. L’assegnazione di un indice specifico seleziona tale elemento; l’assegnazione del valore sentinella speciale `0x7FFD` (32765 in notazione decimale) cancella il filtro, in modo che tutti gli elementi di filtro vengano riepilogati contemporaneamente. La selezione singola è il comportamento predefinito e non è necessario abilitarla esplicitamente.

### Visualizzazione di tutti gli elementi
L’impostazione di `currentPageItem` sul valore magico `0x7FFD` equivale a cancellare il filtro: il corpo della tabella pivot riepiloga tutti gli elementi di filtro come se non fosse stato applicato alcun filtro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Crea un nuovo workbook
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Popola i dati Fruit/Year/Amount
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Crea una tabella pivot in E3
            const pivotTables = sheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:C7", 2, 4);
            // Configura i campi pivot: Fruit→Row, Amount→Data, Year→Page
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Cancella il filtro di pagina in modo che tutti gli elementi del campo pagina siano visibili.
            // 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
            // equivale a selezionare "(Tutti)" nel menu a discesa del campo pagina di Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### Visualizzazione di un elemento specifico
L’impostazione di `currentPageItem` su un indice valido seleziona soltanto tale elemento di filtro. L’indice corrisponde alla posizione dell’elemento nell’elenco ordinato degli elementi del campo filtro; ad esempio, `1` seleziona il secondo elemento dopo l’ordinamento.

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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Crea la cartella di lavoro
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Aggiungi dati di esempio (Fruit/Year/Amount)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Aggiungi una tabella pivot a E3
                const pivotTables = sheet.pivotTables;
                const pivotTable = pivotTables.add("=A1:C5", 2, 4);
                // Aggiungi campi: Fruit→Riga, Amount→Dati, Year→Pagina
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Operazioni specifiche del campo di pagina
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = secondo elemento in ordine (ad es. "2021")
                // Aggiorna e calcola la tabella pivot
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Filtro con selezione multipla**
Il filtro con selezione multipla trasforma il menu a discesa del filtro in un elenco di caselle di controllo e consente all’utente finale di selezionare contemporaneamente più elementi di filtro. Aspose.Cells espone due proprietà che lavorano insieme. `pivotField.isMultipleItemSelectionAllowed` deve essere impostata su `true` prima che l’interfaccia utente di selezione multipla possa essere utilizzata. Una volta abilitata, `pivotItem.isHidden` controlla quali elementi vengono visualizzati nell’elenco di caselle di controllo, consentendo di mostrare tutti gli elementi oppure di limitare l’elenco a soli elementi specifici autorizzati.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — La tabella pivot e il campo pagina vengono costruiti esattamente come
                //   nello Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Riga,
                //   Amount→Dati, Year→Pagina tramite AddFieldToArea).
                //   Di seguito applichiamo il filtro con selezione multipla al campo pagina.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Dati di esempio: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTable = pivots.add("=A1:C10", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Abilita la selezione multipla sul campo pagina
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Parte B — seleziona solo gli elementi specifici in base al valore di origine
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Nota:** Quando si utilizza il filtro con selezione multipla tramite `pivotItem.isHidden`, **almeno un `PivotItem` deve rimanere visibile** (`isHidden === false`). Se tutti gli elementi sono nascosti, Excel si arresta in modo anomalo all’apertura del file oppure visualizza una tabella pivot vuota. Verificare sempre che l’elenco degli elementi autorizzati per la selezione multipla includa almeno un elemento presente nei dati di origine.

## **Quale API e quale modalità utilizzare?**
La tabella seguente riepiloga quando utilizzare ciascuna API e modalità, così da consentire di scegliere la combinazione corretta senza leggere ogni scenario in dettaglio.
| Scenario / Caso d’uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro in base al nome della colonna di origine (caso più comune) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Di alto livello, in una sola riga. Utilizzare questa opzione, a meno che non sia necessario un riferimento a `PivotField`. |
| Aggiungere un campo filtro quando è già disponibile un oggetto `PivotField` | `pivotTable.getPageFields().add(pivotField)` | n/a | Utilizzare quando l’oggetto del campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento di filtro (modalità predefinita) | `pivotField.currentPageItem` | impostata su un indice specifico | Ad esempio, `1` mostra il secondo elemento dell’elenco ordinato. |
| Mostrare tutti gli elementi / cancellare il filtro | `pivotField.currentPageItem` | impostata su `0x7FFD` | Il valore magico `0x7FFD` (32765 in notazione decimale) è il valore sentinella per «tutti gli elementi». |
| Abilitare l’interfaccia utente di selezione multipla in Excel | `pivotField.isMultipleItemSelectionAllowed` | impostata su `true` | Necessaria prima che le assegnazioni a `isHidden` diventino effettive. |
| Nascondere / mostrare singoli elementi in un elenco con selezione multipla | `pivotItem.isHidden` | impostata per elemento | Almeno un elemento deve rimanere visibile (`isHidden === false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro con selezione multipla. Se ogni `PivotItem` di un campo filtro con selezione multipla è nascosto, Excel si arresta in modo anomalo all’apertura oppure visualizza una tabella pivot vuota. Definire l’elenco degli elementi autorizzati in base ai dati di origine, assicurandosi che almeno un elemento rimanga visibile, in modo che le cartelle di lavoro salvate si aprano in modo affidabile su ogni computer.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}
---
title: Aggiungere campi di riga e colonna alla tabella pivot con Aspose.Cells for JavaScript via C++
linktitle: Aggiungere campi di riga e colonna alla tabella pivot con Aspose.Cells for JavaScript via C++
description: Scopri come aggiungere campi pivot di riga e colonna a una tabella pivot e controllare i subtotali dei campi pivot utilizzando PivotField.SetSubtotals con PivotFieldSubtotalType in Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tabella pivot, campo di riga, campo di colonna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotali, JavaScript, tabella pivot di Excel
type: docs
weight: 220
url: /it/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiunta di un campo all'area delle righe o delle colonne**
Il metodo `pivotTable.addFieldToArea(fieldType, fieldName)` sposta un campo di base dai dati di origine in una delle quattro regioni pivot. L'argomento `fieldType` accetta uno dei seguenti valori `PivotFieldType`.
- `Row` — campi disposti verticalmente a sinistra
- `Column` — campi disposti orizzontalmente nella parte superiore
- `Data` — campi i cui valori vengono aggregati
- `Page` — campi utilizzati come filtri del rapporto
L'ordine di annidamento dei campi è importante. Aggiungendo `Category` all'area delle righe prima e quindi `Item`, si ottiene una tabella pivot il cui raggruppamento esterno è `Category` e quello interno è `Item`. Invertendo l'ordine, si inverte la gerarchia.

## **Subtotali dei campi pivot**
Il metodo `pivotField.setSubtotals(subtotalType, shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata abilita o disabilita in modo indipendente un singolo tipo di subtotale. Passando `shown = true`, il subtotale viene visualizzato, mentre `shown = false` lo nasconde. Poiché ogni chiamata influisce su un solo tipo, chiamare il metodo più volte con diversi valori `subtotalType` consente di definire un sottoinsieme personalizzato di subtotali.
L'enumerazione `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.
- `Automatic` — Aspose.Cells seleziona l'opzione predefinita (in genere `Sum` per i campi numerici)
- `None` — sopprime tutte le righe di subtotale
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando nella regione delle righe (o delle colonne) sono presenti due o più campi pivot. Un singolo campo non offre un riferimento significativo tra un gruppo e l'altro su cui calcolare il subtotale; pertanto, le chiamate a `setSubtotals` non hanno alcun effetto visivo in questo caso. Questo articolo inserisce quindi in ogni esempio due campi nell'area delle righe (`Category` esterno, `Item` interno), in modo che sia visibile il confine del subtotale per ciascun gruppo `Category`.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**
Se non si chiama mai `setSubtotals`, Aspose.Cells applica la selezione `Automatic` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.Automatic, true)` sul campo di riga `Category` esterno.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scenario 2 — Soppressione di tutti i subtotali (None)**
La chiamata `setSubtotals(PivotFieldSubtotalType.None, true)` rimuove tutte le righe di subtotale dalla tabella pivot, lasciando solo le righe dei campi e il totale complessivo in basso. Questo approccio è utile quando si desidera visualizzare i dati raggruppati grezzi senza alcuna riga di riepilogo.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scenario 3 — Sottoinsieme personalizzato di subtotali (Sum + Average)**
Non è necessario limitarsi a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` opera indipendentemente su un tipo; pertanto, chiamando il metodo due volte — una con `Sum` e una con `Average` — si ottiene un sottoinsieme personalizzato di due righe di subtotale per ogni gruppo `Category`.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Riepilogo**
I tre scenari differiscono soltanto per le chiamate a `setSubtotals`. Tutto il resto — il set di dati, i campi e le aree alle quali sono assegnati — è identico, il che rende i layout direttamente confrontabili.
- **Posizionamento dei campi.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` sposta una colonna dall'area dei dati di origine in una regione. All'interno di una stessa regione, l'ordine delle chiamate corrisponde all'ordine di visualizzazione; la prima chiamata determina quindi il raggruppamento più esterno. I subtotali richiedono due o più campi nella stessa regione: con un solo campo non vi sono gruppi tra cui calcolare un subtotale.
- **Scenario 1 — subtotali automatici.** Se `setSubtotals` non viene chiamato, la scelta viene lasciata a Excel, che applica il proprio subtotale predefinito ai campi numerici. La chiamata a `setSubtotals` con `PivotFieldSubtotalType.Automatic` registra esplicitamente tale scelta anziché lasciarla implicita.
- **Scenario 2 — nessun subtotale.** `setSubtotals` con `PivotFieldSubtotalType.None` disattiva il subtotale predefinito; la tabella pivot mantiene le righe dei campi e il totale complessivo, ma elimina le righe di subtotale che Excel inserirebbe tra le righe dei campi e il totale complessivo.
- **Scenario 3 — un sottoinsieme selezionato.** Ogni chiamata abilita o disabilita esattamente un tipo di subtotale, e le chiamate si cumulano anziché resettarsi a vicenda. Chiamando il metodo una volta con `PivotFieldSubtotalType.Sum` e una volta con `PivotFieldSubtotalType.Average`, entrambi rimangono abilitati e la tabella pivot visualizza un subtotale `Sum`, un subtotale `Average` e un totale complessivo.

{{% alert color="primary" %}}
Il comportamento dei subtotali non è specifico della regione delle righe. Le stesse chiamate a `setSubtotals` su un campo ottenuto da `pivotTable.getColumnFields()` producono gli stessi tre layout sull'asse delle colonne, poiché l'impostazione appartiene al campo pivot e non all'asse su cui è posizionato.
{{% /alert %}}

## **Articoli correlati**
- [Campi pagina nelle tabelle pivot](/cells/it/javascript-cpp/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
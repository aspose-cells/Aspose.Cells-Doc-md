---
title: Mostra Valori Come in Tabella Pivot
linktitle: Mostra Valori Come in Tabella Pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, classifiche e altro con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tabella pivot, mostra valori come, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /it/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili Scenari d'Uso**
Una tabella pivot aggrega normalmente ogni campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza da un elemento base scelto o una classifica — così è possibile eseguire analisi comparative senza formule ausiliarie o colonne calcolate.  
Gli usi tipici includono l'analisi della quota totale, comprese le percentuali di una riga, colonna o totale generale; reportistica cumulativa usando un totale cumulativo in un campo periodo; analisi della varianza rispetto a un elemento di riferimento usando la differenza da o la differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o dal più grande al più piccolo.  
In Aspose.Cells for JavaScript via C++, l'enumerazione `PivotShowValuesAsType` seleziona il calcolo secondario. La proprietà di sola lettura `PivotField.showValuesSetting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà scrivibili `showValuesAs`, `baseFieldIndex` e `baseItemIndex` configurano il comportamento; il metodo di comodità `PivotField.showValuesAs(...)` applica le stesse impostazioni in una sola chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.dataFields`.

## **Membri dell'Enumerazione PivotShowValuesAsType**
Il campo dati mantiene la sua funzione di aggregazione, come Sum o Count, mentre Show Values As trasforma solo il modo in cui il valore aggregato è visualizzato.  
Oltre a impostare direttamente le proprietà `PivotShowValuesSetting` (vedi l'ultima sezione), un metodo di comodità a chiamata unica applica la stessa configurazione. È disponibile in due forme — una che indica il campo base e l'elemento base per indice, l'altra per nome:

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parametro | Significato | Quando È Richiesto |
| --- | --- | --- |
| `showValuesAsType` | Il calcolo secondario `PivotShowValuesAsType` da applicare. | Sempre. |
| `baseField` | Indice basato su zero del campo base tra i campi base della tabella pivot (ad esempio, l'indice del campo riga a cui appartiene l'elemento base), o — nella forma per nome — il nome del campo base. | Gli otto formati relativi al campo base elencati sotto (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); per tutti gli altri formati passare `0` (o `null` nella forma per nome). |
| `baseItem` | Indice basato su zero dell'elemento base, con due sentinelle: -1 seleziona l'elemento precedente e -2 quello successivo (il binding JavaScript via C++ non esporta le costanti denominate — passare i valori letterali). La forma per nome prende invece la didascalia dell'elemento base, e `null` quando il formato selezionato non richiede alcun elemento base. | Solo i tre formati basati su elemento (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) valutano l'elemento base; i cinque formati relativi al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, entrambe le classifiche) lo ignorano — passare `0` o `null`. |

| Tipo di Calcolo | Comportamento | Parametri Elemento Base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato è visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice, didascalia o sentinella precedente/prossimo) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice, didascalia o sentinella precedente/prossimo) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `baseItem` (indice, didascalia o sentinella precedente/prossimo) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (campo che guida l'ordine di accumulazione) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale di riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale di colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale generale. | — |
| `Index` | Visualizza il valore usando la formula di indice di Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale padre. | `baseField` (campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (campo di accumulo) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | `baseField` (campo i cui elementi definiscono l'ambito di classifica) |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | `baseField` (campo i cui elementi definiscono l'ambito di classifica) |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive le proprietà `PivotShowValuesSetting` (`showValuesAs`, `baseFieldIndex` e `baseItemIndex`) — il metodo e l'oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base ed elemento base nella finestra di dialogo Show Values As di Excel.
{{% /alert %}}

## **Mostra Valori come Percentuale del Totale**
Chiama il metodo `PivotField.showValuesAs` con `PivotShowValuesAsType.PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale generale. I numeri visualizzati sono quindi letti come proporzioni dell'intero set di risultati. Questo formato misura ogni valore rispetto solo al totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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

                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Ottieni e Configura PivotField.showValuesSetting**
Leggi la configurazione corrente tramite `PivotField.showValuesSetting`: la proprietà di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui proprietà descrivono il calcolo Show Values As attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs` — scrive tutte le impostazioni in una sola chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone lo stato che `showValuesAs` scrive:
- `showValuesAs` seleziona il calcolo secondario `PivotShowValuesAsType`.
- `baseFieldIndex` specifica l'indice basato su zero del campo base tra i campi pivot. È usato dai formati relativi al campo base.
- `baseItemIndex` specifica l'elemento base: un indice basato su zero di uno specifico elemento pivot, o uno dei due valori sentinella — -1 per l'elemento precedente, -2 per quello successivo (il binding non esporta le costanti denominate). È usato dai formati basati su elemento.
- `baseFieldName` e `baseItemCaption` sono visualizzazioni di sola lettura che segnalano il nome del campo base risolto e la didascalia dell'elemento base; ad esempio, dopo aver selezionato la sentinella dell'elemento precedente, `baseItemCaption` restituisce `(previous)`.  
Dopo aver chiamato `showValuesAs`, chiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e rigenerato con la configurazione aggiornata.

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
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Articoli Correlati**
- [Gestire i Campi Valore nella Tabella Pivot](/cells/it/javascript-cpp/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/javascript-cpp/refresh-pivot-table/)
- [Applicare Stile alla Tabella Pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
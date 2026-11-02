---
title: Mostra valori come nella tabella pivot
linktitle: Mostra valori come nella tabella pivot
description: Visualizza i valori dei campi dati della tabella pivot come percentuale del totale, differenza da un elemento base, totali cumulativi, ranghi e altro con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tabella pivot, mostra valori come, formato visualizzazione dati, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /it/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot normalmente aggrega ogni campo dati con una funzione di aggregazione come `Sum` o `Count`. La funzionalità **Show Values As** di Excel sostituisce ogni risultato visualizzato con un calcolo secondario derivato da quell'aggregato — ad esempio, una percentuale del totale generale, un totale cumulativo, una differenza da un elemento base scelto o un rango — così è possibile eseguire analisi comparative senza formule di supporto o colonne calcolate.  
Gli usi tipici includono l'analisi della quota del totale, comprese le percentuali di riga, colonna o totale generale; la reportistica cumulativa usando un totale cumulativo in un campo di periodo; l'analisi delle varianze rispetto a un elemento di riferimento usando differenza o differenza percentuale da un elemento base; e la classificazione dei valori dal più piccolo al più grande o viceversa.  
In Aspose.Cells for JavaScript via C++, `PivotFieldDataDisplayFormat` seleziona il calcolo secondario. La proprietà di sola lettura `PivotField.showValuesSetting` restituisce un oggetto `PivotShowValuesSetting`, le cui proprietà scrivibili `calculationType`, `baseFieldIndex`, `baseItemPositionType` e `baseItemIndex` configurano il comportamento; il metodo di convenienza `PivotField.showValuesAs(...)` applica le stesse quattro impostazioni in un'unica chiamata. Applica queste impostazioni a un campo dati o valore ottenuto da `PivotTable.dataFields`.

## **Membri dell'enumerazione PivotFieldDataDisplayFormat**
Il campo dati mantiene la sua funzione di aggregazione, come Sum o Count, mentre **Show Values As** trasforma solo il modo in cui il valore aggregato viene visualizzato.  
Oltre a scrivere direttamente le proprietà di `PivotShowValuesSetting` (vedi ultima sezione), un metodo di convenienza a chiamata singola applica la stessa configurazione:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Parametro | Significato | Quando è richiesto |
| --- | --- | --- |
| `displayFormat` | Il calcolo secondario `PivotFieldDataDisplayFormat` da applicare. | Sempre. |
| `baseField` | Indice base‑zero del campo base tra i campi base della tabella pivot (ad esempio, l’indice del campo riga a cui appartiene l’elemento base). | Solo per i sei formati a base di riferimento riportati di seguito (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignorato da ogni altro formato. |
| `baseItemPositionType` | Come l’elemento base è scelto rispetto all’elemento corrente: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo per i tre formati con elemento di base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignorato da ogni altro formato. |
| `baseItem` | Indice base‑zero dell’elemento base. | Solo quando `baseItemPositionType` è `Custom` (l’indice dell’elemento seleziona l’elemento base esatto); ignorato per `Previous` / `Next` e da tutti i formati non basati su elemento — passare `0`. |

| Tipo di calcolo | Comportamento | Parametri elemento base |
| --- | --- | --- |
| `Normal` | Nessun calcolo secondario; il valore aggregato viene visualizzato così com'è (predefinito). | — |
| `DifferenceFrom` | Visualizza il valore come differenza dal valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Visualizza il valore come percentuale del valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Visualizza il valore come differenza percentuale dal valore di un elemento base in un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Visualizza il valore come totale cumulativo per gli elementi successivi di un campo base. | `baseField` (il campo il cui ordine degli elementi guida l’accumulo) |
| `PercentageOfRow` | Visualizza il valore come percentuale del totale della riga. | — |
| `PercentageOfColumn` | Visualizza il valore come percentuale del totale della colonna. | — |
| `PercentageOfTotal` | Visualizza il valore come percentuale del totale generale. | — |
| `Index` | Visualizza il valore usando la formula indice di Excel ((valore * totale generale) / (totale riga * totale colonna)). | — |
| `PercentageOfParentRowTotal` | Visualizza il valore come percentuale del totale della riga padre (per campi riga annidati). | — |
| `PercentageOfParentColumnTotal` | Visualizza il valore come percentuale del totale della colonna padre (per campi colonna annidati). | — |
| `PercentageOfParentTotal` | Visualizza il valore come percentuale del totale del padre. | `baseField` (il campo padre di riferimento) |
| `PercentageOfRunningTotalIn` | Visualizza il valore come percentuale di un totale cumulativo in un campo base. | `baseField` (il campo di accumulo) |
| `RankSmallestToLargest` | Classifica il valore dal più piccolo (1) al più grande. | — |
| `RankLargestToSmallest` | Classifica il valore dal più grande (1) al più piccolo. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` scrive le proprietà `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) — il metodo e l’oggetto proprietà sono due modi per configurare lo stesso stato, rispecchiando i selettori di campo base e elemento base nella finestra di dialogo **Show Values As** di Excel.
{{% /alert %}}

## **Mostra valori come percentuale del totale**
Chiama il metodo `PivotField.showValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` per convertire ogni cella del campo dati, incluso il totale generale, nella sua quota del totale generale. I numeri visualizzati risultano quindi proporzioni dell’intero insieme di risultati. Questo formato misura ogni valore solo rispetto al totale generale, quindi non richiede né campo base né elemento base — gli argomenti finali (`0`, `PivotItemPositionType.Previous`, `0`) sono segnaposto che il formato ignora, come indicato nella tabella dei parametri sopra.

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
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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

## **Ottieni e configura PivotField.showValuesSetting**
Leggi la configurazione corrente tramite `PivotField.showValuesSetting`: la proprietà di sola lettura restituisce l'oggetto `PivotShowValuesSetting` del campo, le cui quattro proprietà descrivono il calcolo **Show Values As** attivo. Per modificare la configurazione, chiama il metodo `PivotField.showValuesAs` — scrive tutte e quattro le impostazioni in un’unica chiamata, così non è necessario assegnare le proprietà una per una.  
L'oggetto `PivotShowValuesSetting` espone le quattro proprietà che `showValuesAs` scrive:
- `calculationType` seleziona il calcolo secondario `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` specifica l’indice base‑zero del campo base entro i campi pivot. È usato dai formati a base di riferimento.
- `baseItemPositionType` determina come l’elemento base è posizionato rispetto all’elemento corrente e accetta `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `baseItemIndex` specifica l’indice base‑zero dell’elemento base ed è usato quando `baseItemPositionType` è `Custom`.
Dopo aver chiamato `showValuesAs`, chiama nuovamente `PivotTable.calculateData()` affinché il corpo della tabella pivot venga ricalcolato e ridisegnato con la nuova configurazione.

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
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
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

## **Articoli correlati**
- [Gestione dei campi valore nella tabella pivot](/cells/it/javascript-cpp/manage-value-fields/)
- [Aggiornamento della tabella pivot](/cells/it/javascript-cpp/refresh-pivot-table/)
- [Applicazione di stile alla tabella pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
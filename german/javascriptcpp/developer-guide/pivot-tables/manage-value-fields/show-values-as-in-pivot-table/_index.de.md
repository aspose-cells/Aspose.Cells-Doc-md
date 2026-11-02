---
title: Werte anzeigen als in Pivot-Tabelle
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Anzeige von Pivot-Tabellendatenfeldwerten als Prozentsatz des Gesamttotals, Differenz zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /de/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot-Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel‑Funktion **Werte anzeigen als** ersetzt jedes dargestellte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel ein Prozentsatz des Gesamttotals, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Anwendungen umfassen Analysen des Anteils am Gesamtergebnis, einschließlich Prozentsätzen einer Zeile, Spalte oder Gesamtsumme; kumulative Berichte mithilfe einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Artikel durch Differenz oder prozentuale Differenz zu einem Basiselement; und die Rangfolge von Werten vom Kleinsten zum Größten oder umgekehrt. In Aspose.Cells for JavaScript via C++ wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.showValuesSetting` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen beschreibbare Eigenschaften `calculationType`, `baseFieldIndex`, `baseItemPositionType` und `baseItemIndex` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Anwenden können Sie diese Einstellungen auf ein Daten‑ oder Wertefeld, das Sie über `PivotTable.dataFields` erhalten.

## **Aufzählungsmitglieder der PivotFieldDataDisplayFormat‑Enumeration**
Das Datenfeld behält seine Aggregatfunktion, wie Summe oder Anzahl, während **Werte anzeigen als** nur die Anzeige des aggregierten Werts verändert. Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Eigenschaften (siehe letzten Abschnitt) wendet eine Ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an:

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die sekundäre Berechnung `PivotFieldDataDisplayFormat`, die angewendet werden soll. | Immer. |
| `baseField` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem der Basis‑Artikel gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie der Basis‑Artikel relativ zum aktuellen Artikel ausgewählt wird: `PivotItemPositionType.Previous`, `.Next` oder `.Custom`. | Nur für die drei Basis-Element-Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basis‑Artikels. | Nur wenn `baseItemPositionType` `Custom` ist (der Index gibt den genauen Basis‑Artikel an); bei `Previous` / `Next` und allen nicht‑Basis‑Formaten wird `0` übergeben. |

| Berechnungstyp | Verhalten | Parameter des Basis‑Artikels |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zum Wert eines Basis‑Artikels in einem Basis‑Feld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Wertes eines Basis‑Artikels in einem Basis‑Feld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Artikels in einem Basis‑Feld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinander folgende Artikel eines Basis‑Feldes an. | `baseField` (das Feld, dessen Artikelreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `Index` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert × Gesamtsumme) / (Zeilensumme × Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme (bei verschachtelten Zeilenfeldern) an. | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme (bei verschachtelten Spaltenfeldern) an. | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basis‑Feld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom Kleinsten (1) zum Größten. | — |
| `RankLargestToSmallest` | Rangiert den Wert vom Größten (1) zum Kleinsten. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die Eigenschaften des `PivotShowValuesSetting`‑Objekts (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`). Die Methode und das Eigenschafts‑Objekt stellen zwei Wege dar, denselben Zustand zu konfigurieren, analog zu den Basis‑Feld‑ und Basis‑Artikel‑Auswahlen im Dialog **Werte anzeigen als** von Excel.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamttotals anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs` mit `PivotFieldDataDisplayFormat.PercentageOfTotal` auf, um jede Zelle des Datenfeldes, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen stellen also Anteile am kompletten Ergebnis‑Datensatz dar. Dieses Format vergleicht jeden Wert ausschließlich mit der Gesamtsumme, sodass kein Basis‑Feld oder Basis‑Artikel erforderlich ist – die nachfolgenden Argumente (`0`, `PivotItemPositionType.Previous`, `0`) sind Platzhalter, die das Format ignoriert, wie aus der Parameter‑Tabelle ersichtlich ist.

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

## **Abrufen und Konfigurieren von PivotField.showValuesSetting**
Lesen Sie die aktuelle Konfiguration über `PivotField.showValuesSetting`: Die schreibgeschützte Eigenschaft gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen vier Eigenschaften die aktive **Werte anzeigen als**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen. Das `PivotShowValuesSetting`‑Objekt stellt die vier Eigenschaften bereit, die `showValuesAs` schreibt:
- `calculationType` wählt die sekundäre Berechnung `PivotFieldDataDisplayFormat` aus.
- `baseFieldIndex` gibt den nullbasierten Index des Basis‑Feldes innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `baseItemPositionType` bestimmt, wie der Basis‑Artikel relativ zum aktuellen Artikel positioniert ist, und akzeptiert `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` oder `PivotItemPositionType.Custom`.
- `baseItemIndex` gibt den nullbasierten Index des Basis‑Artikels an und wird verwendet, wenn `baseItemPositionType` `Custom` ist.
Nachdem Sie `showValuesAs` aufgerufen haben, führen Sie erneut `PivotTable.calculateData()` aus, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration gerendert wird.

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

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/javascript-cpp/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
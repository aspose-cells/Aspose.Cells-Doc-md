---
title: Werte anzeigen als in Pivot‑Tabelle
linktitle: Werte anzeigen als in Pivot‑Tabelle
description: Anzeige von Pivot‑Tabellen‑Datenfeldwerten als Prozentsatz der Gesamtsumme, als Differenz zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, Pivot‑Tabelle, Werte anzeigen als, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /de/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregationsfunktion wie `Sum` oder `Count`. Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die sich aus diesem Aggregat ableitet – beispielsweise ein Prozentsatz der Gesamtsumme, eine laufende Summe, eine Differenz zu einem gewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Einsätze umfassen Analyse des Anteils am Gesamtergebnis, einschließlich Prozentsätzen einer Zeile, Spalte oder Gesamtsumme; kumulative Berichte mittels einer laufenden Summe in einem Perioden‑Feld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz oder prozentualer Differenz zu einem Basiselement; sowie das Rangieren von Werten vom Kleinsten zum Größten oder umgekehrt. In Aspose.Cells for JavaScript via C++ wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.showValuesSetting` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen beschreibbare Eigenschaften `showValuesAs`, `baseFieldIndex` und `baseItemIndex` das Verhalten konfigurieren; die Komfort‑Methode `PivotField.showValuesAs(...)` wendet dieselben Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertfeld an, das Sie über `PivotTable.dataFields` erhalten.

## **PivotShowValuesAsType‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregationsfunktion, wie Sum oder Count, bei, während **Show Values As** nur die Anzeige des aggregierten Werts ändert. Neben dem direkten Schreiben der Eigenschaften des `PivotShowValuesSetting` (siehe den letzten Abschnitt) gibt es eine Ein‑Aufruf‑Komfort‑Methode, die dieselbe Konfiguration anwendet. Sie ist in zwei Formen verfügbar – eine, die Basisfeld und Basiselement per Index adressiert, und eine, die per Name adressiert:

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

| Parameter | Bedeutung | Erforderlich |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basiselement gehört) oder – in der Namens‑Form – der Name des Basisfelds. | Für die acht basisrelativen Formate unten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); für alle anderen Formate `0` (bzw. `null` in der Namens‑Form) übergeben. |
| `baseItem` | Nullbasierter Index des Basiselements, mit zwei Sentinels: -1 wählt das vorherige Element und -2 das nachfolgende (die JavaScript‑via‑C++‑Bindung exportiert die benannten Konstanten nicht – übergeben Sie die literal Werte). In der Namens‑Form wird die Beschriftung des Basiselements verwendet, und `null`, wenn das gewählte Format kein Basiselement benötigt. | Nur die drei Basis‑Element‑Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) benötigen das Basiselement; die fünf feld‑relativen Formate (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, beide Rang‑Formate) ignorieren es – `0` oder `null` übergeben. |

| Berechnungstyp | Verhalten | Parameter des Basiselements |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index, eine Beschriftung oder das vorherige/nächste Sentinel) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index, eine Beschriftung oder das vorherige/nächste Sentinel) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index, eine Beschriftung oder das vorherige/nächste Sentinel) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinander folgende Elemente eines Basisfeldes an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `Index` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Feld, dessen Gesamtsumme die Referenz ist) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom Kleinsten (1) zum Größten. | `baseField` (das Feld, dessen Elemente den Rang‑Umfang bestimmen) |
| `RankLargestToSmallest` | Rangiert den Wert vom Größten (1) zum Kleinsten. | `baseField` (das Feld, dessen Elemente den Rang‑Umfang bestimmen) |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die Eigenschaften des `PivotShowValuesSetting` (`showValuesAs`, `baseFieldIndex` und `baseItemIndex`) — die Methode und das Eigenschaftsobjekt sind zwei Wege, denselben Zustand zu konfigurieren und spiegeln die Basisfeld‑ und Basiselement‑Auswähler im Excel‑Dialog **Show Values As** wider.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs` mit `PivotShowValuesAsType.PercentageOfTotal` auf, um jede Datenfeld‑Zelle, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich gegen die Gesamtsumme, sodass weder Basisfeld noch Basiselement erforderlich sind – die nachfolgenden Argumente (`0`, `0`) sind Platzhalter, die das Format ignoriert, wie in der obigen Parametertabelle erklärt.

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

## **Abrufen und Konfigurieren von PivotField.showValuesSetting**
Lesen Sie die aktuelle Konfiguration über `PivotField.showValuesSetting`: Die schreibgeschützte Eigenschaft gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen Eigenschaften die aktivierte **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs` auf – sie schreibt alle Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen.  
Das Objekt `PivotShowValuesSetting` stellt den Zustand bereit, den `showValuesAs` schreibt:

- `showValuesAs` wählt die sekundäre Berechnung vom Typ `PivotShowValuesAsType` aus.  
- `baseFieldIndex` gibt den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisrelativen Formaten verwendet.  
- `baseItemIndex` gibt das Basiselement an: einen nullbasierten Index eines bestimmten Pivot‑Elements oder einen der beiden Sentinel‑Werte — -1 für das vorherige Element, -2 für das nachfolgende (die Bindung exportiert die benannten Konstanten nicht). Er wird von den Basis‑Element‑Formaten verwendet.  
- `baseFieldName` und `baseItemCaption` sind schreibgeschützte Ansichten, die den aufgelösten Basisfeld‑Namen bzw. die Basis‑Element‑Beschriftung melden; nach Auswahl des Sentinel‑Elements für das vorherige Element liefert `baseItemCaption` beispielsweise `(previous)`.

Nachdem Sie `showValuesAs` aufgerufen haben, rufen Sie erneut `PivotTable.calculateData()` auf, damit der Pivot‑Körper mit der aktualisierten Konfiguration neu berechnet und neu gerendert wird.

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

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/javascript-cpp/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
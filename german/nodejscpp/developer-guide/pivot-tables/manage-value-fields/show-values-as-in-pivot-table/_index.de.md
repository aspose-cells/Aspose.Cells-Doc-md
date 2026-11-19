---
title: Werte anzeigen als in Pivot-Tabelle
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Zeigt Werte der Datenfelder einer Pivot‑Tabelle als Prozentsatz des Gesamtergebnisses, als Unterschied zu einem Basiselement, als laufende Summe, Ranglisten und mehr mit Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Pivot‑Tabelle, Werte anzeigen als, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /de/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT`. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel ein Prozentsatz des Gesamtergebnisses, eine laufende Summe, ein Unterschied zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können.  
Typische Anwendungsfälle umfassen die Analyse des Anteils am Gesamtergebnis, einschließlich Prozentsätze einer Zeile, Spalte oder des Gesamtergebnisses; kumulative Berichte mit einer laufenden Summe in einem Zeitraumfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Unterschied oder prozentualer Differenz zu einem Basiselement; sowie das Rangordnen von Werten vom Kleinsten zum Größten oder umgekehrt.  
In Aspose.Cells for Node.js via C++ wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Der schreibgeschützte Zugriff `PivotField.getShowValuesSetting()` liefert ein Objekt vom Typ `PivotShowValuesSetting`, dessen Methoden `setShowValuesAs()`, `setBaseFieldIndex()` und `setBaseItemIndex()` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotShowValuesAsType Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion, wie SUM oder COUNT, bei, während **Show Values As** nur die Anzeige des aggregierten Werts transformiert.  
Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Einstellungen (siehe den letzten Abschnitt) wendet eine Ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an. Sie ist in zwei Formen verfügbar – eine, die das Basisfeld und Basiselement per Index anspricht, und eine, die den Namen verwendet:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parameter | Bedeutung | Wann erforderlich |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfelds, zu dem das Basiselement gehört) oder – in der Namensform – der Name des Basisfelds. | Die acht unten aufgeführten basisrelativen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); übergeben Sie `0` (oder `null` in der Namensform) für jedes andere Format. |
| `baseItem` | Nullbasierter Index des Basiselements mit zwei Sentinelwerten: -1 wählt das vorherige Element und -2 das nachfolgende (die Node.js via C++‑Bindung exportiert die benannten Konstanten nicht – übergeben Sie die wörtlichen Werte). Die Namensform verwendet stattdessen die Beschriftung des Basiselements und `null`, wenn das ausgewählte Format kein Basiselement benötigt. | Nur die drei basiselementbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) berücksichtigen das Basiselement; die fünf feldrelativen Formate (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` sowie beide Rangformate) ignorieren es – übergeben Sie `0` oder `null`. |

| Berechnungstyp | Verhalten | Basiselement‑Parameter |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Unterschied zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung, bzw. das vorherige bzw. nächste Sentinel) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung, bzw. das vorherige bzw. nächste Sentinel) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung, bzw. das vorherige bzw. nächste Sentinel) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz des Gesamtergebnisses an. | — |
| `Index` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtergebnis) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Feld, dessen Gesamtsumme die Referenz ist) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangt den Wert vom Kleinsten (1) bis zum Größten. | `baseField` (das Feld, dessen Elemente den Rangumfang bestimmen) |
| `RankLargestToSmallest` | Rangt den Wert vom Größten (1) bis zum Kleinsten. | `baseField` (das Feld, dessen Elemente den Rangumfang bestimmen) |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Einstellungen (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()` und `getBaseItemIndex()`/`setBaseItemIndex()`) – die Methode und das Property‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren, analog zu den Basisfeld‑ und Basiselement‑Auswahlen im **Show Values As**‑Dialog von Excel.
{{% /alert %}}

## **Werte anzeigen als Prozentsatz des Gesamtergebnisses**
Rufen Sie die Methode `PivotField.showValuesAs()` mit `PivotShowValuesAsType.PercentageOfTotal` auf, um jede Datenfeld‑Zelle, einschließlich des Gesamtergebnisses, in ihren Anteil am Gesamtergebnis zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich am Gesamtergebnis, sodass kein Basisfeld oder Basiselement erforderlich ist – die nachfolgenden Argumente (`0`, `0`) sind Platzhalter, die das Format ignoriert, wie in der obigen Parametertabelle angegeben.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting()**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Der schreibgeschützte Zugriff gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen Einstellungen die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs()` auf – sie schreibt alle Einstellungen in einem Aufruf, sodass Sie sie nicht einzeln festlegen müssen.  
Das Objekt `PivotShowValuesSetting` stellt den von `showValuesAs()` geschriebenen Zustand bereit:
- `getShowValuesAs()` und `setShowValuesAs()` wählen die sekundäre Berechnung vom Typ `PivotShowValuesAsType` aus.
- `getBaseFieldIndex()` und `setBaseFieldIndex()` geben den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisrelativen Formaten verwendet.
- `getBaseItemIndex()` und `setBaseItemIndex()` geben das Basiselement an: einen nullbasierten Index eines bestimmten Pivot‑Elements oder einen der beiden Sentinelwerte – -1 für das vorherige Element, -2 für das nachfolgende (die Bindung exportiert die benannten Konstanten nicht). Er wird von den basiselementbezogenen Formaten verwendet.
- `getBaseFieldName()` und `getBaseItemCaption()` sind schreibgeschützte Ansichten, die den aufgelösten Namen des Basisfelds bzw. die Beschriftung des Basiselements zurückgeben; zum Beispiel liefert `getBaseItemCaption()` nach Auswahl des vorherigen‑Element‑Sentinels den Wert `(previous)`.
Rufen Sie nach dem Aufruf von `showValuesAs()` erneut `PivotTable.calculateData()` auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration erneut gerendert wird.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/nodejs-cpp/manage-value-fields/)
- [Aktualisieren der Pivot‑Tabelle](/cells/de/nodejs-cpp/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
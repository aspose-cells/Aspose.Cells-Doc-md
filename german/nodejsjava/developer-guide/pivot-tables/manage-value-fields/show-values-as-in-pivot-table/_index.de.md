---
title: Werte anzeigen als in Pivot‑Tabelle
linktitle: Werte anzeigen als in Pivot‑Tabelle
description: Zeigt die Datenfeldwerte einer Pivot‑Tabelle als Prozentsatz der Gesamtsumme, als Differenz zu einem Basiselement, fortlaufende Summen, Rangfolgen und mehr an mit Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Pivot‑Tabelle, Werte anzeigen als, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /de/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT`. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – beispielsweise einen Prozentsatz des Gesamtergebnisses, eine fortlaufende Summe, eine Differenz zu einem gewählten Basiselement oder einen Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Anwendungsfälle umfassen Analysen des Anteils am Gesamtwert, einschließlich Prozentsätzen einer Zeile, Spalte oder Gesamtsumme; kumulative Berichte mit einer fortlaufenden Summe in einem Periodenfeld; Varianzanalysen gegenüber einem Benchmark‑Element mittels Differenz oder prozentualer Differenz zu einem Basiselement; sowie das Rangordnen von Werten vom Kleinsten zum Größten oder umgekehrt. In Aspose.Cells for Node.js via Java wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Die schreibgeschützte Methode `PivotField.getShowValuesSetting()` liefert ein `PivotShowValuesSetting`‑Objekt, dessen Methoden `setShowValuesAs()`, `setBaseFieldIndex()` und `setBaseItemIndex()` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotShowValuesAsType‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion, wie SUM oder COUNT, während **Show Values As** nur die Anzeige des aggregierten Wertes transformiert. Neben der direkten Verwendung der `PivotShowValuesSetting`‑Setter (siehe letzten Abschnitt) wendet eine einteilige Komfortmethode dieselbe Konfiguration an. Sie ist in zwei Varianten verfügbar – eine, die das Basisfeld und Basiselement per Index adressiert, und eine, die sie per Name angibt:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parameter | Bedeutung | Erforderlich, wenn |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, dem das Basiselement zugeordnet ist) oder – in der Namensform – der Name des Basisfelds. | Für die acht basisbezogenen Formate unten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); für alle anderen Formate `0` (oder `null` in der Namensform) übergeben. |
| `baseItem` | Nullbasierter Index des Basiselements, mit zwei Sonderwerten: -1 wählt das vorherige Element und -2 das nachfolgende (die Paket‑Root‑Bibliothek exportiert die Konstanten von `PivotShowValuesSetting` nicht – die Literalwerte übergeben). In der Namensform wird stattdessen die Beschriftung des Basiselements verwendet, und `null`, wenn das gewählte Format kein Basiselement benötigt. | Nur die drei basiselementbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) benötigen das Basiselement; die fünf feldbezogenen Formate (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, beide Rangformate) ignorieren es – `0` oder `null` übergeben. |

| Berechnungstyp | Verhalten | Parameter für Basiselement |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (Index, Beschriftung oder vorheriges/nächstes Sentinel) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Wertes eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als fortlaufende Summe für aufeinander folgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mittels der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Feld, dessen Summe die Referenz ist) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer fortlaufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert vom Kleinsten (1) zum Größten. | `baseField` (das Feld, dessen Elemente den Rangumfang bestimmen) |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert vom Größten (1) zum Kleinsten. | `baseField` (das Feld, dessen Elemente den Rangumfang bestimmen) |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt den Zustand von `PivotShowValuesSetting` über `setShowValuesAs()`, `setBaseFieldIndex()` und `setBaseItemIndex()` – die Methode und das Property‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren und spiegeln die Auswahl von Basisfeld und Basiselement im **Show Values As**‑Dialog von Excel wider.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs()` mit `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` auf, um jede Datenfeldzelle, einschließlich der Gesamtsumme, in deren Anteil an der Gesamtsumme zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des kompletten Ergebnis‑Sets dar. Dieses Format vergleicht jeden Wert ausschließlich mit der Gesamtsumme, sodass weder Basisfeld noch Basiselement benötigt werden – die überzähligen Argumente (`0`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle zeigt.

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting()**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Die schreibgeschützte Methode liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen Einstellungen die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs()` auf – sie schreibt alle Einstellungen in einem Aufruf, sodass Sie sie nicht einzeln setzen müssen.
Das `PivotShowValuesSetting`‑Objekt stellt den Zustand bereit, den `showValuesAs()` schreibt:
- `getShowValuesAs()` / `setShowValuesAs()` wählt die sekundäre Berechnung vom Typ `PivotShowValuesAsType` aus.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` gibt den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `getBaseItemIndex()` / `setBaseItemIndex()` gibt das Basiselement an: einen nullbasierten Index eines konkreten Pivot‑Elements oder einen der beiden Sonderwerte – -1 für das vorherige Element, -2 für das nachfolgende (die Paket‑Root‑Bibliothek exportiert die benannten Konstanten nicht). Er wird von den basiselementbezogenen Formaten verwendet.
- `getBaseFieldName()` und `getBaseItemCaption()` sind schreibgeschützte Ansichten, die den aufgelösten Basisfeldnamen bzw. die Basiselement‑Beschriftung zurückgeben; nach Auswahl des vorherigen‑Element‑Sentinels liefert `getBaseItemCaption()` z. B. `(previous)`.
Nachdem `showValuesAs()` aufgerufen wurde, führen Sie `PivotTable.calculateData()` erneut aus, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [Verwalten von Wertfeldern in Pivot‑Tabelle](/cells/de/nodejs-java/manage-value-fields/)
- [Aktualisieren der Pivot‑Tabelle](/cells/de/nodejs-java/refresh-pivot-table/)
- [Anwenden von Stil auf Pivot‑Tabelle](/cells/de/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
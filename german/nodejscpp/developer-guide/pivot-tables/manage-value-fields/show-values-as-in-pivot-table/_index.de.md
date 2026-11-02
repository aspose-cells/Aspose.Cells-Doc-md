---
title: Werte anzeigen als in Pivot-Tabelle
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Anzeige von Pivot-Tabellen-Datenfeldwerten als Prozentsatz des Gesamtergebnisses, als Differenz zu einem Basis‑Element, laufende Summen, Ranglisten und mehr mit Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /de/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT`. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel einen Prozentsatz des Gesamtergebnisses, eine laufende Summe, eine Differenz zu einem ausgewählten Basis‑Element oder einen Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Anwendungen umfassen die Analyse des Anteils am Gesamtergebnis (Prozentsätze einer Zeile, Spalte oder Gesamtsumme), Berichte mit laufenden Summen in einem Periodenfeld, Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz oder prozentualer Differenz zu einem Basis‑Element sowie das Rangordnen von Werten von klein nach groß oder umgekehrt. In Aspose.Cells for Node.js via C++ wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Der schreibgeschützte Accessor `PivotField.getShowValuesSetting()` liefert ein `PivotShowValuesSetting`‑Objekt, dessen beschreibbare Methoden `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` und `setBaseItemIndex()` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotFieldDataDisplayFormat‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion, zum Beispiel SUM oder COUNT, während **Show Values As** lediglich die Darstellung des aggregierten Werts verändert.  
Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Eigenschaften (siehe letzten Abschnitt) wendet eine Ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Parameter | Bedeutung | Wann erforderlich |
| --- | --- | --- |
| `displayFormat` | Die anzuwendende sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat`. | Immer. |
| `baseField` | Nullbasierter Index des Basis‑Feldes unter den Basis‑Feldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basis‑Element gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basis‑Element relativ zum aktuellen Element gewählt wird: `PivotItemPositionType.PREVIOUS`, `.NEXT` oder `.CUSTOM`. | Nur für die drei Basis-Element-Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basis‑Elements. | Nur wenn `baseItemPositionType` auf `CUSTOM` gesetzt ist (der Index wählt das genaue Basis‑Element); wird bei `PREVIOUS` / `NEXT` und bei allen Nicht‑Basis‑Formaten ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Werts eines Basis‑Elements in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basis‑Feldes an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme (bei verschachtelten Zeilenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme (bei verschachtelten Spaltenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basis‑Feld an. | `baseField` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert von klein nach groß (1 = kleinstes). | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert von groß nach klein (1 = größtes). | — |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Einstellungen (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, und `getBaseItemIndex()`/`setBaseItemIndex()`) – die Methode und das Eigenschafts‑Objekt stellen zwei Wege dar, denselben Zustand zu konfigurieren, analog zu den Basis‑Feld‑ und Basis‑Element‑Auswahlhilfen im Excel‑Dialog **Show Values As**.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamtergebnisses anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs()` mit `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` auf, um jede Zelle des Datenfeldes, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich relativ zur Gesamtsumme, sodass kein Basis‑Feld oder Basis‑Element erforderlich ist – die nachfolgenden Argumente (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle anmerkt.

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
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting()**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Der schreibgeschützte Accessor liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen vier Eigenschaften die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs()` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen.  
Das `PivotShowValuesSetting`‑Objekt stellt die vier Einstellungen bereit, die `showValuesAs()` schreibt:
- `getCalculationType()` und `setCalculationType()` wählen die sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat` aus.
- `getBaseFieldIndex()` und `setBaseFieldIndex()` geben den nullbasierten Index des Basis‑Feldes innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `getBaseItemPositionType()` und `setBaseItemPositionType()` bestimmen, wie das Basis‑Element relativ zum aktuellen Element positioniert ist, und akzeptieren `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` oder `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` und `setBaseItemIndex()` geben den nullbasierten Index des Basis‑Elements an und werden verwendet, wenn `getBaseItemPositionType()` auf `CUSTOM` gesetzt ist.  
Nachdem `showValuesAs()` aufgerufen wurde, führen Sie erneut `PivotTable.calculateData()` aus, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration gerendert wird.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/nodejs-cpp/manage-value-fields/)
- [Aktualisieren der Pivot‑Tabelle](/cells/de/nodejs-cpp/refresh-pivot-table/)
- [Anwenden von Stil auf Pivot‑Tabelle](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
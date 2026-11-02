---
title: Werte anzeigen als in PivotTable
linktitle: Werte anzeigen als in PivotTable
description: Anzeige von Datenfeldwerten einer Pivot‑Tabelle als Prozentsatz der Gesamtsumme, Differenz zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Pivot‑Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /de/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Einsatzszenarien**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregationsfunktion wie `SUM` oder `COUNT`. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel ein Prozentsatz der Gesamtsumme, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können.  
Typische Anwendungsfälle umfassen die Analyse des Anteils an der Gesamtsumme, einschließlich Prozentsätze einer Zeile, Spalte oder des Gesamtsumme; kumulative Berichte mithilfe einer laufenden Summe in einem Zeitraumfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz oder prozentualer Differenz zu einem Basiselement; sowie das Rangieren von Werten von klein nach groß oder von groß nach klein.  
In Aspose.Cells for Node.js via Java wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Die schreibgeschützte Methode `PivotField.getShowValuesSetting()` gibt ein Objekt vom Typ `PivotShowValuesSetting` zurück. Mit ihren Methoden `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` und `setBaseItemIndex()` wird das Verhalten konfiguriert; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotFieldDataDisplayFormat Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregationsfunktion, z. B. SUM oder COUNT, während **Show Values As** nur die Anzeige des aggregierten Werts verändert.  
Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Einstellungen (siehe letzten Abschnitt) wendet eine Ein‑Aufruf‑Methode dieselbe Konfiguration an:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Parameter | Bedeutung | Wann erforderlich |
| --- | --- | --- |
| `displayFormat` | Die sekundäre Berechnung `PivotFieldDataDisplayFormat`, die angewendet werden soll. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfelds, zu dem das Basiselement gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basiselement relativ zum aktuellen Element gewählt wird: `PivotItemPositionType.PREVIOUS`, `.NEXT` oder `.CUSTOM`. | Nur für die drei Basis-Element-Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basiselements. | Nur wenn `baseItemPositionType` auf `CUSTOM` gesetzt ist (der Index wählt das exakte Basiselement); wird für `PREVIOUS` / `NEXT` und alle Nicht‑Basis‑Formate ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz des Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme (bei verschachtelten Zeilenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme (bei verschachtelten Spaltenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert von klein nach groß (1 = kleinstes). | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert von groß nach klein (1 = größtes). | — |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Einstellungen (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` und `setBaseItemIndex()`) – die Methode und das Einstellungsobjekt sind zwei Wege, denselben Zustand zu konfigurieren, analog zu den Basisfeld‑ und Basiselement‑Auswahlen im Dialogfeld **Show Values As** von Excel.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs()` mit `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` auf, um jede Zelle eines Datenfeldes, einschließlich des Gesamtsumme, in ihren Anteil an der Gesamtsumme zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnissatzes dar. Dieses Format misst jeden Wert nur gegen die Gesamtsumme, sodass weder ein Basisfeld noch ein Basiselement benötigt werden – die nachfolgenden Argumente (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle zeigt.

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
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Die schreibgeschützte Methode gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen vier Einstellungen die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs()` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie sie nicht einzeln zuweisen müssen.  
Das `PivotShowValuesSetting`‑Objekt stellt die vier von `showValuesAs()` geschriebenen Einstellungen bereit:
- `getCalculationType()` / `setCalculationType()` wählt die sekundäre Berechnung `PivotFieldDataDisplayFormat` aus.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` gibt den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` bestimmt, wie das Basiselement relativ zum aktuellen Element positioniert ist, und akzeptiert `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` oder `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex()` gibt den nullbasierten Index des Basiselements an und wird verwendet, wenn `getBaseItemPositionType()` auf `CUSTOM` gesetzt ist.
Nachdem Sie `showValuesAs()` aufgerufen haben, rufen Sie erneut `PivotTable.calculateData()` auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```javascript
const AsposeCells = require("aspose.cells");
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
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
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
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/nodejs-java/manage-value-fields/)
- [Aktualisieren der Pivot‑Tabelle](/cells/de/nodejs-java/refresh-pivot-table/)
- [Anwenden von Stil auf Pivot‑Tabelle](/cells/de/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
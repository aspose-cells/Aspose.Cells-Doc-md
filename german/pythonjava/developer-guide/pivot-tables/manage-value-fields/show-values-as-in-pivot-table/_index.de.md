---
title: Werte anzeigen wie in Pivot-Tabelle
description: Anzeige von Pivot-Tabellen-Datenfeldwerten als Prozentsatz des Gesamtergebnisses, Unterschied zu einem Basiselement, fortlaufende Summen, Ranglisten und mehr mit Aspose.Cells für Python über Java.
linktitle: Show Values As
keywords: Aspose.Cells, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /de/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregationsfunktion wie `Sum` oder `Count`. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel einen Prozentsatz des Gesamtergebnisses, eine fortlaufende Summe, eine Differenz zu einem ausgewählten Basis‑Element oder einen Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Anwendungsfälle umfassen die Analyse des Anteils am Gesamtergebnis, einschließlich Prozentsätzen einer Zeile, Spalte oder des Gesamtergebnisses; kumulative Berichte mittels einer fortlaufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz oder prozentualer Differenz zu einem Basis‑Element; und das Rangieren von Werten vom kleinsten zum größten oder vom größten zum kleinsten. In Aspose.Cells für Python über Java wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Die schreibgeschützte Methode `PivotField.getShowValuesSetting()` liefert ein `PivotShowValuesSetting`‑Objekt, dessen schreibbare Methoden `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` und `setBaseItemIndex` das Verhalten konfigurieren; die Komfort‑Methode `PivotField.showValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Werte‑Feld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotFieldDataDisplayFormat‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregationsfunktion, wie Summe oder Anzahl, während **Show Values As** nur die Anzeige des aggregierten Werts verändert.  
Zusätzlich zum direkten Setzen der `PivotShowValuesSetting`‑Eigenschaften (siehe letzten Abschnitt) kann die Ein‑Aufruf‑Komfort‑Methode dieselbe Konfiguration anwenden:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die sekundäre Berechnung `PivotFieldDataDisplayFormat`, die angewendet wird. | Immer. |
| `baseField` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basis‑Element gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basis‑Element relativ zum aktuellen Element ausgewählt wird: `PivotItemPositionType.Previous`, `.Next` oder `.Custom`. | Nur für die drei Basis-Element-Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basis‑Elements. | Nur wenn `baseItemPositionType` `Custom` ist (der Index wählt das exakte Basis‑Element); wird für `Previous` / `Next` und bei allen Nicht‑Basis‑Formaten ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zum Wert eines Basis‑Elements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Werts eines Basis‑Elements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Elements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `RunningTotalIn` | Zeigt den Wert als fortlaufende Summe für aufeinanderfolgende Elemente eines Basisfeldes an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz des Gesamtergebnisses an. | — |
| `Index` | Zeigt den Wert mittels der Excel‑Index‑Formel ((Wert * Gesamtergebnis) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Zeilensumme an (bei verschachtelten Zeilenfeldern). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz seiner übergeordneten Spaltensumme an (bei verschachtelten Spaltenfeldern). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz seines übergeordneten Gesamtergebnisses an. | `baseField` (das übergeordnete Referenzfeld) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer fortlaufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom kleinsten (1) zum größten. | — |
| `RankLargestToSmallest` | Rangiert den Wert vom größten (1) zum kleinsten. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die Werte von `PivotShowValuesSetting` über `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` und `setBaseItemIndex` – die Methode und das Einstellungs‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren und spiegeln die Basis‑Feld‑ und Basis‑Element‑Auswahl im Show‑Values‑As‑Dialog von Excel wider.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamtergebnisses anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs` mit `PivotFieldDataDisplayFormat.PercentageOfTotal` auf, um jede Zelle des Datenfeldes, einschließlich des Gesamtergebnisses, in ihren Anteil am Gesamtergebnis zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich am Gesamtergebnis, daher werden kein Basis‑Feld und kein Basis‑Element benötigt – die nachfolgenden Argumente (`0`, `PivotItemPositionType.Previous`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle zeigt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting()**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Die schreibgeschützte Methode gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen vier Eigenschaften die aktive Show‑Values‑As‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen. Das Objekt `PivotShowValuesSetting` stellt die vier Eigenschaften bereit, die `showValuesAs` schreibt:
- `getCalculationType()` gibt die sekundäre Berechnung `PivotFieldDataDisplayFormat` zurück, während `setCalculationType(...)` sie ändert.
- `getBaseFieldIndex()` und `setBaseFieldIndex(...)` geben den nullbasierten Index des Basisfeldes innerhalb der Pivot‑Felder an. Sie wird von den basisbezogenen Formaten verwendet.
- `getBaseItemPositionType()` und `setBaseItemPositionType(...)` bestimmen, wie das Basis‑Element relativ zum aktuellen Element positioniert ist und akzeptieren `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` oder `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` und `setBaseItemIndex(...)` geben den nullbasierten Index des Basis‑Elements an und werden verwendet, wenn `BaseItemPositionType` `Custom` ist. Nachdem Sie `showValuesAs` aufgerufen haben, rufen Sie erneut `PivotTable.calculateData()` auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/python-java/manage-value-fields/)
- [Aktualisieren von Pivot‑Tabelle](/cells/de/python-java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot‑Tabelle](/cells/de/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
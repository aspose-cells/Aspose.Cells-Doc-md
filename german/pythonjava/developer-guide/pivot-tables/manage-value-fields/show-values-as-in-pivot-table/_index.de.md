---
title: Werte anzeigen als in PivotTable
linktitle: Werte anzeigen als in PivotTable
description: Zeigen Sie PivotTable-Datenfeldwerte als Prozentsatz des Gesamtergebnisses, als Unterschied zu einem Basiselement, laufende Summen, Rangfolgen und mehr mit Aspose.Cells for Python via Java.
keywords: Aspose.Cells, PivotTable, Werte anzeigen als, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /de/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Eine PivotTable aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT`. Die Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel ein Prozentsatz des Gesamtergebnisses, eine laufende Summe, ein Unterschied zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können. Typische Verwendungen umfassen Analysen des Anteils am Gesamtergebnis, einschließlich Prozentsätzen einer Zeile, Spalte oder des Gesamtergebnisses; kumulative Berichte mittels einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element mit Unterschied zu oder prozentualem Unterschied zu einem Basiselement; sowie das Rangordnen von Werten vom Kleinsten zum Größten oder umgekehrt. In Aspose.Cells for Python via Java wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Die schreibgeschützte Methode `PivotField.getShowValuesSetting()` liefert ein `PivotShowValuesSetting`‑Objekt, dessen Methoden `setShowValuesAs(...)`, `setBaseFieldIndex(...)` und `setBaseItemIndex(...)` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotShowValuesAsType‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion bei, z. B. `SUM` oder `COUNT`, während *Show Values As* nur die Anzeige des aggregierten Wertes ändert. Neben der direkten Verwendung der `PivotShowValuesSetting`‑Setter (siehe letzten Abschnitt) wendet eine ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an. Sie ist in zwei Formen verfügbar – eine, die das Basisfeld und das Basiselement per Index adressiert, und eine, die sie per Name adressiert:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `show_values_as_type` | Der `PivotShowValuesAsType`‑Sekundärwert, der angewendet werden soll. | Immer. |
| `base_field` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der PivotTable (z. B. der Index des Zeilenfeldes, zu dem das Basiselement gehört), oder – in der Namensform – der Name des Basisfeldes. | Die acht basis‑relativen Formate unten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); für alle anderen Formate `0` (bzw. `None` in der Namensform) übergeben. |
| `base_item` | Nullbasierter Index des Basiselements, mit zwei Sentinel‑Werten: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) wählt das vorherige Element und `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) das folgende. Die Namensform nimmt die Beschriftung des Basiselements und `None`, wenn das ausgewählte Format kein Basiselement benötigt. | Nur die drei basiselementbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) benötigen das Basiselement; die fünf feld‑relativen Formate (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, beide Rangformate) ignorieren es – übergeben Sie `0` oder `None`. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Unterschied zum Wert eines Basiselements in einem Basisfeld an. | `base_field` + `base_item` (Index oder Beschriftung bzw. vorheriger/folgender Sentinel) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Wertes eines Basiselements in einem Basisfeld an. | `base_field` + `base_item` (Index oder Beschriftung bzw. vorheriger/folgender Sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `base_field` + `base_item` (Index oder Beschriftung bzw. vorheriger/folgender Sentinel) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfeldes an. | `base_field` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mithilfe der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Zeilensumme (für verschachtelte Zeilenfelder) an. | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Spaltensumme (für verschachtelte Spaltenfelder) an. | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz seiner übergeordneten Gesamtsumme an. | `base_field` (das übergeordnete Feld, dessen Gesamtsumme die Referenz ist) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `base_field` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert vom Kleinsten (1) zum Größten. | `base_field` (das Feld, dessen Elemente den Rangbereich definieren) |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert vom Größten (1) zum Kleinsten. | `base_field` (das Feld, dessen Elemente den Rangbereich definieren) |

{{% alert color="primary" %}}
`showValuesAs(...)` schreibt die Werte von `PivotShowValuesSetting` über `setShowValuesAs`, `setBaseFieldIndex` und `setBaseItemIndex` – die Methode und das Einstellungs‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren und entsprechen den Basisfeld‑ und Basiselement‑Auswahlmöglichkeiten im Dialog **Show Values As** von Excel.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs` mit `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` auf, um jede Datenfeld‑Zelle, einschließlich der Gesamtsumme, in ihren Anteil am Gesamtergebnis zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des vollständigen Ergebnis‑Sets dar. Dieses Format vergleicht jeden Wert ausschließlich mit der Gesamtsumme, sodass kein Basisfeld oder Basiselement nötig ist – die nachfolgenden Argumente (`0`, `0`) sind Platzhalter, die das Format ignoriert, wie die Parametertabelle oben anmerkt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting()**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Die schreibgeschützte Methode liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen Eigenschaften die aktive *Show Values As*‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs` auf – sie schreibt alle Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln setzen müssen. Das `PivotShowValuesSetting`‑Objekt gibt den Zustand wieder, den `showValuesAs` schreibt:
- `getShowValuesAs()` liefert die `PivotShowValuesAsType`‑Sekundärberechnung, während `setShowValuesAs(...)` sie ändert.
- `getBaseFieldIndex()` und `setBaseFieldIndex(...)` geben den nullbasierten Index des Basisfeldes innerhalb der Pivot‑Felder an. Er wird von den basis‑relativen Formaten verwendet.
- `getBaseItemIndex()` und `setBaseItemIndex(...)` geben das Basiselement an: einen nullbasierten Index eines bestimmten Pivot‑Elements oder einen der beiden Sentinel‑Werte – `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) für das vorherige Element, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) für das folgende. Er wird von den basiselement‑bezogenen Formaten verwendet.
- `getBaseFieldName()` und `getBaseItemCaption()` sind schreibgeschützte Ansichten, die den aufgelösten Basisfeldnamen bzw. die Basis‑Element‑Beschriftung melden; nach der Auswahl des vorherigen‑Element‑Sentinels liefert `getBaseItemCaption()` beispielsweise `(previous)`.
Nach dem Aufruf von `showValuesAs` rufen Sie `PivotTable.calculateData()` erneut auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in PivotTable](/cells/de/python-java/manage-value-fields/)
- [Aktualisieren der PivotTable](/cells/de/python-java/refresh-pivot-table/)
- [Anwenden von Format auf PivotTable](/cells/de/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
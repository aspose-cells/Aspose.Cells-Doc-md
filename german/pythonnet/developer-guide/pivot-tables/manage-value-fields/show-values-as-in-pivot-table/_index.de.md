---
title: Werte anzeigen als in PivotTable
linktitle: Werte anzeigen als in PivotTable
description: Pivot‑Tabellendatenfeldwerte als Prozentsatz der Gesamtsumme, Differenz zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for Python via .NET anzeigen.
keywords: Aspose.Cells for Python via .NET, PivotTable, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /de/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
Eine Pivot‑Tabelle fasst normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT` zusammen. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus diesem Aggregat abgeleitet wird – beispielsweise ein Prozentsatz der Gesamtsumme, eine laufende Gesamtsumme, eine Differenz zu einem gewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen durchführen können, ohne Hilfsformeln oder berechnete Spalten zu verwenden.  
Typische Anwendungsfälle umfassen die Analyse des Anteils an der Gesamtsumme, einschließlich Prozentsätzen einer Zeile, Spalte oder des Gesamtergebnisses; kumulierte Berichte mittels einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz zu oder prozentualer Differenz von einem Basiselement; sowie die Rangfolge von Werten vom Kleinsten zum Größten oder vom Größten zum Kleinsten.  
In Aspose.Cells for Python via .NET wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.show_values_setting` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen beschreibbare Eigenschaften `calculation_type`, `base_field_index`, `base_item_position_type` und `base_item_index` das Verhalten konfigurieren; die Komfortmethode `PivotField.show_values_as(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das aus `PivotTable.data_fields` abgerufen wird.

## **Aufzählungsmitglieder von PivotFieldDataDisplayFormat**
Das Datenfeld behält seine Aggregatfunktion, wie `SUM` oder `COUNT`, bei, während Show Values As lediglich die Anzeige des aggregierten Werts verändert.  
Abgesehen davon, dass die Eigenschaften von `PivotShowValuesSetting` direkt geschrieben werden (siehe den letzten Abschnitt), wendet eine Ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `display_format` | Die anzuwendende sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat`. | Immer. |
| `base_field` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basis‑Element gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); von allen anderen Formaten wird es ignoriert. |
| `base_item_position_type` | Wie das Basis‑Element relativ zum aktuellen Element ausgewählt wird: `PivotItemPositionType.PREVIOUS`, `.NEXT` oder `.CUSTOM`. | Nur für die drei Basis-Element-Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); von allen anderen Formaten wird es ignoriert. |
| `base_item` | Nullbasierter Index des Basis‑Elements. | Nur wenn `base_item_position_type` auf `CUSTOM` gesetzt ist (der Element‑Index wählt das exakte Basis‑Element); wird für `PREVIOUS`/`NEXT` und alle nicht‑Basis‑Formate ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` nur bei `CUSTOM`) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Werts eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` nur bei `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` nur bei `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinander folgende Elemente eines Basis‑Feldes an. | `base_field` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mittels der Excel‑Index‑Formel ((Wert × Gesamtsumme) / (Zeilensumme × Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basis‑Feld an. | `base_field` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangt den Wert vom Kleinsten (1) zum Größten. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangt den Wert vom Größten (1) zum Kleinsten. | — |

{{% alert color="primary" %}}
`show_values_as(...)` schreibt die `PivotShowValuesSetting`‑Eigenschaften (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — die Methode und das Eigenschaftsobjekt stellen zwei Wege dar, denselben Zustand zu konfigurieren, analog zu den Basis‑Feld‑ und Basis‑Element‑Auswahlen im Show Values As‑Dialog von Excel.
{{% /alert %}}

## **Werte anzeigen als Prozentsatz der Gesamtsumme**
Rufen Sie die Methode `PivotField.show_values_as` mit `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` auf, um jede Zelle eines Datenfeldes, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert nur gegenüber der Gesamtsumme, daher wird kein Basis‑Feld oder Basis‑Element benötigt – die nachfolgenden Argumente (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sind Platzhalter, die das Format ignoriert, wie in der obigen Parametertabelle angegeben.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Abrufen und Konfigurieren von PivotField.show_values_setting**
Lesen Sie die aktuelle Konfiguration über `PivotField.show_values_setting`: Die schreibgeschützte Eigenschaft gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen vier Eigenschaften die aktive Show‑Values‑As‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.show_values_as` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen.
- `calculation_type` wählt die sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat` aus.
- `base_field_index` gibt den nullbasierten Index des Basisfeldes innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `base_item_position_type` bestimmt, wie das Basis‑Element relativ zum aktuellen Element positioniert wird und akzeptiert `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` oder `PivotItemPositionType.CUSTOM`.
- `base_item_index` gibt den nullbasierten Index des Basis‑Elements an und wird verwendet, wenn `base_item_position_type` auf `CUSTOM` steht.
Nachdem `show_values_as` aufgerufen wurde, rufen Sie erneut `PivotTable.calculate_data()` auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/python-net/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/python-net/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
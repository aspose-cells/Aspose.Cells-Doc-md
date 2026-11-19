---
title: Werte anzeigen als in Pivot‑Tabelle
linktitle: Werte anzeigen als in Pivot‑Tabelle
description: Zeigt Werte von Pivot‑Tabellen‑Datenfeldern als Prozentsatz des Gesamttotals, als Unterschied zu einem Basiselement, als laufende Summe, als Rangliste und mehr an, mit Aspose.Cells für Python via .NET.
keywords: Aspose.Cells, Pivot-Tabelle, Werte anzeigen als, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /de/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `SUM` oder `COUNT`. Die Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – beispielsweise ein Prozentsatz der Gesamtsumme, eine laufende Summe, ein Unterschied zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können.  
Typische Einsatzbereiche umfassen die Analyse des Anteils am Gesamtergebnis, inklusive Prozentsätze einer Zeile, Spalte oder Gesamtsumme; kumulative Berichte mit einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Unterschied oder prozentualem Unterschied zu einem Basiselement; sowie das Rangordnen von Werten vom Kleinsten zum Größten oder umgekehrt.  
In Aspose.Cells für Python via .NET wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.show_values_setting` liefert ein `PivotShowValuesSetting`‑Objekt, dessen beschreibbare Eigenschaften `show_values_as`, `base_field_index` und `base_item_index` das Verhalten konfigurieren; die Komfortmethode `PivotField.show_values_as(...)` wendet dieselben Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.data_fields` erhalten.

## **Aufzählungselemente der PivotShowValuesAsType‑Enumeration**
Das Datenfeld behält seine Aggregatfunktion, wie `SUM` oder `COUNT`, bei, während **Show Values As** nur die Anzeige des aggregierten Werts transformiert.  
Zusätzlich zum direkten Schreiben der Eigenschaften des `PivotShowValuesSetting` (siehe letzten Abschnitt) wendet eine Ein‑Aufruf‑Komfortmethode dieselbe Konfiguration an. Sie ist in zwei Formen verfügbar – eine, die das Basisfeld und Basiselement per Index adressiert, und eine, die Namen verwendet:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parameter | Bedeutung | Wann erforderlich |
| --- | --- | --- |
| `show_values_as_type` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `base_field` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basis‑Element gehört) oder – in der Namensform – der Name des Basisfelds. | Die acht basisrelativen Formate unten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); für alle anderen Formate `0` (oder `None` in der Namensform) übergeben. |
| `base_item` | Nullbasierter Index des Basis‑Elements, mit zwei Sentineln: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) wählt das vorherige Element und `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) das folgende. In der Namensform wird die Beschriftung des Basis‑Elements verwendet, und `None`, wenn das gewählte Format kein Basis‑Element benötigt. | Nur die drei Basis‑Element‑Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) verwenden das Basis‑Element; die fünf feldbezogenen Formate (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, beide Rang‑Formate) ignorieren es – `0` oder `None` übergeben. |

| Berechnungstyp | Verhalten | Basis‑Element‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `base_item` (ein Index oder eine Beschriftung, oder das vorherige/nächste Sentinel) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Wertes eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `base_item` (ein Index oder eine Beschriftung, oder das vorherige/nächste Sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Elements in einem Basis‑Feld an. | `base_field` + `base_item` (ein Index oder eine Beschriftung, oder das vorherige/nächste Sentinel) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basis‑Feldes an. | `base_field` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme (bei verschachtelten Zeilenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme (bei verschachtelten Spaltenfeldern) an. | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `base_field` (das übergeordnete Feld, dessen Summe als Referenz dient) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basis‑Feld an. | `base_field` (das Akkumulations‑Feld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert vom Kleinsten (1) zum Größten. | `base_field` (das Feld, dessen Elemente den Rangbereich definieren) |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert vom Größten (1) zum Kleinsten. | `base_field` (das Feld, dessen Elemente den Rangbereich definieren) |

{{% alert color="primary" %}}
`show_values_as(...)` schreibt die Eigenschaften des `PivotShowValuesSetting` (`show_values_as`, `base_field_index`, `base_item_index`) — die Methode und das Eigenschaftsobjekt sind zwei Wege, denselben Zustand zu konfigurieren, analog zu den Basis‑Feld‑ und Basis‑Element‑Auswahlen im Excel‑Dialog „Show Values As“.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamttotals anzeigen**
Rufen Sie die Methode `PivotField.show_values_as` mit `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` auf, um jede Zelle des Datenfeldes, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich gegenüber der Gesamtsumme, sodass weder Basisfeld noch Basiselement benötigt werden – die nachfolgenden Argumente (`0`, `0`) sind Platzhalter, die das Format ignoriert, wie die Parameter‑Tabelle oben erläutert.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Abrufen und Konfigurieren von PivotField.show_values_setting**
Lesen Sie die aktuelle Konfiguration über `PivotField.show_values_setting`: Die schreibgeschützte Eigenschaft liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen Eigenschaften die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.show_values_as` auf – sie schreibt alle Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen.  
Das `PivotShowValuesSetting`‑Objekt stellt den Zustand bereit, den `show_values_as` schreibt:
- `show_values_as` wählt die sekundäre Berechnung vom Typ `PivotShowValuesAsType` aus.
- `base_field_index` gibt den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisrelativen Formaten verwendet.
- `base_item_index` gibt das Basiselement an: einen nullbasierten Index eines bestimmten Pivot‑Elements oder eines der beiden Sentinels — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) für das vorherige Element, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) für das folgende. Er wird von den Basis‑Element‑Formaten verwendet.
- `base_field_name` und `base_item_caption` sind schreibgeschützte Ansichten, die den aufgelösten Namen des Basisfelds bzw. die Beschriftung des Basiselements melden; zum Beispiel liefert `base_item_caption` nach Auswahl des vorherigen Sentinels den Wert `(previous)`.
Nachdem Sie `show_values_as` aufgerufen haben, rufen Sie erneut `PivotTable.calculate_data()` auf, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/python-net/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/python-net/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
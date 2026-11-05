---
title: Bedingte Formatierung zu einer PivotTable hinzufügen
linktitle: Bedingte Formatierung zu einer PivotTable hinzufügen
description: Bedingte Formatierung zu einer PivotTable in Aspose.Cells for Python via .NET hinzufügen, eine Regel über den Datenbereich mit apply_to und einem PivotConditionFormatScopeType‑Bereich verankern oder das Ziel mit add_cell_area und pivot_areas festlegen und dann Regeln und Stile über format_conditions.add_condition anhängen.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, PivotTable, bedingte Formatierung, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /de/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Die auf der übergeordneten Seite und auf der verwandten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal gefärbt und behält sein Format bei, egal welche Werte vorliegen. Bedingte Formatierung ist das regelbasierte Gegenstück – jeden Betrag über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten bewerteten Elemente markieren – und die Hervorhebung folgt den Werten, sobald die PivotTable neu berechnet oder aktualisiert wird.
In Aspose.Cells befindet sich die bedingte Formatierung von PivotTable in der Sammlung `pivot_table.conditional_formats`. Jeder Eintrag ist ein `PivotConditionalFormat`, das zwei Fragen unabhängig voneinander beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)` definiert, was dem Bereichsauswahl‑Werkzeug der Excel‑Benutzeroberfläche entspricht, oder über `add_cell_area(cell_area: CellArea)` und die Sammlung `pivot_areas`, die den Bereich explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `format_conditions` mit `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` hinzugefügt, und jede Bedingung trägt ihr eigenes `style`.

{{% alert color="primary" %}}
Rufen Sie nicht `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` oder `format_conditions.add_area(cell_area: CellArea)` auf dem `format_conditions`‑Objekt eines `PivotConditionalFormat` auf. Diese beiden Überladungen stammen aus der normalen Arbeitsblatt‑Bedingte‑Formatierung‑API und funktionieren nicht für PivotTables – der Zellbereich wird niemals in einen Pivot‑Bereich umgewandelt, sodass die Anfrage stillschweigend ignoriert wird. Definieren Sie den Bereich immer direkt am `pivot_conditional_format` (`apply_to`, `add_cell_area` oder `pivot_areas`) und fügen Sie die Regel mit einer der `add_condition`‑Überladungen hinzu.
{{% /alert %}}

## **Eine Regel mit einem Bereich anwenden (wie in der Excel-Oberfläche)**
Die erste Methode positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der PivotTable wird durch ihre nullbasierten Arbeitsblatt‑Koordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.DATA` – alle Wertzellen, die die PivotTable erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.FIELD` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, beispielsweise ein Zeilen‑Feld‑Label; bei Übergabe einer Wertzelle wird eine Ausnahme ausgelöst.
- `PivotConditionFormatScopeType.SELECTION` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das nachstehende Beispiel erstellt eine PivotTable für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `PivotConditionFormatScopeType.DATA`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rotem Hintergrund hervor. Bei den Werten Apfel 220, Banane 330, Kirsche 200 und der Gesamtsumme 750 färbt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot-Tabelle mit ihrer oberen linken Ecke bei E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Regel - hebe Beträge hervor, die größer als 200 sind
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Wird dieselbe Regel am Zeilen‑Feld‑Label E4 (Zeile 3, Spalte 4) mit dem `PivotConditionFormatScopeType.FIELD`‑Bereich verankert, wird sie stattdessen auf F4:F6 angewendet – dieselbe Datenspalte ohne die Gesamtsummen‑Zeile – weil der Bereich nun das Feld `Fruit` und nicht den gesamten Wertebereich beschreibt. Der `PivotConditionFormatScopeType.SELECTION`‑Bereich, der an F4 verankert ist, löst nur F4 aus.

## **Region manuell definieren**
Die zweite Methode überspringt die Bereichsauswahl und benennt den Bereich explizit im `PivotConditionalFormat`.

### **Ein Arbeitsblatt-Rechteck mit add_cell_area**
`add_cell_area(cell_area: CellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblatt‑Koordinaten, und der Bereich ist exakt das übergebene Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Ziel das Rechteck F4:F6 (die Wertzellen ohne Gesamtsumme)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Regel - kursiv auf hellgelb für Beträge zwischen 150 und 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Ein semantischer Pivot-Bereich mit pivot_areas**
`pivot_areas` ist dasselbe semantische Regionen‑Modell, das die verwandte Seite für statische Stile verwendet. Erstellen Sie eine `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `select` oder `select_field` aus und fügen Sie ihn mit `pivot_areas.add_pivot_area(pivot_area)` hinzu. Ein semantischer Bereich bleibt an seinem Feld befestigt, sodass das bedingte Format dem Feld folgt, wenn die PivotTable aktualisiert wird und das Layout sich verschiebt. Die Überladung `pivot_areas.add(pivot_area)` lässt sich zwar noch kompilieren, ist jedoch als veraltet gekennzeichnet – bevorzugen Sie `add_pivot_area`.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Befestigen Sie die Regel an das Datenfeld 'Amount' als semantischen Bereich
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Regel - grauer Text für Beträge unter 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Wo die Regeln gespeichert werden und wie sie nach einem Neuladen erhalten bleiben**
Jeder Aufruf von `pivot_table.conditional_formats.add()` fügt der PivotTable ein `PivotConditionalFormat` hinzu. Die Bedingungen, deren Formeln und Stile werden mit der Arbeitsmappe gespeichert – beim erneuten Öffnen der Datei im nachstehenden Beispiel werden dieselbe Regel mit ihrem Typ, Operator und Formel unverändert angezeigt, und `get_cell_areas()` meldet dieselben Bereiche. Einträge, die nie eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe entfernt, genauso wie Excel ein bedingtes Format verwirft, das keine Regel besitzt.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Dies gibt aus:
# Bedingte Formate: 1
# Format 0: Zellwert GreaterThan formula1==200
#     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
```

## **Verwandte Artikel**
- [Stil auf PivotTable anwenden](/cells/de/python-net/apply-style-to-pivot-table/)
- [Teil einer PivotTable formatieren](/cells/de/python-net/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in PivotTable](/cells/de/python-net/top-10-show-or-filter-in-pivot-table/)
- [PivotTable nach Beschriftung oder Wert filtern](/cells/de/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
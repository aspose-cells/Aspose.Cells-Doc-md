---
title: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
linktitle: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
description: Bedingte Formatierung zu einer Pivot‑Tabelle in Aspose.Cells for Python via Java hinzufügen – eine Regel mit applyTo an den Datenbereich und einem PivotConditionFormatScopeType‑Bereich anheften oder das Ziel mit addCellArea und getPivotAreas definieren und anschließend Regeln und Stile über getFormatConditions().addCondition anhängen.
keywords: Aspose.Cells for Python via Java, Pivot‑Tabelle, bedingte Formatierung, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /de/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Die auf der übergeordneten Seite und auf der Schwesterseite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal eingefärbt und behält sein Format bei, egal welche Werte vorliegen. Bedingte Formatierung ist das regelbasierte Gegenstück – jeden Betrag über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten bewerteten Elemente kennzeichnen – und die Hervorhebung folgt den Werten, wann immer die Pivot‑Tabelle neu berechnet oder aktualisiert wird.  
In Aspose.Cells befindet sich die bedingte Formatierung von Pivot‑Tabellen in der Sammlung `PivotTable.getConditionalFormats()`. Jeder Eintrag ist ein `PivotConditionalFormat`, das zwei Fragen unabhängig voneinander beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, was dem Bereichsauswahl‑Werkzeug der Excel‑Benutzeroberfläche entspricht, oder über `PivotConditionalFormat.addCellArea(CellArea)` und die Sammlung `PivotConditionalFormat.getPivotAreas()`, die den Bereich explizit benennen.
- **Was testet die Regel?** Eine oder mehrere Bedingungen werden zu `PivotConditionalFormat.getFormatConditions()` mit `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` hinzugefügt, und jede Bedingung enthält ihr eigenes `Style`.

{{% alert color="primary" %}}
Rufen Sie nicht `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` oder `FormatConditionCollection.addArea(CellArea)` auf dem Objekt `PivotConditionalFormat.getFormatConditions()` eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen aus der regulären arbeitsblattbasierten bedingten Formatierungs‑API und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird niemals in einen Pivot‑Bereich konvertiert, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie den Bereich immer direkt auf dem `PivotConditionalFormat` selbst (`applyTo`, `addCellArea` oder `getPivotAreas()`) und fügen Sie die Regel mit einer der `addCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Eine Regel mit einem Bereich anwenden (wie in der Excel‑Benutzeroberfläche)**
Die erste Methode positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.DATA` – alle Wertzellen, die die Pivot‑Tabelle erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.FIELD` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, z. B. ein Zeilenfeld‑Label; die Übergabe einer Wertzelle löst eine Ausnahme aus.
- `PivotConditionFormatScopeType.SELECTION` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.  
Das untenstehende Beispiel erstellt eine Pivot‑Tabelle für den Obstverkauf, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `DATA`‑Bereich und hebt jeden Betrag über 200 in fettem Weiß auf Rot hervor. Bei den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 malt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

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
    Color,
    BackgroundType,
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot‑Tabelle mit ihrer oberen linken Ecke bei E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Verankern Sie das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Regel - Werte größer als 200 hervorheben
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Wird dieselbe Regel am Zeilenfeld‑Label E4 (Zeile 3, Spalte 4) mit dem `FIELD`‑Bereich verankert, löst sie sich stattdessen zu F4:F6 – dieselbe Datenspalte ohne die Gesamtsummenzeile – weil der Bereich nun das Feld `Fruit` statt des gesamten Wertebereichs beschreibt. Der `SELECTION`‑Bereich, der an F4 verankert ist, löst sich nur zu F4 auf.

## **Den Bereich manuell definieren**
Die zweite Methode verzichtet auf die Bereichsauswahl und benennt den Bereich explizit auf dem `PivotConditionalFormat`.

### **Ein Arbeitsblatt‑Rechteck mit addCellArea()**
`addCellArea(CellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich entspricht exakt dem übergebenen Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts darstellen.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Ziel das Rechteck F4:F6 (die Wertezellen ohne Gesamtsumme)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Regel – kursiv auf hellgelb für Beträge zwischen 150 und 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Ein semantischer Pivot‑Bereich mit getPivotAreas()**
Die Sammlung `getPivotAreas()` verwendet dasselbe semantische Regionen‑Modell, das die Schwesterseite für statische Stile nutzt. Erstellen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `PivotArea.select(...)` oder `PivotArea.selectField(...)` aus und fügen Sie es mit `getPivotAreas().addPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt an sein Feld gebunden, sodass das bedingte Format dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert und das Layout verändert wird. Die Überladung `getPivotAreas().add(PivotArea)` kompiliert noch, ist jedoch als veraltet markiert – bevorzugen Sie `addPivotArea`.

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
    Color,
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Regel dem Datenfeld 'Amount' als semantischer Bereich zuordnen
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Regel – grauer Text für Beträge unter 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Wo die Regeln gespeichert werden und wie sie ein Neuladen überstehen**
Jeder Aufruf von `PivotTable.getConditionalFormats().add()` fügt ein `PivotConditionalFormat` zur Pivot‑Tabelle hinzu. Die Bedingungen, ihre Formeln und ihre Stile werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der Datei im untenstehenden Beispiel zeigt dieselben beiden Regeln mit ihren Typen, Operatoren und Formeln unverändert, und `PivotConditionalFormat.getCellAreas()` gibt dieselben Bereiche zurück. Einträge, denen nie eine Bedingung zugewiesen wurde, werden beim Speichern der Arbeitsmappe verworfen, ähnlich wie Excel ein bedingtes Format ohne Regel entfernt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Dies gibt aus:
# Conditional formats: 1
# Format 0: Zellwert GrößerAls Formel1==200
#     rows 4-7, columns 6-6        (F4:F7, der aufgelöste Datenbereich)
jpype.shutdownJVM()
```

## **Related Articles**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/python-java/apply-style-to-pivot-table/)
- [Teil einer Pivot‑Tabelle formatieren](/cells/de/python-java/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Tabelle](/cells/de/python-java/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Tabellen nach Beschriftung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}
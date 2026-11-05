---
title: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
linktitle: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
description: Bedingte Formatierung zu einer Pivot‑Tabelle in Aspose.Cells for Java hinzufügen – verankern Sie eine Regel im Datenbereich mit applyTo und einem PivotConditionFormatScopeType‑Bereich oder definieren Sie das Ziel mit addCellArea und getPivotAreas und fügen Sie anschließend Regeln und Stile über FormatConditions.addCondition hinzu.
keywords: Aspose.Cells for Java, Pivot‑Tabelle, bedingte Formatierung, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /de/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Die auf der übergeordneten Seite und auf der verwandten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmalig gefärbt und behält sein Format, unabhängig von den Werten. Bedingte Formatierung ist das regelgesteuerte Gegenstück – heben Sie jeden Betrag über 200 hervor, schattieren Sie die mittleren fünfzig Prozent oder markieren Sie die am schlechtesten platzierten Elemente – und die Hervorhebung folgt den Werten, wann immer die Pivot‑Tabelle neu berechnet oder aktualisiert wird.  
In Aspose.Cells befindet sich die bedingte Formatierung einer Pivot‑Tabelle in der `PivotTable.getConditionalFormats()`‑Sammlung. Jeder Eintrag ist ein `PivotConditionalFormat`, das zwei Fragen unabhängig voneinander beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `applyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, was dem Bereichsauswahl‑Werkzeug der Excel‑Benutzeroberfläche entspricht, oder über `addCellArea(CellArea)` und die `getPivotAreas()`‑Sammlung, die den Bereich explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `getFormatConditions()` mit `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` hinzugefügt, und jede Bedingung enthält ihr eigenes `Style`.

{{% alert color="primary" %}}
Rufen Sie nicht `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` oder `FormatConditionCollection.addArea(CellArea)` auf der `getFormatConditions()`‑Sammlung eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen von der normalen worksheet‑bedingten Formatierungs‑API und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird nie in einen Pivot‑Bereich konvertiert, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie den Bereich stets direkt auf dem `PivotConditionalFormat` selbst (`applyTo`, `addCellArea` oder `getPivotAreas()`) und fügen Sie die Regel mit einer der `addCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Regel mit einem Bereich anwenden (wie in der Excel‑UI)**
Der erste Ansatz positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.DATA` – alle Wertzellen, die die Pivot‑Tabelle erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.FIELD` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, etwa ein Zeilenfeld‑Label; wird eine Wertzelle übergeben, wird eine Ausnahme ausgelöst.
- `PivotConditionFormatScopeType.SELECTION` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das nachstehende Beispiel erstellt eine Pivot‑Tabelle für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `DATA`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rot hervor. Bei den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 wird die Regel auf F4, F5 und F7 angewendet – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot‑Tabelle mit ihrer oberen linken Ecke bei E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Regel – hebe Beträge hervor, die größer als 200 sind
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Verankert man dieselbe Regel im Zeilen‑Feld‑Label E4 (Zeile 3, Spalte 4) mit dem `FIELD`‑Bereich, löst sie sich stattdessen auf F4:F6 – dieselbe Datenspalte ohne die Gesamtsummen‑Zeile – weil der Bereich nun das `Fruit`‑Feld und nicht den gesamten Wertebereich beschreibt. Der `SELECTION`‑Bereich, der bei F4 verankert ist, löst sich ausschließlich auf F4 auf.

## **Region manuell definieren**
Der zweite Ansatz überspringt die Bereichsauswahl und benennt den Bereich explizit auf dem `PivotConditionalFormat`.

### **Ein Arbeitsblatt‑Rechteck mit addCellArea**
`addCellArea(CellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich entspricht exakt dem übergebenen Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekannter fester Rechteck des aktuellen Pivot‑Layouts bilden.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Zielbereich ist das Rechteck F4:F6 (die Wertzellen ohne Gesamtsumme)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regel – kursiv auf hellgelb für Beträge zwischen 150 und 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ein semantischer Pivot‑Bereich mit getPivotAreas**
`getPivotAreas()` liefert dasselbe semantische Bereichs‑Modell zurück, das die verwandte Seite für statische Stile verwendet. Erzeugen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `select` oder `selectField` aus und fügen Sie ihn mit `getPivotAreas().addPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt an seinem Feld befestigt, sodass das bedingte Format dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert wird und das Layout verschoben wird. Die Überladung `getPivotAreas().add(PivotArea)` lässt sich zwar noch kompilieren, ist jedoch als veraltet gekennzeichnet – bevorzugen Sie `addPivotArea`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Hängen Sie die Regel an das Datenfeld Amount als semantischen Bereich an
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel - grauer Text für Beträge unter 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder Aufruf von `getConditionalFormats().add()` fügt ein `PivotConditionalFormat` zur Pivot‑Tabelle hinzu. Die Bedingungen, deren Formeln und Stile werden mit der Arbeitsmappe gespeichert – beim erneuten Öffnen der Datei im nachstehenden Beispiel werden dieselben beiden Regeln mit ihren Typen, Operatoren und Formeln intakt angezeigt, und `getCellAreas()` liefert dieselben Bereiche. Einträge, die nie eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe verworfen, ähnlich wie Excel ein bedingtes Format ohne Regel entfernt.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Dies gibt aus:
// Bedingte Formate: 1
// Format 0: CellValue GreaterThan formula1==200
//     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
```

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [Teil einer Pivot‑Tabelle formatieren](/cells/de/java/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Tabelle](/cells/de/java/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Tabellen nach Label oder Wert filtern](/cells/de/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}
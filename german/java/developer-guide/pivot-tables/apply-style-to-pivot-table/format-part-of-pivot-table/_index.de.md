---
title: Teil einer Pivot‑Tabelle formatieren
linktitle: Teil einer Pivot‑Tabelle formatieren
description: Teil einer Pivot‑Tabelle in Aspose.Cells for Java formatieren, indem Stile auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke über PivotTable.format angewendet werden; Formate werden in PivotTable.getPivotFormats gespeichert und bleiben erhalten, wenn die Pivot‑Tabelle neu berechnet wird.
keywords: Aspose.Cells for Java, Pivot‑Tabelle, Formatierung, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /de/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
`PivotTable.formatAll` wendet einen einzigen Stil auf die gesamte Pivot‑Tabelle an und wird auf der übergeordneten Seite behandelt. Sie unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.  
In der Praxis muss in der Regel nur ein Teil einer Pivot‑Tabelle hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die Wertzellen, die von einem Feld erzeugt werden, die Gesamtsummenzeile oder ein beliebiges Rechteck, z. B. die ersten beiden Elementzeilen.  
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer Pivot‑Tabelle ist nicht gleichwertig. Excel speichert die Formatierung von Pivot‑Tabellen als semantische `PivotArea`‑Bereiche und nicht als gewöhnliche Zellformat‑Datensätze. Ein Pivot‑Area‑Format bleibt an einem Bereich wie den Beschriftungen eines Feldes oder den Datenwerten befestigt und wird neu aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebenes Format hingegen gehört zu dieser Zellposition und wird vom Pivot‑Modell nicht verfolgt.  
Aspose.Cells stellt die komplette Überladungsfamilie von `PivotTable.format` bereit, sodass beide Arten von Formatierungen verfügbar sind:
- `format(PivotArea, Style)` verankert einen Stil in einem semantischen Bereich, der mit `PivotArea.select` oder `PivotArea.selectField` erstellt wird.
- `format(CellArea, Style)` verankert einen Stil in einem Arbeitsblattrechteck innerhalb der Pivot‑Tabelle.
- `format(int row, int column, Style)` zielt auf eine einzelne Zelle.
- `formatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Pivot‑Area formatieren**
Der semantische Bereichs‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstellen Sie ein `PivotArea` mit `new PivotArea(pivotTable)`. Das Objekt beschreibt einen semantischen Bereich, der zu dieser spezifischen Pivot‑Tabelle gehört.
1. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer gegebenen Achse mit `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` aus.  
   - `PivotTableSelectionType.DATA_AND_LABEL` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.  
   - `PivotTableSelectionType.LABEL_ONLY` wählt nur die Beschriftungen des Feldes aus.  
   - `PivotTableSelectionType.DATA_ONLY` wählt nur die Datenzellen des Feldes aus.
1. Wählen Sie ein Feld anhand seines Namens mit `PivotArea.selectField(PivotFieldType axisType, String fieldName)` aus. Wenn ein Zeilenfeld nach Name ausgewählt wird, löst sich der Bereich zu den Wertzellen, die von den Elementen dieses Feldes erzeugt werden.
1. Erstellen Sie ein `Style` mit `Workbook.createStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und einfarbiges Hintergrundmuster und übergeben Sie den Stil an `PivotTable.format(area, style)`.
1. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.getPivotFormats()` hinzu.
1. Feldverankerte Formate werden beim Berechnen der Pivot‑Daten angewendet. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.calculateData()` auf, damit die Stile sichtbar werden.  
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.select` und `PivotTableSelectionType.LABEL_ONLY`, formatiert die durch dasselbe Zeilenfeld erzeugten Wertzellen mit `PivotArea.selectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Zellbereich einer Pivot‑Tabelle formatieren**
Verwenden Sie `PivotTable.format(CellArea, Style)`, wenn der interessierende Bereich ein einfaches Arbeitsblattrechteck und kein semantischer Pivot‑Bereich ist.  
Ein `CellArea` wird durch die Eigenschaften `getStartRow()`, `getStartColumn()`, `getEndRow()` und `getEndColumn()` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur Endposition (einschließlich) umfasst.  
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `calculateData()` ist nicht erforderlich, damit der Stil erscheint.  
Ein `CellArea`‑Rechteck kann sowohl Beschriftungs‑ als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.  
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Wie Pivot‑Bereiche und Zellbereiche zugeordnet werden**
Excel speichert die Formatierung von Pivot‑Tabellen als `pivotArea`‑Datensätze und nicht als gewöhnliche Arbeitsblatt‑Zellstil‑Datensätze. Dasselbe Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanfrage beim Aufzeichnen in Pivot‑Bereiche übersetzt wird.  
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Bereichen ist in beide Richtungen Many‑to‑Many.  
- Ein `CellArea` kann mehrere Pivot‑Bereiche erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Datenregeln zerlegt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig behandelt.  
- Ein Pivot‑Bereich kann sich in mehrere disjunkte `CellArea`‑Instanzen auflösen. Ein semantischer Bereich wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb gibt `PivotArea.getCellAreas()` eine Sammlung zurück und nicht ein einzelnes Rechteck.  
Jede über `PivotTable.format` ausgeführte Formatierungsoperation wird in `PivotTable.getPivotFormats()` protokolliert. Jeder `PivotTableFormat`‑Eintrag gibt das zugehörige `PivotArea` und den darauf angewendeten `Style` wieder. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.  
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `getOnlyLabel()` und `getOnlyData()` bereit. Das untenstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, prüft `PivotTable.getPivotFormats()` und gibt die `CellArea`‑Koordinaten aus, zu denen jeder gespeicherte Pivot‑Bereich aufgelöst wird.

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
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Da die Formate als Pivot‑Bereiche und nicht als gewöhnliche Zellstile gespeichert werden, überstehen sie Neuberechnungen und Aktualisierungen. Wenn die Pivot‑Tabelle mit `PivotTable.refreshData` aktualisiert, mit `calculateData` neu berechnet oder gespeichert und erneut geladen wird, löst sich jeder gespeicherte Pivot‑Bereich erneut auf die aktuelle Position seines Bereichs auf und sein Stil wird erneut angewendet.
{{% /alert %}}

Verwenden Sie ein `PivotArea`, das mit `select` oder `selectField` aufgebaut wurde, wenn eine Hervorhebung über Aktualisierungen hinweg an ein Feld oder einen semantischen Bereich gebunden bleiben muss, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Layout der Pivot‑Tabelle ausreicht. Die Einzelzellen‑Überladung `format(int row, int column, Style)` zielt auf eine einzelne Zelle. Verwenden Sie `formatAll`, das auf der übergeordneten Seite behandelt wird, wenn die gesamte Pivot‑Tabelle auf einmal neu gestaltet werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [Pivot‑Tabellen‑Zeilen‑ und Spaltenfelder hinzufügen](/cells/de/java/pivot-table-add-row-and-column-fields/)
- [Wertfelder in Pivot‑Tabelle verwalten](/cells/de/java/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}
---
title: Teil einer Pivot-Tabelle formatieren
linktitle: Teil einer Pivot-Tabelle formatieren
description: Formatiere einen Teil einer Pivot‑Tabelle in Aspose.Cells for Node.js via Java, indem Stile auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke über PivotTable.format angewendet werden; die Formate werden in PivotTable.getPivotFormats() gespeichert und bleiben erhalten, wenn die Pivot‑Tabelle aktualisiert wird.
keywords: Aspose.Cells for Node.js via Java, Pivot‑Tabelle, Format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /de/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.formatAll` wendet einen einzelnen Stil auf die gesamte Pivot‑Tabelle an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.  
In der Praxis muss meist nur ein Teil einer Pivot‑Tabelle hervorgehoben werden. Häufige Ziele sind die Beschriftungen eines Zeilenfeldes, die Wertzellen, die von einem Feld erzeugt werden, die Gesamtsummen‑Zeile oder ein beliebiges Rechteck, z. B. die ersten beiden Element‑Zeilen.  
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer Pivot‑Tabelle ist nicht gleichbedeutend. Excel speichert Pivot‑Tabellen‑Formatierungen als semantische `PivotArea`‑Regionen statt als gewöhnliche Zell‑Style‑Einträge. Ein `PivotArea`‑Format bleibt an einer Region wie den Beschriftungen oder Datenwerten eines Feldes befestigt und wird neu aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil hingegen ist an diese Zellenposition gebunden und wird vom Pivot‑Modell nicht verfolgt.  
Aspose.Cells stellt die vollständige Überladungsfamilie von `PivotTable.format` bereit, sodass beide Arten von Formatierung verfügbar sind:
- `format(PivotArea, Style)` verankert einen Stil in einer semantischen Region, die mit `PivotArea.select` oder `PivotArea.selectField` erstellt wurde.
- `format(CellArea, Style)` verankert einen Stil in einem Arbeitsblatt‑Rechteck innerhalb der Pivot‑Tabelle.
- `format(int row, int column, Style)` adressiert eine einzelne Zelle.
- `formatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Eine Pivot‑Area formatieren**
Der semantische Area‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstelle ein `PivotArea` mit `new PivotArea(pivotTable)`. Das Objekt beschreibt eine semantische Region, die zu dieser speziellen Pivot‑Tabelle gehört.
2. Wähle ein Feld über seine nullbasierte Position auf einer bestimmten Achse mit `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` aus.  
   - `PivotTableSelectionType.DATA_AND_LABEL` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.  
   - `PivotTableSelectionType.LABEL_ONLY` wählt nur die Beschriftungen des Feldes aus.  
   - `PivotTableSelectionType.DATA_ONLY` wählt nur die Datenzellen des Feldes aus.
3. Wähle ein Feld über den Namen mit `PivotArea.selectField(PivotFieldType axisType, string fieldName)` aus. Wenn ein Zeilenfeld nach Namen ausgewählt wird, löst die Region die Wertzellen auf, die durch die Elemente dieses Feldes erzeugt werden.
4. Erstelle ein `Style` mit `Workbook.createStyle()`, konfiguriere dessen Schriftart, Vordergrundfarbe und ein durchgängiges Hintergrundmuster und übergebe den Stil an `PivotTable.format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.getPivotFormats()` hinzu.
6. Feldverankerte Formate werden beim Berechnen der Pivot‑Daten aufgetragen. Daher sollte `PivotTable.calculateData()` nach dem Anwenden der Formate aufgerufen werden, damit die Stile sichtbar werden.  
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Fruchtverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.select` und `PivotTableSelectionType.LABEL_ONLY`, formatiert die durch dasselbe Zeilenfeld erzeugten Wertzellen mit `PivotArea.selectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Ein Cell‑Area der Pivot‑Tabelle formatieren**
Verwende `PivotTable.format(CellArea, Style)`, wenn der interessierende Bereich ein schlichtes Arbeitsblatt‑Rechteck und keine semantische Pivot‑Region ist.  
`CellArea` wird durch die öffentlichen Felder `StartRow`, `StartColumn`, `EndRow` und `EndColumn` beschrieben. Die Werte sind nullbasierte Arbeitsblatt‑Koordinaten, und die Endkoordinaten geben die letzte Zeile bzw. Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur Endposition einschließt.  
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `calculateData()` ist nicht erforderlich, damit der Stil erscheint.  
Ein `CellArea`‑Rechteck kann sowohl Beschriftungs‑ als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.  
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Wie Pivot‑Areas und Cell‑Areas abgebildet werden**
Excel speichert Pivot‑Tabellen‑Formatierungen als `pivotArea`‑Datensätze statt als gewöhnliche Arbeitsblatt‑Zell‑Style‑Einträge. Das gleiche Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanfrage beim Aufzeichnen in Pivot‑Areas übersetzt wird.  
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Areas ist in beide Richtungen viele‑zu‑viele.  
- Ein `CellArea` kann mehrere Pivot‑Areas erzeugen. Erstreckt sich das Rechteck über sowohl Beschriftungs‑ als auch Wertzellen, wird es in separate Label‑ und Daten‑Regeln aufgeteilt, da das Pivot‑Modell Label‑ und Datenformatierung unabhängig voneinander behandelt.  
- Eine Pivot‑Area kann sich in mehrere getrennte `CellArea`‑Instanzen auflösen. Eine semantische Region wie eine Gesamtsummen‑Zeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke umfassen. Deshalb gibt `PivotArea.getCellAreas()` eine Sammlung zurück statt eines einzelnen Rechtecks.  
Jeder über `PivotTable.format` durchgeführte Formatierungsvorgang wird in `PivotTable.getPivotFormats()` protokolliert. Jeder `PivotTableFormat`‑Eintrag stellt das zugehörige `PivotArea` und den darauf angewendeten `Style` dar. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.  
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `getOnlyLabel()` und `getOnlyData()` bereit. Das nachstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte umfasst, prüft `PivotTable.getPivotFormats()` und gibt die `CellArea`‑Koordinaten aus, zu denen jede gespeicherte Pivot‑Area aufgelöst wird.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
        );
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
Da die Formate als Pivot‑Areas und nicht als gewöhnliche Zell‑Styles gespeichert werden, überleben sie Neuberechnungen und Aktualisierungen. Wird die Pivot‑Tabelle mit `PivotTable.refreshData()` aktualisiert, mit `calculateData()` neu berechnet oder gespeichert und erneut geladen, löst jede gespeicherte Pivot‑Area ihre aktuelle Position erneut auf und ihr Stil wird wieder angewendet.
{{% /alert %}}

Verwende ein mit `select` oder `selectField` gebautes `PivotArea`, wenn eine Hervorhebung über mehrere Aktualisierungen hinweg an einem Feld oder einer semantischen Region befestigt bleiben muss, und nutze ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Layout der Pivot‑Tabelle ausreicht. Die Einzelzellen‑Überladung `format(int row, int column, Style)` adressiert eine einzelne Zelle. Verwende `formatAll`, das auf der übergeordneten Seite behandelt wird, wenn die gesamte Pivot‑Tabelle auf einmal neu gestylt werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Hinzufügen von Zeilen‑ und Spaltenfeldern zur Pivot‑Tabelle](/cells/de/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Verwalten von Werte‑Feldern in der Pivot‑Tabelle](/cells/de/nodejs-java/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
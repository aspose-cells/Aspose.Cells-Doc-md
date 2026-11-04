---
title: Teil einer Pivot-Tabelle formatieren
linktitle: Teil einer Pivot-Tabelle formatieren
description: Teil einer Pivot-Tabelle in Aspose.Cells for Node.js via C++ formatieren, indem Stile auf semantische PivotArea‑Bereiche oder CellArea‑Rechtecke über PivotTable.format angewendet werden, wobei Formate in PivotTable.getPivotFormats() gespeichert und beim Aktualisieren der Pivot‑Tabelle beibehalten werden.
keywords: Aspose.Cells, Node.js via C++, Pivot-Tabelle, Format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /de/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
`PivotTable.formatAll` wendet einen einzigen Stil auf die gesamte Pivot‑Tabelle an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.
In der Praxis muss normalerweise nur ein Teil einer Pivot‑Tabelle hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die von einem Feld erzeugten Wertzellen, die Gesamtsummenzeile oder ein beliebiges Rechteck, z. B. die ersten beiden Elementzeilen.
Das Anwenden eines Stils direkt auf die Arbeitsblattzellen einer Pivot‑Tabelle ist nicht gleichwertig. Excel speichert die Formatierung von Pivot‑Tabellen als semantische `PivotArea`‑Bereiche statt als gewöhnliche Zellstil‑Einträge. Ein Pivot‑Area‑Format bleibt an einem Bereich wie den Beschriftungen eines Feldes oder dessen Datenwerten befestigt und wird neu aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil gehört hingegen zu dieser Zellposition und wird vom Pivot‑Modell nicht nachverfolgt.
Aspose.Cells stellt die vollständige Überladungsfamilie von `PivotTable.format` bereit, sodass beide Arten der Formatierung verfügbar sind:
- `format(PivotArea, Style)` verankert einen Stil in einem semantischen Bereich, der mit `PivotArea.select` oder `PivotArea.selectField` erstellt wird.
- `format(CellArea, Style)` verankert einen Stil in einem Arbeitsblattrechteck innerhalb der Pivot‑Tabelle.
- `format(number row, number column, Style)` richtet sich an eine einzelne Zelle.
- `formatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Eine Pivot‑Area formatieren**
Der semantische Area‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstellen Sie ein `PivotArea` mit `new PivotArea(pivotTable)`. Das Objekt beschreibt einen semantischen Bereich, der zu dieser spezifischen Pivot‑Tabelle gehört.
2. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer angegebenen Achse mit `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LabelOnly` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DataOnly` wählt nur die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld nach Namen mit `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Wenn ein Zeilenfeld nach Namen ausgewählt wird, löst sich der Bereich zu den Wertzellen auf, die von den Elementen dieses Feldes erzeugt werden.
4. Erstellen Sie ein `Style` mit `workbook.createStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und einfarbiges Hintergrundmuster und übergeben Sie den Stil an `pivotTable.format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `pivotTable.getPivotFormats()` hinzu.
6. Feldverankerte Formate werden gezeichnet, wenn die Pivot‑Daten berechnet werden. Rufen Sie daher nach dem Anwenden der Formate `pivotTable.calculateData()` auf, damit die Stile sichtbar werden.
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.select` und `PivotTableSelectionType.LabelOnly`, formatiert die von demselben Zeilenfeld erzeugten Wertzellen mit `PivotArea.selectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Einen Cell‑Area der Pivot‑Tabelle formatieren**
Verwenden Sie `PivotTable.format(CellArea, Style)`, wenn der gewünschte Bereich ein einfaches Arbeitsblattrechteck und kein semantischer Pivot‑Bereich ist.
`CellArea` wird durch die Eigenschaften `startRow`, `startColumn`, `endRow` und `endColumn` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile bzw. Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur Endposition (einschließlich) umfasst.
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `pivotTable.calculateData()` ist nicht erforderlich, damit der Stil erscheint.
Ein `CellArea`‑Rechteck kann sowohl Beschriftungszellen als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Wie Pivot‑Areas und Cell‑Areas abgebildet werden**
Excel speichert die Formatierung von Pivot‑Tabellen als `pivotArea`‑Datensätze anstelle gewöhnlicher Arbeitsblatt‑Zellstil‑Datensätze. Dasselbe Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanforderung bei ihrer Aufzeichnung in Pivot‑Areas übersetzt wird.
Die Beziehung zwischen dem vom Benutzer angegebenen `CellArea` und den intern gespeicherten Pivot‑Areas ist in beiden Richtungen viele‑zu‑viele.
- Ein `CellArea` kann mehrere Pivot‑Areas erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Datenregeln zerlegt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig behandelt.
- Ein Pivot‑Area kann sich in mehrere nicht zusammenhängende `CellArea`‑Instanzen auflösen. Ein semantischer Bereich wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb liefert `PivotArea.getCellAreas()` eine Sammlung statt eines einzelnen Rechtecks.
Jeder über `pivotTable.format()` ausgeführte Formatierungsvorgang wird in `pivotTable.getPivotFormats()` protokolliert. Jeder `PivotTableFormat`‑Eintrag stellt das zugehörige `PivotArea` und den darauf angewendeten `Style` dar. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das verschiedene semantische Bereiche enthält, mehrere Einträge hinzufügen kann.
Um die gespeicherten Bereiche zu unterscheiden, stellt jedes `PivotArea` die Flags `getOnlyLabel()` und `getOnlyData()` bereit. Das untenstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `pivotTable.getPivotFormats()` und gibt die `CellArea`‑Koordinaten aus, zu denen jedes gespeicherte Pivot‑Area aufgelöst wird.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
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
Da die Formate als Pivot‑Areas und nicht als gewöhnliche Zellstile gespeichert werden, überleben sie Neuberechnungen und Aktualisierungen. Wenn die Pivot‑Tabelle mit `pivotTable.refreshData()` aktualisiert, mit `pivotTable.calculateData()` neu berechnet oder gespeichert und erneut geladen wird, löst sich jede gespeicherte Pivot‑Area erneut auf die aktuelle Position ihres Bereichs auf und ihr Stil wird erneut angewendet.
{{% /alert %}}

Verwenden Sie ein `PivotArea`, das mit `select` oder `selectField` erstellt wurde, wenn eine Hervorhebung über Aktualisierungen hinweg an einem Feld oder einem semantischen Bereich haften bleiben muss, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreicht. Die Einzelzellen‑Überladung `format(number row, number column, Style)` richtet sich an eine einzelne Zelle. Verwenden Sie `formatAll`, das auf der übergeordneten Seite behandelt wird, wenn die gesamte Pivot‑Tabelle auf einmal neu gestaltet werden soll.

## **Verwandte Artikel**
- [Format auf Pivot‑Tabelle anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)
- [Hinzufügen von Zeilen‑ und Spaltenfeldern zur Pivot‑Tabelle](/cells/de/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Verwalten von Wertefeldern in der Pivot‑Tabelle](/cells/de/nodejs-cpp/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
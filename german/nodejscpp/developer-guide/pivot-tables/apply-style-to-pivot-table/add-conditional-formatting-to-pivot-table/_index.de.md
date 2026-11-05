---
title: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
linktitle: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
description: Fügen Sie einer Pivot‑Tabelle in Aspose.Cells for Node.js via C++ eine bedingte Formatierung hinzu – verankern Sie eine Regel im Datenbereich mit `applyTo` und einem `PivotConditionFormatScopeType`‑Bereich oder definieren Sie das Ziel mit `addCellArea` und `pivotAreas` und hängen Sie anschließend Regeln und Formate über `formatConditions.addCondition` an.
keywords: Aspose.Cells for Node.js via C++, Pivot‑Tabelle, bedingte Formatierung, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /de/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Die auf der übergeordneten Seite und der Schwesterseite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal eingefärbt und behält sein Format bei, unabhängig von den Werten. Bedingte Formatierung ist das regelgesteuerte Gegenstück – heben Sie jeden Betrag über 200 hervor, schattieren Sie die mittleren fünfzig Prozent oder markieren Sie die niedrigst platzierten Einträge – und die Hervorhebung folgt den Werten, wann immer die Pivot‑Tabelle neu berechnet oder aktualisiert wird.  
In Aspose.Cells befindet sich die bedingte Formatierung von Pivot‑Tabellen in der Sammlung `pivotTable.getConditionalFormats()`. Jeder Eintrag ist ein `PivotConditionalFormat`, der unabhängig zwei Fragen beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `applyTo(row, column, scope)` definiert, was dem Bereichsauswahlwerkzeug der Excel‑Benutzeroberfläche entspricht, oder über `addCellArea(cellArea)` und die Sammlung `pivotConditionalFormat.getPivotAreas()`, die den Bereich explizit benennt.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `formatConditions` hinzugefügt, die über `pivotConditionalFormat.getFormatConditions()` abgerufen werden, mittels `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, und jede Bedingung trägt ihr eigenes Format über `getStyle()`.

{{% alert color="primary" %}}
Rufen Sie nicht `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` oder `formatConditions.addArea(cellArea)` auf dem `formatConditions`‑Objekt eines Pivot‑bedingten Formats auf. Diese beiden Überladungen werden von der normalen Arbeitsblatt‑bedingten‑Formatierungs‑API geerbt und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird nie in einen Pivot‑Bereich umgewandelt, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie den Bereich immer am `pivotConditionalFormat`‑Objekt selbst (`applyTo`, `addCellArea` oder `getPivotAreas()`) und fügen Sie die Regel mit einer der `addCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Regel mit einem Bereich anwenden (wie in der Excel-Oberfläche)**
Der erste Ansatz positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird über ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich teilt Aspose.Cells mit, wie weit die Regel von dieser Zelle ausreichen soll:
- `PivotConditionFormatScopeType.DATA` – alle Wertezellen, die die Pivot‑Tabelle erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.FIELD` – die Wertezellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, z. B. eine Zeilen‑Feld‑Bezeichnung; wird eine Wertzelle übergeben, wird eine Ausnahme ausgelöst.
- `PivotConditionFormatScopeType.SELECTION` – nur die Wertezellen an der Kreuzung, die die Zelle auswählt, typischerweise eine einzelne Wertezelle.
Das nachfolgende Beispiel erstellt eine Pivot‑Tabelle für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `DATA`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rot hervor. Mit den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 malt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

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
// Pivot-Tabelle mit ihrer oberen linken Ecke bei E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Regel - Werte größer als 200 hervorheben
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Die gleiche Regel an der Zeilen‑Feld‑Bezeichnung E4 (Zeile 3, Spalte 4) mit dem `FIELD`‑Bereich verankert, löst stattdessen F4:F6 – dieselbe Datenspalte ohne die Gesamtsummen‑Zeile – weil der Bereich nun das Feld `Fruit` beschreibt und nicht den gesamten Werte‑Bereich. Der `SELECTION`‑Bereich, der an F4 verankert ist, löst nur F4 auf.

## **Region manuell definieren**

### **Ein Arbeitsblattrechteck mit addCellArea**
`addCellArea(cellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich entspricht exakt dem übergebenen Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

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
// Ziel das Rechteck F4:F6 (die Wertzellen ohne Gesamtsumme)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Regel - kursiv auf hellgelb für Beträge zwischen 150 und 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ein semantischer Pivot‑Bereich mit getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` ist dasselbe semantische‑Bereich‑Modell, das die Schwesterseite für statische Stile verwendet. Erzeugen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `select` bzw. `selectField` aus und fügen Sie es mit `pivotAreas.addPivotArea(pivotArea)` hinzu. Ein semantischer Bereich bleibt an sein Feld gebunden, sodass das bedingte Format dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert wird und das Layout sich ändert. Die Überladung `pivotAreas.add(pivotArea)` lässt sich zwar noch kompilieren, ist aber als veraltet markiert – bevorzugen Sie `addPivotArea`.

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
// Regel an das Datenfeld Amount als semantischen Bereich anhängen
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel – grauer Text für Beträge unter 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder Aufruf von `conditionalFormats.add()` hängt ein `PivotConditionalFormat` an die Pivot‑Tabelle an. Die Bedingungen, deren Formeln und Formate werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der Datei im nachstehenden Beispiel zeigt dieselbe Regel mit ihrem Typ, Operator und Formel unverändert, und `getCellAreas()` gibt dieselben Bereiche zurück. Einträge, die niemals eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe verworfen, genauso wie Excel ein bedingtes Format entfernt, das keine Regel enthält.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Dies wird ausgegeben:
// Bedingte Formatierungen: 1
// Format 0: Zellwert GrößerAls Formel1==200
//     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
```

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)
- [Teil einer Pivot‑Tabelle formatieren](/cells/de/nodejs-cpp/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Tabelle](/cells/de/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Tabellen nach Beschriftung oder Wert filtern](/cells/de/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
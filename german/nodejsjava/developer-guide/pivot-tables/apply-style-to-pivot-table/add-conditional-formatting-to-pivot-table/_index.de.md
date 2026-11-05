---
title: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
linktitle: Bedingte Formatierung zu einer Pivot‑Tabelle hinzufügen
description: Bedingte Formatierung zu einer Pivot‑Tabelle in Aspose.Cells for Node.js via Java hinzufügen – eine Regel mit applyTo und einem PivotConditionFormatScopeType‑Bereich an den Datenbereich anheften oder das Ziel mit addCellArea und getPivotAreas definieren und dann Regeln und Stile über getFormatConditions().addCondition anhängen.
keywords: Aspose.Cells, Pivot‑Tabelle, bedingte Formatierung, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /de/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Die auf der übergeordneten Seite und auf der verwandten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal eingefärbt und behält sein Format, egal welche Werte vorliegen. Bedingte Formatierung ist das regelbasierte Gegenstück – jeden Betrag über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten bewerteten Elemente markieren – und die Hervorhebung folgt den Werten, sobald die Pivot‑Tabelle neu berechnet oder aktualisiert wird.  
In Aspose.Cells for Node.js via Java befindet sich die bedingte Formatierung einer Pivot‑Tabelle in der `pivotTable.getConditionalFormats()`‑Sammlung. Jeder Eintrag ist ein `PivotConditionalFormat`, das zwei Fragen unabhängig voneinander beantwortet:
- **Wo wird die Regel angewendet?** Das Zielgebiet wird entweder über `applyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, was dem Bereichsauswahl‑Steuerlement der Excel‑Benutzeroberfläche entspricht, oder über `addCellArea(CellArea)` und die `getPivotAreas()`‑Sammlung, die das Gebiet explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `getFormatConditions()` mit `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` hinzugefügt, und jede Bedingung trägt ihr eigenes `getStyle()`.

{{% alert color="primary" %}}
Rufen Sie **nicht** `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` oder `FormatConditionCollection.addArea(CellArea)` auf dem `getFormatConditions()`‑Objekt eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen aus der normalen Arbeitsblatt‑Bedingten‑Formatierungs‑API und funktionieren für Pivot‑Tabellen nicht – der Zellenbereich wird niemals in einen Pivot‑Bereich konvertiert, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie das Gebiet immer am `PivotConditionalFormat` selbst (`applyTo`, `addCellArea` oder `getPivotAreas()`) und fügen Sie die Regel mit einer der `addCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Regel mit einem Bereich anwenden (wie in der Excel-Oberfläche)**
Die erste Methode positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich sagt Aspose.Cells, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.DATA` – alle Wertzellen, die die Pivot‑Tabelle erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.FIELD` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feld‑Zelle sein, z. B. ein Zeilen‑Feld‑Label; wird eine Wertzelle übergeben, wird eine Ausnahme ausgelöst.
- `PivotConditionFormatScopeType.SELECTION` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das nachfolgende Beispiel erstellt eine Pivot‑Tabelle für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format an Zelle F4 (Zeile 3, Spalte 5) mit dem `DATA`‑Bereich und hebt jeden Betrag über 200 fett, weiß auf rotem Hintergrund hervor. Bei den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 wird die Regel F4, F5 und F7 färben – das aufgelöste Gebiet ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

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
// Pivot-Tabelle mit ihrer oberen linken Ecke bei E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) im Datenbereich
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Regel - markiere Beträge größer als 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Wird dieselbe Regel am Zeilen‑Feld‑Label E4 (Zeile 3, Spalte 4) mit dem `FIELD`‑Bereich verankert, löst sie F4:F6 aus – dieselbe Datenspalte ohne die Zeile der Gesamtsumme – weil der Bereich nun das Feld `Fruit` beschreibt statt des gesamten Werte‑Gebiets. Der `SELECTION`‑Bereich, verankert bei F4, löst nur F4 aus.

## **Region manuell definieren**
Die zweite Methode überspringt die Bereichsauswahl und benennt das Gebiet explizit am `PivotConditionalFormat`.

### **Ein Arbeitsblattrechteck mit addCellArea**
`addCellArea(CellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und das Gebiet ist exakt das übergebene Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie diese Methode, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

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
// Zielrechteck F4:F6 (die Wertzellen ohne die Gesamtsumme)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regel - kursiv in hellgelb für Beträge zwischen 150 und 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ein semantischer Pivot‑Bereich mit PivotAreas**
`getPivotAreas()` ist dasselbe semantische‑Bereich‑Modell, das die verwandte Seite für statische Stile nutzt. Erzeugen Sie ein `PivotArea`, wählen Sie ein Feld oder Gebiet mit `select` oder `selectField` und fügen Sie es mit `getPivotAreas().addPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt seinem Feld zugeordnet, sodass das bedingte Format dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert und das Layout verschoben wird. Die Überladung `getPivotAreas().add(PivotArea)` kompiliert weiterhin, ist jedoch als veraltet markiert – bevorzugen Sie `addPivotArea`.

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
// Regel an das Datenfeld Amount als semantischen Bereich anhängen
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel - grauer Text für Beträge unter 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder `add()`‑Aufruf auf `getConditionalFormats()` fügt der Pivot‑Tabelle ein `PivotConditionalFormat` hinzu. Die Bedingungen, ihre Formeln und ihre Stile werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der Datei im nachfolgenden Beispiel zeigt dieselben beiden Regeln mit ihren Typen, Operatoren und Formeln unverändert, und `getCellAreas()` meldet dieselben Gebiete. Einträge, denen nie eine Bedingung zugewiesen wurde, werden beim Speichern der Arbeitsmappe verworfen, genauso wie Excel ein bedingtes Format ohne Regel verwirft.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Das wird ausgegeben:
// Bedingte Formate: 1
// Format 0: Zellwert GrößerAls formula1==200
//     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
```

## **Related Articles**
- [Stil auf Pivot-Tabelle anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Teil einer Pivot-Tabelle formatieren](/cells/de/nodejs-java/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Tabelle](/cells/de/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Tabellen nach Bezeichnung oder Wert filtern](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
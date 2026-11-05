---
title: Bedingte Formatierung zu einer PivotTable hinzufügen
linktitle: Bedingte Formatierung zu einer PivotTable hinzufügen
description: Bedingte Formatierung zu einer PivotTable in Aspose.Cells for JavaScript via C++ hinzufügen, indem eine Regel mit applyTo und einem PivotConditionFormatScopeType‑Bereich an den Datenbereich angeheftet oder das Ziel mit addCellArea und pivotAreas definiert wird, und anschließend Regeln und Stile über formatConditions.addCondition anhängt.
keywords: Aspose.Cells for JavaScript via C++, PivotTable, bedingte Formatierung, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /de/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Die auf der übergeordneten Seite und der verwandten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal gemalt und behält sein Format, unabhängig von den Werten. Bedingte Formatierung ist das regelbasierte Gegenstück – jede Summe über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten platzierten Elemente markieren – und die Hervorhebung folgt den Werten, wann immer die PivotTable neu berechnet oder aktualisiert wird.
In Aspose.Cells befindet sich die bedingte Formatierung von PivotTable in der Sammlung `pivotTable.conditionalFormats`. Jeder Eintrag ist ein `PivotConditionalFormat`, der zwei Fragen unabhängig beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `applyTo(row, column, scope)` definiert, was dem Bereichsauswahl‑Tool der Excel‑Benutzeroberfläche entspricht, oder über `addCellArea(cellArea)` und die Sammlung `pivotAreas`, die den Bereich explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `formatConditions` mit `addCondition(type, operatorType, formula1, formula2)` hinzugefügt, und jede Bedingung trägt ihr eigenes `style`.

{{% alert color="primary" %}}
Rufen Sie nicht `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` oder `formatConditions.addArea(cellArea)` auf dem `formatConditions`‑Objekt eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen aus der regulären Worksheet‑Bedingten‑Formatierungs‑API und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird nie in einen Pivot‑Bereich konvertiert, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie den Bereich immer direkt auf dem `PivotConditionalFormat` selbst (`applyTo`, `addCellArea` oder `pivotAreas`) und fügen Sie die Regel mit einer der `addCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Eine Regel mit einem Bereich anwenden (wie in der Excel‑Benutzeroberfläche)**
Die erste Methode positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der PivotTable wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich teilt Aspose.Cells mit, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.Data` – alle Wertzellen, die die PivotTable erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.Field` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, z. B. ein Zeilenfeld‑Label; das Übergeben einer Wertzelle löst eine Ausnahme aus.
- `PivotConditionFormatScopeType.Selection` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das nachstehende Beispiel erstellt eine PivotTable für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `Data`‑Bereich und hebt jede Summe über 200 fett weiß auf rot hervor. Mit den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 färbt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Regel – hebe Beträge hervor, die größer als 200 sind
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) gibt die Datei als Bytes zurück
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Das Anbringen derselben Regel am Zeilenfeld‑Label E4 (Zeile 3, Spalte 4) mit dem `Field`‑Bereich löst stattdessen F4:F6 – dieselbe Datenspalte ohne die Gesamtsummenzeile – da der Bereich nun das `Fruit`‑Feld und nicht das gesamte Werte‑Gebiet beschreibt. Der `Selection`‑Bereich, verankert bei F4, löst nur F4 aus.

## **Den Bereich manuell definieren**
Die zweite Methode überspringt die Bereichsauswahl und benennt den Bereich explizit auf dem `PivotConditionalFormat`.

### **Ein Arbeitsblatt‑Rechteck mit addCellArea**
`addCellArea(cellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich entspricht exakt dem übergebenen Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Ziele das Rechteck F4:F6 (die Wertzellen ohne die Gesamtsumme)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Regel - kursiv auf hellgelb für Beträge zwischen 150 und 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Ein semantischer Pivot‑Bereich mit pivotAreas**
`pivotAreas` ist dasselbe semantische Regionsmodell, das die verwandte Seite für statische Stile verwendet. Erzeugen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `select` oder `selectField` aus und fügen Sie es mit `pivotAreas.addPivotArea(pivotArea)` hinzu. Ein semantischer Bereich bleibt an sein Feld gebunden, sodass das bedingte Format dem Feld folgt, wenn die PivotTable aktualisiert und das Layout verschoben wird. Die Überladung `pivotAreas.add(pivotArea)` funktioniert weiterhin, ist jedoch als veraltet markiert – bevorzugen Sie `addPivotArea`.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Regel an das Datenfeld Amount als semantische Region anhängen
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Regel – grauer Text für Beträge unter 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder Aufruf von `conditionalFormats.add()` fügt ein `PivotConditionalFormat` zur PivotTable hinzu. Die Bedingungen, ihre Formeln und ihre Formate werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der von Beispiel 1 in Node gespeicherten Datei zeigt dieselbe Regel mit ihrem Typ, Operator und Formel unverändert, und `getCellAreas()` gibt denselben Bereich zurück. Auf dieser Plattform werden die Eigenschaften `type` und `operator` einer Bedingung als numerische Enum‑Werte dargestellt. Einträge, die nie eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe verworfen, ähnlich wie Excel ein bedingtes Format ohne Regel entfernt.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Lade die Datei neu, die im ersten Beispiel geschrieben wurde
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Dies gibt aus:
    // Bedingte Formate: 1
    // Format 0: 1 2 formula1==200   (Typ 1 = Zellwert, Operator 2 = GrößerAls)
    //     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
    process.exit(0);
});
```

## **Verwandte Artikel**
- [Stil auf Pivot‑Table anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [Teil einer Pivot‑Table formatieren](/cells/de/javascript-cpp/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Table](/cells/de/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Table nach Beschriftung oder Wert filtern](/cells/de/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}
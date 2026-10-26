---
title: PivotTable einfügen
linktitle: PivotTable einfügen
description: Erstellen und formatieren Sie PivotTables in Excel-Kalkulationsdateien mit Aspose.Cells for Node.js via Java.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /de/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Zusammenfassungsbericht: Sie verdichtet einen großen Block an Rohdaten, der Zeile für Zeile vorliegt, zu einer kompakten Matrix, ganz ohne eine einzige Formel. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Umsatzsummen pro Produkt, Region oder Quartal statt langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten machen aus einer flachen Liste einen Kreuzbericht, in dem Trends auf einen Blick erkennbar sind.
- **Auf Details eingehen** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen einzusehen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, berechnet eine einzige Aktualisierung den gesamten Bericht neu.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Ausgabenaufschlüsselungen und Bestandsanalysen – beispielsweise die Frage: „Wie lassen sich diese Zahlen nach Kategorie und Zeit aufteilen?“ Aspose.Cells for Node.js via Java erstellt dieselben PivotTables programmgesteuert, sodass die von Ihrer Anwendung erzeugten Arbeitsmappen einsatzfertige Berichte statt ausschließlich Rohdaten enthalten können.

### **Objektmodell der PivotTable**
Aspose.Cells stellt eine Reihe von Klassen bereit, mit denen PivotTables erstellt und gesteuert werden. Die Bausteine sind:
- `PivotField` stellt ein Feld in einer `PivotTable` dar.
- `PivotFieldCollection` stellt eine Auflistung aller `PivotField`-Objekte in der `PivotTable` dar.
- `PivotTable` stellt eine PivotTable auf einem Arbeitsblatt dar.
- `PivotTableCollection` stellt eine Auflistung aller `PivotTable`-Objekte auf einem Arbeitsblatt dar.

### **Erstellen einer einfachen PivotTable mit Aspose.Cells**
Das Erstellen einer PivotTable umfasst drei Schritte: Schreiben Sie die Quelldaten in Zellen eines Arbeitsblatts, fügen Sie die PivotTable an einer Zielposition hinzu und platzieren Sie die Felder der PivotTable im Zeilen-, Spalten- und Datenbereich.
1. Fügen Sie einem Arbeitsblatt mithilfe der Methode `putValue` der Zelle Daten hinzu. Diese Daten dienen als Datenquelle der PivotTable.
2. Fügen Sie dem Arbeitsblatt eine PivotTable hinzu, indem Sie die Methode `add` der Auflistung `PivotTables` aufrufen: `add(sourceData, row, column)`. `sourceData` ist der Quellbereich (zum Beispiel „A1:C8“); `row` und `column` sind die 0-basierten Koordinaten der Zielzelle an der linken oberen Ecke der PivotTable (Zelle E3 entspricht Zeile 2, Spalte 4). Die Methode gibt direkt das neue Objekt `PivotTable` zurück.
3. Ordnen Sie die Felder mithilfe der Methode `addFieldToArea` des Objekts `PivotTable` zu: Ein Feldname wird dem Zeilenbereich (`PivotFieldType.ROW`), dem Spaltenbereich (`PivotFieldType.COLUMN`) oder dem Datenbereich (`PivotFieldType.DATA`) zugeordnet.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Nach Ausführung des Beispielcodes wird dem Arbeitsblatt eine PivotTable hinzugefügt.

```javascript
const AsposeCells = require("aspose.cells");

// Erstelle eine neue Arbeitsmappe und rufe das erste Arbeitsblatt ab
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Schreibe die Quelldaten: Umsätze pro Sport und Quartal
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Füge am Zielcell E3 eine Pivot-Tabelle hinzu, deren Quelle A1:C8 ist
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Weise die Pivot-Felder zu: Sport zu Zeilen, Quarter zu Spalten, Sales zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Speichere die Arbeitsmappe
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Wenn ein Zellenbereich als Datenquelle zugewiesen wird, muss er von oben links nach unten rechts verlaufen. Beispielsweise ist „A1:C3“ gültig, „C3:A1“ jedoch nicht.
{{% /alert %}}

## Verwandte Artikel
- [Filterfelder zu einer PivotTable in Aspose.Cells for Node.js via Java hinzufügen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for Node.js via Java anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Layout des Seitenfelds in einer PivotTable ändern](/cells/de/nodejs-java/change-page-field-layout/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Wertfelder von PivotTables in Aspose.Cells for Node.js via Java verwalten](/cells/de/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}
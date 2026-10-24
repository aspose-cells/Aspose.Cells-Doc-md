---
title: Pivot-Felder in der Pivot-Tabelle gruppieren
linktitle: Pivot-Felder in der Pivot-Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Zeitperioden wie Monate und Quartale sowie in Zahlenbereiche gruppieren, indem Sie PivotField.Group und PivotFieldGroupOptions in Aspose.Cells for Node.js via C++ verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.Group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, JavaScript
type: docs
weight: 80
url: /de/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Einsatzszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Werte enthält, z. B. ein Datumsfeld mit Hunderten von Datumsangaben oder ein Zahlenfeld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Werte in aussagekräftige Abschnitte zusammengefasst: Daten in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0–1, 2–3, 4–5. Dadurch wird eine große Pivot-Tabelle kompakt und leichter analysierbar. Aspose.Cells stellt diese Funktion über die Methode `pivotField.group()` (automatische Gruppierung nach Datentyp) und `pivotField.group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen) bereit.
- Bei der Datumsgruppierung werden die einzelnen Daten in größere Zeiträume wie Tage, Monate, Quartale und Jahre zusammengefasst und eine Zeithierarchie aufgebaut (z. B. Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im ZEILEN- oder SPALTEN-Bereich einer Pivot-Tabelle platziert sind. Ein Daten-(Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `pivotField.group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das nur Daten (und Leerwerte) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und Leerwerte) enthält, wird anhand eines automatischen Intervalls in Zahlenbereiche gruppiert.

```javascript
const AsposeCells = require("aspose.cells.node");
// Beispielarbeitsmappe laden
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Auf das zweite Arbeitsblatt und seine Pivot-Tabelle zugreifen
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Das erste Zeilenfeld automatisch gruppieren.
// Das Feld enthält Datumsangaben, daher wird es nach Monaten gruppiert.
const field = pt.getRowFields().get(0);
field.group();
// Die Daten der Pivot-Tabelle berechnen und die Ausgabedatei speichern
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` ermöglicht eine benutzerdefinierte Gruppierungskonfiguration. Legen Sie für Datumsfelder `startDate`, `endDate` und `groupTypes` fest. Legen Sie für Zahlenfelder `startNumber`, `endNumber` und `interval` fest. Die Eigenschaft `newPivotField` steuert, ob die Gruppierung neue Pivot-Felder neben dem ursprünglichen Feld erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datums-Zeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Die Bildschirmaufnahme zeigt den Effekt: Das Datums-Zeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.groupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgeführt sind, werden die gruppierten Felder immer vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.groupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Auf das zweite Arbeitsblatt und dessen Pivot-Tabelle zugreifen
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Das erste Zeilenfeld (Anrissfeld) nach Monaten und Quartalen gruppieren
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Die Pivot-Tabellendaten berechnen und die Ausgabedatei speichern
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot-Tabelle gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein Zahlenfeld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist zunächst ein Daten-(Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert anschließend das Zahlenfeld mithilfe von `startNumber = 0`, `endNumber = 5` und `interval = 2` in die Bereiche 0–1, 2–3 und 4–5.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Zugriff auf das zweite Arbeitsblatt und seine Pivot-Tabelle
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo ist ein Datenfeld: zuerst in den Zeilenbereich verschieben,
// da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Numerisches Feld in die Bereiche 0-1, 2-3, 4-5 gruppieren
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Pivot-Tabellen-Daten berechnen und Ausgabedatei speichern
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Methodenüberladungen `pivotField.groupBy()` sind veraltet und wurden aus der API-Oberfläche entfernt. `pivotField.group()` und `pivotField.group(PivotFieldGroupOptions)` sind die Nachfolger.
- In Microsoft Excel ERSETZT das Gruppieren eines Zahlenfeldes das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfeldes NEUE Pivot-Felder (eines pro Gruppenebene, z. B. Quartale und Monate) neben dem ursprünglichen Feld ERSTELLT. Ab Aspose.Cells 26.10 verhalten sich die Methoden `pivotField.group()` genauso wie Excel. Die Eigenschaft `pivotFieldGroupOptions.newPivotField` ist aus Gründen der Kompatibilität mit älteren Versionen vorhanden: Standardmäßig ist sie für die Zahlengruppierung auf false und für die Datums-Zeit-Gruppierung auf true gesetzt. Setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `pivotFieldGroupOptions.interval` wirkt sich nur auf die Zahlengruppierung sowie auf die Datumsgruppierung nach Tagen (z. B. das Gruppieren von Daten in 7-Tage-Zeiträume) aus. Sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in der Pivot-Tabelle hinzufügen](/cells/de/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Beschriftung oder Wert filtern](/cells/de/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/nodejs-cpp/add-page-field-in-pivot-table/)
- [Formatierung auf Pivot-Tabelle anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}
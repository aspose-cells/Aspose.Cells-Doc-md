---
title: Gruppieren von Pivot-Feldern in der Pivot-Tabelle
linktitle: Gruppieren von Pivot-Feldern in der Pivot-Tabelle
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Datumsperioden wie Monate und Quartale sowie in Zahlenbereiche gruppieren, indem Sie PivotField.group und PivotFieldGroupOptions in Aspose.Cells for Node.js via Java verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, Node.js
type: docs
weight: 80
url: /de/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, beispielsweise ein Datumsfeld mit Hunderten von Datumswerten oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Daten in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0-1, 2-3, 4-5. Dadurch wird eine große Pivot-Tabelle kompakt und lässt sich leichter analysieren. Aspose.Cells for Node.js via Java bietet diese Funktion über die Methode `PivotField.group()` (automatische Gruppierung nach Datentyp) und `PivotField.group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen).
- Bei der Datumsgruppierung werden die einzelnen Daten in größere Zeiträume wie Tage, Monate, Quartale und Jahre zusammengefasst und es wird eine Zeithierarchie aufgebaut (z. B. Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im Bereich ZEILE oder SPALTE einer Pivot-Tabelle platziert sind. Ein Daten-(Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.group()` untersucht den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das nur Daten (und Leerzeichen) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und Leerzeichen) enthält, wird anhand eines automatischen Intervalls in Zahlenbereiche gruppiert.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Auf das zweite Arbeitsblatt und seine Pivot-Tabelle zugreifen
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Das erste Zeilenfeld automatisch gruppieren.
// Das Feld enthält Daten, daher wird es nach Monaten gruppiert.
let field = pt.getRowFields().get(0);
field.group();
// Die Daten der Pivot-Tabelle berechnen und die Ausgabedatei speichern
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` stellt eine benutzerdefinierte Gruppierungskonfiguration bereit. Für Datumsfelder legen Sie `StartDate`, `EndDate` und `GroupTypes` fest. Für numerische Felder legen Sie `StartNumber`, `EndNumber` und `Interval` fest. Die Eigenschaft `NewPivotField` steuert, ob die Gruppierung neue Pivot-Felder neben dem ursprünglichen Feld erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datums-Zeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Der Screenshot zeigt die Wirkung: Das Datums-Zeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.GroupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgeführt sind, werden die gruppierten Felder immer von der größten Periode bis zur kleinsten angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.GroupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```javascript
const AsposeCells = require("aspose.cells");
// Lade die Beispielarbeitsmappe
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Greife auf das zweite Arbeitsblatt und seine Pivot-Tabelle zu
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Gruppiere das erste Zeilenfeld (ein Datumsfeld) nach Monaten und Quartalen
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Berechne die Pivot-Tabellendaten und speichere die Ausgabedatei
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot-Tabelle gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist zunächst ein Daten-(Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert dann das numerische Feld in die Bereiche 0-1, 2-3 und 4-5 unter Verwendung von `StartNumber = 0`, `EndNumber = 5` und `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// Laden Sie die Beispielarbeitsmappe
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Auf das zweite Arbeitsblatt und seine Pivot-Tabelle zugreifen
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo ist ein Datenfeld: Verschieben Sie es zuerst in den Zeilenbereich,
// da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Gruppieren Sie das numerische Feld in die Bereiche 0-1, 2-3, 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Pivot-Tabellendaten berechnen und Ausgabedatei speichern
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `PivotField.GroupBy()` sind veraltet und aus der API-Oberfläche entfernt. `PivotField.group()` und `PivotField.group(PivotFieldGroupOptions)` sind die Ersatzmethoden.
- In Microsoft Excel ERSETZT das Gruppieren eines numerischen Feldes das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfeldes NEUE Pivot-Felder (eines pro Gruppenebene, z. B. Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells for Node.js via Java 26.10 folgen die Methoden `PivotField.group()` demselben Verhalten wie Excel. Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` ist aus Kompatibilität mit älteren Versionen vorhanden: Der Standardwert ist false für numerische Gruppierung und true für Datum-Uhrzeit-Gruppierung; setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.Interval` wirkt sich nur auf die numerische Gruppierung und auf die Datumsgruppierung nach Tagen aus (z. B. das Gruppieren von Daten in 7-Tage-Zeiträume); sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in der Pivot-Tabelle hinzufügen](/cells/de/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Beschriftung oder Wert filtern](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in der Pivot-Tabelle hinzufügen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Formatvorlage auf Pivot-Tabelle anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}
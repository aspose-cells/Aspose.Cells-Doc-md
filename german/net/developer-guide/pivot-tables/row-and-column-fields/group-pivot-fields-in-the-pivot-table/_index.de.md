---
title: Pivot-Felder in der Pivot-Tabelle gruppieren
linktitle: Pivot-Felder in der Pivot-Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Zeiträume wie Monate und Quartale sowie in Zahlenbereiche gruppieren, indem Sie PivotField.Group und PivotFieldGroupOptions in Aspose.Cells for .NET verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.Group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, C#
type: docs
weight: 80
url: /de/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, z. B. ein Datumsfeld mit Hunderten von Datumsangaben oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Datumsangaben in Monate, Quartale und Jahre, und Zahlen in Bereiche wie 0–1, 2–3, 4–5. Dadurch wird eine große Pivot-Tabelle kompakt und einfacher zu analysieren. Aspose.Cells bietet diese Funktion über die Methode `PivotField.Group()` (automatisches Gruppieren nach Datentyp) und `PivotField.Group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen).
- Beim Datumsgruppieren werden die einzelnen Datumsangaben in größere Zeiträume wie Tage, Monate, Quartale und Jahre zusammengefasst und eine Zeithierarchie aufgebaut (z. B. Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Zeiträumeebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im ROW- oder COLUMN-Bereich einer Pivot-Tabelle platziert sind. Ein Datenfeld (Wertfeld) kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.Group()` prüft den Datentyp des Felds und gruppiert es automatisch. Ein Feld, das nur Datumsangaben (und leere Werte) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und leere Werte) enthält, wird mit einem automatischen Intervall in Zahlenbereiche gruppiert.

```csharp
using Aspose.Cells.Pivot;
// Laden Sie die Beispielarbeitsmappe
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Zugriff auf das zweite Arbeitsblatt und dessen Pivot-Tabelle
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Das erste Zeilenfeld automatisch gruppieren.
// Das Feld enthält Datumsangaben, daher wird es nach Monaten gruppiert.
PivotField field = pt.RowFields[0];
field.Group();
// Berechnen Sie die Pivot-Tabellendaten und speichern Sie die Ausgabedatei
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` stellt eine benutzerdefinierte Gruppierungskonfiguration bereit. Für Datumsfelder setzen Sie `StartDate`, `EndDate` und `GroupTypes`. Für numerische Felder setzen Sie `StartNumber`, `EndNumber` und `Interval`. Die Eigenschaft `NewPivotField` steuert, ob die Gruppierung neue Pivot-Felder neben dem ursprünglichen Feld erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datumszeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Der Screenshot zeigt den Effekt: Das Datumszeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.GroupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgelistet sind, werden die gruppierten Felder immer vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.GroupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```csharp
using Aspose.Cells.Pivot;
// Laden Sie die Beispielarbeitsmappe
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Greifen Sie auf das zweite Arbeitsblatt und seine Pivot-Tabelle zu
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Gruppieren Sie das erste Zeilenfeld (ein Datumsfeld) nach Monaten und Quartalen
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// Berechnen Sie die Pivot-Tabellendaten und speichern Sie die Ausgabedatei
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot-Tabelle gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist zunächst ein Datenfeld (Wertfeld). Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert dann das numerische Feld mit `StartNumber = 0`, `EndNumber = 5` und `Interval = 2` in die Bereiche 0–1, 2–3 und 4–5.

```csharp
using Aspose.Cells.Pivot;
// Laden der Beispielarbeitsmappe
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Zugriff auf das zweite Arbeitsblatt und seine Pivot-Tabelle
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo ist ein Datenfeld: verschieben Sie es zuerst in den Zeilenbereich,
// da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// Gruppieren des numerischen Felds in die Bereiche 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// Berechnen der Pivot-Tabellendaten und Speichern der Ausgabedatei
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Methodenüberladungen `PivotField.GroupBy()` sind veraltet und aus der API-Oberfläche entfernt. `PivotField.Group()` und `PivotField.Group(PivotFieldGroupOptions)` sind die Ersetzungen.
- In Microsoft Excel ersetzt die Gruppierung eines numerischen Feldes das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während die Gruppierung eines Datumsfeldes NEUE Pivot-Felder (eines pro Gruppierungsebene, z. B. Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells 26.10 folgen die Methoden `PivotField.Group()` demselben Verhalten wie Excel. Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` existiert aus Kompatibilität mit früheren Versionen: Der Standardwert ist false für numerische Gruppierung und true für Datums-Zeit-Gruppierung. Setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.Interval` wirkt sich nur auf numerische Gruppierung und auf Datumsgruppierung nach Tagen aus (z. B. Gruppierung von Datumsangaben in 7-Tage-Perioden); sie wird ignoriert, wenn Datumsangaben nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in Pivot-Tabelle hinzufügen](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Beschriftung oder Wert filtern](/cells/de/net/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Formatvorlage auf Pivot-Tabelle anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
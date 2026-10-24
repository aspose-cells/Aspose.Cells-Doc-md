---
title: Pivot-Felder in der Pivot-Tabelle gruppieren
linktitle: Pivot-Felder in der Pivot-Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Datumsperioden wie Monate und Quartale sowie in Zahlenbereiche gruppieren können, indem Sie PivotField.group und PivotFieldGroupOptions in Aspose.Cells for Java verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, Java
type: docs
weight: 80
url: /de/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Einsatzszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, etwa ein Datumsfeld mit Hunderten von Daten oder ein Zahlenfeld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Daten in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0-1, 2-3, 4-5. Dadurch wird eine große Pivot-Tabelle kompakt und leichter zu analysieren. Aspose.Cells stellt diese Funktionalität über die Methode `PivotField.group()` (automatische Gruppierung nach Datentyp) und `PivotField.group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen) bereit.
- Bei der Datumsgruppierung werden die einzelnen Daten in größere Perioden wie Tage, Monate, Quartale und Jahre zusammengefasst und eine Zeithierarchie aufgebaut (beispielsweise Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im ZEILEN- oder SPALTEN-Bereich einer Pivot-Tabelle platziert sind. Ein Daten- (Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das ausschließlich Daten (und Leerwerte) enthält, wird nach Monaten gruppiert. Ein Feld, das ausschließlich Zahlen (und Leerwerte) enthält, wird mithilfe eines automatischen Intervalls in Zahlenbereiche gruppiert.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` stellt eine benutzerdefinierte Gruppierungskonfiguration bereit. Für Datumsfelder setzen Sie `startDate`, `endDate` und `groupTypes`. Für Zahlenfelder setzen Sie `startNumber`, `endNumber` und `interval`. Die Eigenschaft `newPivotField` steuert, ob die Gruppierung neben dem ursprünglichen Feld neue Pivot-Felder erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datums-Zeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Der Screenshot zeigt die Wirkung: Das Datums-Zeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.groupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgeführt sind, werden die gruppierten Felder immer von der größten zur kleinsten Periode angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.groupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene dargestellt.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot-Tabelle gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein Zahlenfeld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist zunächst ein Daten- (Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert anschließend das Zahlenfeld mit `startNumber = 0`, `endNumber = 5` und `interval = 2` in die Bereiche 0-1, 2-3 und 4-5.

```java
import com.aspose.cells.*;
// Laden Sie die Beispielarbeitsmappe
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Auf das zweite Arbeitsblatt und seine Pivot-Tabelle zugreifen
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo ist ein Datenfeld: Verschieben Sie es zuerst in den Zeilenbereich,
// da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Gruppieren Sie das numerische Feld in die Bereiche 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Berechnen Sie die Pivot-Tabellendaten und speichern Sie die Ausgabedatei
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `PivotField.groupBy()` sind veraltet und wurden aus der API-Oberfläche entfernt. `PivotField.group()` und `PivotField.group(PivotFieldGroupOptions)` sind die Ersetzungen.
- In Microsoft Excel ERSETZT das Gruppieren eines Zahlenfelds das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfelds NEUE Pivot-Felder (eines pro Gruppenebene, beispielsweise Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells 26.10 folgen die Methoden `PivotField.group()` demselben Verhalten wie Excel. Die Eigenschaft `PivotFieldGroupOptions.newPivotField` ist aus Kompatibilität mit älteren Versionen vorhanden: Standardmäßig ist sie für die Zahlengruppierung false und für die Datum-Uhrzeit-Gruppierung true; setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.interval` wirkt sich nur auf die Zahlengruppierung und auf die Datumsgruppierung nach Tagen aus (beispielsweise das Gruppieren von Daten in 7-Tage-Perioden); sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in der Pivot-Tabelle hinzufügen](/cells/de/java/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Label oder Wert filtern](/cells/de/java/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in der Pivot-Tabelle hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)
- [Stil auf Pivot-Tabelle anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}
---
title: Gruppieren von Pivot-Feldern in der Pivot-Tabelle
linktitle: Gruppieren von Pivot-Feldern in der Pivot-Tabelle
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Zeiträume wie Monate und Quartale sowie in Zahlenbereiche gruppieren, indem Sie PivotField.Group und PivotFieldGroupOptions in Aspose.Cells for Python via .NET verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Felder gruppieren, PivotField.Group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, Python via .NET
type: docs
weight: 80
url: /de/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, z. B. ein Datumsfeld mit Hunderten von Datumsangaben oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Daten in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0–1, 2–3, 4–5. Dadurch wird eine große Pivot-Tabelle kompakt und leichter zu analysieren. Aspose.Cells for Python via .NET stellt diese Funktion über die Methode `pivot_field.group()` (automatische Gruppierung nach Datentyp) und `pivot_field.group(pivot_field_group_options)` (benutzerdefinierte Gruppierungsoptionen) bereit.
- Bei der Datumsgruppierung werden die einzelnen Daten zu größeren Zeiträumen wie Tagen, Monaten, Quartalen und Jahren zusammengefasst und eine Zeithierarchie aufgebaut (z. B. Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im Zeilen- oder Spaltenbereich einer Pivot-Tabelle platziert sind. Ein Daten- (Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst zum Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `pivot_field.group()` untersucht den Datentyp des Felds und gruppiert es automatisch. Ein Feld, das nur Daten (und leere Werte) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und leere Werte) enthält, wird mit einem automatischen Intervall in Zahlenbereiche gruppiert.

```python
import aspose.cells as ac
# Laden Sie die Beispielarbeitsmappe
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Zugriff auf das zweite Arbeitsblatt und dessen Pivot-Tabelle
pt = wb.worksheets[1].pivot_tables[0]
# Gruppieren Sie das erste Zeilenfeld automatisch.
# Das Feld enthält Datumsangaben, daher wird es nach Monaten gruppiert.
field = pt.row_fields[0]
field.group()
# Berechnen Sie die Pivot-Tabellendaten und speichern Sie die Ausgabedatei
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` stellt eine benutzerdefinierte Gruppierungskonfiguration bereit. Für Datumsfelder setzen Sie `start_date`, `end_date` und `group_types`. Für numerische Felder setzen Sie `start_number`, `end_number` und `interval`. Die Eigenschaft `new_pivot_field` steuert, ob das Gruppieren neue Pivot-Felder neben dem ursprünglichen erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datumszeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Pivot-Tabellendaten und speichert das gruppierte Ergebnis. Der Screenshot zeigt den Effekt: Das Datumszeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.group_types` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgelistet sind, werden die gruppierten Felder immer vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.group_types` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Lade die Beispielarbeitsmappe
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Greife auf das zweite Arbeitsblatt und seine Pivot-Tabelle zu
pt = wb.worksheets[1].pivot_tables[0]
# Gruppiere das erste Zeilenfeld (ein Datumsfeld) nach Monaten und Quartalen
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Berechne die Pivot-Tabellen-Daten und speichere die Ausgabedatei
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Pivot-Tabelle nach Monaten und Quartalen gruppiert](group-pivot-fields-in-the-pivot-table_1.png)

### **Numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist zunächst ein Daten- (Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert dann das numerische Feld mit `start_number=0`, `end_number=5` und `interval=2` in die Bereiche 0–1, 2–3 und 4–5.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Laden Sie die Beispielarbeitsmappe
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Greifen Sie auf das zweite Arbeitsblatt und dessen Pivot-Tabelle zu
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo ist ein Datenfeld: verschieben Sie es zuerst in den Zeilenbereich,
# da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Gruppieren Sie das numerische Feld in die Bereiche 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Berechnen Sie die Pivot-Tabellendaten und speichern Sie die Ausgabedatei
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `pivot_field.group_by()` sind veraltet und aus der API-Oberfläche entfernt. `pivot_field.group()` und `pivot_field.group(pivot_field_group_options)` sind die Ersatzmethoden.
- In Microsoft Excel ERSETZT das Gruppieren eines numerischen Felds das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfelds NEUE Pivot-Felder (eines pro Gruppenebene, z. B. Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells 26.10 verhalten sich die Methoden `pivot_field.group()` genauso wie in Excel. Die Eigenschaft `PivotFieldGroupOptions.new_pivot_field` ist aus Kompatibilität mit älteren Versionen vorhanden: Sie ist bei numerischer Gruppierung standardmäßig auf false und bei Datums-Zeit-Gruppierung auf true gesetzt; setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.interval` wirkt sich nur auf die numerische Gruppierung und auf die Datumsgruppierung nach Tagen aus (z. B. Gruppierung von Daten in 7-Tage-Zeiträume); sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Hinzufügen von Zeilen- und Spaltenfeldern in der Pivot-Tabelle](/cells/de/python-net/pivot-table-add-row-and-column-fields/)
- [Filtern von Pivot-Tabellen nach Beschriftung oder Wert](/cells/de/python-net/filter-by-label-or-value-of-pivot-table/)
- [Hinzufügen eines Seitenfelds in der Pivot-Tabelle](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Anwenden eines Stils auf die Pivot-Tabelle](/cells/de/python-net/apply-style-to-pivot-table/)
- [Aktualisieren der Pivot-Tabelle](/cells/de/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}
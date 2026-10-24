---
title: Pivot-Felder in der Pivot-Tabelle gruppieren
linktitle: Pivot-Felder in der Pivot-Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Datumsperioden wie Monate und Quartale sowie in numerische Bereiche gruppieren, indem Sie PivotField.group und PivotFieldGroupOptions in Aspose.Cells for Python via Java verwenden.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, Python
type: docs
weight: 80
url: /de/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Einsatzszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, z. B. ein Datumsfeld mit Hunderten von Datumsangaben oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Datumsangaben in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0–1, 2–3, 4–5. Dadurch wird eine große Pivot-Tabelle kompakt und leichter analysierbar. Aspose.Cells stellt diese Funktion über die Methode `PivotField.group()` (automatische Gruppierung nach Datentyp) und `PivotField.group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen) bereit.
- Die Datumsgruppierung fasst einzelne Datumsangaben zu größeren Zeiträumen wie Tagen, Monaten, Quartalen und Jahren zusammen und bildet eine Zeithierarchie (beispielsweise Jahre, Quartale, Monate). Trends über die Zeit werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im Zeilen- oder Spaltenbereich einer Pivot-Tabelle platziert sind. Ein Daten-(Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst zum Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das ausschließlich Datumsangaben (und leere Zellen) enthält, wird nach Monaten gruppiert. Ein Feld, das ausschließlich Zahlen (und leere Zellen) enthält, wird mit einem automatischen Intervall in Zahlenbereiche gruppiert.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Lade die Beispielarbeitsmappe
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Greife auf das zweite Arbeitsblatt und seine Pivot-Tabelle zu
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Gruppiere das erste Zeilenfeld automatisch.
# Das Feld enthält Datumsangaben, daher wird es nach Monaten gruppiert.
field = pt.getRowFields().get(0)
field.group()
# Berechne die Pivot-Tabellen-Daten und speichere die Ausgabedatei
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` bietet benutzerdefinierte Gruppierungskonfigurationen. Für Datumsfelder setzen Sie `StartDate`, `EndDate` und `GroupTypes`. Für numerische Felder setzen Sie `StartNumber`, `EndNumber` und `Interval`. Die Eigenschaft `NewPivotField` steuert, ob die Gruppierung neue Pivot-Felder neben dem ursprünglichen erzeugt (siehe den Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datums-Zeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Der Screenshot zeigt die Wirkung: Das Datums-Zeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.GroupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgeführt sind, werden die gruppierten Felder immer vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.GroupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Laden Sie die Beispielarbeitsmappe
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Zugriff auf das zweite Arbeitsblatt und seine Pivot-Tabelle
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Gruppieren Sie das erste Zeilenfeld (ein Datumsfeld) nach Monaten und Quartalen
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Berechnen Sie die Pivot-Tabellen-Daten und speichern Sie die Ausgabedatei
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Pivot-Tabelle, gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist ursprünglich ein Daten-(Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert dann das numerische Feld mithilfe von `StartNumber = 0`, `EndNumber = 5` und `Interval = 2` in die Bereiche 0–1, 2–3 und 4–5.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Laden Sie die Beispielarbeitsmappe
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Greifen Sie auf das zweite Arbeitsblatt und seine Pivot-Tabelle zu
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo ist ein Datenfeld: Verschieben Sie es zuerst in den Zeilenbereich,
# da nur Zeilen-/Spaltenfelder gruppiert werden können
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Gruppieren Sie das numerische Feld in die Bereiche 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Berechnen Sie die Pivot-Tabellen-Daten und die Ausgabedatei
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Methodenüberladungen `PivotField.groupBy()` sind veraltet und aus der API-Oberfläche entfernt. `PivotField.group()` und `PivotField.group(PivotFieldGroupOptions)` sind die Ersetzungen.
- In Microsoft Excel ersetzt das Gruppieren eines numerischen Feldes das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfeldes NEUE Pivot-Felder (eines pro Gruppierungsebene, beispielsweise Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells 26.10 verhalten sich die Methoden `PivotField.group()` genauso wie Excel. Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` ist für die Kompatibilität mit älteren Versionen vorhanden: Standardmäßig ist sie bei numerischer Gruppierung auf false und bei Datums-Zeit-Gruppierung auf true gesetzt; setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.Interval` wirkt sich nur auf die numerische Gruppierung sowie auf die Datumsgruppierung nach Tagen aus (beispielsweise das Gruppieren von Datumsangaben in 7-Tage-Zeiträume); sie wird ignoriert, wenn Datumsangaben nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in Pivot-Tabelle hinzufügen](/cells/de/python-java/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Beschriftung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/python-java/add-page-field-in-pivot-table/)
- [Stil auf Pivot-Tabelle anwenden](/cells/de/python-java/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}
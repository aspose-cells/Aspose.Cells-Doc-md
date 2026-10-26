---
title: Pivot-Felder in der Pivot-Tabelle gruppieren
linktitle: Pivot-Felder in der Pivot-Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen- und Spalten-Pivot-Felder in einer Pivot-Tabelle in Datumsperioden wie Monate und Quartale sowie in numerische Bereiche gruppieren können, unter Verwendung von PivotField.Group und PivotFieldGroupOptions in Aspose.Cells for C++.
keywords: Aspose.Cells, Pivot-Tabelle, Pivot-Feld gruppieren, PivotField.Group, PivotFieldGroupOptions, Datumsgruppierung, Zahlengruppierung, Monate, Quartale, Zahlenbereich, C++
type: docs
weight: 80
url: /de/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Einsatzszenarien**
- Das Gruppieren von Pivot-Feldern ist nützlich, wenn ein Zeilen- oder Spaltenfeld einer Pivot-Tabelle viele unterschiedliche Elemente enthält, z. B. ein Datumsfeld mit Hunderten von Datumswerten oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in aussagekräftige Abschnitte zusammengefasst: Datumswerte in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0-1, 2-3, 4-5. Dadurch wird eine große Pivot-Tabelle kompakt und leichter zu analysieren. Aspose.Cells bietet diese Funktionalität über die Methode `PivotField.Group()` (automatische Gruppierung nach Datentyp) und `PivotField.Group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen).
- Die Datumsgruppierung fasst einzelne Datumswerte zu größeren Zeiträumen wie Tagen, Monaten, Quartalen und Jahren zusammen und bildet eine Zeithierarchie (z. B. Jahre, Quartale, Monate). Trends im Zeitverlauf werden auf einen Blick sichtbar, und jede Periodenebene wird zu einem eigenen Pivot-Feld im Zeilen- oder Spaltenbereich der Pivot-Tabelle.
- Das Gruppieren ist nur für Felder verfügbar, die im ZEILEN- oder SPALTEN-Bereich einer Pivot-Tabelle platziert sind. Ein Daten-(Wert-)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der Pivot-Tabelle hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.Group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das nur Datumswerte (und leere Werte) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und leere Werte) enthält, wird mit einem automatischen Intervall in Zahlenbereiche gruppiert.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` bietet eine benutzerdefinierte Gruppierungskonfiguration. Für Datumsfelder setzen Sie `StartDate`, `EndDate` und `GroupTypes`. Für numerische Felder setzen Sie `StartNumber`, `EndNumber` und `Interval`. Die Eigenschaft `NewPivotField` steuert, ob die Gruppierung neue Pivot-Felder neben dem ursprünglichen Feld erstellt (siehe Abschnitt „Hinweis" am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datums-Zeilenfeld der Beispiel-Pivot-Tabelle nach Monaten und Quartalen zwischen einem Start- und Enddatum. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Daten der Pivot-Tabelle und speichert das gruppierte Ergebnis. Der Screenshot zeigt den Effekt: Das Datums-Zeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `options.GroupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppentypen aufgeführt sind, werden die gruppierten Felder immer vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate vor den Quartalen in `options.GroupTypes` aufgeführt, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene angezeigt.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Beispielarbeitsmappe laden
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Auf das zweite Arbeitsblatt und dessen Pivot-Tabelle zugreifen
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Das erste Zeilenfeld (ein Datumsfeld) nach Monaten und Quartalen gruppieren
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Gruppentypen festlegen: Monate und Quartale
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Gruppierung auf das erste Zeilenfeld anwenden
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Pivot-Tabellendaten berechnen und die Ausgabedatei speichern
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Pivot-Tabelle nach Monaten und Quartalen gruppiert](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel-Pivot-Tabelle ist ursprünglich ein Daten-(Wert-)Feld. Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot-Tabelle und gruppiert dann das numerische Feld in die Bereiche 0-1, 2-3 und 4-5 unter Verwendung von `StartNumber = 0`, `EndNumber = 5` und `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `PivotField.GroupBy()` sind veraltet und aus der API-Oberfläche entfernt. `PivotField.Group()` und `PivotField.Group(PivotFieldGroupOptions)` sind die Nachfolger.
- In Microsoft Excel ERSETZT die Gruppierung eines numerischen Feldes das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während die Gruppierung eines Datumsfeldes NEUE Pivot-Felder (eines pro Gruppenebene, z. B. Quartale und Monate) neben dem ursprünglichen Feld erstellt. Ab Aspose.Cells 26.10 folgen die Methoden `PivotField.Group()` demselben Verhalten wie Excel. Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` existiert aus Kompatibilität mit älteren Versionen: Der Standardwert ist false für die numerische Gruppierung und true für die Datums-Zeit-Gruppierung; setzen Sie sie auf false, wenn die Datumsgruppierung das ursprüngliche Pivot-Feld ersetzen soll, anstatt neue Pivot-Felder zu erstellen.
- Die Eigenschaft `PivotFieldGroupOptions.Interval` wirkt sich nur auf die numerische Gruppierung und auf die Datumsgruppierung nach Tagen aus (z. B. das Gruppieren von Daten in 7-Tage-Perioden); sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen- und Spaltenfelder in der Pivot-Tabelle hinzufügen](/cells/de/cpp/pivot-table-add-row-and-column-fields/)
- [Pivot-Tabellen nach Beschriftung oder Wert filtern](/cells/de/cpp/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in der Pivot-Tabelle hinzufügen](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Stil auf eine Pivot-Tabelle anwenden](/cells/de/cpp/apply-style-to-pivot-table/)
- [Pivot-Tabelle aktualisieren](/cells/de/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}
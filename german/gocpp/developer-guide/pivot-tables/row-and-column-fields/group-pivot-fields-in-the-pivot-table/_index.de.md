---
title: Pivot-Felder in der PivotTable mit Golang über C++ gruppieren
linktitle: Pivot-Felder in der PivotTable mit Golang über C++ gruppieren
description: Erfahren Sie, wie Sie in Aspose.Cells for Go via C++ mit PivotField.Group und PivotFieldGroupOptions Zeilen- und Spaltenfelder in einer PivotTable in Datumszeiträume wie Monate und Quartale sowie in Zahlenbereiche gruppieren.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, PivotTable, Pivot-Feld, Pivot-Felder gruppieren, Gruppierung, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, Datumsgruppierung, Zahlenbereich, Go
type: docs
weight: 80
url: /de/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Das Gruppieren von Pivot-Feldern ist hilfreich, wenn ein Zeilen- oder Spaltenfeld einer PivotTable viele unterschiedliche Einträge enthält, etwa ein Datumsfeld mit hundert Datumsangaben oder ein Zahlenfeld mit zahlreichen verstreuten Werten. Die Gruppierung fasst diese Einträge in aussagekräftige Abschnitte zusammen: Datumsangaben nach Monaten, Quartalen und Jahren sowie Zahlen nach Bereichen wie 0-1, 2-3, 4-5. Dadurch wird eine große PivotTable kompakter und lässt sich leichter analysieren. Aspose.Cells bietet diese Funktion über die Methode `PivotField.Group()` (automatische Gruppierung nach Datentyp) und `PivotField.Group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen).
- Die Datumsgruppierung verdichtet einzelne Datumsangaben zu größeren Zeiträumen, etwa Tagen, Monaten, Quartalen und Jahren, und erstellt eine Zeithierarchie (zum Beispiel Jahre, Quartale, Monate). Zeitverläufe werden auf einen Blick sichtbar, und jede Zeitebene wird im Zeilen- oder Spaltenbereich der PivotTable zu einem eigenen Pivot-Feld.
- Die Gruppierung ist nur für Felder verfügbar, die im Zeilen- oder Spaltenbereich einer PivotTable liegen. Ein Datenfeld (Wertfeld) kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, müssen Sie es zunächst dem Zeilen- oder Spaltenbereich der PivotTable hinzufügen.

## **Pivot-Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.Group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das ausschließlich Datumswerte (und Leerzellen) enthält, wird nach Monaten gruppiert. Ein Feld, das ausschließlich Zahlenwerte (und Leerzellen) enthält, wird mithilfe eines automatischen Intervalls in Zahlenbereiche gruppiert.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **Pivot-Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` stellt die Konfiguration für benutzerdefinierte Gruppierungen bereit. Für Datumsfelder legen Sie `StartDate`, `EndDate` und `GroupTypes` fest (Datumswerte werden als Werte vom Go-Typ `time.Time` übergeben). Für Zahlenfelder legen Sie `StartNumber`, `EndNumber` und `Interval` fest. Das Verhalten von `newPivotField` bestimmt, ob beim Gruppieren neben dem ursprünglichen Feld neue Pivot-Felder erstellt werden (siehe Hinweisabschnitt am Ende dieses Artikels).

### **Datumsfeld nach Monaten und Quartalen gruppieren**
Im folgenden Beispiel wird das Datumszeilenfeld der Beispiel-PivotTable anhand von Monaten und Quartalen zwischen einem Start- und Enddatum gruppiert. Der Code lädt die [Beispiel-Excel-Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung aus, berechnet die Daten der PivotTable und speichert das gruppierte Ergebnis. Das Bildschirmfoto zeigt die Wirkung: Das Datumszeilenfeld ist nun nach Quartalen und Monaten gruppiert.
Beachten Sie, dass die Reihenfolge der Werte in `GroupTypes` ignoriert wird. Unabhängig von der Reihenfolge, in der die Gruppentypen aufgeführt sind, werden die gruppierten Felder stets vom größten zum kleinsten Zeitraum angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel sind die Monate in `GroupTypes` vor den Quartalen aufgeführt; die Quartale werden jedoch als äußere Ebene und die Monate als innere Ebene angezeigt.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![Nach Monaten und Quartalen gruppierte PivotTable](group-pivot-fields-in-the-pivot-table_1.png)

### **Zahlenfeld in Bereiche gruppieren**
`FieldTwo` ist in der Beispiel-PivotTable zunächst ein Datenfeld (Wertfeld). Da nur Zeilen- oder Spaltenfelder gruppiert werden können, ruft der Code zunächst `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben. Anschließend aktualisiert er die PivotTable und gruppiert das Zahlenfeld mit `StartNumber = 0`, `EndNumber = 5` und `Interval = 2` in die Bereiche 0-1, 2-3 und 4-5.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `PivotField.GroupBy()` sind veraltet und wurden aus der API-Oberfläche entfernt. `PivotField.Group()` und `PivotField.Group(PivotFieldGroupOptions)` sind die entsprechenden Ersatzmethoden.
- In Microsoft Excel ersetzt die Gruppierung eines Zahlenfelds das ursprüngliche Pivot-Feld durch die gruppierten Bereiche, während die Gruppierung eines Datumsfelds neben dem ursprünglichen Feld NEUE Pivot-Felder erstellt (je ein Pivot-Feld pro Gruppierungsebene, beispielsweise für Quartale und Monate). Ab Aspose.Cells 26.10 folgt die Gruppierung mit den Methoden `PivotField.Group()` und `PivotField.Group(PivotFieldGroupOptions)` demselben Verhalten wie Excel.
- Die Eigenschaft `PivotFieldGroupOptions.Interval` wirkt nur bei der Gruppierung von Zahlen und bei der Datumsgruppierung nach Tagen (beispielsweise beim Gruppieren von Datumsangaben in 7-tägige Zeiträume). Sie wird ignoriert, wenn Datumsangaben nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Top 10 in einer PivotTable anzeigen oder filtern](/cells/de/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [In einer PivotTable Werte als anzeigen](/cells/de/go-cpp/show-values-as-in-pivot-table/)
- [Teil einer PivotTable formatieren](/cells/de/go-cpp/format-part-of-pivot-table/)
- [Bedingte Formatierung zu einer PivotTable hinzufügen](/cells/de/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}
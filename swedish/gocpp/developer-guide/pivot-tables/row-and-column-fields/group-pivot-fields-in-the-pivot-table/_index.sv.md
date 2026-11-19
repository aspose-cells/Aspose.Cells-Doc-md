---
title: Gruppera pivotfält i pivottabellen med Golang via C++
linktitle: Gruppera pivotfält i pivottabellen med Golang via C++
description: Lär dig hur du grupperar pivotfält i rad- och kolumnområdena i en pivottabell till datumperioder som månader och kvartal samt till numeriska intervall med hjälp av PivotField.Group och PivotFieldGroupOptions i Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, pivottabell, pivotfält, gruppera pivotfält, Gruppera, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, datumgruppering, numeriskt intervall, Go
type: docs
weight: 80
url: /sv/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett fält i pivottabellens rad- eller kolumnområde innehåller många olika objekt, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering slår samman dessa objekt till meningsfulla avsnitt: datum grupperas till månader, kvartal och år, medan numeriska värden grupperas till intervall som 0-1, 2-3, 4-5. Det gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells erbjuder den här funktionen via metoderna `PivotField.Group()` (automatisk gruppering baserat på datatyp) respektive `PivotField.Group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering slår samman enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel år, kvartal, månader). Trender över tid blir synliga direkt, och varje periodnivå blir ett eget pivotfält i pivottabellens rad- eller kolumnområde.
- Gruppering är endast tillgänglig för fält i pivottabellens rad- eller kolumnområde. Ett datafält (värdefält) kan inte grupperas direkt. Om du vill gruppera ett sådant fält måste du först lägga till det i pivottabellens rad- eller kolumnområde.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.Group()` undersöker fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller tal (och tomma celler) grupperas i numeriska intervall där intervallet väljs automatiskt.

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

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` används för att konfigurera anpassad gruppering. För datumfält anger du `StartDate`, `EndDate` och `GroupTypes` (datum skickas som Go-värden av typen `time.Time`). För numeriska fält anger du `StartNumber`, `EndNumber` och `Interval`. Inställningen `newPivotField` avgör om gruppering skapar nya pivotfält bredvid det ursprungliga fältet (se avsnittet Obs i slutet av den här artikeln).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempelets pivottabell efter månader och kvartal mellan ett start- och ett slutdatum. Koden läser in [Excel-exempelfilen](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar data i pivottabellen och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att värdenas ordning i `GroupTypes` ignoreras. Oavsett i vilken ordning grupperingstyperna anges, visas de grupperade fälten alltid från den största perioden till den minsta perioden: år, kvartal, månader, dagar, timmar, minuter, sekunder. I det här exemplet anges månaderna före kvartalen i `GroupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

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

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelets pivottabell är ursprungligen ett datafält (värdefält). Eftersom endast fält i rad- eller kolumnområdet kan grupperas anropar koden först `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` för att flytta `FieldTwo` till radområdet. Därefter uppdateras pivottabellen. Det numeriska fältet grupperas sedan i intervallen 0-1, 2-3 och 4-5 med hjälp av `StartNumber = 0`, `EndNumber = 5` och `Interval = 2`.

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

## **Obs**

{{% alert color="primary" %}}
- Metodöverlagringarna för `PivotField.GroupBy()` är föråldrade och har tagits bort ur API:et. `PivotField.Group()` och `PivotField.Group(PivotFieldGroupOptions)` ersätter dem.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel kvartal och månader) bredvid det ursprungliga fältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.Group()` samma beteende som Excel.
- Egenskapen `PivotFieldGroupOptions.Interval` får endast effekt vid numerisk gruppering och vid datumgruppering efter dagar (till exempel när datum grupperas i perioder på sju dagar); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Visa topp 10 eller filtrera i pivottabell](/cells/sv/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Visa värden som i pivottabell](/cells/sv/go-cpp/show-values-as-in-pivot-table/)
- [Formatera del av pivottabell](/cells/sv/go-cpp/format-part-of-pivot-table/)
- [Lägg till villkorsstyrd formatering i pivottabell](/cells/sv/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}
---
title: Top‑10‑Anzeige oder -Filter in Pivot‑Tabelle
linktitle: Top‑10‑Anzeige oder -Filter in Pivot‑Tabelle
description: Erfahren Sie, wie Sie nur die am höchsten‑ oder am niedrigsten bewerteten Elemente eines Pivot‑Felds in Aspose.Cells für Go über C++ anzeigen. Dieser Artikel behandelt die Excel‑97‑2003‑Methode Top10AutoShow, das Auslesen der Optionen mit Top10AutoShowSettings und den Excel‑2007‑365‑Top‑10‑Filter über FilterTop10.
keywords: Aspose.Cells, Go via C++, Pivot‑Tabelle, Top‑10, AutoShow, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /de/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld dutzende Mitglieder enthält. Ein Top‑10‑Bericht zeigt nur die am höchsten bzw. am niedrigsten bewerteten Elemente an, was genau das ist, was Ranglistenberichte benötigen – „Top 5‑Produkte nach Umsatz“ oder „unterste 3‑Regionen nach Verkaufsanzahl“. Aspose.Cells unterstützt dafür zwei Mechanismen, die zwei Generationen von Microsoft Excel entsprechen.
- **Excel 97‑2003 AutoShow** – die Methode `PivotField.Top10AutoShow()`. Dies ist die klassische Einstellung „Die obersten/untersten N Elemente anzeigen“, die direkt im Pivot‑Feld gespeichert wird. Sie funktioniert in jeder Excel‑Version, sowohl alt als auch neu, da sie Teil des ursprünglichen Pivot‑Tabellen‑Formats ist.
- **Excel 2007‑365 Top‑10‑Filter** – die Methode `PivotField.FilterTop10()`. Dies ist der moderne Top‑10‑Wertfilter, der im Feldmenü unter „Wertfilter“ zu finden ist. Er wird als an das Feld angehängtes `PivotFilter`‑Objekt gespeichert und ermöglicht eine Rangliste basierend auf Element‑Anzahl bzw. Prozentsatz.

## **Top‑10‑Anzeige in Excel 97‑2003 (Top10AutoShow)**
Das klassische AutoShow wird mit einem einzigen Aufruf von `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)` konfiguriert:
- `isAutoShow` — aktiviert oder deaktiviert die AutoShow‑Einstellung für das Feld.
- `isTop` — `true` behält die am höchsten bewerteten Elemente (Top) bei, `false` die am niedrigsten (Bottom).
- `count` — gibt an, wie viele Elemente behalten werden sollen, z. B. 10 für einen klassischen Top‑10‑Bericht.
- `rankBy` — der nullbasierte Index des **Datenfelds**, dessen Werte die Elemente ranken. Übergeben Sie -1, um die Elemente nach dem Feld selbst zu ranken.

### **Durch ein Werte‑Feld ranken**
Ranken Sie die Elemente des Zeilenfelds nach einem normalen Werte‑Feld wie Summe der Verkäufe. Das folgende Beispiel erstellt eine Pivot‑Tabelle mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die Top 2‑Sportarten nach Umsatz an. `rankBy` ist 0, weil „Summe der Verkäufe“ das Datenfeld mit Index 0 ist.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Durch das Feld selbst ranken**
Ein Feld kann auch nach sich selbst gerankt werden – übergeben Sie -1 an `rankBy`. Für diese Variante wird kein zusätzliches Datenfeld benötigt; das Feld muss lediglich im Zeilen‑ (oder Spalten‑) Bereich liegen. Das folgende Beispiel zeigt die untersten 3 Sportarten, die nach dem Feld selbst gerankt werden. Wenn diese Einstellung gespeichert wird, wird das Attribut `rankBy` aus dem Pivot‑Tabellen‑XML weggelassen, weil -1 der Standardwert des Formats ist, und `GetRankBy()` liest -1 zurück.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Aktuelle AutoShow‑Optionen lesen**
Die Methode `PivotField.GetTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`‑Objekt zurück, das die derzeit im Feld gespeicherten AutoShow‑Optionen offenlegt. Verwenden Sie es, um zu prüfen, wie eine vorhandene Arbeitsmappe oder eine gerade konfigurierte Pivot‑Tabelle ihre Elemente darstellt – einschließlich aus Datei geladener Arbeitsmappen.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

Die Einstellungen entsprechen den klassischen AutoShow‑Attributen, die in das Pivot‑Tabellen‑XML geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), sodass die zurückgelesenen Werte von allen Excel‑Versionen beachtet werden.

## **Hinweis**

{{% alert color="primary" %}}
- Nach dem Aufruf von `Top10AutoShow()` rufen Sie erneut `PivotTable.CalculateData()` auf – die Einstellungen werden erst beim nächsten Neuberechnen im gerenderten Layout wirksam.
- Die AutoShow‑Einstellungen funktionieren mit Zeilen‑ und Spaltenfeldern. Ein Feld, das ausschließlich im Seiten‑ (Filter‑) Bereich liegt, kann nicht auf diese Weise gerankt werden, da seine Elemente nicht im Pivot‑Körper angeordnet werden.
{{% /alert %}}

## **Excel 2007‑365: Top‑10‑Filter (FilterTop10)**
Moderne Excel‑Versionen stellen Top 10 als Wertfilter im Feldmenü (Wertfilter, Top 10…) bereit. Aspose.Cells modelliert dies mit der Methode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, die das erstellte `PivotFilter` zurückgibt:
- `valueFieldIndex` — der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Elemente ranken.
- `type` — gibt an, was `itemCount` bedeutet. `PivotFilterType.Count` behält eine feste Anzahl von Elementen (Option „Elemente“ im Dialog). `PivotFilterType.Percent` behält einen Prozentsatz der Elemente, sodass `itemCount` den Prozentsatz selbst darstellt – 30 behält die obersten 30 %. `PivotFilterType.Sum` rankiert nach kumulativer Werteabdeckung.
- `isTop` — `true` für Top, `false` für Bottom.
- `itemCount` — das N in Top N; seine Einheit hängt von `type` ab.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Die AutoShow‑Einstellungen und `FilterTop10` sind zwei separate Funktionen. AutoShow schreibt das klassische Attribut `autoShow` auf das Pivot‑Feld und wird von allen Excel‑Versionen bis zurück zu Excel 97 berücksichtigt. `FilterTop10` schreibt einen modernen `PivotFilter`‑Eintrag, der Excel 2007 oder neuer erfordert. Wird eine Arbeitsmappe in einer älteren Excel‑Version geöffnet, fällt eine Pivot‑Tabelle, die den modernen Filter verwendet, auf die Anzeige aller Elemente zurück. Für Dokumente, die über alte Werkzeuge weitergereicht werden müssen, bevorzugen Sie `Top10AutoShow`; für moderne Arbeitsmappen bevorzugen Sie `FilterTop10`, da es mit den anderen Wertfiltern kombinierbar ist.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot‑Felder in der Pivot‑Tabelle gruppieren](/cells/de/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}
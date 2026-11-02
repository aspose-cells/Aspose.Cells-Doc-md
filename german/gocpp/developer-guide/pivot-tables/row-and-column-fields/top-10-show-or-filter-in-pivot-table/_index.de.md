---
title: Top 10 in einer PivotTable anzeigen oder filtern
linktitle: Top 10 in einer PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie in Aspose.Cells for Go via C++ nur die am höchsten oder am niedrigsten rangierten Elemente eines Pivot-Felds anzeigen. Dieser Artikel behandelt die AutoShow-Einstellungen für Excel 97-2003 (SetIsAutoShow und verwandte Methoden), das Zurücklesen der Optionen und den Top-10-Filter für Excel 2007-365 über FilterTop10.
keywords: Aspose.Cells, Go via C++, PivotTable, Top 10, AutoShow, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /de/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwierig zu lesen sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die am höchsten oder am niedrigsten rangierten Elemente, was Ranking-Berichte genau benötigen – „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt zwei Mechanismen, die den beiden Generationen von Microsoft Excel entsprechen.
- **AutoShow für Excel 97-2003** – die vier Set-Methoden von `PivotField`: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` und `SetAutoShowField`. Dies ist die klassische Einstellung „Obere/Untere N Elemente anzeigen“, die direkt im Pivot-Feld gespeichert wird. Sie funktioniert in jeder Excel-Version, ob alt oder neu, da sie Bestandteil des ursprünglichen PivotTable-Formats ist.
- **Top-10-Filter für Excel 2007-365** – die Methode `PivotField.FilterTop10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter „Wertfiltern“ zu finden ist. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und bietet eine Rangfolge, die auf der Anzahl der Elemente oder einem Prozentsatz basiert.

## **Top 10 in Excel 97-2003 anzeigen (AutoShow)**
Die klassische AutoShow-Funktion wird mithilfe von vier Setter-Aufrufen für `PivotField` konfiguriert:
- `SetIsAutoShow(bool)` – aktiviert oder deaktiviert die AutoShow-Einstellung für das Feld.
- `SetIsAscendShow(bool)` – `false` behält die am höchsten rangierten Elemente bei („Oben“), `true` behält die am niedrigsten rangierten Elemente bei („Unten“).
- `SetAutoShowCount(int32)` – die Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `SetAutoShowField(int32)` – der nullbasierte Index des **Datenfelds**, dessen Werte für die Einordnung der Elemente maßgeblich sind. Übergeben Sie -1, um die Elemente nach dem Feld selbst einzuordnen.
Die Elemente können nach einem Wertfeld oder nach dem Feld selbst eingeordnet werden. Nachstehend werden zwei naheliegende Varianten vorgestellt.

### **Nach einem Wertfeld ordnen**
Ordnen Sie die Elemente des Zeilenfelds nach einem gewöhnlichen Wertfeld wie etwa „Summe von Sales“. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die beiden Sportarten mit dem höchsten Umsatz. `rankBy` ist 0, da „Summe von Sales“ das Datenfeld mit Index 0 ist.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Die besten 2 Elemente anzeigen, sortiert nach „Summe von Sales“ (Index des Datenfelds 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Nach dem Feld selbst ordnen**
Ein Feld kann auch nach sich selbst eingeordnet werden – übergeben Sie -1 an `SetAutoShowField`. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die drei am niedrigsten rangierten Sportarten. Wenn diese Einstellung gespeichert wird, wird das `rankBy`-Attribut aus dem XML der PivotTable ausgelassen, da -1 der Standardwert des Formats ist, und `GetAutoShowField()` liest -1 zurück.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Die unteren 3 Elemente anzeigen, die nach dem Feld selbst sortiert sind (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Aktuelle AutoShow-Optionen lesen**
Die Lesemethoden `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` und `GetAutoShowField()` von `PivotField` bieten Zugriff auf die aktuell im Feld gespeicherten AutoShow-Optionen. Verwenden Sie sie, um zu prüfen, wie die Elemente in einer vorhandenen Arbeitsmappe beziehungsweise einer gerade konfigurierten PivotTable dargestellt werden – auch in Arbeitsmappen, die aus einer Datei geladen wurden.

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
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

Die vier Optionen entsprechen den klassischen AutoShow-Attributen, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), sodass die zurückgelesenen Werte von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Rufen Sie nach dem Ändern einer der AutoShow-Set-Methoden erneut `PivotTable.CalculateData()` auf – die Einstellungen wirken sich erst bei der nächsten Neuberechnung auf das dargestellte Layout aus.
- Die AutoShow-Einstellungen funktionieren mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seitenbereich (Filterbereich) liegt, kann auf diese Weise nicht eingeordnet werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (FilterTop10)**
Moderne Excel-Versionen bieten Top 10 im Feldmenü als Wertfilter (Wertfilter, Top 10...) an. Aspose.Cells bildet diesen mit der Methode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte für die Einordnung der Elemente maßgeblich sind.
- `type` – legt fest, was `itemCount` bedeutet. `PivotFilterType.Count` behält eine feste Anzahl von Elementen bei (die Option „Elemente“ im Dialog). `PivotFilterType.Percent` behält einen Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist – 30 behält die oberen 30 Prozent bei. `PivotFilterType.Sum` ordnet die Elemente nach der kumulierten Wertabdeckung ein.
- `isTop` – `true` für „Oben“, `false` für „Unten“.
- `itemCount` – das N in „Top N“; die Einheit hängt von `type` ab.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top-10-Filter — die beiden besten Elemente anhand von "Sum of Sales" beibehalten (Datenfeldindex 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Für einen prozentualen Filter stattdessen die besten 30 % der Elemente beibehalten:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Die AutoShow-Einstellungen und `FilterTop10` sind zwei getrennte Features. AutoShow schreibt das klassische Attribut `autoShow` in das Pivot-Feld und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `FilterTop10` schreibt einen modernen `PivotFilter`-Eintrag, der nur von Excel 2007 oder höher unterstützt wird. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, zeigt eine PivotTable, die den modernen Filter verwendet, alle Elemente an. Für Dokumente, die mithilfe älterer Tools verarbeitet und wieder gespeichert werden müssen, sind die AutoShow-Set-Methoden vorzuziehen; für moderne Arbeitsmappen ist `FilterTop10` vorzuziehen, da es sich mit den anderen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}
---
title: Werte anzeigen als in Pivot-Tabelle
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Zeigt Pivot-Tabellendatenfeldwerte als Prozentsatz des Gesamtergebnisses, als Unterschied zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /de/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Eine Pivot-Tabelle aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel einen Prozentsatz des Gesamtergebnisses, eine laufende Summe, einen Unterschied zu einem ausgewählten Basiselement oder einen Rang – sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können.  
Typische Anwendungsfälle umfassen die Analyse des Anteils am Gesamtergebnis, einschließlich Prozentsätze einer Zeile, Spalte oder des Gesamtergebnisses; kumulative Berichte mithilfe einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element mittels Unterschied oder prozentualem Unterschied zu einem Basiselement; sowie das Rangordnen von Werten von klein nach groß oder umgekehrt.  
In Aspose.Cells for Go via C++ wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Der Accessor `PivotField.GetShowValuesSetting()` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen Methoden `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` und `SetBaseItemIndex` das Verhalten konfigurieren; die Komfortmethode `PivotField.ShowValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.GetDataFields()` erhalten.

## **Aufzählungsmitglieder der PivotFieldDataDisplayFormat-Enumeration**
Das Datenfeld behält seine Aggregatfunktion, wie Sum oder Count, während **Show Values As** nur die Darstellung des aggregierten Wertes verändert.  
Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Werte (siehe den letzten Abschnitt) wendet eine einmalige Komfortmethode dieselbe Konfiguration an:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die sekundäre Berechnung `PivotFieldDataDisplayFormat`, die angewendet werden soll. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der Pivot-Tabelle (z. B. der Index des Zeilenfelds, zu dem das Basiselement gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basiselement relativ zum aktuellen Element gewählt wird: `PivotItemPositionType.Previous`, `.Next` oder `.Custom`. | Nur für die drei Basis-Element-Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basiselements. | Nur wenn `baseItemPositionType` auf `Custom` gesetzt ist (der Index wählt das exakte Basiselement); bei `Previous` / `Next` und bei allen Nicht‑Basis‑Formaten ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Parameter des Basiselements |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Unterschied zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Wertes eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentualen Unterschied zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz des Gesamtergebnisses an. | — |
| `Index` | Zeigt den Wert mittels der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (bei verschachtelten Zeilenfeldern). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (bei verschachtelten Spaltenfeldern). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom Kleinsten (1) zum Größten. | — |
| `RankLargestToSmallest` | Rangiert den Wert vom Größten (1) zum Kleinsten. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Werte (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — die Methode und das Einstellungsobjekt sind zwei Wege, denselben Zustand zu konfigurieren, und spiegeln die Basis‑Feld‑ und Basis‑Element‑Auswähler im Excel‑Dialog **Show Values As** wider.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamtergebnisses anzeigen**
Rufen Sie die Methode `PivotField.ShowValuesAs` mit `PivotFieldDataDisplayFormat.PercentageOfTotal` auf, um jede Zelle des Datenfeldes, einschließlich des Gesamtergebnisses, in ihren Anteil am Gesamtergebnis zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format bezieht jeden Wert ausschließlich auf das Gesamtergebnis, sodass kein Basisfeld oder Basiselement erforderlich ist – die nachfolgenden Argumente (`0`, `PivotItemPositionType.Previous`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle angibt.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **Abrufen und Konfigurieren von PivotField.ShowValuesSetting**
Lesen Sie die aktuelle Konfiguration über `PivotField.GetShowValuesSetting()`: Der Accessor liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen vier Getter‑Methoden die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.ShowValuesAs` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Werte niemals einzeln setzen müssen.  
Das Objekt `PivotShowValuesSetting` stellt die vier Werte bereit, die `ShowValuesAs` schreibt:
- `GetCalculationType()` / `SetCalculationType()` wählt die sekundäre Berechnung `PivotFieldDataDisplayFormat` aus.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` gibt den nullbasierten Index des Basisfelds innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` bestimmt, wie das Basiselement relativ zum aktuellen Element positioniert ist, und akzeptiert `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` oder `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` gibt den nullbasierten Index des Basiselements an und wird verwendet, wenn der Positionstyp `Custom` ist.  
Nachdem Sie `ShowValuesAs` aufgerufen haben, führen Sie erneut `PivotTable.CalculateData()` aus, damit der Pivot‑Körper neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **Verwandte Artikel**
- [Pivot-Felder in der Pivot‑Tabelle gruppieren](/cells/de/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Top‑10-Anzeigen oder -Filter in Pivot‑Tabelle](/cells/de/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Slicer aktualisieren](/cells/de/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}
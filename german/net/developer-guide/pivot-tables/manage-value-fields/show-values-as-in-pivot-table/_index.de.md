---
title: Werte anzeigen als in PivotTable
linktitle: Werte anzeigen als in PivotTable
description: Zeigt Werte von PivotTable‑Datenfeldern als Prozentsatz der Gesamtsumme, als Unterschied zu einem Basiselement, als laufende Summe, als Rang und mehr mit Aspose.Cells for .NET.
keywords: Aspose.Cells, PivotTable, Werte anzeigen als, DataDisplayFormat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /de/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable aggregiert jedes Datenfeld normalerweise mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel einen Prozentsatz der Gesamtsumme, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder einen Rang – sodass Sie Vergleichsanalysen durchführen können, ohne Hilfsspalten oder berechnete Spalten zu verwenden. Typische Anwendungen umfassen die Analyse von Anteilen an der Gesamtsumme (Prozentsätze von Zeilen, Spalten oder Gesamtsumme), kumulative Berichte mittels einer laufenden Summe in einem Periodenfeld, Varianzanalyse gegenüber einem Benchmark‑Element mittels Differenz zu oder prozentualer Differenz zu einem Basiselement sowie die Rangfolge von Werten vom kleinsten zum größten oder umgekehrt. In Aspose.Cells for .NET wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.ShowValuesSetting` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen beschreibbare Eigenschaften `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` und `BaseItemIndex` das Verhalten konfigurieren; die Komfortmethode `PivotField.ShowValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das Sie über `PivotTable.DataFields` erhalten.

## **PivotFieldDataDisplayFormat Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion (z. B. Sum oder Count) bei, während **Show Values As** nur die Anzeige des aggregierten Wertes verändert. Zusätzlich zum direkten Setzen der `PivotShowValuesSetting`‑Eigenschaften (siehe letzter Abschnitt) kann die Ein‑Aufruf‑Methode dieselbe Konfiguration übernehmen:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die anzuwendende sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der PivotTable (z. B. der Index des Zeilenfeldes, dem das Basiselement zugeordnet ist). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basiselement relativ zum aktuellen Element gewählt wird: `PivotItemPositionType.Previous`, `.Next` oder `.Custom`. | Nur für die drei Basis-Element-Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basiselements. | Nur wenn `baseItemPositionType` auf `Custom` gesetzt ist (der Index wählt das exakte Basiselement); für `Previous` / `Next` und alle nicht‑Basis‑Formate zu übergeben mit `0`. |

| Berechnungstyp | Verhalten | Parameter des Basiselements |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Wertes eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur bei `Custom`) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfeldes an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `Index` | Zeigt den Wert anhand der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (bei verschachtelten Zeilenfeldern). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (bei verschachtelten Spaltenfeldern). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom kleinsten (1) zum größten. | — |
| `RankLargestToSmallest` | Rangiert den Wert vom größten (1) zum kleinsten. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Eigenschaften (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — die Methode und das Property‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren und spiegeln die Auswahl von Basisfeld und Basiselement im Dialog **Show Values As** von Excel wider.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.ShowValuesAs` mit `PivotFieldDataDisplayFormat.PercentageOfTotal` auf, um jede Zelle des Datenfeldes, inklusive der Gesamtsumme, in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen stellen somit Anteile am gesamten Ergebnis‑Datensatz dar. Dieses Format bezieht sich ausschließlich auf die Gesamtsumme, sodass kein Basisfeld oder Basiselement benötigt wird – die nachfolgenden Argumente (`0`, `PivotItemPositionType.Previous`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle angibt.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Abrufen und Konfigurieren von PivotField.ShowValuesSetting**
Lesen Sie die aktuelle Konfiguration über `PivotField.ShowValuesSetting`: Die schreibgeschützte Eigenschaft liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen vier Eigenschaften die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.ShowValuesAs` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln setzen müssen. Das `PivotShowValuesSetting`‑Objekt stellt die vier Eigenschaften bereit, die `ShowValuesAs` schreibt:
- `CalculationType` wählt die sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` gibt den nullbasierten Index des Basisfeldes innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `BaseItemPositionType` bestimmt, wie das Basiselement relativ zum aktuellen Element positioniert wird, und akzeptiert `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` oder `PivotItemPositionType.Custom`.
- `BaseItemIndex` gibt den nullbasierten Index des Basiselements an und wird verwendet, wenn `BaseItemPositionType` auf `Custom` gesetzt ist.
Nachdem Sie `ShowValuesAs` aufgerufen haben, rufen Sie erneut `PivotTable.CalculateData()` auf, damit der Pivot‑Körper mit der aktualisierten Konfiguration neu berechnet und gerendert wird.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in PivotTable](/cells/de/net/manage-value-fields/)
- [Arbeiten mit Anzeigeformaten von Datenfeldern in PivotTable](/cells/de/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Aktualisieren von PivotTable](/cells/de/net/refresh-pivot-table/)
- [Stil auf PivotTable anwenden](/cells/de/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
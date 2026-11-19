---
title: „Werte anzeigen als“ in PivotTable
linktitle: „Werte anzeigen als“ in PivotTable
description: Datenfeldwerte in PivotTables mit Aspose.Cells for .Net als Prozent der Gesamtsumme, als Differenz zu einem Basiselement, als laufende Summe, als Rang und vieles mehr anzeigen.
keywords: Aspose.Cells, PivotTable, Werte anzeigen als, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /de/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Funktion **Werte anzeigen als** in Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus diesem Aggregat abgeleitet wird – zum Beispiel einen Prozentsatz der Gesamtsumme, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder einen Rang –, sodass Sie vergleichende Analysen ohne Hilfsformeln oder berechnete Spalten durchführen können.
Typische Anwendungen sind die Analyse der Anteile an der Gesamtsumme, einschließlich von Prozentsätzen im Verhältnis zur Zeilen-, Spalten- oder Gesamtsumme; kumulierte Berichte unter Verwendung einer laufenden Summe in einem Periodenfeld; die Varianzanalyse mit einem Basiselement als Referenz, wobei die Differenz oder die prozentuale Differenz verwendet wird; sowie die Rangfolge der Werte vom kleinsten zum größten oder vom größten zum kleinsten.
In Aspose.Cells for .Net wählt die Enumeration `PivotShowValuesAsType` die sekundäre Berechnung aus. Die schreibgeschützte Eigenschaft `PivotField.ShowValuesSetting` gibt ein `PivotShowValuesSetting`-Objekt zurück, dessen schreibbaren Eigenschaften `ShowValuesAs`, `BaseFieldIndex` und `BaseItemIndex` das Verhalten konfigurieren; die Komfortmethode `PivotField.ShowValuesAs(...)` wendet dieselben Einstellungen mit einem einzigen Aufruf an. Wenden Sie diese Einstellungen auf ein Daten- oder Wertfeld an, das Sie aus `PivotTable.DataFields` erhalten haben.

## **Mitglieder der Enumeration PivotShowValuesAsType**
Das Datenfeld behält seine Aggregatfunktion, etwa Sum oder Count, während „Werte anzeigen als“ ausschließlich die Anzeige des aggregierten Werts verändert.
Zusätzlich zum direkten Schreiben der `PivotShowValuesSetting`-Eigenschaften (siehe letzter Abschnitt) bietet eine Komfortmethode mit einem einzigen Aufruf dieselbe Konfiguration. Sie ist in zwei Überladungen verfügbar – eine übergibt Basisfeld und Basiselement anhand des Index, die andere anhand des Namen:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Parameter | Bedeutung | Wann er erforderlich ist |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds innerhalb der Basisfelder der PivotTable (zum Beispiel der Index des Zeilenfelds, zu dem das Basiselement gehört) oder – in der String-Überladung – der Name des Basisfelds. | Erforderlich für die acht basisbezogenen Formate unten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); für alle anderen Formate ist `0` (oder `null` in der String-Überladung) zu übergeben. |
| `baseItem` | Nullbasierter Index des Basiselements sowie zwei Sentinel-Werte: `PivotShowValuesSetting.PreviousPivotItem` (-1) wählt das vorhergehende Element und `PivotShowValuesSetting.NextPivotItem` (-2) das nachfolgende aus. Die String-Überladung verwendet stattdessen die Beschriftung des Basiselements und `null`, wenn das gewählte Format kein Basiselement benötigt. | Nur die drei basiselementbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) berücksichtigen das Basiselement; die fünf feldbezogenen Formate (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` sowie beide Rangformate) ignorieren es – übergeben Sie `0` oder `null`. |

| Berechnungstyp | Verhalten | Basiselementparameter |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zu einem Basiselement in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der vorherige/nächste Sentinel-Wert) |
| `PercentageOf` | Zeigt den Wert als Prozent des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der vorherige/nächste Sentinel-Wert) |
| `PercentageDifferenceFrom` | Zeigt die prozentuale Differenz zwischen dem Wert und dem Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der vorherige/nächste Sentinel-Wert) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozent der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozent der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozent der Gesamtsumme an. | — |
| `Index` | Zeigt den Wert mit der Excel-Indexformel an ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)). | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozent der Summe der übergeordneten Zeile an (bei verschachtelten Zeilenfeldern). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozent der Summe der übergeordneten Spalte an (bei verschachtelten Spaltenfeldern). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozent der Summe des übergeordneten Elements an. | `baseField` (das übergeordnete Feld, dessen Summe als Referenz dient) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozent einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Weist dem Wert den Rang vom kleinsten (1) bis zum größten zu. | `baseField` (das Feld, dessen Elemente den Umfang der Rangfolge definieren) |
| `RankLargestToSmallest` | Weist dem Wert den Rang vom größten (1) bis zum kleinsten zu. | `baseField` (das Feld, dessen Elemente den Umfang der Rangfolge definieren) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` schreibt den Zustand des `PivotShowValuesSetting`-Objekts (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`) – die Methode und das Eigenschaftsobjekt stellen zwei Möglichkeiten dar, denselben Zustand zu konfigurieren, analog zu den Feldern zur Auswahl von Basisfeld und Basiselement im Excel-Dialog „Werte anzeigen als“.
{{% /alert %}}

## **Werte als Prozent der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.ShowValuesAs` mit `PivotShowValuesAsType.PercentageOfTotal` auf, um jede Zelle des Datenfelds – einschließlich der Gesamtsumme – in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen werden somit als Anteile an der gesamten Ergebnismenge dargestellt. Dieses Format bezieht jeden Wert ausschließlich auf die Gesamtsumme und benötigt daher weder ein Basisfeld noch ein Basiselement – die abschließenden Argumente (`0`, `0`) sind Platzhalter, die von diesem Format ignoriert werden, wie oben in der Parametertabelle vermerkt.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.ShowValuesSetting abrufen und konfigurieren**
Lesen Sie die aktuelle Konfiguration über `PivotField.ShowValuesSetting` aus: Die schreibgeschützte Eigenschaft gibt das `PivotShowValuesSetting`-Objekt des Felds zurück, dessen Eigenschaften die aktive Berechnung „Werte anzeigen als“ beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.ShowValuesAs` auf – sie schreibt alle Einstellungen mit einem einzigen Aufruf, sodass Sie die Eigenschaften nicht einzeln zuweisen müssen.
Die folgenden Eigenschaften bilden den von `ShowValuesAs` geschriebenen Zustand ab:
- `ShowValuesAs` wählt die sekundäre Berechnung `PivotShowValuesAsType` aus.
- `BaseFieldIndex` gibt den nullbasierten Index des Basisfelds innerhalb der PivotTable-Felder an. Er wird von den basisbezogenen Formaten verwendet.
- `BaseItemIndex` gibt das Basiselement an: einen nullbasierten Index eines bestimmten Pivot-Elements oder einen der beiden Sentinel-Werte – `PivotShowValuesSetting.PreviousPivotItem` (-1) für das vorhergehende Element, `PivotShowValuesSetting.NextPivotItem` (-2) für das nachfolgende. Dieser Wert wird von den basiselementbezogenen Formaten verwendet.
- `BaseFieldName` und `BaseItemCaption` sind schreibgeschützte Eigenschaften, die den aufgelösten Namen des Basisfelds beziehungsweise die Beschriftung des Basiselements zurückgeben; nachdem der Sentinel-Wert für das vorherige Element ausgewählt wurde, gibt `BaseItemCaption` beispielsweise `(previous)` zurück.
Rufen Sie nach dem Aufruf von `ShowValuesAs` erneut `PivotTable.CalculateData()` auf, damit der Datenbereich der PivotTable mit der aktualisierten Konfiguration neu berechnet und neu gerendert wird.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Wertfelder in einer PivotTable verwalten](/cells/de/net/manage-value-fields/)
- [Arbeiten mit Anzeigeformaten von DataField in einer PivotTable](/cells/de/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Eine PivotTable aktualisieren](/cells/de/net/refresh-pivot-table/)
- [Einen Stil auf eine PivotTable anwenden](/cells/de/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
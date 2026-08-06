---
title: Seitenfeldlayout in Pivot-Tabelle ändern
linktitle: Seitenfeldlayout in Pivot-Tabelle ändern
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET das Layout des Seitenfeldbereichs in einer Pivot-Tabelle steuern können, einschließlich der Einstellung der Anzeigereihenfolge, der Umbruchanzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Seitenfeldreihenfolge, Seitenfeldumbruchanzahl, Seitenfeld verschieben
type: docs
weight: 191
url: /de/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs — den Streifen mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle — steuern können, einschließlich Anzeigereihenfolge, Umbruchanzahl und Neuanordnung der Felder.

{{% /alert %}}

## **Einführung**

Eine Pivot-Tabelle in Microsoft Excel bietet einen dedizierten **Seitenfeldbereich**, der oberhalb des Zeilen-/Spalten-/Datenkörpers der Tabelle liegt. Dieser Bereich wird als Streifen mit Dropdown-Filtersteuerelementen dargestellt (eines pro Seitenfeld) und wird von Endbenutzern angeklickt, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region aufzuteilen. Aspose.Cells modelliert diesen Bereich über die Sammlung `PivotTable.PageFields` und stellt drei Eigenschaften bereit, die steuern, wie der Streifen visuell angeordnet wird:

- `PivotTable.PageFieldOrder` (ein Wert vom Typ `Aspose.Cells.PrintOrderType`) legt fest, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* davon platziert werden.
- `PivotTable.PageFieldWrapCount` legt fest, wie viele Seitenfelder pro Zeile oder Spalte platziert werden, bevor ein Umbruch erfolgt.
- `PivotTable.PageFields.Move(currIndex, destIndex)` ordnet die Seitenfelder neu, ohne den Anordnungsmodus zu ändern.

Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, sodass Sie die resultierenden Layouts direkt vergleichen können.

## **Quelldaten**

Alle drei folgenden Beispiele laden diese acht Zeilen Verkaufsdaten in ein Arbeitsblatt namens `PivotData`. Die Daten enthalten zwei Seitenfeldkandidaten (`Year`, `Region`), einen Zeilenfeldkandidaten (`Fruit`) und ein Maß (`Amount`), wodurch die Prüfung des Seitenfeldstreifens aussagekräftig wird.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Alle acht Zeilen werden in jedem Codebeispiel in identischer Reihenfolge gefüllt, sodass die Quelldaten zwischen den Szenarien nie abweichen — nur die Layout-Eigenschaften des Seitenfelds unterscheiden sich.

## **Beispiel 1: Über dann abwärts**

Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzigen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, platzieren `Year` zuerst und `Region` an zweiter Stelle auf der Seitenachse (die Reihenfolge der `AddFieldToArea`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen dann `PageFieldOrder` auf `PrintOrderType.OverThenDown` mit `PageFieldWrapCount = 2`. Mit `OverThenDown` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzigen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass der Streifen eine Zeile mit Breite zwei einnimmt.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// Kopfzeilen (Zeile 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Zeile 1: Apfel, 2022, Nord, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Zeile 2: Apfel, 2023, Nord, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Zeile 3: Banane, 2022, Süd, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Zeile 4: Banane, 2023, Süd, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Zeile 5: Kirsche, 2022, Ost, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Zeile 6: Kirsche, 2023, Ost, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Zeile 7: Traube, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Zeile 8: Traube, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// PivotTableReport-Blatt hinzufügen
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Pivot-Tabelle erstellen, die aus PivotData!A1:D9 stammt und bei A1 auf PivotTableReport platziert wird
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Felder hinzufügen
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Frucht
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Jahr
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Region
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Betrag
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Aktualisieren und berechnen
pivotTable.CalculateData();

// Speichern
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Beispiel 2: Abwärts dann über**

In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (mit `Year` zuerst) und `Amount` (Summe) als Datenfeld — genau wie in Beispiel 1. Anschließend setzen wir `PageFieldOrder` auf `PrintOrderType.DownThenOver` und `PageFieldWrapCount` auf `2`. Mit `DownThenOver` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt — `Year` oben, `Region` direkt darunter — und bilden eine einzige Spalte am oberen Rand der Pivot-Tabelle. Der Streifen nimmt daher zwei Zeilen mit Breite eins ein, im Gegensatz zu Beispiel 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Beispiel 3: Ein Seitenfeld verschieben**

Im dritten Szenario behalten wir diesen Datensatz und diese Feldzuordnung bei, legen ein neutrales Layout fest (`OverThenDown` mit Umbruchanzahl `2`) und demonstrieren dann die Operation `PageFields.Move`. Der Aufruf `Move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) an Position 1, und das Seitenfeld, das sich an Position 1 befand (`Region`), rückt an Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Umbruch und Anordnungsmodus bleiben unverändert, sodass der Streifen weiterhin horizontal nebeneinander dargestellt wird — nur die Reihenfolge der beiden Dropdowns wurde vertauscht.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Verwandte Artikel**

- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/net/add-page-field-in-pivot-table/) — die übergeordnete Seite, die einführt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabellen](/cells/de/net/pivot-table-add-row-and-column-fields/) — behandelt die Zuweisung von Feldern zu den Zeilen- und Spaltenachsen und ergänzt die hier gezeigte Arbeit an der Seitenachse.
- [Wertfelder in Pivot-Tabellen verwalten](/cells/de/net/manage-value-fields/) — beschreibt, wie der Daten- (Wert-) Bereich konfiguriert wird, einschließlich der in diesem Artikel verwendeten `Sum`-Aggregation.
- [Pivot-Tabelle aktualisieren](/cells/de/net/refresh-pivot-table/) — erläutert `RefreshData` und `CalculateData`, die nach der Neuanordnung von Seitenfeldern erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/net/apply-style-to-pivot-table/) — zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem der Seitenfeldstreifen angeordnet wurde.

{{< app/cells/assistant language="csharp" >}}
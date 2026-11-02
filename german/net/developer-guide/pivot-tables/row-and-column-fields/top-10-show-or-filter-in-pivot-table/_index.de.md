---
title: Top 10 in einer PivotTable anzeigen oder filtern
linktitle: Top 10 in einer PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie in Aspose.Cells for .Net nur die am höchsten oder am niedrigsten rangierten Elemente eines Pivot-Felds in einer PivotTable anzeigen. Dieser Artikel behandelt die Methode Top10AutoShow in Excel 97-2003, das Lesen von Optionen mit Top10AutoShowSettings sowie den Top 10-Filter in Excel 2007-365 über FilterTop10.
keywords: Aspose.Cells, .NET, PivotTable, Top 10, automatische Anzeige, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /de/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die sämtliche Elemente eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die am höchsten oder am niedrigsten rangierten Elemente bei und erfüllt damit genau die Anforderungen von Berichten mit Rangfolge – „Top 5-Produkte nach Umsatz“ oder „Bottom 3-Regionen nach Verkaufsanzahl“. Aspose.Cells unterstützt zwei Mechanismen dafür, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** — die Methode `PivotField.Top10AutoShow()`. Dies ist die klassische Einstellung „Oben-/Unten-N-Elemente anzeigen“, die direkt im Pivot-Feld gespeichert wird. Sie funktioniert in allen Excel-Versionen, ob alten oder neuen, da sie Teil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top 10-Filter** — die Methode `PivotField.FilterTop10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter der Kategorie „Wertfilter“ zu finden ist. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und bietet Filteroptionen auf Basis der Elementanzahl und des Prozentsatzes.

## **Top 10 in Excel 97-2003 anzeigen (Top10AutoShow)**
Das klassische AutoShow wird mit einem einzigen Aufruf von `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)` konfiguriert:
- `isAutoShow` — aktiviert oder deaktiviert die AutoShow-Einstellung für das Feld.
- `isTop` — `true` behält die am höchsten rangierten Elemente (Oben) bei, `false` die am niedrigsten rangierten (Unten).
- `count` — Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` — nullbasierter Index des **Datenfelds**, nach dessen Werten die Elemente rangiert werden. Übergeben Sie -1, um die Elemente nach dem Feld selbst zu rangieren.
Die Rangfolge kann durch ein Wertfeld oder durch das Feld selbst bestimmt werden. Zwei naheliegende Varianten werden im Folgenden gezeigt.

### **Nach einem Wertfeld rangieren**
Rangieren Sie die Elemente des Zeilenfelds nach einem herkömmlichen Wertfeld wie „Sum of Sales“. Im folgenden Beispiel wird eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) erstellt und anschließend werden die zwei Sportarten mit dem höchsten Umsatz angezeigt. `rankBy` ist 0, da „Sum of Sales“ das Datenfeld mit dem Index 0 ist.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Die Top-2-Elemente nach "Sum of Sales" anzeigen (Index des Datenfelds 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Nach dem Feld selbst rangieren**
Ein Feld kann auch nach sich selbst rangiert werden – übergeben Sie -1 als `rankBy`. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die untersten drei Sportarten, wobei das Feld selbst als Rangmaßstab dient. Wenn diese Einstellung gespeichert wird, wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `Top10AutoShowSettings.RankBy` gibt in diesem Fall -1 zurück.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Die unteren 3 Elemente anzeigen, die nach dem Feld selbst sortiert sind (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Die Eigenschaft `PivotField.Top10AutoShowSettings` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die aktuell im Feld gespeicherten AutoShow-Optionen offenlegt. Verwenden Sie es, um zu prüfen, wie die Elemente einer bestehenden Arbeitsmappe oder einer soeben konfigurierten PivotTable dargestellt werden – auch in aus Dateien geladenen Arbeitsmappen.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Die vier Eigenschaften entsprechen den klassischen AutoShow-Attributen, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Daher entsprechen die zurückgelesenen Werte den Werten, die jede Excel-Version berücksichtigt.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten `PivotField`-Eigenschaften `IsAutoShow`, `IsAscendShow`, `AutoShowCount` und `AutoShowField` sind als veraltet markiert. Verwenden Sie stattdessen das `Top10AutoShowSettings`-Objekt: `IsAutoShow` wird zu `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` wird zu `Top10AutoShowSettings.IsTop`, `AutoShowCount` wird zu `Top10AutoShowSettings.AutoShowCount` und `AutoShowField` wird zu `Top10AutoShowSettings.RankBy`. Die Methode `Top10AutoShow()` selbst ist der unterstützte Weg, um die Einstellungen zu ändern.
- `Top10AutoShow` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seitenbereich (Filterbereich) liegt, kann auf diese Weise nicht rangiert werden, da seine Elemente nicht im PivotTable-Bereich angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top 10-Filter (FilterTop10)**
Im Feldmenü moderner Excel-Versionen wird Top 10 als Wertfilter angeboten (Wertfilter, Top 10 ...). Aspose.Cells bildet diesen Filter mit der Methode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` — nullbasierter Index des Datenfelds, dessen aggregierte Werte für die Rangfolge der Elemente maßgeblich sind.
- `type` — bestimmt, was `itemCount` bedeutet. `PivotFilterType.Count` behält eine feste Anzahl von Elementen bei (Option „Elemente“ im Dialogfeld). `PivotFilterType.Percent` behält einen bestimmten Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist – 30 behält die obersten 30 Prozent. `PivotFilterType.Sum` bestimmt die Rangfolge anhand der kumulierten Abdeckung der Werte.
- `isTop` — `true` für Oben, `false` für Unten.
- `itemCount` — die Anzahl N in „Top N“; die Einheit hängt von `type` ab.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Top-10-Filter — die beiden besten Elemente nach "Sum of Sales" beibehalten (Datenfeldindex 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// Für einen prozentualen Filter stattdessen die besten 30 Prozent der Elemente beibehalten:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` und `FilterTop10` sind zwei getrennte Funktionen. AutoShow schreibt den klassischen Attributsatz mit `autoShow` in das Pivot-Feld und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `FilterTop10` schreibt einen modernen `PivotFilter`-Eintrag, der Excel 2007 oder höher erfordert. Beim Öffnen einer Arbeitsmappe in einer älteren Excel-Version zeigt eine PivotTable, die den modernen Filter verwendet, alle Elemente an. Für Dokumente, die durch Legacy-Tools verarbeitet und erneut gespeichert werden müssen, ist `Top10AutoShow` vorzuziehen; für moderne Arbeitsmappen ist `FilterTop10` vorzuziehen, da dieser Filter mit den anderen Wertfiltern kombiniert werden kann.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/net/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/net/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/net/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
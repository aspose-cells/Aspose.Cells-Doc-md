---
title: Formatteil einer Pivot‑Tabelle
linktitle: Formatteil einer Pivot‑Tabelle
description: Formatieren Sie einen Teil einer Pivot‑Tabelle in Aspose.Cells for .NET, indem Sie Stile auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke mittels PivotTable.Format anwenden, die Formate werden in PivotTable.PivotFormats gespeichert und bleiben erhalten, wenn die Pivot‑Tabelle aktualisiert wird.
keywords: Aspose.Cells, Pivot‑Tabelle, Format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /de/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.FormatAll` wendet einen einzigen Stil auf die gesamte Pivot‑Tabelle an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.  
In der Praxis muss lediglich ein Teil einer Pivot‑Tabelle hervorgehoben werden. Gängige Ziele sind die Beschriftungen eines Zeilenfeldes, die durch ein Feld erzeugten Wertzellen, die Gesamtsummenzeile oder ein beliebiges Rechteck wie die ersten beiden Elementzeilen.  
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer Pivot‑Tabelle ist nicht gleichbedeutend. Excel speichert Pivot‑Tabellen‑Formatierung als semantische `PivotArea`‑Regionen anstatt als normale Zell‑Stil‑Einträge. Ein Pivot‑Area‑Format bleibt einer Region wie den Beschriftungen eines Feldes oder Datenwerten zugeordnet und wird erneut aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil gehört zu dieser Zellposition und wird vom Pivot‑Modell nicht verfolgt.  
Aspose.Cells stellt die gesamte Überladungsfamilie `PivotTable.Format` bereit, sodass beide Arten von Formatierungen verfügbar sind:
- `Format(PivotArea, Style)` verankert einen Stil in einer semantischen Region, die mit `PivotArea.Select` oder `PivotArea.SelectField` aufgebaut wird.
- `Format(CellArea, Style)` verankert einen Stil in einem Arbeitsblatt‑Rechteck innerhalb der Pivot‑Tabelle.
- `Format(int row, int column, Style)` richtet sich an eine einzelne Zelle.
- `FormatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Pivot‑Bereich formatieren**
Der semantische Arbeitsablauf ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Berichtsteil folgen muss.
1. Erstellen Sie ein `PivotArea` mit `new PivotArea(pivotTable)`. Das Objekt beschreibt eine semantische Region, die zu dieser spezifischen Pivot‑Tabelle gehört.
2. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer angegebenen Achse mit `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LabelOnly` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DataOnly` wählt nur die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld anhand seines Namens mit `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Wenn ein Zeilenfeld nach Namen ausgewählt wird, löst sich die Region zu den Werte‑Zellen, die von den Elementen dieses Feldes erzeugt werden.
4. Erstellen Sie ein `Style` mit `Workbook.CreateStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und ein einfarbiges Hintergrundmuster und übergeben Sie den Stil an `PivotTable.Format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.PivotFormats` hinzu.
6. Feldgeankerte Formate werden angewendet, wenn die Pivot‑Daten berechnet werden. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.CalculateData()` auf, damit die Stile sichtbar werden.  
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.Select` und `PivotTableSelectionType.LabelOnly`, formatiert die von demselben Zeilenfeld erzeugten Werte‑Zellen mit `PivotArea.SelectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Zellbereich der Pivot‑Tabelle formatieren**
Verwenden Sie `PivotTable.Format(CellArea, Style)`, wenn die interessierende Region ein einfaches Arbeitsblatt‑Rechteck und keine semantische Pivot‑Region ist.  
`CellArea` wird durch die Eigenschaften `StartRow`, `StartColumn`, `EndRow` und `EndColumn` beschrieben. Die Werte sind nullbasierte Arbeitsblatt‑Koordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur End‑Position (einschließlich) abdeckt.  
Im Gegensatz zu einem feldgeankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `CalculateData()` ist nicht erforderlich, damit der Stil erscheint.  
Ein `CellArea`‑Rechteck kann sowohl Beschriftungszellen als auch Werte‑Zellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.  
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe, ohne eine weitere Neuberechnung durchzuführen.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Wie Pivot‑Bereiche und Zellbereiche zugeordnet werden**
Excel speichert Pivot‑Tabellen‑Formatierungen als `pivotArea`‑Datensätze und nicht als gewöhnliche Arbeitsblatt‑Zellstil‑Datensätze. Dasselbe Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanforderung beim Aufzeichnen in Pivot‑Bereiche übersetzt wird.  
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Bereichen ist in beiden Richtungen viele‑zu‑viele.  
- Ein `CellArea` kann mehrere Pivot‑Bereiche erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Werte‑Zellen umfasst, wird es in separate Beschriftungs‑ und Daten‑Regeln aufgeteilt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig voneinander behandelt.  
- Ein Pivot‑Bereich kann sich in mehrere disjunkte `CellArea`‑Instanzen auflösen. Eine semantische Region wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb gibt `PivotArea.GetCellAreas()` eine Sammlung statt eines einzelnen Rechtecks zurück.  
Jede über `PivotTable.Format` durchgeführte Formatierungsoperation wird in `PivotTable.PivotFormats` protokolliert. Jeder `PivotTableFormat`‑Eintrag enthält das zugehörige `PivotArea` und den darauf angewendeten `Style`. Die `PivotArea`‑Überladung fügt pro Aufruf genau einen Eintrag hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.  
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `OnlyLabel` und `OnlyData` bereit. Das nachstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `PivotTable.PivotFormats` und gibt die `CellArea`‑Koordinaten aus, zu denen jeder gespeicherte Pivot‑Bereich aufgelöst wird.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Da die Formate als Pivot‑Bereiche und nicht als gewöhnliche Zellstile gespeichert werden, überstehen sie eine Neuberechnung und Aktualisierung. Wenn die Pivot‑Tabelle mit `PivotTable.RefreshData` aktualisiert, mit `CalculateData` neu berechnet oder gespeichert und erneut geladen wird, löst sich jeder gespeicherte Pivot‑Bereich erneut zu seiner aktuellen Position auf und sein Stil wird erneut angewendet.
{{% /alert %}}

Verwenden Sie ein `PivotArea`, das mit `Select` oder `SelectField` erstellt wurde, wenn eine Hervorhebung über Aktualisierungen hinweg an ein Feld oder eine semantische Region gebunden bleiben muss, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreichend ist. Die Einzelzellen‑Überladung `Format(int row, int column, Style)` richtet sich an eine einzelne Zelle. Nutzen Sie `FormatAll`, das auf der übergeordneten Seite erläutert wird, wenn die gesamte Pivot‑Tabelle auf einmal neu gestaltet werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Pivot‑Tabellen‑Zeilen‑ und‑Spaltenfelder hinzufügen](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [Wertfelder in Pivot‑Tabelle verwalten](/cells/de/net/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
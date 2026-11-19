---
title: Sparklines in Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells ist eine .NET-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt — Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Spalten- und Gewinn/Verlust‑Sparklines mit der Aspose.Cells‑Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, .NET Bibliothek, Tabellenkalkulation, Sparklines, Linien‑Sparkline, Spalten‑Sparkline, Gewinn/Verlust‑Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten‑ und Gewinn/Verlust‑Sparklines, und jede kann hinsichtlich Farbe, Linienstärke, Hoch‑/Tieppunkte und Markierungen angepasst werden.
{{% /alert %}}

## **Einführung**
Sparklines sind winzige Diagramme in einer Zelle, die nützlich sind, wenn Sie einen schnellen Trend neben einer Zeile oder Spalte von Daten anzeigen möchten, ohne den Platz eines vollständigen Diagramms zu belegen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Spalte** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Möglichkeit über die APIs `SparklineGroup` und `SparklineGroupCollection` im Namespace `Aspose.Cells.Charts` wider.  
In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, über `worksheet.SparklineGroups.Add(...)` erstellt, welche ein `SparklineGroup`‑Objekt zurückgibt. Mit diesem Objekt können Sie den Sparkline‑Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch‑/Tieppunkt‑Indikatoren festlegen.  
Dieser Artikel führt durch die drei von Aspose.Cells unterstützten Sparkline‑Typen — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien‑Sparklines**
Eine Linien‑Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist daher die natürlichste Wahl, um Trends im Zeitverlauf darzustellen. In Aspose.Cells wird eine Linien‑Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.Add` übergeben wird.
1. Erstellen Sie eine neue `Workbook`‑Instanz und greifen Sie auf das erste Arbeitsblatt zu.  
2. Befüllen Sie eine Zeile mit Quelldaten (z. B. Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.  
3. Erstellen Sie ein `CellArea`, das die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.  
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — signalisiert Aspose.Cells, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.  
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien‑Sparkline können Sie die Linienfarbe über `group.Line.Color` festlegen (erwartet ein `CellsColor` aus `Aspose.Cells.Drawing`), die Linienstärke anpassen und Hoch‑/Tieppunkt‑Markierungen ein‑/ausschalten.  
6. Speichern Sie die Arbeitsmappe.  
Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt in Zelle F1 eine Linien‑Sparkline ein, die diese Werte nachzeichnet. Zusätzlich wird die Linienfarbe auf Rot gesetzt und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Spalten‑Sparklines**
Eine Spalten‑Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Damit eignet sie sich gut für Daten, bei denen die Größe eine Bedeutung hat — beispielsweise monatliche Verkaufszahlen oder Zählwerte. In Aspose.Cells erstellen Sie eine Spalten‑Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.Add` übergeben.
Der Vorgang entspricht dem Linien‑Sparkline‑Beispiel:
1. Erstellen Sie eine neue `Workbook`‑Instanz und greifen Sie auf das erste Arbeitsblatt zu.  
2. Befüllen Sie eine Zeile mit Quelldaten (z. B. Zeile 1, Spalten A bis E) mit den gewünschten Werten.  
3. Erstellen Sie ein `CellArea`, das die Zielzelle beschreibt.  
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` auf.  
5. Passen Sie optional die resultierende `SparklineGroup` an — beispielsweise indem Sie `group.Type` setzen, um den Typ zu bestätigen, oder die Balkenfarbe anpassen.  
6. Speichern Sie die Arbeitsmappe unter einer separaten Ausgabedatei, damit sie das Beispiel mit der Linien‑Sparkline nicht überschreibt.
Das untenstehende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und erzeugt eine Spalten‑Sparkline in F1. Negative Werte werden als nach unten gerichtete Balken dargestellt, positive Werte als nach oben gerichtete Balken, wodurch positive und negative Beiträge auf einen Blick leicht erkennbar sind.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Gewinn/Verlust‑Sparklines**
Eine Gewinn/Verlust‑Sparkline ist eine spezielle Variante der Spalten‑Sparkline, die nur zwei Ergebnisse darstellt: Ein positiver Wert wird als „Aufwärts‑“Balken (ein Gewinn) und ein null‑ oder negativer Wert als „Abwärts‑“Balken (ein Verlust) gezeichnet. Gewinn/Verlust‑Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehen‑/Durchfallen‑Ergebnisse oder beliebige binäre Ergebnisse im Zeitverlauf zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust‑Sparkline erzeugt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.Add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum‑Wert, der das Gewinn/Verlust‑Rendering anfordert.)
1. Erstellen Sie eine neue `Workbook`‑Instanz und greifen Sie auf das erste Arbeitsblatt zu.  
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust‑Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Wertes unerheblich — nur das Vorzeichen zählt. Positive Werte werden zu Aufwärts‑Balken, nicht‑positive Werte zu Abwärts‑Balken.  
3. Erstellen Sie ein `CellArea`, das die Zielzelle beschreibt.  
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` auf.  
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, z. B. indem Sie Akzentfarben für die Gewinn‑ und Verlust‑Balken festlegen.  
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele gleichzeitig auf dem Datenträger vorhanden sein können.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Kombinieren aller drei Sparkline‑Typen**
Das kombinierte Beispiel unten erstellt eine einzige Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt anschließend drei Sparkline‑Gruppen in den Zellen F1, F2 und F3 ein — jeweils einen der drei Typen — sodass die resultierende Datei alle drei Sparkline‑Stile gleichzeitig demonstriert.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **Anpassen des Sparkline‑Aussehens**
Sobald ein `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie vor dem Speichern der Arbeitsmappe mehrere seiner visuellen Eigenschaften auslesen oder ändern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.Type`** — der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe gesetzt, kann aber zum Bestätigen wieder ausgelesen werden.  
- **`group.Line.Color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.CreateCellsColor()`. Diese Eigenschaft wird für die Strichfarbe einer Linien‑Sparkline verwendet.  
- **`group.Line.Weight`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.  
- **Hoch‑/Tieppunkt‑Markierungen** — Schalter, die kleine Markierungen an den höchsten bzw. niedrigsten Datenpunkten aktivieren, um Extreme zu betonen.  
- **Erste/Letzte/Negative‑Punkt‑Markierungen** — Schalter, die Markierungen am ersten, letzten und negativen Datenpunkt ein‑ bzw. ausschalten.  
Um eine Farbe zu ändern, erstellen Sie stets eine `CellsColor`‑Instanz und weisen Sie sie der relevanten Eigenschaft zu. Weisen Sie nicht direkt ein `System.Drawing.Color` einer Sparkline‑Farbeigenschaft zu — diese erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `SparklineGroups.Add` selbst gibt ein voll typisiertes `SparklineGroup`‑Objekt zurück, sodass Sie Eigenschaftszuweisungen an den Rückgabewert anhängen oder das Objekt in einer lokalen Variable speichern und vor dem Speichern anpassen können.

## Verwandte Artikel
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for .NET](/cells/de/net/convert-sparkline-to-image-and-html/)
- [Filterfelder zu einer Pivot‑Tabelle in Aspose.Cells for .NET hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf Pivot‑Tabellen in Aspose.Cells for .NET anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Seitenfeldlayout in Pivot‑Tabelle ändern](/cells/de/net/change-page-field-layout/)
- [Excel in OFD-Format konvertieren](/cells/de/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}
---
title: Sparklines in Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Säulen- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Säulen-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, die jeweils hinsichtlich Farbe, Liniengewicht, Hoch-/Tiefpunkte und Markierungen angepasst werden können.

## **Einführung**
Sparklines sind winzige Diagramme in Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Säule** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Fähigkeit über die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `Aspose.Cells.Charts` befinden.
In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.SparklineGroups.Add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Liniengewicht, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.
Dieser Artikel führt durch jede der drei von Aspose.Cells unterstützten Sparkline-Typen — **Linie**, **Säule** und **Gewinn/Verlust** — und zeigt, wie sie hinzugefügt, in ihren Farben angepasst und die resultierende Arbeitsmappe gespeichert werden.

## **Linien-Sparklines**
Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte in einer Reihe und ist damit die natürlichste Wahl, um Trends im Zeitverlauf darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.Add` übergeben wird.
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie eine Reihe von Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.Line.Color` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), das Liniengewicht anpassen und Markierungen für Hoch-/Tiefpunkte umschalten.
6. Speichern Sie die Arbeitsmappe.
Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

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
            // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Schritt 3: Erstellen Sie einen CellArea, der auf die Zielzelle F1 zeigt
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // Spalte F (0-indiziert)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // Zeile 1 (0-indiziert)
            dest.EndRow = 0;
            // Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
            // SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Schritt 6: Aktivieren Sie Hochpunkt- und Tiefpunkt-Markierungen
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Schritt 7: Speichern Sie die Arbeitsmappe
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Säulen-Sparklines**
Eine Säulen-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Damit eignet sie sich gut für Daten, deren Größe bedeutsam ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Säulen-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.Add` übergeben.
Die Vorgehensweise entspricht dem Beispiel für Linien-Sparklines:
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel, indem Sie `group.Type` setzen, um den Typ zu bestätigen, oder die Balkenfarbe anpassen.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit das Linien-Sparkline-Beispiel nicht überschrieben wird.
Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Säulen-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, sodass positive und negative Beiträge auf einen Blick leicht erkennbar sind.

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
            // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie das erste Arbeitsblatt
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Schritt 2: Schreiben Sie Beispielwerte in A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Schritt 4: Fügen Sie eine Spalten-Sparkline zur Zielzelle hinzu
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Schritt 5: Bestätigen Sie den Sparkline-Typ durch Lesen von group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Schritt 6: Speichern Sie die Arbeitsmappe
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Gewinn/Verlust-Sparklines**
Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulen-Sparkline, die nur zwei Ergebnisse anzeigt: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein Wert von Null oder negativ als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse im Zeitverlauf zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.Add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, spielt die Größe des Werts keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele koexistieren können.

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
            // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Schritt 2: Füllen Sie Beispieldaten in Zeile 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spalte 5, Zeile 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // Zeile 1
            dest.EndRow = 0;
            // Schritt 4: Fügen Sie eine Win/Loss-Sparkline hinzu (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Schritt 5: Passen Sie die Sparkline-Gruppe an
            // Aktivieren Sie Hochpunkt- und Tiefpunkt-Markierungen
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Setzen Sie die Hochpunktfarbe auf Grün
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Setzen Sie die Tiefpunktfarbe auf Rot
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Setzen Sie die Farbe für negative Punkte auf Orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Setzen Sie die Standardreihenfarbe (verwendet für positive Balken)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Schritt 6: Speichern Sie die Arbeitsmappe
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine jedes Typs — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie das erste Arbeitsblatt
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Schritt 2: Füllen Sie Beispieldaten in Zeile 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Schritt 3: Fügen Sie eine Linien-Sparkline-Gruppe bei F1 hinzu
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Passen Sie die Farbe der Linien-Sparkline über CellsColor an
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Schritt 4: Fügen Sie eine Spalten-Sparkline-Gruppe bei F2 hinzu
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Passen Sie die Farbe der Spalten-Sparkline-Serie an
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Schritt 5: Fügen Sie eine Gewinn/Verlust (Gestapelte) Sparkline-Gruppe bei F3 hinzu
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Passen Sie die Farbe der Gewinn/Verlust-Sparkline-Serie an
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Schritt 6: Speichern Sie die Arbeitsmappe
workbook.Save("output_all.xlsx");
```

## **Anpassen des Sparkline-Erscheinungsbilds**
Sobald eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.Type`** — der `SparklineType` (Linie, Säule oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung wieder auslesen.
- **`group.Line.Color`** — die Linienfarbe, ausgedrückt als eine `CellsColor`, die über `workbook.CreateCellsColor()` erstellt wird. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet werden soll.
- **`group.Line.Weight`** — das Liniengewicht in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich, um Extremwerte hervorzuheben.
- **Markierungen für den ersten/letzten/negativen Punkt** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.
Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie den Sparkline-Farbeigenschaften nicht direkt eine `System.Drawing.Color` zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `SparklineGroups.Add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen auf den Rückgabewert verketten oder ihn in einer lokalen Variablen speichern und vor dem Speichern anpassen können.
{{% /alert %}}

## Verwandte Artikel
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for .NET](/cells/de/net/convert-sparkline-to-image-and-html/)
- [Filterfelder zu einer Pivot-Tabelle hinzufügen in Aspose.Cells for .NET](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen anwenden in Aspose.Cells for .NET](/cells/de/net/apply-style-to-pivot-table/)
- [Seitenfeld-Layout in Pivot-Tabelle ändern](/cells/de/net/change-page-field-layout/)
- [Excel in das OFD-Format konvertieren](/cells/de/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}
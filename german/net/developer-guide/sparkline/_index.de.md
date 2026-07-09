---
title: Sparklines in Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – Miniaturdiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Spalten- und Gewinn/Verlust-Sparklines mithilfe der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Alert 1 translation: keep "Aspose.Cells" as-is, translate rest.

Now the body content - let me translate section by section.

"## **Introduction**" -> "## **Einführung**"

"In Aspose.Cells, every sparkline you add is created through `worksheet.SparklineGroups.Add(...)`" - keep code references in English.

"This article walks through each of the three sparkline types supported by Aspose.Cells — **Line**, **Column**, and **Win/Loss** — and shows how to add them, customize their colors, and save the resulting workbook."

Let me translate to German:
"Dieser Artikel behandelt jeden der drei Sparkline-Typen, die von Aspose.Cells unterstützt werden — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie sie hinzugefügt, ihre Farben angepasst und die resultierende Arbeitsmappe gespeichert werden."

## **Line Sparklines** -> ## **Linien-Sparklines**

Let me continue translating...

I need to be careful with:
- "workbook" -> "Arbeitsmappe"
- "worksheet" -> "Arbeitsblatt"
- "CellArea" - keep as-is
- "SparklineGroup" - keep as-is

For German technical documentation style, I'll use formal Sie form or general terms. Since this is technical documentation, I'll keep it neutral/formal.

Let me also check the "Related Articles" section - these are links that should not be translated in terms of URL, but I could potentially translate the link text. Actually, looking at the rules, URLs must remain unchanged. The link text "Accessing Cells of a Worksheet" could potentially be translated, but looking at the rules more carefully, this seems to be a navigation section. I'll translate the link text to be consistent.

Actually, looking more carefully at the rules:
- "10. **URLs and Paths**: All URLs, file paths, and directory paths must remain unchanged."

The URLs should remain unchanged, but link text is generally translatable. However, for technical accuracy, link text often refers to the exact article titles, so I should probably keep them as-is or translate them carefully. Let me translate them to match the article titles in German, but keep the URLs in English.

Wait - actually for "Related Articles" links, these are likely existing articles with their own titles. If the actual article pages have English titles, the link text should match. But since these are likely existing articles that have been translated, the link text might also be in German. To be safe, I'll translate them since these are typically UI/link text that can be translated.

Let me also check the assistant shortcode at the end - this needs to stay exactly as-is.

Let me now write the complete translation:

Actually, I should also consider that "win/loss" is often translated as "Gewinn/Verlust" in German, and "stacked" as "gestapelt". But the code references `SparklineType.Stacked` which must stay as-is.

Let me finalize the translation. I'll be careful to:
1. Keep all product names exactly
2. Keep all code, namespace, API references exactly
3. Keep all shortcodes exactly
4. Keep all CODE_BLOCK placeholders exactly
5. Keep all URLs exactly
6. Translate the rest to proper German technical style

Let me write this out now.</think>


{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, die jeweils in Bezug auf Farbe, Linienstärke, Höchst-/Tiefstpunkte und Markierungen angepasst werden können.

{{% /alert %}}

## **Einführung**

Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms zu beanspruchen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Spalte** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Fähigkeit durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `Aspose.Cells.Charts` befinden.

In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.SparklineGroups.Add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle sowie visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Höchst-/Tiefstpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil gemeinsam haben. Wenn Sie `Add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline in dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel behandelt jeden der drei von Aspose.Cells unterstützten Sparkline-Typen — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie sie hinzugefügt, ihre Farben angepasst und die resultierende Arbeitsmappe gespeichert werden.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.Add` übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe über `group.Line.Color` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Markierungen für Höchst-/Tiefstpunkte umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Höchst- und Tiefstpunkte aktiviert.

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
            // Schritt 1: Eine Arbeitsmappe erstellen und das erste Arbeitsblatt abrufen
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Schritt 2: Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1 schreiben
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Schritt 3: Eine CellArea erstellen, die auf die Zielzelle F1 zeigt
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // Spalte F (0-indiziert)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // Zeile 1 (0-indiziert)
            dest.EndRow = 0;

            // Schritt 4: Eine Liniendiagramm-Sparkline von A1:E1 zu F1 hinzufügen
            // SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Schritt 5: Eine rote CellsColor erstellen und der Sparkline-Linienfarbe zuweisen
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Schritt 6: Hochpunkt- und Tiefpunkt-Markierungen aktivieren
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Schritt 7: Die Arbeitsmappe speichern
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Spalten-Sparklines**

Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dadurch eignet sie sich gut für Daten, deren Größe aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.Add` übergeben.

Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel indem Sie `group.Type` setzen, um den Typ zu bestätigen, oder indem Sie die Balkenfarbe anpassen.
6. Speichern Sie die Arbeitsmappe in eine separate Ausgabedatei, damit das Beispiel der Linien-Sparkline nicht überschrieben wird.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken gezeichnet, wodurch positive und negative Beiträge auf einen Blick leicht erkennbar sind.

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

            // Schritt 5: Bestätigen Sie den Sparkline-Typ, indem Sie group.Type lesen
            Console.WriteLine("Sparkline Type added: " + group.Type);

            // Schritt 6: Speichern Sie die Arbeitsmappe
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die nur zwei Ergebnisse anzeigt: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein Wert von Null oder ein negativer Wert wird als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.Add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um das Gewinn/Verlust-Rendering anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder als Verlust behandeln, spielt die Größe des Werts keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte werden zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel indem Sie Akzentfarben für die Gewinn- und Verlust-Balken festlegen.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele gleichzeitig auf der Festplatte existieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die vorherigen beiden Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert — und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

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

            // Schritt 3: Erstellen Sie eine CellArea, die auf F1 zeigt (Spalte 5, Zeile 0)
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
            // Aktivieren Sie Hoch- und Tiefpunkt-Markierungen
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // Setzen Sie die Farbe des Hochpunkts auf Grün
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // Setzen Sie die Farbe des Tiefpunkts auf Rot
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // Setzen Sie die Farbe des Negativpunkts auf Orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // Setzen Sie die Standard-Serienfarbe (wird für positive Balken verwendet)
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

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien leicht isoliert inspiziert werden können. In einem realen Szenario möchten Sie jedoch häufig mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt einzufügen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann eine andere Zielzelle oder einen anderen Bereich anvisieren. Beispielsweise könnten Sie eine Linien-Sparkline in F1, eine Spalten-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — alle lesen aus denselben Quelldaten in Zeile 1 — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Schritt 2: Beispieldaten in Zeile 1 (A1:E1) einfügen
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Schritt 3: Eine Liniendiagramm-Sparkline-Gruppe bei F1 hinzufügen
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// Passen Sie die Farbe der Liniendiagramm-Sparkline über CellsColor an
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Schritt 4: Eine Säulendiagramm-Sparkline-Gruppe bei F2 hinzufügen
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Passen Sie die Farbe der Säulendiagramm-Sparkline-Serie an
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Schritt 5: Eine Gewinn/Verlust (gestapelte) Sparkline-Gruppe bei F3 hinzufügen
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

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzigen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich gemeinsam nutzen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines „Dashboard" aus In-Cell-Visualisierungen direkt innerhalb eines bestehenden Arbeitsblatts zu erstellen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbildes**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.Type`** — der `SparklineType` (Linie, Spalte oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zurücklesen, um ihn zu bestätigen.
- **`group.Line.Color`** — die Linienfarbe, ausgedrückt als eine `CellsColor`, die über `workbook.CreateCellsColor()` erstellt wird. Dies ist die Eigenschaft, die für die Strichfarbe von Linien-Sparklines verwendet werden sollte.
- **`group.Line.Weight`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Höchst-/Tiefstpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich, um Extreme hervorzuheben.
- **Markierungen für erste/letzte/negative Punkte** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie `Sparkline`-Farbeigenschaften nicht direkt eine `System.Drawing.Color` zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `SparklineGroups.Add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen auf dem Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.

## **Verwandte Artikel**

- [Zugreifen auf Zellen eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/)
- [Formatieren von Arbeitsblattzellen in einer Arbeitsmappe](/cells/de/net/format-worksheet-cells-in-a-workbook/)
- [Anpassen von Diagrammen](/cells/de/net/customizing-charts/)
- [Erstellen dynamischer Diagramme](/cells/de/net/create-dynamic-charts/)
- [Verwalten von Daten in Excel-Dateien](/cells/de/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}
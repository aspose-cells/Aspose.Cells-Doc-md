---
title: Sparklines in Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells ist eine C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – Minidiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man mit der Aspose.Cells-Bibliothek Linien-, Säulen- und Gewinn/Verlust-Sparklines hinzufügt und anpasst.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Säulen-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind Minidiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, wobei jede hinsichtlich Farbe, Linienstärke, Hoch-/Tiefpunkten und Markierungen angepasst werden kann.

{{% /alert %}}

## **Einführung**

Sparklines sind kleine In-Cell-Diagramme, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Spalte** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktionalität durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `Aspose.Cells.Charts` befinden.

In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.SparklineGroups.Add(...)` erstellt, was ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil gemeinsam haben. Wenn Sie `Add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline innerhalb dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel führt durch jede der drei von Aspose.Cells unterstützten Sparkline-Typen – **Linie**, **Spalte** und **Gewinn/Verlust** – und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte in einer Reihe, was sie zur natürlichsten Wahl macht, um Trends im Zeitverlauf darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.Add` übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument – `false` – teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.Line.Color` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Schritt 1: Eine Arbeitsmappe erstellen und das erste Arbeitsblatt abrufen
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Schritt 2: Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1 schreiben
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Schritt 3: Einen CellArea erstellen, der auf die Zielzelle F1 zeigt
    CellArea dest;
    dest.StartColumn = 5;   // Spalte F (0-indiziert)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // Zeile 1 (0-indiziert)
    dest.EndRow = 0;

    // Schritt 4: Eine Linien-Sparkline von A1:E1 in F1 hinzufügen
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Schritt 5: Eine rote CellsColor erstellen und der Sparkline-Linienfarbe zuweisen
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Schritt 6: Hoch- und Tiefpunktmarkierungen aktivieren
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Schritt 7: Die Arbeitsmappe speichern
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Säulen-Sparklines**

Eine Säulen-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie gut geeignet für Daten, deren Größe aussagekräftig ist – zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Säulen-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.Add` übergeben.

Das Vorgehen spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an – zum Beispiel durch Setzen von `group.Type`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit diese das Beispiel der Linien-Sparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Säulen-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken dargestellt und positive Werte als nach oben verlaufende Balken, wodurch positive und negative Beiträge auf einen Blick leicht zu erkennen sind.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Schritt 2: Schreiben Sie Beispieldaten in A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Schritt 4: Fügen Sie eine Spalten-Sparkline zur Zielzelle hinzu
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Schritt 5: Bestätigen Sie den Sparkline-Typ durch Lesen von group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Schritt 6: Speichern Sie die Arbeitsmappe
    wb.Save(u"output_column.xlsx");

    std::cout << "Arbeitsmappe als output_column.xlsx gespeichert" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulen-Sparkline, die so konzipiert ist, dass sie nur zwei Ergebnisse anzeigt: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein Null- oder negativer Wert wird als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, bestanden/nicht bestanden-Ergebnissen oder beliebige binäre Ergebnisse im Zeitverlauf zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.Add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)

Das Vorgehen ist dasselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Werts nicht relevant – nur sein Vorzeichen. Positive Werte werden zu Aufwärtsbalken und nicht-positive Werte werden zu Abwärtsbalken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die beiden vorherigen Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert – und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie das erste Arbeitsblatt
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Schritt 2: Füllen Sie Beispieldaten in Zeile 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spalte 5, Zeile 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // Zeile 1
    dest.EndRow = 0;

    // Schritt 4: Fügen Sie eine Win/Loss-Sparkline hinzu (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Schritt 5: Passen Sie die Sparkline-Gruppe an
    // Aktivieren Sie Hochpunkt- und Tiefpunkt-Markierungen
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Setzen Sie die Hochpunktfarbe auf Grün
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Setzen Sie die Tiefpunktfarbe auf Rot
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Setzen Sie die Farbe der negativen Punkte auf Orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Setzen Sie die Standardreihenfarbe (verwendet für positive Balken)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Schritt 6: Speichern Sie die Arbeitsmappe
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, sodass die Ausgabedateien leicht isoliert zu überprüfen sind. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt einzufügen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann auf eine andere Zielzelle oder einen anderen Bereich abzielen. Beispielsweise könnten Sie eine Linien-Sparkline in F1, eine Säulen-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren – alle lesen aus denselben Quelldaten in Zeile 1 – sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das kombinierte Beispiel unten erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu – eine jedes Typs – sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Schritt 2: Füllen Sie Beispieldaten in Zeile 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Schritt 3: Fügen Sie eine Linien-Sparkline-Gruppe bei F1 hinzu
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Passen Sie die Farbe der Linien-Sparkline über CellsColor an
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Schritt 4: Fügen Sie eine Spalten-Sparkline-Gruppe bei F2 hinzu
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Passen Sie die Farbe der Spalten-Sparkline-Serie an
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Schritt 5: Fügen Sie eine Gewinn/Verlust (Gestapelt) Sparkline-Gruppe bei F3 hinzu
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Passen Sie die Farbe der Gewinn/Verlust-Sparkline-Serie an
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Schritt 6: Speichern Sie die Arbeitsmappe
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzigen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich gemeinsam nutzen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines „Dashboard" von In-Cell-Visualisierungen direkt innerhalb eines bestehenden Arbeitsblatts aufzubauen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbilds**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.Type`** – der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung zurücklesen.
- **`group.Line.Color`** – die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.CreateCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline zu verwenden ist.
- **`group.Line.Weight`** – die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** – Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremwerten.
- **Erste/Letzte/Negative Punkt-Markierungen** – Flags, die Markierungen am ersten, letzten und negativen Datenpunkt umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen sie der entsprechenden Eigenschaft zu. Weisen Sie keinen rohen Farbwert direkt den Sparkline-Farbeigenschaften zu – sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `SparklineGroups.Add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variable speichern und vor dem Speichern anpassen können.



{{< app/cells/assistant language="cpp" >}}
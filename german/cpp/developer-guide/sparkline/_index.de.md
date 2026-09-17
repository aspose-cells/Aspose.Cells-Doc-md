---
title: Sparklines in Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells ist eine C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – kleinen Diagrammen, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie Sie Linien-, Spalten- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügen und anpassen können.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Sparklines, Liniendiagramm-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind kleine Diagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, und jede kann hinsichtlich Farbe, Liniendicke, Hoch-/Tiefpunkte und Markierungen angepasst werden.

## **Einführung**
Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenreihe oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien**, **Spalten** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktionalität durch die APIs `SparklineGroup` und `SparklineGroupCollection` wider, die sich im Namespace `Aspose.Cells.Charts` befinden.
In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.SparklineGroups.Add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Liniendicke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.
Dieser Artikel führt durch jede der drei von Aspose.Cells unterstützten Sparkline-Typen — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie sie hinzugefügt, ihre Farben angepasst und die resultierende Arbeitsmappe gespeichert werden.

## **Linien-Sparklines**
Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe, was sie zur natürlichsten Wahl für die Darstellung von Trends über die Zeit macht. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.Add` übergeben wird.
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Reihe von Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.Line.Color` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Liniendicke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.
Im folgenden Beispiel wird eine Arbeitsmappe erstellt, die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 geschrieben und eine Linien-Sparkline in Zelle F1 hinzugefügt, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Schritt 3: Erstellen Sie einen CellArea, der auf die Zielzelle F1 zeigt
    CellArea dest;
    dest.StartColumn = 5;   // Spalte F (0-indiziert)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // Zeile 1 (0-indiziert)
    dest.EndRow = 0;
    // Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Schritt 6: Aktivieren Sie die Hochpunkt- und Tiefpunkt-Markierungen
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Schritt 7: Speichern Sie die Arbeitsmappe
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Spalten-Sparklines**
Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie besonders geeignet für Daten, deren Größe aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.Add` übergeben.
Das Vorgehen spiegelt das Beispiel der Linien-Sparkline wider:
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
3. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` auf.
4. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel durch Setzen von `group.Type` zur Bestätigung des Typs oder durch Anpassen der Balkenfarbe.
5. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit diese das Beispiel der Linien-Sparkline nicht überschreibt.
Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, was positive und negative Beiträge auf einen Blick leicht erkennbar macht.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Schritt 2: Schreiben Sie Beispielwerte in A1:E1
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
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gewinn/Verlust-Sparklines**
Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die nur zwei Ergebnisse anzeigt: Ein positiver Wert wird als "Aufwärts"-Balken (ein Gewinn) und ein nichtpositiver Wert als "Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehen/Nichtbestehen-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.Add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, spielt die Größe des Werts keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele nebeneinander auf der Festplatte existieren können.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Schritt 1: Eine Arbeitsmappe erstellen und das erste Arbeitsblatt abrufen
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Schritt 2: Beispieldaten in Zeile 1 einfügen: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Schritt 3: Einen CellArea-Bereich erstellen, der auf F1 zeigt (Spalte 5, Zeile 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // Zeile 1
    dest.EndRow = 0;
    // Schritt 4: Eine Win/Loss-Sparkline hinzufügen (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // Schritt 5: Die Sparkline-Gruppe anpassen
    // Hochpunkt- und Tiefpunkt-Markierungen aktivieren
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Die Hochpunktfarbe auf Grün setzen
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Die Tiefpunktfarbe auf Rot setzen
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Die Farbe der negativen Punkte auf Orange setzen
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Die Standardreihenfarbe festlegen (für positive Balken verwendet)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Schritt 6: Die Arbeitsmappe speichern
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Schritt 2: Beispieldaten in Zeile 1 (A1:E1) einfügen
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Schritt 3: Fügen Sie eine Liniendiagramm-Sparkline-Gruppe bei F1 hinzu
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Passen Sie die Farbe der Liniendiagramm-Sparkline über CellsColor an
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Schritt 4: Fügen Sie eine Säulendiagramm-Sparkline-Gruppe bei F2 hinzu
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Passen Sie die Farbe der Säulendiagramm-Sparkline-Serie an
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Schritt 5: Fügen Sie eine Gewinn-/Verlust-Sparkline-Gruppe (gestapelt) bei F3 hinzu
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Passen Sie die Farbe der Gewinn-/Verlust-Sparkline-Serie an
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Schritt 6: Speichern Sie die Arbeitsmappe
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Anpassen des Sparkline-Erscheinungsbilds**
Nachdem eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.Type`** — der `SparklineType` (Linie, Spalte oder Gestapelt). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung zurücklesen.
- **`group.Line.Color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.CreateCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet werden sollte.
- **`group.Line.Weight`** — die Liniendicke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten aktivieren, nützlich zur Hervorhebung von Extremwerten.
- **Erster/Letzter/Negativer-Punkt-Markierungen** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.
Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie keinen rohen Farbwert direkt den Sparkline-Farbeigenschaften zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `SparklineGroups.Add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
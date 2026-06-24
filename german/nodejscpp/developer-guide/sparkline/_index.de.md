---
title: Sparklines in Aspose.Cells for Node.js via C++
linktitle: Sparklines
description: Aspose.Cells ist eine Node.js-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – Miniaturdiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Säulen- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, Node.js-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Säulen-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, wobei jede hinsichtlich Farbe, Linienstärke, Hoch-/Tiefpunkten und Markierungen angepasst werden kann.

{{% /alert %}}

## **Einführung**

Sparklines sind kleine Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Zeile oder Spalte von Daten anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Säule** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktionalität durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `Aspose.Cells.Charts` befinden.

In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.sparklineGroups.add(...)` erstellt, was ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil gemeinsam nutzen. Wenn Sie `add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline innerhalb dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel führt durch jede der drei von Aspose.Cells unterstützten Sparkline-Typen — **Linie**, **Säule** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte in einer Reihe, was sie zur natürlichsten Wahl macht, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `sparklineGroups.add` übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.line.color` festlegen (was eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Es passt auch die Linienfarbe auf Rot an und aktiviert Markierungen für die Hoch- und Tiefpunkte.

```javascript
const AsposeCells = require("aspose.cells");

// Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Schritt 3: Erstellen Sie eine CellArea, die auf die Zielzelle F1 verweist
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // Spalte F (0-indiziert)
dest.setEndColumn(5);
dest.setStartRow(0);      // Zeile 1 (0-indiziert)
dest.setEndRow(0);

// Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
// SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Schritt 6: Aktivieren Sie die Markierungen für Höchst- und Tiefpunkte
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Schritt 7: Speichern Sie die Arbeitsmappe
workbook.save("output_line.xlsx");
```

## **Säulen-Sparklines**

Eine Säulen-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie gut geeignet für Daten, deren Größe bedeutsam ist — zum Beispiel monatliche Verkaufszahlen oder Zählwerte. In Aspose.Cells erstellen Sie eine Säulen-Sparkline, indem Sie `SparklineType.Column` an die Methode `sparklineGroups.add` übergeben.

Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel, indem Sie `group.type` setzen, um den Typ zu bestätigen, oder indem Sie die Balkenfarbe anpassen.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Linien-Sparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Säulen-Sparkline in F1. Negative Werte werden als nach unten gerichtete Balken und positive Werte als nach oben gerichtete Balken dargestellt, was es einfach macht, positive und negative Beiträge auf einen Blick zu erkennen.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Schritt 2: Schreibe Beispielwerte in A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Schritt 3: Erstelle eine CellArea, die auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Schritt 4: Füge eine Spalten-Sparkline zur Zielzelle hinzu
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Schritt 5: Bestätige den Sparkline-Typ durch Lesen von group.Type
console.log("Sparkline Type added: " + group.getType());

// Schritt 6: Speichere die Arbeitsmappe
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulen-Sparkline, die entwickelt wurde, um nur zwei Ergebnisse anzuzeigen: ein positiver Wert wird als "Aufwärts"-Balken (ein Gewinn) und ein Null- oder negativer Wert wird als "Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `sparklineGroups.add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Werts nicht relevant — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte werden zu Abwärts-Balken.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die vorherigen beiden Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert — und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Schritt 2: Beispieldaten in Zeile 1 befüllen: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Schritt 3: Eine CellArea erstellen, die auf F1 zeigt (Spalte 5, Zeile 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // Zeile 1
dest.setEndRow(0);

// Schritt 4: Eine Gewinn/Verlust-Sparkline hinzufügen (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Schritt 5: Die Sparkline-Gruppe anpassen
// Hochpunkt- und Tiefpunkt-Markierungen aktivieren
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Die Hochpunktfarbe auf Grün setzen
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// Die Tiefpunktfarbe auf Rot setzen
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// Die Farbe der negativen Punkte auf Orange setzen
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// Die Standard-Serienfarbe festlegen (für positive Balken)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Schritt 6: Die Arbeitsmappe speichern
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien isoliert leicht zu prüfen sind. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt zu legen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann auf eine andere Zielzelle oder einen anderen Bereich abzielen. Beispielsweise könnten Sie eine Linien-Sparkline in F1, eine Säulen-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — die alle aus denselben Quelldaten in Zeile 1 lesen — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das kombinierte Beispiel unten erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — einen von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Schritt 2: Beispieldaten in Zeile 1 (A1:E1) einfügen
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Schritt 3: Eine Linien-Sparkline-Gruppe bei F1 hinzufügen
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Linien-Sparkline-Farbe über CellsColor anpassen
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Schritt 4: Eine Spalten-Sparkline-Gruppe bei F2 hinzufügen
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Farbe der Spalten-Sparkline-Serie anpassen
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Schritt 5: Eine Gewinn/Verlust (Gestapelte) Sparkline-Gruppe bei F3 hinzufügen
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Farbe der Gewinn/Verlust-Sparkline-Serie anpassen
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Schritt 6: Arbeitsmappe speichern
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzigen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich gemeinsam nutzen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines "Dashboard" aus Zellen-Visualisierungen direkt in einem bestehenden Arbeitsblatt aufzubauen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbilds**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.sparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.type`** — der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung zurücklesen.
- **`group.line.color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.createCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet werden soll.
- **`group.line.weight`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremwerten.
- **Erste/Letzte/Negative Punkt-Markierungen** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie `System.Drawing.Color` nicht direkt den Sparkline-Farbeigenschaften zu — diese erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `sparklineGroups.add` selbst gibt ein voll typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.



{{< app/cells/assistant language="javascript" >}}
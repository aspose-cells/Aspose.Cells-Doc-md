---
title: Sparklines in Aspose.Cells for Node.js via C++
linktitle: Sparklines
description: Aspose.Cells ist eine Node.js-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt — Minidiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie Sie Linien-, Spalten- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügen und anpassen.
keywords: Aspose.Cells, Node.js-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind Minidiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, und jede kann hinsichtlich Farbe, Liniendicke, Hoch-/Tiefpunkten und Markierungen angepasst werden.
{{% /alert %}}

## **Einführung**
Sparklines sind winzige Diagramme in Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien**, **Spalten** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Fähigkeit durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs im Namespace `Aspose.Cells.Charts` wider.
In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.sparklineGroups.add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle sowie visuelle Eigenschaften wie Linienfarbe, Liniendicke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.
Dieser Artikel geht durch jeden der drei von Aspose.Cells unterstützten Sparkline-Typen — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**
Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `sparklineGroups.add` übergeben wird.
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie eine Reihe von Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.line.color` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Liniendicke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.
Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.startColumn = 5;
lineArea.endColumn = 5;
lineArea.startRow = 0;
lineArea.endRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.startColumn = 5;
columnArea.endColumn = 5;
columnArea.startRow = 1;
columnArea.endRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.startColumn = 5;
stackedArea.endColumn = 5;
stackedArea.startRow = 2;
stackedArea.endRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Spalten-Sparklines**
Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie gut geeignet für Daten, deren Größe bedeutsam ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.Column` an die Methode `sparklineGroups.add` übergeben.
Die Vorgehensweise spiegelt das Linien-Sparkline-Beispiel wider:
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel durch Setzen von `group.type`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Linien-Sparkline-Beispiel nicht überschreibt.
Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, was positive und negative Beiträge auf einen Blick leicht erkennbar macht.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // F
dest.endColumn = 5;
dest.startRow = 0;      // row 1
dest.endRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Gewinn/Verlust-Sparklines**
Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die nur zwei Ergebnisse anzeigt: ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein null oder negativer Wert als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `sparklineGroups.add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um das Gewinn/Verlust-Rendering anzufordern.)
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, spielt die Größe des Werts keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Setzen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;
dest.endColumn = 5;
dest.startRow = 0;
dest.endRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — einen von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```javascript
const AsposeCells = require("aspose.cells.node");
// Step 1: Create a Workbook and get the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
const dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // column F (0-indexed)
dest.endColumn = 5;
dest.startRow = 0;      // row 1 (0-indexed)
dest.endRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.Red);
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Anpassen des Sparkline-Erscheinungsbilds**
Sobald eine `SparklineGroup` erstellt und zu `worksheet.sparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.type`** — der `SparklineType` (Linie, Spalte oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zurücklesen, um ihn zu bestätigen.
- **`group.line.color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.createCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline zu verwenden ist.
- **`group.line.weight`** — die Liniendicke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich, um Extreme hervorzuheben.
- **Erste/Letzte/Negative Punkt-Markierungen** — Flags, die Markierungen am ersten, letzten und negativen Datenpunkt umschalten.
Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie keine `System.Drawing.Color` direkt den Sparkline-Farbeigenschaften zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `sparklineGroups.add` selbst gibt ein voll typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.

{{< app/cells/assistant language="nodejs-cpp" >}}
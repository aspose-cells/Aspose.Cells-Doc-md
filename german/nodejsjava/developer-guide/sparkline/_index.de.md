---
title: Sparklines in Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells ist eine Node.js-via-Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – kleinen Diagrammen, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie Sie Linien-, Säulen- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügen und anpassen.
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Säulen-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind kleine Diagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, und jede kann hinsichtlich Farbe, Linienstärke, Hoch-/Tiefpunkten und Markierungen angepasst werden.
{{% /alert %}}

## **Einführung**
Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenreihe oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien**, **Säulen** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktionalität durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs im `com.aspose.cells.Charts`-Namespace wider.
In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.SparklineGroups.add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.
Dieser Artikel führt durch jede der drei von Aspose.Cells unterstützten Sparkline-Typen – **Linie**, **Säule** und **Gewinn/Verlust** – und zeigt, wie sie hinzugefügt, ihre Farben angepasst und die resultierende Arbeitsmappe gespeichert werden.

## **Linien-Sparklines**
Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.add` übergeben wird.
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument – `false` – teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.Line.Color` festlegen (die eine `CellsColor` aus `com.aspose.cells.Drawing` erwartet), die Linienstärke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.
Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Schritt 2: Schreibe die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Schritt 3: Erstelle eine CellArea, die auf die Zielzelle F1 zeigt
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // Spalte F (0-indiziert)
dest.setEndColumn(5);
dest.setStartRow(0);      // Zeile 1 (0-indiziert)
dest.setEndRow(0);
// Schritt 4: Füge eine Linien-Sparkline von A1:E1 in F1 hinzu
// SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Schritt 5: Erstelle eine rote CellsColor und weise sie der Sparkline-Linienfarbe zu
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Schritt 6: Aktiviere die Hochpunkt- und Tiefpunkt-Markierungen
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Schritt 7: Speichere die Arbeitsmappe
workbook.save("output_line.xlsx");
```

## **Säulen-Sparklines**
Eine Säulen-Sparkline rendert jeden Datenpunkt als vertikalen Balken. Dies macht sie gut geeignet für Daten, deren Größenordnung aussagekräftig ist – zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Säulen-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.add` übergeben.
Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an – zum Beispiel durch Setzen von `group.Type`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Linien-Sparkline nicht überschreibt.
Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Säulen-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, was positive und negative Beiträge auf einen Blick leicht erkennbar macht.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Schritt 2: Beispielwerte in A1:E1 schreiben
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Schritt 3: Eine CellArea erstellen, die auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Schritt 4: Eine Sparkline vom Typ „Spalte“ zur Zielzelle hinzufügen
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Schritt 5: Den Sparkline-Typ durch Auslesen von group.Type bestätigen
console.log("Sparkline Type added: " + group.getType());
// Schritt 6: Arbeitsmappe speichern
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Gewinn/Verlust-Sparklines**
Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulen-Sparkline, die nur zwei Ergebnisse anzeigt: ein positiver Wert wird als "Aufwärts"-Balken (ein Gewinn) und ein Wert von Null oder negativ als "Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehen/Nichtbestehen-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größenordnung des Werts nicht wichtig – nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte werden zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Schritt 2: Beispieldaten in Zeile 1 einfügen: A1=5, B1=-3, C1=8, D1=-2, E1=6
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
// Schritt 4: Eine Win/Loss-Sparkline hinzufügen (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Schritt 5: Die Sparkline-Gruppe anpassen
// Hoch- und Tiefpunkt-Markierungen aktivieren
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Die Farbe des Hochpunkts auf Grün setzen
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Die Farbe des Tiefpunkts auf Rot setzen
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Die Farbe des negativen Punkts auf Orange setzen
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Die Standardreihenfarbe festlegen (für positive Balken verwendet)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Schritt 6: Die Arbeitsmappe speichern
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu – eine von jedem Typ – sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Schritt 2: Beispieldaten in Zeile 1 (A1:E1) einfügen
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Schritt 3: Linien-Sparkline-Gruppe bei F1 hinzufügen
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Linien-Sparkline-Farbe über CellsColor anpassen
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Schritt 4: Spalten-Sparkline-Gruppe bei F2 hinzufügen
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Spalten-Sparkline-Serienfarbe anpassen
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Schritt 5: Win/Loss (Gestapelte) Sparkline-Gruppe bei F3 hinzufügen
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Win/Loss-Sparkline-Serienfarbe anpassen
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Schritt 6: Arbeitsmappe speichern
workbook.save("output_all.xlsx");
```

## **Anpassen der Sparkline-Darstellung**
Sobald eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.Type`** – der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zurücklesen, um ihn zu bestätigen.
- **`group.Line.Color`** – die Linienfarbe, ausgedrückt als eine `CellsColor`, die über `workbook.createCellsColor()` erstellt wurde. Dies ist die zu verwendende Eigenschaft für die Strichfarbe der Linien-Sparkline.
- **`group.Line.Weight`** – die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** – Flags, die kleine Markierungen auf den höchsten und niedrigsten Datenpunkten einschalten, nützlich, um Extreme hervorzuheben.
- **Markierungen für erste/letzte/negative Punkte** – Flags, die Markierungen auf den ersten, letzten und negativen Datenpunkten umschalten.
Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen sie der entsprechenden Eigenschaft zu. Weisen Sie den Sparkline-Farbeigenschaften kein `java.awt.Color` direkt zu – sie erwarten den `CellsColor`-Typ aus `com.aspose.cells.Drawing`. Die Methode `SparklineGroups.add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.

{{< app/cells/assistant language="javascript" >}}
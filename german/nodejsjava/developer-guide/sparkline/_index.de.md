---
title: Sparklines in Aspose.Cells für Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells ist eine Node.js via Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt — kompakte Diagramme, die innerhalb von Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Spalten- und Gewinn/Verlust-Sparklines mithilfe der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, Node.js via Java-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind kompakte Diagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, und jede kann in Bezug auf Farbe, Linienstärke, Hoch-/Tiefpunkte und Markierungen angepasst werden.

{{% /alert %}}

## **Einführung**

Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien-**, **Spalten-** und **Gewinn/Verlust-Sparklines**. Aspose.Cells spiegelt diese Funktionalität durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `com.aspose.cells.Charts` befinden.

In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.SparklineGroups.add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil teilen. Wenn Sie `add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline innerhalb dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und denselben Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel führt durch jeden der drei Sparkline-Typen, die von Aspose.Cells unterstützt werden — **Linien-**, **Spalten-** und **Gewinn/Verlust-Sparklines** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe, was sie zur natürlichsten Wahl für die Darstellung von Trends über die Zeit macht. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `SparklineGroups.add` übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Reihe von Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.Line.Color` festlegen (die eine `CellsColor` aus `com.aspose.cells.Drawing` erwartet), die Linienstärke anpassen und Hoch-/Tiefpunkt-Markierungen umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Schritt 2: Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1 schreiben
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Schritt 3: Einen CellArea erstellen, der auf die Zielzelle F1 zeigt
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // Spalte F (0-indiziert)
dest.setEndColumn(5);
dest.setStartRow(0);      // Zeile 1 (0-indiziert)
dest.setEndRow(0);

// Schritt 4: Eine Linien-Sparkline von A1:E1 zu F1 hinzufügen
// SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Schritt 5: Eine rote CellsColor erstellen und der Sparkline-Linienfarbe zuweisen
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Schritt 6: Hochpunkt- und Tiefpunkt-Markierungen aktivieren
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Schritt 7: Die Arbeitsmappe speichern
workbook.save("output_line.xlsx");
```

## **Spalten-Sparklines**

Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie gut geeignet für Daten, deren Größe bedeutsam ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.Column` an die Methode `SparklineGroups.add` übergeben.

Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel indem Sie `group.Type` setzen, um den Typ zu bestätigen, oder indem Sie die Balkenfarbe anpassen.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Linien-Sparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, was positive und negative Beiträge auf einen Blick leicht erkennbar macht.

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

// Schritt 4: Eine Spalten-Sparkline zur Zielzelle hinzufügen
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Schritt 5: Den Sparkline-Typ durch Lesen von group.Type bestätigen
console.log("Sparkline Type added: " + group.getType());

// Schritt 6: Die Arbeitsmappe speichern
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die entwickelt wurde, um nur zwei Ergebnisse anzuzeigen: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein Null- oder negativer Wert wird als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `SparklineGroups.add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, spielt die Größe des Wertes keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärtsbalken und nicht-positive Werte werden zu Abwärtsbalken.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel indem Sie Akzentfarben für die Gewinn- und Verlust-Balken festlegen.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele nebeneinander auf der Festplatte existieren können.

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

// Die Hochpunktfarbe auf Grün setzen
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Die Tiefpunktfarbe auf Rot setzen
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Die Farbe der negativen Punkte auf Orange setzen
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// Die Standard-Serienfarbe festlegen (für positive Balken verwendet)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// Schritt 6: Die Arbeitsmappe speichern
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien leicht isoliert inspiziert werden können. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt zu platzieren, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann auf eine andere Zielzelle oder einen anderen Bereich abzielen. Beispielsweise könnten Sie eine Linien-Sparkline in F1, eine Spalten-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — alle lesen aus denselben Quelldaten in Zeile 1 — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

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
lineColor.setColor(AsposeCells.Color.getBlue());
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
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Schritt 5: Eine Win/Loss (gestapelte) Sparkline-Gruppe bei F3 hinzufügen
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Farbe der Win/Loss-Sparkline-Serie anpassen
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Schritt 6: Arbeitsmappe speichern
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzigen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich teilen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines „Dashboard" aus In-Cell-Visualisierungen direkt in einem vorhandenen Arbeitsblatt aufzubauen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbildes**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.SparklineGroups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.Type`** — der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung zurücklesen.
- **`group.Line.Color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.createCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet werden soll.
- **`group.Line.Weight`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremen.
- **Erste/Letzte/Negative Punktmarkierungen** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie den Sparkline-Farbeigenschaften nicht direkt eine `java.awt.Color` zu — sie erwarten den Typ `CellsColor` aus `com.aspose.cells.Drawing`. Die Methode `SparklineGroups.add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.



{{< app/cells/assistant language="javascript" >}}
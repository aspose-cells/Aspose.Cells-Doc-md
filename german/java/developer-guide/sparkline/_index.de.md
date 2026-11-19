---
title: Sparklines in Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells ist eine Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – das sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erläutert, wie man mit der Aspose.Cells-Bibliothek Linien-, Säulen- und Gewinn/Verlust-Sparklines hinzufügt und anpasst.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Säulen-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Erstellen von Sparklines innerhalb von Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, die jeweils in Bezug auf Farbe, Linienstärke, Hoch-/Tiefpunkte sowie Markierungen angepasst werden können.
{{% /alert %}}

## **Einführung**
Sparklines sind winzige Diagramme in einer Zelle, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Säule** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Fähigkeit über die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die im Namespace `Aspose.Cells.Charts` zu finden sind.
In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.getSparklineGroups().add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle sowie visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.
Dieser Artikel geht jede der drei von Aspose.Cells unterstützten Sparkline-Typen durch — **Linie**, **Säule** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**
Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.LINE` an die Methode `add` übergeben wird.
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe über `group.getLine().setColor(...)` festlegen (die einen `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Markierungen für Hoch-/Tiefpunkte umschalten.
6. Speichern Sie die Arbeitsmappe.
Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte werden aktiviert.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
CellArea dest = new CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.add returns the index of the newly added group
int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
CellsColor red = workbook.createCellsColor();
red.setColor(com.aspose.cells.Color.getRed());
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Säulen-Sparklines**
Eine Säulen-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie besonders geeignet für Daten, deren Größenordnung aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Säulen-Sparkline, indem Sie `SparklineType.COLUMN` an die Methode `add` übergeben.
Das Vorgehen entspricht dem Beispiel für die Linien-Sparkline:
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel durch Setzen von `group.getType()` zur Bestätigung des Typs oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in eine separate Ausgabedatei, damit das Beispiel der Linien-Sparkline nicht überschrieben wird.
Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 nach A1:E1 und rendert eine Säulen-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken dargestellt, positive Werte als nach oben verlaufende Balken, wodurch positive und negative Beiträge auf einen Blick leicht erkennbar sind.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Save the workbook
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Gewinn/Verlust-Sparklines**
Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulen-Sparkline, die nur zwei Ergebnisse anzeigt: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) dargestellt, und ein Null- oder negativer Wert wird als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.
In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.STACKED` an die Methode `add` übergeben wird. (Trotz des Namens ist `SparklineType.STACKED` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)
1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, spielt die Größenordnung des Wertes keine Rolle — nur sein Vorzeichen. Positive Werte werden zu Aufwärtsbalken, nicht-positive Werte zu Abwärtsbalken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele koexistieren können.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Populate sample data
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Build a CellArea pointing to F1 (column 5, row 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(Color.fromArgb(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);
// Save the workbook
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Use static factory method
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Use static factory method
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Use static factory method
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Anpassen des Sparkline-Erscheinungsbilds**
Sobald eine `SparklineGroup` erstellt und zu `worksheet.getSparklineGroups()` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:
- **`group.getType()`** — der `SparklineType` (LINE, COLUMN oder STACKED). Er wird beim Hinzufügen der Gruppe festgelegt, kann aber zur Bestätigung wieder ausgelesen werden.
- **`group.getLine().setColor(...)`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.createCellsColor()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet wird.
- **`group.getLine().setWeight(...)`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremen.
- **Erster/Letzter/Negativer Punkt-Markierungen** — Flags, die Markierungen am ersten, letzten und negativen Datenpunkt umschalten.
Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie `java.awt.Color` nicht direkt den Sparkline-Farbeigenschaften zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die Methode `add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen auf dem Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.

{{< app/cells/assistant language="java" >}}
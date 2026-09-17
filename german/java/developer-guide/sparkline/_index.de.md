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
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Schritt 1: Erstellen Sie eine Workbook und holen Sie sich das erste Arbeitsblatt
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // Schritt 3: Erstellen Sie eine CellArea, die auf die Zielzelle F1 zeigt
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // Spalte F (0-indexiert)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // Zeile 1 (0-indexiert)
            dest.EndRow = 0;
            // Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
            // SparklineGroups.add gibt den Index der neu hinzugefügten Gruppe zurück
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // Schritt 6: Aktivieren Sie die Hochpunkt- und Tiefpunkt-Markierungen
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // Schritt 7: Speichern Sie die Arbeitsmappe
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
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
// Beispielwerte in A1:E1 schreiben
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Eine CellArea erstellen, die auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Eine Spalten-Sparkline zur Zielzelle hinzufügen
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Den Sparkline-Typ durch Lesen von group.Type bestätigen
System.out.println("Sparkline Type added: " + group.getType());
// Die Arbeitsmappe speichern
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
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Beispieldaten einfügen
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Eine CellArea erstellen, die auf F1 zeigt (Spalte 5, Zeile 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Eine Win/Loss-Sparkline hinzufügen (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Die Sparkline-Gruppe anpassen
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Die Farbe des Höchstpunkts auf Grün setzen
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Die Farbe des Tiefstpunkts auf Rot setzen
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// Die Farbe des Negativpunkts auf Orange setzen
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// Die Standardreihenfarbe festlegen (für positive Balken verwendet)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue-Näherung
group.setSeriesColor(seriesColor);
// Die Arbeitsmappe speichern
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**
Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```java
import com.aspose.cells.*;
// Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie das erste Arbeitsblatt
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Schritt 2: Füllen Sie Beispieldaten in Zeile 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Schritt 3: Fügen Sie eine Linien-Sparkline-Gruppe bei F1 hinzu
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Verwenden Sie die statische Factory-Methode
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Passen Sie die Farbe der Linien-Sparkline über CellsColor an
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Schritt 4: Fügen Sie eine Säulen-Sparkline-Gruppe bei F2 hinzu
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Verwenden Sie die statische Factory-Methode
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Passen Sie die Farbe der Säulen-Sparkline-Serie an
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Schritt 5: Fügen Sie eine Gewinn/Verlust (gestapelte) Sparkline-Gruppe bei F3 hinzu
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Verwenden Sie die statische Factory-Methode
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Passen Sie die Farbe der Gewinn/Verlust-Sparkline-Serie an
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Schritt 6: Speichern Sie die Arbeitsmappe
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
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
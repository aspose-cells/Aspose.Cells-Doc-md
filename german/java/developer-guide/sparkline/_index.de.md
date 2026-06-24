---
title: Sparklines in Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells ist eine Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt — Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Spalten- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, und jede kann in Bezug auf Farbe, Linienstärke, Hoch-/Tiefpunkte und Markierungen angepasst werden.

{{% /alert %}}

## **Einführung**

Sparklines sind winzige Diagramme in Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linie**, **Spalte** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Fähigkeit durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs im Namespace `Aspose.Cells.Charts` wider.

In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.getSparklineGroups().add(...)` erstellt, was ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil teilen. Wenn Sie `add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline in dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel geht durch jede der drei Sparkline-Typen, die von Aspose.Cells unterstützt werden — **Linie**, **Spalte** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte in einer Reihe und ist damit die natürlichste Wahl, um Trends über die Zeit darzustellen. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.LINE` an die `add`-Methode übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Reihe von Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Optional können Sie die zurückgegebene `SparklineGroup` anpassen. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.getLine().setColor(...)` festlegen (die eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Markierungen für Hoch-/Tiefpunkte umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot angepasst und Markierungen für die Hoch- und Tiefpunkte aktiviert.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Schritt 3: Erstellen Sie einen CellArea, der auf die Zielzelle F1 zeigt
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // Spalte F (0-indiziert)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // Zeile 1 (0-indiziert)
            dest.EndRow = 0;

            // Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 ein
            // SparklineGroups.add gibt den Index der neu hinzugefügten Gruppe zurück
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Schritt 6: Aktivieren Sie die Hoch- und Tiefpunktmarkierungen
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

## **Spalten-Sparklines**

Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie gut geeignet für Daten, deren Größe aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.COLUMN` an die `add`-Methode übergeben.

Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` auf.
5. Optional können Sie die resultierende `SparklineGroup` anpassen — zum Beispiel durch Setzen von `group.getType()`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Linien-Sparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken gezeichnet, was es einfach macht, positive und negative Beiträge auf einen Blick zu erkennen.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Beispielwerte in A1:E1 schreiben
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// CellArea erstellen, die auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Spalten-Sparkline zur Zielzelle hinzufügen
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Sparkline-Typ durch Lesen von group.Type bestätigen
System.out.println("Sparkline Type added: " + group.getType());

// Arbeitsmappe speichern
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die entwickelt wurde, um nur zwei Ergebnisse anzuzeigen: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) gezeichnet, und ein Null- oder negativer Wert wird als „Abwärts"-Balken (ein Verlust) gezeichnet. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehen/Nichtbestehen-Ergebnisse oder beliebige binäre Ergebnisse über die Zeit zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.STACKED` an die `add`-Methode übergeben wird. (Trotz des Namens ist `SparklineType.STACKED` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Werts nicht wichtig — nur sein Vorzeichen. Positive Werte werden zu Aufwärtsbalken und nicht-positive Werte werden zu Abwärtsbalken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` auf.
5. Optional können Sie die zurückgegebene `SparklineGroup` anpassen, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlustbalken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die vorherigen beiden Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert — und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

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

// Erstellen Sie einen CellArea, der auf F1 zeigt (Spalte 5, Zeile 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Fügen Sie eine Win/Loss-Sparkline hinzu (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Passen Sie die Sparkline-Gruppe an
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Setzen Sie die Farbe des Hochpunkts auf Grün
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Setzen Sie die Farbe des Tiefpunkts auf Rot
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Setzen Sie die Farbe des Negativpunkts auf Orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Setzen Sie die Standard-Serienfarbe (für positive Balken verwendet)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue-Annäherung
group.setSeriesColor(seriesColor);

// Speichern Sie die Arbeitsmappe
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien leicht isoliert zu überprüfen sind. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt zu legen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann eine andere Zielzelle oder einen anderen Bereich anvisieren. Zum Beispiel könnten Sie eine Linien-Sparkline in F1, eine Spalten-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — alle lesen aus denselben Quelldaten in Zeile 1 — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das kombinierte Beispiel unten erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```java
import com.aspose.cells.*;

// Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
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

// Schritt 4: Fügen Sie eine Spalten-Sparkline-Gruppe bei F2 hinzu
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Verwenden Sie die statische Factory-Methode
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Passen Sie die Farbe der Spalten-Sparkline-Serie an
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Schritt 5: Fügen Sie eine Win/Loss (gestapelte) Sparkline-Gruppe bei F3 hinzu
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Verwenden Sie die statische Factory-Methode
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Passen Sie die Farbe der Win/Loss-Sparkline-Serie an
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzigen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich teilen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines „Dashboard" von Visualisierungen in Zellen direkt innerhalb eines bestehenden Arbeitsblatts zu erstellen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbilds**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.getSparklineGroups()` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.getType()`** — der `SparklineType` (LINE, COLUMN oder STACKED). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung zurücklesen.
- **`group.getLine().setColor(...)`** — die Linienfarbe, ausgedrückt als eine `CellsColor`, die über `workbook.createCellsColor()` erstellt wurde. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline verwendet werden sollte.
- **`group.getLine().setWeight(...)`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremen.
- **Erste/Letzte/Negative Punktmarkierungen** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Weisen Sie `java.awt.Color` nicht direkt den Sparkline-Farbeigenschaften zu — sie erwarten den `CellsColor`-Typ aus `Aspose.Cells.Drawing`. Die `add`-Methode selbst gibt ein volltypisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.



{{< app/cells/assistant language="java" >}}
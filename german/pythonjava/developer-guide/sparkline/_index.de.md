---
title: Sparklines in Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells ist eine Python via Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt – Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Säulen- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, Python via Java-Bibliothek, Tabellenkalkulation, Sparklines, Liniensparkline, Säulensparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind Miniaturdiagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Säulen- und Gewinn/Verlust-Sparklines, die jeweils hinsichtlich Farbe, Linienstärke, Hoch-/Tiefpunkten und Markierungen angepasst werden können.

{{% /alert %}}

## **Einführung**

Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenreihe oder Datenspalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien**, **Säulen** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktion durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs wider, die sich im Namespace `Aspose.Cells.Charts` befinden.

In Aspose.Cells wird jede hinzugefügte Sparkline über `worksheet.getSparklineGroups().add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle sowie visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Hoch-/Tiefpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil gemeinsam nutzen. Wenn Sie `add` aufrufen und eine Datenreihe sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline in dieser Zelle. Ist Ihr Zielbereich breiter als eine Zelle, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel geht alle drei Sparkline-Typen durch, die von Aspose.Cells unterstützt werden — **Linien**, **Säulen** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Liniensparklines**

Eine Liniensparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl, um Trends im Zeitverlauf darzustellen. In Aspose.Cells wird eine Liniensparkline erstellt, indem `SparklineType.LINE` an die `add`-Methode übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie eine Datenreihe (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` auf. Das dritte Argument — `false` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Liniensparkline können Sie die Linienfarbe mit `group.getLine().getColor()` festlegen (was eine `CellsColor` aus `Aspose.Cells.Drawing` erwartet), die Linienstärke anpassen und Markierungen für Hoch-/Tiefpunkte ein- oder ausschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt in Zelle F1 eine Liniensparkline hinzu, die diese Werte nachzeichnet. Außerdem wird die Linienfarbe auf Rot gesetzt und Markierungen für die Hoch- und Tiefpunkte werden aktiviert.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Schritt 3: Erstellen Sie einen CellArea, der auf die Zielzelle F1 zeigt
dest = CellArea()
dest.setStartColumn(5)  # Spalte F (0-indiziert)
dest.setEndColumn(5)
dest.setStartRow(0)     # Zeile 1 (0-indiziert)
dest.setEndRow(0)

# Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
# SparklineGroups.add gibt den Index der neu hinzugefügten Gruppe zurück
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Schritt 6: Aktivieren Sie die Hochpunkt- und Tiefpunkt-Markierungen
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Schritt 7: Speichern Sie die Arbeitsmappe
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Säulensparklines**

Eine Säulensparkline rendert jeden Datenpunkt als vertikalen Balken. Damit eignet sie sich gut für Daten, deren Größe aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Säulensparkline, indem Sie `SparklineType.COLUMN` an die `add`-Methode übergeben.

Die Vorgehensweise spiegelt das Beispiel der Liniensparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel durch Setzen von `group.getType()`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Liniensparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Säulensparkline in F1. Negative Werte werden als nach unten verlaufende Balken dargestellt und positive Werte als nach oben verlaufende Balken, sodass positive und negative Beiträge auf einen Blick leicht erkennbar sind.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Schritt 2: Schreiben Sie Beispielwerte in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Schritt 4: Fügen Sie der Zielzelle eine Spalten-Sparkline hinzu
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Schritt 5: Bestätigen Sie den Sparkline-Typ durch Lesen von group.Type
print("Sparkline Type added: " + str(group.getType()))

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Säulensparkline, die dazu dient, nur zwei Ergebnisse darzustellen: Ein positiver Wert wird als "Aufwärts"-Balken (ein Gewinn) und ein null oder negativer Wert wird als "Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestehens-/Nichtbestehens-Ergebnisse oder beliebige binäre Ergebnisse im Zeitverlauf zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.STACKED` an die `add`-Methode übergeben wird. (Trotz des Namens ist `SparklineType.STACKED` der Enum-Wert, der verwendet wird, um das Gewinn/Verlust-Rendering anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Befüllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Werts nicht entscheidend — nur sein Vorzeichen. Positive Werte werden zu Aufwärtsbalken und nicht-positive Werte werden zu Abwärtsbalken.
3. Erstellen Sie einen `CellArea`, der die Zielzelle beschreibt.
4. Rufen Sie `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die vorherigen beiden Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert — und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Schritt 2: Füllen Sie Beispieldaten in Zeile 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spalte 5, Zeile 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # Zeile 1
dest.setEndRow(0)

# Schritt 4: Fügen Sie eine Win/Loss-Sparkline hinzu (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Schritt 5: Passen Sie die Sparkline-Gruppe an
# Aktivieren Sie Hoch- und Tiefpunktmarkierungen
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Setzen Sie die Hochpunktfarbe auf Grün
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Setzen Sie die Tiefpunktfarbe auf Rot
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Setzen Sie die Farbe der negativen Punkte auf Orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Setzen Sie die Standardreihenfarbe (verwendet für positive Balken)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien isoliert leicht überprüft werden können. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt einzufügen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann auf eine andere Zielzelle oder einen anderen Bereich abzielen. Beispielsweise könnten Sie eine Liniensparkline in F1, eine Säulensparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — alle lesen aus denselben Quelldaten in Zeile 1 — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das folgende kombinierte Beispiel erstellt eine einzelne Arbeitsmappe, befüllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile gleichzeitig demonstriert.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Schritt 2: Beispieldaten in Zeile 1 (A1:E1) einfügen
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Schritt 3: Fügen Sie eine Linien-Sparkline-Gruppe bei F1 hinzu
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Passen Sie die Linien-Sparkline-Farbe über CellsColor an
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Schritt 4: Fügen Sie eine Spalten-Sparkline-Gruppe bei F2 hinzu
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Passen Sie die Spalten-Sparkline-Serienfarbe an
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Schritt 5: Fügen Sie eine Win/Loss (Gestapelte) Sparkline-Gruppe bei F3 hinzu
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Passen Sie die Win/Loss-Sparkline-Serienfarbe an
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DunkelOrange
stackedGroup.setSeriesColor(stackedColor)

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzelnen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich gemeinsam nutzen oder verschiedene Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines "Dashboard" aus Zellen-Visualisierungen direkt innerhalb eines bestehenden Arbeitsblatts zu erstellen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbilds**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.getSparklineGroups()` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.getType()`** — der `SparklineType` (LINE, COLUMN oder STACKED). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zurücklesen, um den Typ zu bestätigen.
- **`group.getLine().getColor()`** — die Linienfarbe, ausgedrückt als eine `CellsColor`, die über `workbook.createCellsColor()` erstellt wurde. Dies ist die Eigenschaft, die für die Strichfarbe der Liniensparkline verwendet werden sollte.
- **`group.getLine().getWeight()`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Hoch-/Tiefpunkt-Markierungen** — Flags, die kleine Markierungen an den höchsten und niedrigsten Datenpunkten einschalten, nützlich zum Hervorheben von Extremwerten.
- **Markierungen für erste/letzte/negative Punkte** — Flags, die Markierungen an den ersten, letzten und negativen Datenpunkten ein- oder ausschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen sie der entsprechenden Eigenschaft zu. Weisen Sie `java.awt.Color` nicht direkt den Sparkline-Farbeigenschaften zu — sie erwarten den Typ `CellsColor` aus `Aspose.Cells.Drawing`. Die `add`-Methode selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen auf dem Rückgabewert verketten oder es in einer lokalen Variablen speichern und vor dem Speichern anpassen können.

{{< app/cells/assistant language="python" >}}
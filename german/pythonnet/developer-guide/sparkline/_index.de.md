---
title: Sparklines in Aspose.Cells for Python via .NET
linktitle: Sparklines
description: Aspose.Cells ist eine Python-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Erstellen von Sparklines unterstützt — kleinen Diagrammen, die in Arbeitsblattzellen platziert werden. Dieser Artikel erklärt, wie man Linien-, Spalten- und Gewinn/Verlust-Sparklines mit der Aspose.Cells-Bibliothek hinzufügt und anpasst.
keywords: Aspose.Cells, Python-Bibliothek, Tabellenkalkulation, Sparklines, Linien-Sparkline, Spalten-Sparkline, Gewinn/Verlust-Sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /de/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Erstellen von Sparklines in Arbeitsblattzellen. Sparklines sind kleine Diagramme, die in eine einzelne Zelle passen und eine schnelle visuelle Darstellung von Datentrends bieten. Aspose.Cells unterstützt Linien-, Spalten- und Gewinn/Verlust-Sparklines, die jeweils hinsichtlich Farbe, Linienstärke, Höchst-/Tiefstpunkten und Markierungen angepasst werden können.

{{% /alert %}}

## **Einführung**

Sparklines sind winzige Diagramme innerhalb von Zellen, die nützlich sind, wenn Sie einen schnellen Trend neben einer Datenzeile oder -spalte anzeigen möchten, ohne den Platz eines vollständigen Diagramms einzunehmen. Excel unterstützt drei Arten von Sparklines: **Linien**, **Spalten** und **Gewinn/Verlust**. Aspose.Cells spiegelt diese Funktionalität durch die `SparklineGroup`- und `SparklineGroupCollection`-APIs im Namespace `aspose.cells.charts` wider.

In Aspose.Cells wird jede Sparkline, die Sie hinzufügen, durch `worksheet.sparkline_groups.add(...)` erstellt, die ein `SparklineGroup`-Objekt zurückgibt. Sie können dieses Objekt dann verwenden, um den Sparkline-Typ, den Datenbereich, die Zielzelle und visuelle Eigenschaften wie Linienfarbe, Linienstärke, Markierungen und Höchst-/Tiefstpunkt-Indikatoren festzulegen.

{{% alert color="primary" %}}

Eine einzelne `SparklineGroup` kann eine oder mehrere Sparklines enthalten, die denselben Stil teilen. Wenn Sie `add` aufrufen und eine Datenzeile sowie eine einzelne Zielzelle übergeben, erhalten Sie eine Sparkline in dieser Zelle. Wenn Ihr Zielbereich breiter als eine Zelle ist, wird in jeder Zielzelle eine separate Sparkline gezeichnet, die alle denselben Stil und Datenbereich verwenden.

{{% /alert %}}

Dieser Artikel geht jede der drei von Aspose.Cells unterstützten Sparkline-Typen durch — **Linien**, **Spalten** und **Gewinn/Verlust** — und zeigt, wie man sie hinzufügt, ihre Farben anpasst und die resultierende Arbeitsmappe speichert.

## **Linien-Sparklines**

Eine Linien-Sparkline zeichnet eine durchgehende Linie durch die Datenpunkte einer Reihe und ist damit die natürlichste Wahl zur Darstellung von Trends im Zeitverlauf. In Aspose.Cells wird eine Linien-Sparkline erstellt, indem `SparklineType.Line` an die Methode `sparkline_groups.add` übergeben wird.

Der Arbeitsablauf ist derselbe wie für jeden anderen Sparkline-Typ:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie eine Zeile mit Quelldaten (zum Beispiel Zeile 1, Spalten A bis E) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt, in der die Sparkline gezeichnet wird.
4. Rufen Sie `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)` auf. Das dritte Argument — `False` — teilt Aspose.Cells mit, dass der Datenbereich horizontal (eine Zeile) und nicht vertikal (eine Spalte) ist.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an. Für eine Linien-Sparkline können Sie die Linienfarbe mit `group.line.color` festlegen (die eine `CellsColor` aus `aspose.cells.drawing` erwartet), die Linienstärke anpassen und Markierungen für Höchst-/Tiefstpunkte umschalten.
6. Speichern Sie die Arbeitsmappe.

Das folgende Beispiel erstellt eine Arbeitsmappe, schreibt die Werte 5, -3, 8, -2, 6 in die Zellen A1 bis E1 und fügt eine Linien-Sparkline in Zelle F1 hinzu, die diese Werte nachzeichnet. Es passt außerdem die Linienfarbe auf Rot an und aktiviert Markierungen für die Höchst- und Tiefstpunkte.

```python
import aspose.cells as ac
import System.Drawing

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Schritt 2: Schreiben Sie die Beispielwerte 5, -3, 8, -2, 6 in die Zellen A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Schritt 3: Erstellen Sie einen CellArea, der auf die Zielzelle F1 zeigt
dest = ac.CellArea()
dest.start_column = 5   # Spalte F (0-indiziert)
dest.end_column = 5
dest.start_row = 0      # Zeile 1 (0-indiziert)
dest.end_row = 0

# Schritt 4: Fügen Sie eine Linien-Sparkline von A1:E1 in F1 hinzu
# SparklineGroups.Add gibt den Index der neu hinzugefügten Gruppe zurück
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Schritt 5: Erstellen Sie eine rote CellsColor und weisen Sie sie der Sparkline-Linienfarbe zu
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Schritt 6: Aktivieren Sie die Hoch- und Tiefpunktmarkierungen
group.show_high_point = True
group.show_low_point = True

# Schritt 7: Speichern Sie die Arbeitsmappe
workbook.save("output_line.xlsx")
```

## **Spalten-Sparklines**

Eine Spalten-Sparkline stellt jeden Datenpunkt als vertikalen Balken dar. Dies macht sie besonders geeignet für Daten, deren Größe aussagekräftig ist — zum Beispiel monatliche Verkaufszahlen oder Zählungen. In Aspose.Cells erstellen Sie eine Spalten-Sparkline, indem Sie `SparklineType.Column` an die Methode `sparkline_groups.add` übergeben.

Die Vorgehensweise spiegelt das Beispiel der Linien-Sparkline wider:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie denselben Quellbereich (A1:E1) mit den Werten, die Sie visualisieren möchten.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)` auf.
5. Passen Sie optional die resultierende `SparklineGroup` an — zum Beispiel durch Festlegen von `group.type`, um den Typ zu bestätigen, oder durch Anpassen der Balkenfarbe.
6. Speichern Sie die Arbeitsmappe in einer separaten Ausgabedatei, damit sie das Beispiel der Linien-Sparkline nicht überschreibt.

Das folgende Beispiel schreibt die Werte 5, -3, 8, -2, 6 in A1:E1 und rendert eine Spalten-Sparkline in F1. Negative Werte werden als nach unten verlaufende Balken und positive Werte als nach oben verlaufende Balken dargestellt, sodass positive und negative Beiträge auf einen Blick leicht zu erkennen sind.

```python
import aspose.cells as ac

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Schritt 2: Schreiben Sie Beispielwerte in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Schritt 3: Erstellen Sie einen CellArea, der auf F1 zeigt (Spaltenindex 5, Zeilenindex 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Schritt 4: Fügen Sie eine Spalten-Sparkline zur Zielzelle hinzu
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Schritt 5: Bestätigen Sie den Sparkline-Typ durch Lesen von group.Type
print("Sparkline Type added: " + str(group.type))

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Gewinn/Verlust-Sparklines**

Eine Gewinn/Verlust-Sparkline ist eine spezielle Variante der Spalten-Sparkline, die darauf ausgelegt ist, nur zwei Ergebnisse anzuzeigen: Ein positiver Wert wird als „Aufwärts"-Balken (ein Gewinn) und ein Null- oder negativer Wert als „Abwärts"-Balken (ein Verlust) dargestellt. Gewinn/Verlust-Sparklines werden häufig verwendet, um Sequenzen von Gewinnen und Verlusten, Bestanden/Nicht bestanden-Ergebnisse oder beliebige binäre Ergebnisse im Zeitverlauf zu visualisieren.

In Aspose.Cells wird eine Gewinn/Verlust-Sparkline erstellt, indem `SparklineType.Stacked` an die Methode `sparkline_groups.add` übergeben wird. (Trotz des Namens ist `SparklineType.Stacked` der Enum-Wert, der verwendet wird, um die Gewinn/Verlust-Darstellung anzufordern.)

Die Vorgehensweise ist dieselbe wie bei den anderen beiden Typen:

1. Erstellen Sie eine neue `Workbook` und greifen Sie auf das erste Arbeitsblatt zu.
2. Füllen Sie den Quellbereich. Da Gewinn/Verlust-Sparklines jeden Wert entweder als Gewinn oder Verlust behandeln, ist die Größe des Werts nicht entscheidend — nur sein Vorzeichen. Positive Werte werden zu Aufwärts-Balken und nicht-positive Werte zu Abwärts-Balken.
3. Erstellen Sie eine `CellArea`, die die Zielzelle beschreibt.
4. Rufen Sie `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)` auf.
5. Passen Sie optional die zurückgegebene `SparklineGroup` an, zum Beispiel durch Festlegen von Akzentfarben für die Gewinn- und Verlust-Balken.
6. Speichern Sie die Arbeitsmappe unter einem eindeutigen Dateinamen, damit alle drei Beispiele auf der Festplatte koexistieren können.

Das folgende Beispiel verwendet dieselben Eingabedaten wie die vorherigen beiden Abschnitte. Die Werte 5, -3, 8, -2, 6 werden als Gewinn, Verlust, Gewinn, Verlust, Gewinn interpretiert — und die in F1 gezeichnete Sparkline spiegelt genau dieses Muster wider.

```python
import aspose.cells as ac
import System.Drawing

# Schritt 1: Erstellen Sie eine Workbook und holen Sie das erste Arbeitsblatt
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Schritt 2: Füllen Sie Beispieldaten in Zeile 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Schritt 3: Erstellen Sie eine CellArea, die auf F1 zeigt (Spalte 5, Zeile 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # Zeile 1
dest.end_row = 0

# Schritt 4: Fügen Sie eine Win/Loss-Sparkline hinzu (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Schritt 5: Passen Sie die Sparkline-Gruppe an
# Aktivieren Sie Hochpunkt- und Tiefpunkt-Markierungen
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Setzen Sie die Hochpunktfarbe auf Grün
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Setzen Sie die Tiefpunktfarbe auf Rot
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Setzen Sie die Farbe der negativen Punkte auf Orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Setzen Sie die Standardreihenfarbe (wird für positive Balken verwendet)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Kombinieren aller drei Sparkline-Typen**

Die vorherigen drei Beispiele erzeugen jeweils ihre eigene Arbeitsmappe, damit die Ausgabedateien isoliert leicht zu überprüfen sind. In einem realen Szenario möchten Sie jedoch oft mehrere Datenreihen nebeneinander vergleichen. Der sauberste Weg, dies zu tun, besteht darin, mehr als eine Sparkline-Gruppe in dasselbe Arbeitsblatt einzufügen, wobei jede Gruppe einen anderen Stil rendert.

Sie können mehrere `SparklineGroup`-Objekte zur selben `SparklineGroupCollection` hinzufügen, und jede Gruppe kann auf eine andere Zielzelle oder einen anderen Bereich abzielen. Beispielsweise könnten Sie eine Linien-Sparkline in F1, eine Spalten-Sparkline in F2 und eine Gewinn/Verlust-Sparkline in F3 platzieren — alle lesen aus denselben Quelldaten in Zeile 1 — sodass der Leser drei verschiedene visuelle Darstellungen derselben Zahlen sehen kann.

Das kombinierte Beispiel unten erstellt eine einzelne Arbeitsmappe, füllt Zeile 1 mit den Werten 5, -3, 8, -2, 6 und fügt dann drei Sparkline-Gruppen in den Zellen F1, F2 und F3 hinzu — eine von jedem Typ — sodass die resultierende Datei alle drei Sparkline-Stile auf einmal demonstriert.

```python
import aspose.cells as ac
import System.Drawing

# Schritt 1: Erstellen Sie eine Arbeitsmappe und holen Sie sich das erste Arbeitsblatt
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Schritt 2: Füllen Sie Beispieldaten in Zeile 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Schritt 3: Fügen Sie eine Liniendiagramm-Sparkline-Gruppe bei F1 hinzu
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Passen Sie die Farbe der Liniendiagramm-Sparkline über CellsColor an
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Schritt 4: Fügen Sie eine Spalten-Sparkline-Gruppe bei F2 hinzu
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Passen Sie die Serienfarbe der Spalten-Sparkline an
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Schritt 5: Fügen Sie eine Win/Loss (gestapelte) Sparkline-Gruppe bei F3 hinzu
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Passen Sie die Serienfarbe der Win/Loss-Sparkline an
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Schritt 6: Speichern Sie die Arbeitsmappe
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Wenn Sie mehrere Sparkline-Gruppen in einem einzelnen Arbeitsblatt kombinieren, ist jede Gruppe unabhängig. Sie können denselben Quellbereich teilen oder unterschiedliche Quellbereiche verwenden, und sie können unabhängig voneinander gestaltet werden. Dies macht es einfach, ein kleines „Dashboard" mit Zellen-Visualisierungen direkt innerhalb eines bestehenden Arbeitsblatts zu erstellen.

{{% /alert %}}

## **Anpassen des Sparkline-Erscheinungsbilds**

Sobald eine `SparklineGroup` erstellt und zu `worksheet.sparkline_groups` hinzugefügt wurde, können Sie mehrere ihrer visuellen Eigenschaften lesen oder ändern, bevor Sie die Arbeitsmappe speichern. Die am häufigsten angepassten Eigenschaften sind:

- **`group.type`** — der `SparklineType` (Line, Column oder Stacked). Er wird beim Hinzufügen der Gruppe festgelegt, aber Sie können ihn zur Bestätigung wieder auslesen.
- **`group.line.color`** — die Linienfarbe, ausgedrückt als `CellsColor`, erstellt über `workbook.create_cells_color()`. Dies ist die Eigenschaft, die für die Strichfarbe der Linien-Sparkline zu verwenden ist.
- **`group.line.weight`** — die Linienstärke in Punkten. Höhere Werte erzeugen dickere Linien.
- **Höchst-/Tiefstpunkt-Markierungen** — Flags, die kleine Markierungen auf den höchsten und niedrigsten Datenpunkten einschalten, nützlich zur Hervorhebung von Extremen.
- **Erste/Letzte/Negative-Punkt-Markierungen** — Flags, die Markierungen auf den ersten, letzten und negativen Datenpunkten umschalten.

Um eine Farbe zu ändern, erstellen Sie immer eine `CellsColor`-Instanz und weisen Sie sie der entsprechenden Eigenschaft zu. Sparkline-Farbeigenschaften erwarten den `CellsColor`-Typ aus `aspose.cells.drawing` — weisen Sie ihnen nicht direkt einen rohen Farbwert zu. Die Methode `sparkline_groups.add` selbst gibt ein vollständig typisiertes `SparklineGroup`-Objekt zurück, sodass Sie Eigenschaftszuweisungen am Rückgabewert verketten oder ihn in einer lokalen Variable speichern und vor dem Speichern anpassen können.



{{< app/cells/assistant language="python" >}}
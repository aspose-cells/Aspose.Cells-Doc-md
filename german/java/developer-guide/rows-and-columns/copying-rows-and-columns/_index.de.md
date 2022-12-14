---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 30
url: /de/java/copying-rows-and-columns/
---
## **Einführung**
Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.

Wenn eine Zeile (oder Spalte) kopiert wird, werden die darin enthaltenen Daten, einschließlich Formeln – mit aktualisierten Verweisen – und Werten, Kommentaren, Formatierungen, ausgeblendeten Zellen, Bildern und anderen Zeichnungsobjekten ebenfalls kopiert.
## **Kopieren von Zeilen und Spalten mit Microsoft Excel**
1. Wählen Sie die Zeile oder Spalte aus, die Sie kopieren möchten.
1.  Um Zeilen oder Spalten zu kopieren, klicken Sie auf**Kopieren** auf der**Standard** Symbolleiste oder drücken Sie**STRG**+**C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts neben der Stelle aus, an der Sie Ihre Auswahl kopieren möchten.
1.  Klicken Sie beim Kopieren von Zeilen oder Spalten auf**Kopiert Cells** auf der**Einfügung** Speisekarte.

{{% alert color="primary" %}} 

 Wenn Sie klicken**Paste** auf der**Standard** Symbolleiste oder drücken Sie**STRG**+** V** anstatt auf einen Befehl auf der zu klicken**Einfügen**-Menü werden alle Inhalte der Zielzellen ersetzt.

{{% /alert %}} 

## **Einzelne Zeile kopieren**

 Aspose.Cells bietet die[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Klasse. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichenobjekte aus der Quellzeile in die Zielzeile.

 Das[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\))-Methode nimmt die folgenden Parameter an:

-  die Quelle[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Objekt,
- den Quellzeilenindex und
- der Zielzeilenindex.

 Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blatts oder in ein anderes Blatt zu kopieren. Das[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielzeile nicht explizit festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie Sie eine Zeile in einem Arbeitsblatt kopieren. Es verwendet eine Vorlage Microsoft Excel-Datei und kopiert die zweite Zeile (komplett mit Daten, Formatierung, Kommentaren, Bildern usw.) und fügt sie in die 12. Zeile im selben Arbeitsblatt ein.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Die folgende Ausgabe wird generiert, wenn der folgende Code ausgeführt wird.

**Die Zeile wird mit höchster Präzision und Genauigkeit kopiert** 

![todo: Bild_alt_Text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Beim Kopieren von Zeilen ist es wichtig, zusammengehörige Bilder, Diagramme oder andere Zeichenobjekte zu beachten, da dies bei Microsoft Excel dasselbe ist:

1. Wenn der Quellzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Anfangszeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}} 

## **Kopieren mehrerer Zeilen**

 Sie können auch mehrere Zeilen auf ein neues Ziel kopieren, während Sie die verwenden[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))-Methode, die einen zusätzlichen Parameter vom Typ Integer verwendet, um die Anzahl der zu kopierenden Quellzeilen anzugeben.

Unten sehen Sie eine Momentaufnahme der Eingabetabelle mit 3 Datenzeilen, während das unten bereitgestellte Code-Snippet alle 3 Zeilen ab der 7. Zeile an eine neue Position kopiert.

![todo: Bild_alt_Text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Hier ist die resultierende Tabellenansicht nach dem Ausführen des obigen Code-Snippets.

![todo: Bild_alt_Text](copy-rows-and-columns_4.png)

## **Einzelne Spalte kopieren**

 Aspose.Cells bietet die[copySpalte](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Klasse kopiert diese Methode alle Arten von Daten, einschließlich Formeln – mit aktualisierten Referenzen – und Werten, Kommentaren, Zellformaten, ausgeblendeten Zellen, Bildern und anderen Zeichnungsobjekten aus der Quellspalte in die Zielspalte.

 Das[copySpalte](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))-Methode nimmt die folgenden Parameter an:

-  die Quelle[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Objekt,
- Quellspaltenindex und
- der Zielspaltenindex.

 Verwenden Sie die[copySpalte](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))-Methode zum Kopieren einer Spalte innerhalb eines Blatts oder in ein anderes Blatt.

In diesem Beispiel wird eine Spalte aus einem Arbeitsblatt kopiert und in ein Arbeitsblatt in einer anderen Arbeitsmappe eingefügt.

**Eine Spalte wird von einer Arbeitsmappe in eine andere kopiert** 

![todo: Bild_alt_Text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Kopieren mehrerer Spalten**

 Ähnlich zu[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) )-Methode bieten die Aspose.Cells-APIs auch die[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int))-Methode, um mehrere Quellspalten an einen neuen Speicherort zu kopieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

So sehen Quell- und Ergebnistabellen in Excel aus.

![todo: Bild_alt_Text](copy-rows-and-columns_7.png)

![todo: Bild_alt_Text](copy-rows-and-columns_8.png)


## **Einfügen von Zeilen/Spalten mit Einfügeoptionen**
 Aspose.Cells bietet jetzt[Optionen einfügen](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) während der Verwendung von Funktionen[Zeilen kopieren](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) und[Spalten kopieren](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Es ermöglicht die Einstellung geeigneter Einfügeoptionen ähnlich wie in Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}


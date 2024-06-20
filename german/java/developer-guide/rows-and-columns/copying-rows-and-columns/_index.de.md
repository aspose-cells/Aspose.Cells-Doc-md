---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 30
url: /de/java/copying-rows-and-columns/
---

## **Einführung**
Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.

Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten, einschließlich Formeln - mit aktualisierten Verweisen - und Werten, Kommentare, Formatierungen, versteckte Zellen, Bilder und andere Zeichenobjekte ebenfalls kopiert.
## **Kopieren von Zeilen und Spalten mit Microsoft Excel**
1. Wählen Sie die zu kopierende Zeile oder Spalte aus.
1. Zum Kopieren von Zeilen oder Spalten klicken Sie auf **Kopieren** in der **Standard**-Symbolleiste oder drücken Sie **STRG**+**C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Position aus, an der Sie Ihre Auswahl kopieren möchten.
1. Beim Kopieren von Zeilen oder Spalten klicken Sie auf **Kopierte Zellen** im **Einfügen**-Menü.

{{% alert color="primary" %}} 

Wenn Sie auf **Einfügen** in der **Standard**-Symbolleiste klicken oder **STRG**+**V** drücken, anstatt ein Befehl im **Einfügen**-Menü zu klicken, werden die Inhalte der Zielzellen ersetzt.

{{% /alert %}} 

## **Kopieren einer einzelnen Zeile**

Aspose.Cells bietet die [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) Methode der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Klasse. Diese Methode kopiert alle Arten von Daten einschließlich Formeln, Werten, Kommentaren, Zellformaten, versteckten Zellen, Bildern und anderen Zeichenobjekten von der Quellzeile zur Zielzeile.

Die [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) Methode akzeptiert die folgenden Parameter:

- das Quell [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Objekt,
- den Index der Quellzeile, und
- den Index der Zielzeile.

Verwenden Sie diese Methode, um eine Zeile innerhalb eines Arbeitsblatts oder in ein anderes Arbeitsblatt zu kopieren. Die [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie zum Beispiel nicht explizit die Höhe der Zielzeile festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es wird eine Vorlagen-Excel-Datei verwendet, und die zweite Zeile (vollständig mit Daten, Formatierung, Kommentaren, Bildern usw.) wird in die 12. Zeile im selben Arbeitsblatt eingefügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Die folgende Ausgabe wird generiert, wenn der unten stehende Code ausgeführt wird.

**Die Zeile wird mit höchster Präzision und Genauigkeit kopiert** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Beim Kopieren von Zeilen ist es wichtig, darauf hinzuweisen, dass damit verbundene Bilder, Diagramme oder andere Zeichenobjekte genauso wie bei Microsoft Excel behandelt werden:

1. Wenn der Quellzeilenindex 5 beträgt, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Startzeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}} 

## **Mehrere Zeilen kopieren**

Sie können auch mehrere Zeilen auf ein neues Ziel kopieren und dabei die [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) Methode verwenden, die einen zusätzlichen Parameter vom Typ Integer akzeptiert, um die Anzahl der zu kopierenden Quellzeilen anzugeben.

Nachfolgend sehen Sie einen Ausschnitt des Eingabe-Arbeitsblatts mit 3 Zeilen Daten. Der unten stehende Codeausschnitt kopiert alle 3 Zeilen an einen neuen Ort, beginnend mit der 7. Zeile.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Hier ist die resultierende Ansicht des Arbeitsblatts nach Ausführung des obigen Codeausschnitts.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Einzelne Spalte kopieren**

Aspose.Cells bietet die [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) Methode der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Klasse, diese Methode kopiert alle Arten von Daten, einschließlich Formeln - mit aktualisierten Referenzen - und Werten, Kommentaren, Zellformaten, versteckten Zellen, Bildern und anderen Zeichenobjekten von der Quellspalte zur Zielspalte.

Die [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) Methode akzeptiert die folgenden Parameter:

- das Quell [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Objekt,
- Quellspaltenindex, und
- der Zielspaltenindex.

Verwenden Sie die [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) Methode, um eine Spalte innerhalb eines Arbeitsblatts oder in ein anderes Arbeitsblatt zu kopieren.

Dieses Beispiel kopiert eine Spalte aus einem Arbeitsblatt und fügt sie in ein Arbeitsblatt in einer anderen Arbeitsmappe ein.

**Eine Spalte wird von einer Arbeitsmappe in eine andere kopiert** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Mehrere Spalten kopieren**

Ähnlich wie die [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))-Methode bieten die Aspose.Cells-APIs auch die [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int))-Methode, um mehrere Quellspalten an eine neue Position zu kopieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Hier sehen Sie, wie die Quell- und Ergebnis-Arbeitsblätter in Excel aussehen.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Zeilen/Spalten mit Einfügeoptionen einfügen**
Aspose.Cells bietet nun [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) während der Verwendung der Funktionen [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) und [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Es ermöglicht das Festlegen entsprechender Einfügeoptionen ähnlich wie in Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}


---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 40
url: /de/net/copying-rows-and-columns/
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

## **Einfügen von Zeilen und Spalten mit Einfügeoptionen mit Microsoft Excel**

1. Wählen Sie die Zellen aus, die die Daten oder andere Attribute enthalten, die Sie kopieren möchten.
1.  Klicken Sie auf der Registerkarte Start auf**Kopieren**.
1.  Klicken Sie auf die erste Zelle im gewünschten Bereich**Einfügen** was du kopiert hast.
1.  Klicken Sie auf der Registerkarte Startseite auf den Pfeil neben**Paste** , und wählen Sie dann aus**Paste** Speziell.
1.  Wähle aus**Optionen** Sie wollen.

## **Mit Aspose.Cells**

## **Kopieren einzelner Zeilen**

 Aspose.Cells bietet die[**Zeile kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichenobjekte aus der Quellzeile in die Zielzeile.

 Das[**Zeile kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Die Methode nimmt die folgenden Parameter an:

-  die Quelle[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Objekt,
- den Quellzeilenindex und
- der Zielzeilenindex.

 Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blatts oder in ein anderes Blatt zu kopieren. Das[**Zeile kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielzeile nicht explizit festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie Sie eine Zeile in einem Arbeitsblatt kopieren. Es verwendet eine Vorlage Microsoft Excel-Datei und kopiert die zweite Zeile (komplett mit Daten, Formatierung, Kommentaren, Bildern usw.) und fügt sie in die 12. Zeile im selben Arbeitsblatt ein.

 Sie können den Schritt zum Abrufen der Quellzeilenhöhe mit überspringen[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) -Methode und legt dann die Zielzeilenhöhe mithilfe von fest[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) Methode als die[**Zeile kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)-Methode kümmert sich automatisch um die Zeilenhöhe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Beim Kopieren von Zeilen ist es wichtig, zusammengehörige Bilder, Diagramme oder andere Zeichenobjekte zu beachten, da dies bei Microsoft Excel dasselbe ist:

1. Wenn der Quellzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Anfangszeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}}

## **Kopieren mehrerer Zeilen**

Sie können auch mehrere Zeilen auf ein neues Ziel kopieren, während Sie die verwenden[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)-Methode, die einen zusätzlichen Parameter vom Typ Integer akzeptiert, um die Anzahl der zu kopierenden Quellzeilen anzugeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Spalten kopieren**

 Aspose.Cells bietet die[**Spalte kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse kopiert diese Methode alle Arten von Daten, einschließlich Formeln – mit aktualisierten Referenzen – und Werten, Kommentaren, Zellformaten, ausgeblendeten Zellen, Bildern und anderen Zeichnungsobjekten aus der Quellspalte in die Zielspalte.

 Das[**Spalte kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Die Methode nimmt die folgenden Parameter an:

-  die Quelle[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Objekt,
- Quellspaltenindex und
- der Zielspaltenindex.

 Verwenden Sie die[**Spalte kopieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Methode zum Kopieren einer Spalte innerhalb eines Blattes oder in ein anderes Blatt.

In diesem Beispiel wird eine Spalte aus einem Arbeitsblatt kopiert und in ein Arbeitsblatt in einer anderen Arbeitsmappe eingefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Kopieren mehrerer Spalten**

 Ähnlich zu[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) -Methode bieten die Aspose.Cells-APIs auch die[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)-Methode, um mehrere Quellspalten an einen neuen Speicherort zu kopieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Einfügen von Zeilen/Spalten mit Einfügeoptionen**

 Aspose.Cells bietet jetzt[**Optionen einfügen**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) während der Verwendung von Funktionen[**Zeilen kopieren**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) und[**Spalten kopieren**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Es erlaubt, ähnlich wie in Excel, die entsprechende Einfügeoption einzustellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}


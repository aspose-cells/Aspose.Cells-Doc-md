---
title: Zeilen und Spalten kopieren
type: docs
weight: 40
url: /de/net/copying-rows-and-columns/
description: In diesem Artikel wird gezeigt, wie Sie Zeilen und Spalten über Aspose.Cells for .NET API kopieren.
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **Einführung**

Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.
Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten, einschließlich Formeln – mit aktualisierten Referenzen – sowie Werte, Kommentare, Formatierungen, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte kopiert.

##  **So kopieren Sie Zeilen und Spalten mit Microsoft Excel**

1. Wählen Sie die Zeile oder Spalte aus, die Sie kopieren möchten.
1.  Um Zeilen oder Spalten zu kopieren, klicken Sie auf**Kopieren** auf der**Standard** Symbolleiste oder drücken Sie**CTRL**+*C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Stelle aus, an der Sie Ihre Auswahl kopieren möchten.
1.  Klicken Sie beim Kopieren von Zeilen oder Spalten auf**Kopiert Cells** auf der**Einfügen** Speisekarte.

{{% alert color="primary" %}}

 Wenn Sie klicken**Paste** auf der**Standard** Symbolleiste oder drücken Sie**CTRL**+**V**, anstatt auf einen Befehl im **Einfügen zu klicken**Im Menü werden alle Inhalte der Zielzellen ersetzt.

{{% /alert %}}

##  **So fügen Sie Zeilen und Spalten mithilfe der Einfügeoptionen mit Microsoft Excel ein**

1. Wählen Sie die Zellen aus, die die Daten oder andere Attribute enthalten, die Sie kopieren möchten.
1. Klicken Sie auf der Registerkarte „Startseite“ auf *Kopieren**.
1.  Klicken Sie auf die erste Zelle im gewünschten Bereich**Paste** was du kopiert hast.
1.  Klicken Sie auf der Registerkarte „Startseite“ auf den Pfeil neben**Einfügen** und wählen Sie dann **Einfügen** Besonders.
1.  Wähle aus**Optionen** Sie wollen.

##  **So kopieren Sie Zeilen und Spalten mit Aspose.Cells for .NET**

##  **So kopieren Sie einzelne Zeilen**

 Aspose.Cells bietet die[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte, von der Quellzeile in die Zielzeile.

 Der[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Die Methode benötigt die folgenden Parameter:

-  die Quelle[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Objekt,
- der Quellzeilenindex und
- der Zielzeilenindex.

 Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blattes oder in ein anderes Blatt zu kopieren. Der[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Die Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielzeile nicht explizit festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es verwendet eine Excel-Vorlage Microsoft, kopiert die zweite Zeile (komplett mit Daten, Formatierungen, Kommentaren, Bildern usw.) und fügt sie in die 12. Zeile desselben Arbeitsblatts ein.

 Sie können den Schritt zum Ermitteln der Quellzeilenhöhe mit überspringen[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) Methode und legt dann die Zielzeilenhöhe mithilfe der fest[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) Methode wie die[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Die Methode kümmert sich automatisch um die Zeilenhöhe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Beim Kopieren von Zeilen ist es wichtig, zugehörige Bilder, Diagramme oder andere Zeichenobjekte zu beachten, da dies auch bei Microsoft Excel der Fall ist:

1. Wenn der Quellzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Startzeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}}

##  **So kopieren Sie mehrere Zeilen**

Sie können während der Verwendung auch mehrere Zeilen an ein neues Ziel kopieren[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)Methode, die einen zusätzlichen Parameter vom Typ Integer benötigt, um die Anzahl der zu kopierenden Quellzeilen anzugeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **So kopieren Sie Spalten**

 Aspose.Cells bietet die[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse kopiert diese Methode alle Arten von Daten, einschließlich Formeln – mit aktualisierten Referenzen – sowie Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte aus der Quellspalte in die Zielspalte.

 Der[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Die Methode benötigt die folgenden Parameter:

-  die Quelle[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Objekt,
- Quellspaltenindex und
- der Zielspaltenindex.

 Benutzen Sie die[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Methode zum Kopieren einer Spalte innerhalb eines Blattes oder in ein anderes Blatt.

In diesem Beispiel wird eine Spalte aus einem Arbeitsblatt kopiert und in ein Arbeitsblatt in einer anderen Arbeitsmappe eingefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **So kopieren Sie mehrere Spalten**

 Ähnlich zu[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) Methode stellen die Aspose.Cells-APIs auch die bereit[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)Methode, um mehrere Quellspalten an einen neuen Speicherort zu kopieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **So fügen Sie Zeilen und Spalten mit Einfügeoptionen ein**

 Aspose.Cells bietet jetzt[**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) während der Verwendung von Funktionen[**Zeilen kopieren**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) Und[**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Es ermöglicht, die entsprechende Einfügeoption ähnlich wie in Excel festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}


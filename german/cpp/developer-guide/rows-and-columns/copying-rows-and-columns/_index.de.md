---
title: Zeilen und Spalten kopieren
type: docs
weight: 20
url: /de/cpp/copying-rows-and-columns/
---
##  **Einführung**
Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.
Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten, einschließlich Formeln – mit aktualisierten Referenzen – sowie Werte, Kommentare, Formatierungen, ausgeblendete Zellen, Bilder und andere Zeichenobjekte kopiert.
##  **Kopieren von Zeilen und Spalten mit Microsoft Excel**
1. Wählen Sie die Zeile oder Spalte aus, die Sie kopieren möchten.
1.  Um Zeilen oder Spalten zu kopieren, klicken Sie auf**Kopieren** auf der**Standard** Symbolleiste oder drücken Sie**CTRL**+*C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Stelle aus, an der Sie Ihre Auswahl kopieren möchten.
1.  Klicken Sie beim Kopieren von Zeilen oder Spalten auf**Kopiert Cells** auf der**Einfügen** Speisekarte.

{{% alert color="primary" %}} 

 Wenn Sie klicken**Paste** auf der**Standard** Symbolleiste oder drücken Sie**CTRL**+**V**, anstatt auf einen Befehl im **Einfügen zu klicken** Im Menü wird der Inhalt der Zielzellen ersetzt.

{{% /alert %}} 
##  **Verwenden Sie Aspose.Cells**
###  **Zeilen kopieren**
Aspose.Cells stellt die CopyRow-Methode der Klasse Aspose::Cells::ICells bereit. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte, von der Quellzeile in die Zielzeile.

Die CopyRow-Methode akzeptiert die folgenden Parameter:

- das Quellobjekt Cells,
- der Quellzeilenindex und
- der Zielzeilenindex.

Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blattes oder in ein anderes Blatt zu kopieren. Die CopyRow-Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielzeile nicht explizit festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es verwendet eine Excel-Vorlage Microsoft, kopiert die zweite Zeile (komplett mit Daten, Formatierungen, Kommentaren, Bildern usw.) und fügt sie in die 12. Zeile desselben Arbeitsblatts ein.

 Sie können den Schritt zum Ermitteln der Quellzeilenhöhe mit überspringen**GetRowHeigh** Methode und legt dann die Zielzeilenhöhe mithilfe der fest**SetRowHeight** Methode wie die**CopyRow** Die Methode kümmert sich automatisch um die Zeilenhöhe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Beim Kopieren von Zeilen ist es wichtig, zugehörige Bilder, Diagramme oder andere Zeichenobjekte zu beachten, da dies auch bei Microsoft Excel der Fall ist:

1. Wenn der Quellzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Startzeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}} 
###  **Spalten kopieren**
Aspose.Cells stellt die CopyColumn-Methode der Klasse Aspose::Cells::ICells bereit. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln – mit aktualisierten Referenzen – sowie Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte aus der Quelle Spalte in die Zielspalte.

Die CopyColumn-Methode akzeptiert die folgenden Parameter:

- das Quellobjekt Cells,
- Quellspaltenindex und
- der Zielspaltenindex.

Verwenden Sie die CopyColumn-Methode, um eine Spalte innerhalb eines Blatts oder in ein anderes Blatt zu kopieren.

In diesem Beispiel wird eine Spalte aus einem Arbeitsblatt kopiert und in ein Arbeitsblatt in einer anderen Arbeitsmappe eingefügt.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}

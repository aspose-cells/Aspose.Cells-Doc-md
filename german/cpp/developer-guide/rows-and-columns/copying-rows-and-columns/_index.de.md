---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 20
url: /de/cpp/copying-rows-and-columns/
---
## **Einführung**
Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.
Wenn eine Zeile (oder Spalte) kopiert wird, werden die darin enthaltenen Daten, einschließlich Formeln – mit aktualisierten Referenzen – und Werte, Kommentare, Formatierungen, ausgeblendete Zellen, Bilder und andere Zeichnungsobjekte ebenfalls kopiert.
## **Kopieren von Zeilen und Spalten mit Microsoft Excel**
1. Wählen Sie die Zeile oder Spalte aus, die Sie kopieren möchten.
1.  Um Zeilen oder Spalten zu kopieren, klicken Sie auf**Kopieren** auf der**Standard** Symbolleiste oder drücken Sie**STRG**+**C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts neben der Stelle aus, an der Sie Ihre Auswahl kopieren möchten.
1.  Klicken Sie beim Kopieren von Zeilen oder Spalten auf**Kopiert Cells** auf der**Einfügung** Speisekarte.

{{% alert color="primary" %}} 

 Wenn Sie klicken**Paste** auf der**Standard** Symbolleiste oder drücken Sie**STRG**+** V** anstatt auf einen Befehl auf der zu klicken**Einfügen**-Menü wird der Inhalt der Zielzellen ersetzt.

{{% /alert %}} 
## **Mit Aspose.Cells**
### **Zeilen kopieren**
Aspose.Cells stellt die Methode CopyRow der Klasse Aspose::Cells::ICells bereit. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichenobjekte aus der Quellzeile in die Zielzeile.

Die CopyRow-Methode akzeptiert die folgenden Parameter:

- das Quellobjekt Cells,
- den Quellzeilenindex und
- der Zielzeilenindex.

Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blatts oder in ein anderes Blatt zu kopieren. Die CopyRow-Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielzeile nicht explizit festlegen, dieser Wert wird ebenfalls kopiert.

Das folgende Beispiel zeigt, wie Sie eine Zeile in einem Arbeitsblatt kopieren. Es verwendet eine Vorlage Microsoft Excel-Datei und kopiert die zweite Zeile (komplett mit Daten, Formatierung, Kommentaren, Bildern usw.) und fügt sie in die 12. Zeile im selben Arbeitsblatt ein.

 Sie können den Schritt zum Abrufen der Quellzeilenhöhe mit überspringen**GetRowHeigh** -Methode und legt dann die Zielzeilenhöhe mithilfe von fest**SetRowHeight** Methode als die**Zeile kopieren** -Methode kümmert sich automatisch um die Zeilenhöhe.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

Beim Kopieren von Zeilen ist es wichtig, verwandte Bilder, Diagramme oder andere Zeichnungsobjekte zu beachten, da dies bei Microsoft Excel der Fall ist:

1. Wenn der Quellzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Anfangszeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}} 
### **Spalten kopieren**
Aspose.Cells stellt die CopyColumn-Methode der Aspose::Cells::ICells-Klasse bereit, diese Methode kopiert alle Arten von Daten, einschließlich Formeln – mit aktualisierten Referenzen – und Werten, Kommentaren, Zellformaten, versteckten Zellen, Bildern und anderen Zeichnungsobjekten aus der Quelle Spalte in die Zielspalte.

Die CopyColumn-Methode akzeptiert die folgenden Parameter:

- das Quellobjekt Cells,
- Quellspaltenindex und
- der Zielspaltenindex.

Verwenden Sie die CopyColumn-Methode, um eine Spalte innerhalb eines Blatts oder in ein anderes Blatt zu kopieren.

In diesem Beispiel wird eine Spalte aus einem Arbeitsblatt kopiert und in ein Arbeitsblatt in einer anderen Arbeitsmappe eingefügt.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}

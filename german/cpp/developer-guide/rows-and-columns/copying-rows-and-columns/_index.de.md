---
title: Kopieren von Zeilen und Spalten
type: docs
weight: 20
url: /de/cpp/copying-rows-and-columns/
---

## **Einführung**
Manchmal müssen Zeilen und Spalten in einem Arbeitsblatt kopiert werden, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.
Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten wie Formeln - mit aktualisierten Referenzen - und Werte, Kommentare, Formatierungen, ausgeblendete Zellen, Bilder und andere Zeichenobjekte ebenfalls kopiert.
## **Kopieren von Zeilen und Spalten mit Microsoft Excel**
1. Wählen Sie die zu kopierende Zeile oder Spalte aus.
1. Zum Kopieren von Zeilen oder Spalten klicken Sie auf **Kopieren** in der **Standard**-Symbolleiste oder drücken Sie **STRG**+**C**.
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Position aus, an der Sie Ihre Auswahl kopieren möchten.
1. Beim Kopieren von Zeilen oder Spalten klicken Sie auf **Kopierte Zellen** im **Einfügen**-Menü.

{{% alert color="primary" %}} 

Wenn Sie stattdessen auf **Einfügen** in der **Standard**-Symbolleiste klicken oder **STRG**+**V** drücken, werden die Inhalte der Zielzellen ersetzt.

{{% /alert %}} 
## **Verwendung von Aspose.Cells**
### **Kopieren von Zeilen**
Aspose.Cells bietet die Methode CopyRow der Klasse Aspose::Cells::ICells. Diese Methode kopiert alle Arten von Daten einschließlich Formeln, Werten, Kommentaren, Zellformatierungen, ausgeblendeten Zellen, Bilder und andere Zeichenobjekte von der Quellzeile zur Zielzeile.

Die Methode CopyRow verwendet die folgenden Parameter:

- das Quellzellenobjekt,
- den Index der Quellzeile, und
- den Index der Zielzeile.

Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blatts zu kopieren oder in ein anderes Blatt zu kopieren. Die CopyRow-Methode funktioniert ähnlich wie Microsoft Excel. So müssen Sie beispielsweise die Höhe der Zielspalte nicht explizit festlegen, auch dieser Wert wird automatisch kopiert.

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es verwendet eine Vorlage-Microsoft-Excel-Datei und kopiert die zweite Zeile (inklusive Daten, Formatierungen, Kommentare, Bilder usw.) und fügt sie in die 12. Zeile im selben Arbeitsblatt ein.

Sie können den Schritt überspringen, der die Höhe der Quellzeile mithilfe der Methode **GetRowHeigh** abruft und dann die Höhe der Zielspalte mithilfe der Methode **SetRowHeight** festlegt, da die Methode **CopyRow** automatisch die Zeilenhöhe übernimmt.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Beim Kopieren von Zeilen ist es wichtig, darauf zu achten, dass zugehörige Bilder, Diagramme oder andere Zeichenobjekte genauso behandelt werden wie in Microsoft Excel:

1. Wenn der Quellenzeilenindex 5 ist, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Anfangszeilenindex ist 4 und der Endzeilenindex ist 6).
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.

{{% /alert %}} 
### **Spalten kopieren**
Aspose.Cells bietet die CopyColumn Methode der Aspose::Cells::ICells Klasse an, diese Methode kopiert alle Arten von Daten, einschließlich Formeln - mit aktualisierten Verweisen - und Werten, Kommentaren, Zellformaten, versteckten Zellen, Bildern und anderen Zeichenobjekten von der Quellspalte zur Zielspalte.

Die CopyColumn Methode akzeptiert die folgenden Parameter:

- das Quellzellenobjekt,
- Quellspaltenindex, und
- der Zielspaltenindex.

Verwenden Sie die CopyColumn Methode, um eine Spalte innerhalb eines Blatts oder zu einem anderen Blatt zu kopieren.

Dieses Beispiel kopiert eine Spalte aus einem Arbeitsblatt und fügt sie in ein Arbeitsblatt in einer anderen Arbeitsmappe ein.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

---
title: Copy-Paste-Verhalten von EnableClipboardCopyPaste- und PasteType-GridDesktop-Eigenschaften
type: docs
weight: 80
url: /de/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **Mögliche Nutzungsszenarien**
GridDesktop bietet mit der Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.PasteType verschiedene Arten von Optionen zum Kopieren und Einfügen. Diese Optionen werden mit der Aufzählung Aspose.Cells.GridDesktop.Data.GridPasteType angegeben. Einige davon sind wie folgt

- GridPasteType.All

Es kopiert und fügt alles von Quellzellen zu Zielzellen ein.

- GridPasteType.Formulas

Es kopiert und fügt Formeln aus Quellzellen in Zielzellen ein.

- GridPasteType.Comments

Es kopiert und fügt Kommentare aus Quellzellen in Zielzellen ein.

- GridPasteType.RowHeights

Es kopiert und fügt Zeilenhöhen von Quellzellen in Zielzellen ein.

- GridPasteType.ColumnWidths

Es kopiert und fügt Spaltenbreiten von Quellzellen in Zielzellen ein.

usw.
## **Setzen Sie die EnableClipboardCopyPaste-Eigenschaft auf True, um die PasteType-Eigenschaft zu aktivieren**
Die Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.PasteType funktioniert nur, wenn Sie die Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste wie in diesem Screenshot gezeigt auf true setzen.

![todo: Bild_alt_Text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Verhalten der Eigenschaften EnableClipboardCopyPaste und PasteType**
Da EnableClipboardCopyPaste false und PasteType All ist, zeigt der folgende Screenshot, dass beim Kopieren und Einfügen von Zelle B3 in Zelle C5 die Zellenformatierung nicht kopiert wird und nur der Inhalt von Zelle B3 kopiert wird.

![todo: Bild_alt_Text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

Da „EnableClipboardCopyPaste“ auf „true“ und „PasteType“ auf „All“ gesetzt ist, zeigt der folgende Screenshot, dass beim Kopieren und Einfügen von Zelle B3 in Zelle C5 auch die Formatierung der Zelle B3 in Zelle C5 kopiert wird.

![todo: Bild_alt_Text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)



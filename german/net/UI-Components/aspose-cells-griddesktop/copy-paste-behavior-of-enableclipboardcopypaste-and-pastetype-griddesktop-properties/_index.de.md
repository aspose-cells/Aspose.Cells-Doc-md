---
title: Verhalten beim Kopieren und Einfügen der GridDesktop-Eigenschaften „EnableClipboardCopyPaste“ und „PasteType“.
type: docs
weight: 80
url: /de/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Mögliche Nutzungsszenarien**
GridDesktop bietet verschiedene Arten von Optionen zum Kopieren und Einfügen mit der Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.PasteType. Diese Optionen werden mit der Enumeration Aspose.Cells.GridDesktop.Data.GridPasteType angegeben. Einige davon sind wie folgt

- GridPasteType.All

Es kopiert und fügt alles von den Quellzellen in die Zielzellen ein.

- GridPasteType.Formulas

Es kopiert und fügt Formeln aus Quellzellen in Zielzellen ein.

- GridPasteType.Comments

Es kopiert und fügt Kommentare aus Quellzellen in Zielzellen ein.

- GridPasteType.RowHeights

Es kopiert und fügt Zeilenhöhen von Quellzellen in Zielzellen ein.

- GridPasteType.ColumnWidths

Es kopiert und fügt Spaltenbreiten von Quellzellen in Zielzellen ein.

usw.
##  **Setzen Sie die Eigenschaft „EnableClipboardCopyPaste“ auf „True“, um die Eigenschaft „PasteType“ zu aktivieren**
Die Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.PasteType funktioniert nur, wenn Sie die Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste auf true setzen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Verhalten der Eigenschaften „EnableClipboardCopyPaste“ und „PasteType“.**
Vorausgesetzt, dass EnableClipboardCopyPaste „false“ und „PasteType“ „All“ ist, zeigt der folgende Screenshot, dass Zelle B3 kopiert und in Zelle C5 eingefügt wird.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Vorausgesetzt, dass EnableClipboardCopyPaste „true“ und „PasteType“ „All“ ist, wird nach dem Kopieren eines Bilds aus Windows ein Wert angezeigt. Der folgende Screenshot zeigt, dass beim Kopieren und Einfügen von Zelle B3 in Zelle C5 auch das Bild in Zelle C5 kopiert wird.

![Todo: Bild kopieren](copyimage.png)

![Todo: Nach dem Kopieren einfügen](aftercopy.png)



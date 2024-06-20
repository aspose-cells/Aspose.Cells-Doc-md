---
title: Kopieren Einfügen Verhalten von EnableClipboardCopyPaste und PasteType GridDesktop Eigenschaften
type: docs
weight: 80
url: /de/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: Kopieren, einfügen, GridPasteType
description: Dieser Artikel beschreibt, wie das GridPasteType verwendet wird, um Kopier und Einfügevorgänge in GridDesktop durchzuführen.
---

## **Mögliche Verwendungsszenarien**
GridDesktop bietet verschiedene Arten von Kopier- und Einfügevorgängen mit der Eigenschaft Aspose.Cells.GridDesktop.GridDesktop.PasteType. Diese Optionen sind mit der Aufzählung Aspose.Cells.GridDesktop.Data.GridPasteType angegeben. Einige davon sind wie folgt

- GridPasteType.All

Es kopiert und fügt alles von den Quellzellen zu den Zielzellen ein.

- GridPasteType.Formulas

Es kopiert und fügt Formeln von den Quellzellen zu den Zielzellen ein.

- GridPasteType.Comments

Es kopiert und fügt Kommentare von den Quellzellen zu den Zielzellen ein.

- GridPasteType.RowHeights

Es kopiert und fügt Zeilenhöhen von den Quellzellen zu den Zielzellen ein.

- GridPasteType.ColumnWidths

Es kopiert und fügt Spaltenbreiten von Quellzellen in Zielzellen ein.

usw.
## **Legen Sie die Eigenschaft EnableClipboardCopyPaste auf True fest, um die Eigenschaft PasteType zu aktivieren.**
Die Aspose.Cells.GridDesktop.GridDesktop.PasteType-Eigenschaft funktioniert nur, wenn Sie die Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste-Eigenschaft wie in diesem Screenshot gezeigt auf true setzen.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Verhalten der Eigenschaften EnableClipboardCopyPaste und PasteType**
Angenommen, EnableClipboardCopyPaste ist false und PasteType ist All, zeigt der folgende Screenshot, dass beim Kopieren und Einfügen von Zelle B3 in Zelle C5 Folgendes passiert.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Angenommen, EnableClipboardCopyPaste ist true und PasteType ist All, nach dem Kopieren eines Bildes aus Windows zeigt der folgende Screenshot, dass beim Kopieren und Einfügen von Zelle B3 in Zelle C5 auch das Bild kopiert wird.

![todo: Bild kopieren](copyimage.png)

![todo: nach dem Kopieren einfügen](aftercopy.png)



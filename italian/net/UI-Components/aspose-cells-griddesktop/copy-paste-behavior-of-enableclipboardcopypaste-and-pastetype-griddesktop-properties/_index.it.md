---
title: Comportamento di copia incolla di EnableClipboardCopyPaste e delle proprietà PasteType GridDesktop
type: docs
weight: 80
url: /it/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: copia, incolla, GridPasteType
description: Questo articolo descrive come utilizzare il GridPasteType per effettuare operazioni di copia e incolla in GridDesktop.
---

## **Possibili Scenari di Utilizzo**
GridDesktop fornisce differenti opzioni di tipo di copia e incolla con la proprietà PasteType di Aspose.Cells.GridDesktop.GridDesktop. Queste opzioni sono specificate con l'enumerazione Aspose.Cells.GridDesktop.Data.GridPasteType. Alcune di queste sono le seguenti

- GridPasteType.All

Copia e incolla tutto dalle celle di origine alle celle di destinazione.

- GridPasteType.Formulas

Copia e incolla formule dalle celle di origine alle celle di destinazione.

- GridPasteType.Comments

Copia e incolla commenti dalle celle di origine alle celle di destinazione.

- GridPasteType.RowHeights

Copia e incolla l'altezza delle righe dalle celle di origine alle celle di destinazione.

- GridPasteType.ColumnWidths

Copia e incolla le larghezze delle colonne dalle celle di origine alle celle di destinazione.

ecc.
## **Imposta la proprietà EnableClipboardCopyPaste su True per abilitare la proprietà PasteType.**
La proprietà Aspose.Cells.GridDesktop.GridDesktop.PasteType funziona solo se si imposta la proprietà Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste su true come mostrato in questa schermata.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Comportamento delle proprietà EnableClipboardCopyPaste e PasteType**
Dato che EnableClipboardCopyPaste è false e PasteType è All, la seguente schermata mostra che quando la cella B3 viene copiata e incollata nella cella C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Dato che EnableClipboardCopyPaste è true e PasteType è All, dopo aver copiato un'immagine da Windows, la seguente schermata mostra che quando la cella B3 viene copiata e incollata nella cella C5, copia anche l'immagine nella cella C5.

![todo:copiare l'immagine](copiaimmagine.png)

![todo:dopo aver copiato fare incolla](dopocopia.png)



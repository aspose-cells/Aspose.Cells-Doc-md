---
title: Comportamento di copia e incolla delle proprietà EnableClipboardCopyPaste e PasteType GridDesktop
type: docs
weight: 80
url: /it/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Possibili scenari di utilizzo**
GridDesktop fornisce diversi tipi di opzioni di tipo copia e incolla con la proprietà Aspose.Cells.GridDesktop.GridDesktop.PasteType. Queste opzioni vengono specificate con l'enumerazione Aspose.Cells.GridDesktop.Data.GridPasteType. Alcuni di questi sono i seguenti

- GridPasteType.All

Copia e incolla tutto, dalle celle di origine alle celle di destinazione.

- GridPasteType.Formulas

Copia e incolla le formule dalle celle di origine alle celle di destinazione.

- GridPasteType.Comments

Copia e incolla i commenti dalle celle di origine alle celle di destinazione.

- GridPasteType.RowHeights

Copia e incolla l'altezza delle righe dalle celle di origine alle celle di destinazione.

- GridPasteType.ColumnWidths

Copia e incolla la larghezza delle colonne dalle celle di origine alle celle di destinazione.

eccetera.
##  **Imposta la proprietà EnableClipboardCopyPaste su True per abilitare la proprietà PasteType**
La proprietà Aspose.Cells.GridDesktop.GridDesktop.PasteType funziona solo se imposti la proprietà Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste su true come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Comportamento delle proprietà EnableClipboardCopyPaste e PasteType**
Dato che EnableClipboardCopyPaste è false e PasteType è All, lo screenshot seguente mostra che quando la cella B3 viene copiata e incollata nella cella C5.

![cose da fare:immagine_alt_testo](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Dato che EnableClipboardCopyPaste è true e PasteType è All, dopo aver copiato un'immagine da Windows. lo screenshot seguente mostra che quando la cella B3 viene copiata e incollata nella cella C5, copia anche l'immagine nella cella C5.

![todo: copia l'immagine](copyimage.png)

![cose da fare: dopo aver copiato, incolla](aftercopy.png)



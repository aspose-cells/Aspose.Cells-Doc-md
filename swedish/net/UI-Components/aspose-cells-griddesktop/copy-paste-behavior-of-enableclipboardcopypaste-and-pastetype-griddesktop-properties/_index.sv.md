---
title: Copy Paste Beteende för EnableClipboardCopyPaste och PasteType GridDesktop Properties
type: docs
weight: 80
url: /sv/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Möjliga användningsscenarier**
GridDesktop tillhandahåller olika typer av kopierings- och klistraalternativ med egenskapen Aspose.Cells.GridDesktop.GridDesktop.PasteType. Dessa alternativ anges med Aspose.Cells.GridDesktop.Data.GridPasteType-uppräkning. Några av dessa är följande

- GridPasteType.All

Den kopierar och klistrar in allt från källceller till målceller.

- GridPasteType.Formulas

Den kopierar och klistrar in formler från källceller till målceller.

- GridPasteType.Comments

Den kopierar och klistrar in kommentarer från källceller till målceller.

- GridPasteType.RowHeights

Den kopierar och klistrar in radhöjder från källceller till målceller.

- GridPasteType.ColumnWidths

Den kopierar och klistrar in kolumnbredder från källceller till målceller.

etc.
##  **Ställ in EnableClipboardCopyPaste Property True för att aktivera PasteType Property**
Egenskapen Aspose.Cells.GridDesktop.GridDesktop.PasteType fungerar endast om du anger egenskapen Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste som sann som visas i den här skärmdumpen.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Beteende för EnableClipboardCopyPaste och PasteType-egenskaper**
Med tanke på att EnableClipboardCopyPaste är falskt och PasteType är All, visar följande skärmdump att när cell B3 kopieras och klistras in i cell C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Med tanke på att EnableClipboardCopyPaste är sant och PasteType är All, efter att ha kopierat en bild från Windows . Följande skärmdump visar att när cell B3 kopieras och klistras in i cell C5, kopierar den också bilden till cell C5.

![göra: kopiera bilden](copyimage.png)

![att göra: efter kopiera, klistra in](aftercopy.png)



---
title: Kopiera Klistra in Beteende av EnableClipboardCopyPaste och PasteType GridDesktop Egenskaper
type: docs
weight: 80
url: /sv/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: kopiera,klistra,GridPasteType
description: Denna artikel beskriver hur man använder GridPasteType för att göra kopiera klistra operation i GridDesktop.
---

## **Möjliga användningsscenario**
GridDesktop ger olika typer av kopiera-klistra-typalternativ med Aspose.Cells.GridDesktop.GridDesktop.PasteType-egenskapen. Några av dessa är följande

- GridPasteType.All

Det kopierar och klistrar in allt från källceller till målceller.

- GridPasteType.Formulas

Det kopierar och klistrar in formler från källceller till målceller.

- GridPasteType.Comments

Det kopierar och klistrar in kommentarer från källceller till målceller.

- GridPasteType.RowHeights

Det kopierar och klistrar in radhöjder från källceller till målceller.

- GridPasteType.ColumnWidths

Det kopierar och klistrar in kolumnbredder från källceller till målceller.

osv.
## **Ställ EnableClipboardCopyPaste Egenskapen till True för att aktivera PasteType Egenskapen**
Aspose.Cells.GridDesktop.GridDesktop.PasteType-egenskapen fungerar bara om du ställer in Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste-egenskapen till true som visas på denna skärmbild.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Beteende av EnableClipboardCopyPaste och PasteType-egenskaper**
Givet att EnableClipboardCopyPaste är false och PasteType är All, visar följande skärmbild att när cell B3 kopieras och klistras in i cell C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Givet att EnableClipboardCopyPaste är true och PasteType är All, efter att ha kopierat en bild från Windows. visar följande skärmbild att när cell B3 kopieras och klistras in i cell C5 kopieras även bilden till cell C5.

![todo:do copy image](copyimage.png)

![todo:after copy do paste](aftercopy.png)



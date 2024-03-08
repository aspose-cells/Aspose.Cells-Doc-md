---
title: EnableClipboardCopyPaste および PasteType GridDesktop プロパティのコピー＆ペースト動作
type: docs
weight: 80
url: /ja/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **考えられる使用シナリオ**
GridDesktop は、Aspose.Cells.GridDesktop.GridDesktop.PasteType プロパティを使用して、さまざまなタイプのコピー ペースト タイプ オプションを提供します。これらのオプションは、Aspose.Cells.GridDesktop.Data.GridPasteType 列挙で指定されます。その一部は次のとおりです

- GridPasteType.All

ソース セルからターゲット セルまですべてをコピーして貼り付けます。

- GridPasteType.Formulas

数式をソース セルからターゲット セルにコピーして貼り付けます。

- GridPasteType.Comments

コメントをソース セルからターゲット セルにコピーして貼り付けます。

- GridPasteType.RowHeights

行の高さをソース セルからターゲット セルにコピーして貼り付けます。

- GridPasteType.ColumnWidths

列幅をソース セルからターゲット セルにコピーして貼り付けます。

等
##  **PasteType プロパティを有効にするには、EnableClipboardCopyPaste プロパティを True に設定します**
このスクリーンショットに示すように、Aspose.Cells.GridDesktop.GridDesktop.PasteType プロパティは、Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste プロパティを true に設定した場合にのみ機能します。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **EnableClipboardCopyPaste および PasteType プロパティの動作**
EnableClipboardCopyPaste が false で、PasteType が All である場合、次のスクリーンショットは、セル B3 がコピーされてセル C5 に貼り付けられたことを示しています。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

EnableClipboardCopyPaste が true で、PasteType が All である場合、Windows から画像をコピーした後。次のスクリーンショットは、セル B3 をコピーしてセル C5 に貼り付けると、画像もセル C5 にコピーされることを示しています。

![Todo:画像をコピーする](copyimage.png)

![todo:コピーして貼り付けた後](aftercopy.png)



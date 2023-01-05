---
title: EnableClipboardCopyPaste および PasteType GridDesktop プロパティのコピー貼り付け動作
type: docs
weight: 80
url: /ja/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **考えられる使用シナリオ**
GridDesktop は、Aspose.Cells.GridDesktop.GridDesktop.PasteType プロパティを使用して、さまざまなタイプのコピー ペースト タイプ オプションを提供します。これらのオプションは、Aspose.Cells.GridDesktop.Data.GridPasteType 列挙で指定されます。これらのいくつかは次のとおりです

- GridPasteType.All

ソースセルからターゲットセルまですべてをコピーして貼り付けます。

- GridPasteType.Formulas

ソースセルからターゲットセルに数式をコピーして貼り付けます。

- GridPasteType.コメント

ソース セルからターゲット セルにコメントをコピーして貼り付けます。

- GridPasteType.RowHeights

行の高さをソース セルからターゲット セルにコピー アンド ペーストします。

- GridPasteType.ColumnWidths

ソース セルからターゲット セルに列幅をコピーして貼り付けます。

等
## **PasteType プロパティを有効にするには、EnableClipboardCopyPaste プロパティを True に設定します。**
Aspose.Cells.GridDesktop.GridDesktop.PasteType プロパティは、このスクリーンショットに示すように Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste プロパティを true に設定した場合にのみ機能します。

![todo:画像_代替_文章](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **EnableClipboardCopyPaste および PasteType プロパティの動作**
EnableClipboardCopyPaste が false で、PasteType が All の場合、次のスクリーンショットは、セル B3 をコピーしてセル C5 に貼り付けると、セルの書式設定はコピーされず、セル B3 のコンテンツのみがコピーされることを示しています。

![todo:画像_代替_文章](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

EnableClipboardCopyPaste が true で、PasteType が All の場合、次のスクリーンショットは、セル B3 をコピーしてセル C5 に貼り付けると、セル B3 の書式設定もセル C5 にコピーすることを示しています。

![todo:画像_代替_文章](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)



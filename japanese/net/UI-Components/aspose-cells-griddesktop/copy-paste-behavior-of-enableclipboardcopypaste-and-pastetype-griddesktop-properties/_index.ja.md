---
title: EnableClipboardCopyPasteおよびPasteType GridDesktopプロパティのコピペ動作
type: docs
weight: 80
url: /ja/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: コピー、ペースト、GridPasteType
description: この記事では、GridPasteTypeを使用してGridDesktopでコピーペースト操作を行う方法について説明します。
---

## **可能な使用シナリオ**
GridDesktopは、Aspose.Cells.GridDesktop.GridDesktop.PasteTypeプロパティを使用して異なる種類のコピーペーストオプションを提供します。これらのオプションのいくつかは次のとおりです。

- GridPasteType.All

ソースセルからターゲットセルへの全てをコピーしてペーストします。

- GridPasteType.Formulas

ソースセルからターゲットセルへの数式をコピーしてペーストします。

- GridPasteType.Comments

ソースセルからターゲットセルへのコメントをコピーしてペーストします。

- GridPasteType.RowHeights

ソースセルからターゲットセルへの行の高さをコピーしてペーストします。

- GridPasteType.ColumnWidths

ソースセルからターゲットセルへの列の幅をコピーしてペーストします。

など。
## **EnableClipboardCopyPasteプロパティをTrueに設定して、PasteTypeプロパティを有効にする。**
Aspose.Cells.GridDesktop.GridDesktop.PasteTypeプロパティは、このスクリーンショットに示すように、Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPasteプロパティがtrueに設定されている場合にのみ機能します。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **EnableClipboardCopyPasteおよびPasteTypeプロパティの動作**
EnableClipboardCopyPasteがfalseであり、PasteTypeがAllである場合、次のスクリーンショットでは、セルB3をコピーしてセルC5に貼り付けたときの動作が示されています。

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

EnableClipboardCopyPasteがtrueであり、PasteTypeがAllである場合、Windowsから画像をコピーした後、セルB3をコピーしてセルC5に貼り付けたときの動作が次のスクリーンショットで示されています。また、画像もセルC5にコピーされます。

![画像をコピーする](copyimage.png)

![コピーした後に貼り付ける](aftercopy.png)



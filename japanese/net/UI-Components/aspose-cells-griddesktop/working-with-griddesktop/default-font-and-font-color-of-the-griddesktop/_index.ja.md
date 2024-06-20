---
title: GridDesktop のデフォルトのフォントおよびフォントの色
type: docs
weight: 70
url: /ja/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop で行または列のフォント、色を変更する
description: この記事では、GridDesktop のデフォルトのフォントおよびフォントの色について紹介しています。
---

## **可能な使用シナリオ**
時々、GridDesktopのデフォルトのフォントとフォントの色を変更したいことがあります。この目的のために、次の2つのプロパティを使用してください。これらのプロパティには、必要に応じてデザイン時または実行時にアクセスできます。

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **デザイン時にデフォルトのフォントとフォントの色を変更する**
次のスクリーンショットは、GridDesktopのデフォルトのフォントとフォントの色をデザイン時に変更する方法を示しています。

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **ランタイムでデフォルトのフォントとフォントの色を変更する**
次のサンプルコードは、GridDesktopのランタイムでデフォルトのフォントとフォントの色を変更する方法を説明しています。

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

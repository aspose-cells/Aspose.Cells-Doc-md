---
title: GridDesktop のデフォルトのフォントとフォントの色
type: docs
weight: 70
url: /ja/net/default-font-and-font-color-of-the-griddesktop/
---
## **考えられる使用シナリオ**
GridDesktop のデフォルトのフォントとフォントの色を変更したい場合があります。この目的のために、次の 2 つのプロパティを使用してください。必要に応じて、設計時または実行時にこれらのプロパティにアクセスできます。

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **設計時にデフォルトのフォントとフォントの色を変更する**
次のスクリーンショットは、設計時に GridDesktop のデフォルトのフォントとフォントの色を変更する方法を示しています。

![todo:画像_代替_文章](default-font-and-font-color-of-the-griddesktop_1.png)
## **実行時にデフォルトのフォントとフォントの色を変更する**
次のサンプル コードでは、実行時に GridDesktop の既定のフォントとフォントの色を変更する方法について説明します。

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}

---
title: GridWebセルのハイパーリンクオブジェクトにアクセス
type: docs
weight: 100
url: /ja/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb、ハイパーリンク
description: この記事では、GridWebでハイパーリンクを操作する方法について紹介します。
---

## **可能な使用シナリオ**
次の2つのメソッドを使用して、セルにハイパーリンクが含まれているかどうかを確認できます。これらのメソッドは、セルにハイパーリンクが含まれていない場合はnullを返し、ハイパーリンクが含まれている場合はGridHyperlinkオブジェクトを返します。

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **新しいウィンドウまたは既存のウィンドウでハイパーリンクを開く**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **GridWebセルのハイパーリンクオブジェクトにアクセス**
下記のサンプルコードは、セルA1のハイパーリンクにアクセスします。セルA1にハイパーリンクが含まれている場合はGridHyperlinkオブジェクトを返し、それ以外の場合はnullを返します。
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}

---
title: GridWebセルのハイパーリンクオブジェクトにアクセス
type: docs
weight: 60
url: /ja/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **可能な使用シナリオ**
次の2つのメソッドを使用して、セルにハイパーリンクが含まれているかどうかを確認できます。これらのメソッドは、セルにハイパーリンクが含まれていない場合はnullを返し、ハイパーリンクが含まれている場合はGridHyperlinkオブジェクトを返します。

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **新しいウィンドウまたは既存のウィンドウでハイパーリンクを開く**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **GridWebセルのハイパーリンクオブジェクトにアクセス**
下記のサンプルコードは、セルA1のハイパーリンクにアクセスします。セルA1にハイパーリンクが含まれている場合はGridHyperlinkオブジェクトを返し、それ以外の場合はnullを返します。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}

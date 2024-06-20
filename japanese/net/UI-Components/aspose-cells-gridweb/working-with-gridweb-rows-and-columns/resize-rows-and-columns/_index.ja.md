---
title: 行と列のリサイズ
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/resize-rows-and-columns/
keywords: GridWeb, 幅, 高さ, 行の高さ, 列の幅
description: 本記事では、GridWeb で行の高さと列の幅を設定する方法について紹介します。
---

{{% alert color="primary" %}} 

セルの値がセルよりも幅が広い場合、または複数行にわたる場合があります。そのような値は、行と列の高さと幅を変更しない限り、ユーザーには完全に表示されません。Aspose.Cells.GridWeb は、行の高さと列の幅の設定を完全にサポートしています。このトピックでは、具体的な例を挙げながら、これらの機能について詳しく説明します。

{{% /alert %}} 
## **行の高さと列の幅の設定**
### **行の高さの設定**
行の高さを設定するには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ワークシートの Cells コレクションにアクセスします。
1. 指定された行内のすべてのセルの高さを設定します。

{{% alert color="primary" %}} 

Cells コレクションの SetRowHeight および SetColumnWidth メソッドには、インチとピクセルで行の高さと列の幅を設定するためのバリアントも用意されています。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **列の幅の設定**
列の幅を設定するには:

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. ワークシートの Cells コレクションにアクセスします。
1. 指定された列内のすべてのセルの幅を設定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}

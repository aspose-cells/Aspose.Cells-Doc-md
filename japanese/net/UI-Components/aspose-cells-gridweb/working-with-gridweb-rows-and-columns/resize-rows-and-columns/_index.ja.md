---
title: 行と列のサイズ変更
type: docs
weight: 30
url: /ja/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

セルの値が、セルの幅よりも広い場合や、複数の行にある場合があります。このような値は、行と列の高さと幅を変更しない限り、ユーザーに完全には表示されません。 Aspose.Cells.GridWeb は、行の高さと列の幅の設定を完全にサポートしています。このトピックでは、例を使用してこれらの機能について詳しく説明します。

{{% /alert %}} 
## **行の高さと列の幅の操作**
### **行の高さの設定**
行の高さを設定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートの Cells コレクションにアクセスします。
1. 指定した行のすべてのセルの高さを設定します。

{{% alert color="primary" %}} 

Cells コレクションの SetRowHeight メソッドと SetColumnWidth メソッドには、行の高さと列の幅の測定値をインチとピクセルで設定するバリアントもあります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **列幅の設定**
列の幅を設定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートの Cells コレクションにアクセスします。
1. 指定された列のすべてのセルの幅を設定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}

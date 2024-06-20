---
title: GridWebの行と列をコピー
type: docs
weight: 80
url: /ja/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb,コピー
description: 本記事では、GridWebで行と列をコピーする方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebコンポーネントは、GridCellsクラスを使用して行と列をコピーする手段を提供します。この記事では、Aspose.Cells.GridWebが公開するAPIの使用方法について説明します。 

GridCells.CopyRow、GridCells.CopyColumn、GridCells.CopyRowsおよびGridCells.CopyColumnsメソッドは、ソースの行と列からコンテンツ、スタイル、および数式を宛先にコピーします。

{{% /alert %}} 
## **行と列のコピー**
Aspose.Cells.GridWebコンポーネントにまだ慣れていない場合、[Aspose.Cells.GridWebの概要](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/)や[WebフォームアプリケーションにAspose.Cells.GridWebコンポーネントを追加する方法](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/)に関する詳細な記事をご覧になることを強くお勧めします。
### **単一行のコピー**
例を単純にするために、既存のスプレッドシートとその行の合計を計算する単純な数式を使用しています。行をコピーする前のAspose.Cells.GridWebインターフェースでスプレッドシートが表示されます。

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

コードスニペットは以下のように示されています。これにより、アクティブワークシートのGridCellsオブジェクトにアクセスし、最初の行を次の行にコピーすることができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


行のコピー操作の後のAspose.Cells.GridWebの表示例です。

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **単一列のコピー**
次の例では、既存のスプレッドシートとその列の合計を計算する単純な数式を使用しています。列をコピーする前のAspose.Cells.GridWebインターフェースでスプレッドシートが表示されます。

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

上記の例と同様に、次のコードスニペットは、アクティブワークシートのGridCellsオブジェクトにアクセスして、最初の列を次の列にコピーすることができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



列のコピー操作の後のAspose.Cells.GridWebの表示例です。

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

GridCells.CopyRowおよびGridCells.CopyColumnメソッドを使用して、ソースの行と列を複数の行および列にコピーするためにループで使用することができます。

{{% /alert %}} 
### **複数の行のコピー**
GridCells.CopyRowsメソッドを使用して、新しい宛先に複数の行をコピーすることができます。また、コピーするソース行の数を指定するための整数の追加パラメータがあります。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Aspose.Cells.GridWebの見た目は、行のコピー操作前後で以下のようになります。

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **複数の列をコピー**
GridCellsクラスは、追加の整数型のパラメータを取るCopyColumnsメソッドも提供しており、これによりコピーするソース列の数を指定できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Aspose.Cells.GridWebの見た目は、行のコピー操作前後で以下のようになります。

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)

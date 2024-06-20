---
title: 書式設定ありおよびなしでセル文字列の値を取得
type: docs
weight: 230
url: /ja/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\))メソッドを提供しており、これを使用してセルの文字列値を書式設定ありまたはなしで取得できます。たとえば、値が0.012345のセルを持っていて、それを小数点以下2桁のみを表示するように書式設定したとします。その場合、Excelでは0.01として表示されます。[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) メソッドを使用して0.01および0.012345の両方の文字列値を取得できます。[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)列挙型をパラメータとして受け取り、次の値があります。

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **書式設定ありおよびなしでセル文字列の値を取得**
次のサンプルコードは、[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) メソッドの使用方法を説明しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}

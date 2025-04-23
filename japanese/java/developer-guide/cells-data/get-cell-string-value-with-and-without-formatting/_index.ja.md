---
title: 書式設定ありおよびなしでセル文字列の値を取得
type: docs
weight: 230
url: /ja/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)メソッドを提供しており、セルの文字列値をフォーマットの有無に関係なく取得できます。例えば、値が0.012345のセルがあり、小数点以下2桁だけ表示するようにフォーマットされている場合、Excelでは0.01と表示されます。 [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)メソッドを使えば、0.01としても0.012345としても文字列値を取得可能です。このメソッドは以下の値を持つ [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) 列挙型をパラメータとして受け取ります。

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **書式設定ありおよびなしでセル文字列の値を取得**
以下のサンプルコードは、[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)メソッドの使い方を説明しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

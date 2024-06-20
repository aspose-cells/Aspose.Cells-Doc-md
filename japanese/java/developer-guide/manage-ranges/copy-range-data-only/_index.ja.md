---
title: 範囲のデータのみをコピーします。
type: docs
weight: 330
url: /ja/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

場合によっては、セル範囲から別のセル範囲にデータをコピーする必要があり、その際に書式ではなくデータのみをコピーしたい場合があります。Aspose.Cellsでは、これを提供するために[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\))メソッドを提供しています。

{{% /alert %}} 
## **Excelの範囲のデータをコピーする**
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. 範囲を作成します。
1. 指定された書式属性を持つスタイルオブジェクトを作成します。
1. 範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
1. 最初の範囲のデータを[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\))メソッドを使用して2番目の範囲にコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}

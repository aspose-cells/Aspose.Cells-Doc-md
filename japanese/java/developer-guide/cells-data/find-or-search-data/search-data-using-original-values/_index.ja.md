---
title: 元の値を使用してデータを検索
type: docs
weight: 540
url: /ja/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

データの値が一部の方法でフォーマットされているために隠れていることがあります。例えば、セル D4 には式 =Sum(A1:A2) があり、その値は20ですが、--- としてフォーマットされている場合、値 20 は隠れており、Microsoft Excel の検索オプションを使用して見つけることはできません。ただし、[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) を使用すると、Aspose.Cells を使用してそれを見つけることができます。

{{% /alert %}} 
## **元の値を使用したデータの検索**
次のサンプルコードは、上記のポイントを示しています。Microsoft Excel の検索オプションで見つけることができないセル D4 を見つけますが、Aspose.Cells を使用すると[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) を使用してそれを見つけることができます。詳細については、コード内のコメントをご覧ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}

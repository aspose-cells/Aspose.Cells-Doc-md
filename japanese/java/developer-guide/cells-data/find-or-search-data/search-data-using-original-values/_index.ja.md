---
title: 元の値を使用してデータを検索
type: docs
weight: 540
url: /ja/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

時には、データの値が何らかのフォーマットのために非表示になっていることがあります。たとえば、セルD4に数式=Sum(A1:A2)があり、その値が20でも、フォーマットが---の場合、その値20は非表示になり、Microsoft Excelの検索機能では見つかりません。ただし、Aspose.Cellsを使用して[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)で見つけることができます。

{{% /alert %}} 
## **元の値を使用したデータの検索**
以下のサンプルコードは、上記のポイントを示しています。Microsoft Excelの検索オプションでは見つからないセルD4をAspose.Cellsが[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)を使用して見つける方法を示しています。詳細はコード内のコメントをご参照ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

---
title: 改行とテキストの折り返し
type: docs
weight: 10
url: /ja/java/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

セル内のテキストを確実に読み取れるようにするために、明示的な改行とテキストの折り返しを適用できます。テキストの折り返しにより、セル内の 1 行が複数の行に変わり、明示的な改行によって、必要な場所に正確に改行が挿入されます。

{{% /alert %}}

## **テキストを Cell で折り返すには**

セル内でテキストを折り返すには、[**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)財産。

次のサンプル コードは、セル内でテキストの折り返しと明示的な改行を使用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **明示的な改行を使用するには**

Java で '\n' を使用して、セルに明示的な改行を挿入できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}

---
title: 改行とテキストの折り返し
type: docs
weight: 10
url: /ja/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

{{% /alert %}}

## **セル内でテキストを折り返す**

セル内でテキストを折り返すには、[**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)プロパティを使用します。

以下のサンプルコードは、セル内でテキストの折り返しと明示的な改行を使用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **明示的な改行を使用する**

Javaでは、明示的な改行を挿入するために'\n'を使用することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
{{< app/cells/assistant language="java" >}}

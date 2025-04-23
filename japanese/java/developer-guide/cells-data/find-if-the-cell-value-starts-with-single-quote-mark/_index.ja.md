---
title: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 610
url: /ja/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells は現在、セルの値が単一引用符マークで始まるかどうかを確認するための[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) プロパティを提供しています。このプロパティ以前は、例えば sample と 'sample といった文字列を区別する方法がありませんでした。

{{% /alert %}} 
## **セルの値がシングルクォートマークで始まるかどうかを検索**
次のサンプルコードは、[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) プロパティでは sample と 'sample を区別できないことを説明しています。そのため、それらを区別するには [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) プロパティを使用する必要があります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
{{< app/cells/assistant language="java" >}}

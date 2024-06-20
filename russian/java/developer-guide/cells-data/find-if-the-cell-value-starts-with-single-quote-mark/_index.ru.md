---
title: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 610
url: /ru/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Теперь Aspose.Cells предоставляет свойство [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) для определения, начинается ли значение ячейки с одинарной кавычки. До появления этого свойства не было способа различить строки, такие как образец и 'образец и т. д.

{{% /alert %}} 
## **Определите, начинается ли значение ячейки с одинарной кавычки**
В следующем примере кода объясняется, что строки, такие как образец и 'образец, не могут быть отличены с помощью свойства [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). Поэтому мы должны использовать свойство [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) для их различения.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

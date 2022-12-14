---
title: Найдите, начинается ли значение ячейки с одинарной кавычки
type: docs
weight: 610
url: /ru/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells теперь предоставляет[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) свойство, чтобы определить, начинается ли значение ячейки с одинарной кавычки. До этого свойства не было способа различить такие строки, как образец, 'образец и т. д.

{{% /alert %}} 
## **Найдите, начинается ли значение ячейки с одинарной кавычки**
В следующем примере кода поясняется, что такие строки, как sample и 'sample, нельзя различить с помощью[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) имущество. Поэтому мы должны использовать[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)свойство различать их.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

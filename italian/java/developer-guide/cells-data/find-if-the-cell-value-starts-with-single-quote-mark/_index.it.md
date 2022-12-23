---
title: Trova se il valore della cella inizia con virgolette singole
type: docs
weight: 610
url: /it/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells ora fornisce il[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) proprietà per trovare se il valore della cella inizia con una singola virgoletta. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come sample e 'sample etc.

{{% /alert %}} 
## **Trova se il valore della cella inizia con virgolette singole**
Il seguente codice di esempio spiega che le stringhe come sample e 'sample non possono essere differenziate con[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) proprietà. Pertanto dobbiamo usare[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)proprietà per distinguerli.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

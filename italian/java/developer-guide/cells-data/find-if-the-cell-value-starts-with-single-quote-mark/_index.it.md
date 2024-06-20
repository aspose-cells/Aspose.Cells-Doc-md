---
title: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 610
url: /it/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells ora fornisce la proprietà [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) per verificare se il valore della cella inizia con un apice singolo. Prima di questa proprietà, non c'era modo di distinguere tra le stringhe come campione e 'campione etc.

{{% /alert %}} 
## **Verifica se il valore della cella inizia con un apice singolo**
Il seguente codice di esempio spiega che le stringhe come campione e 'campione non possono essere differenziate con la proprietà [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). Pertanto, dobbiamo usare la proprietà [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) per distinguerle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

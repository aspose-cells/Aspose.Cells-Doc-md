---
title: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 610
url: /es/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells ahora proporciona la propiedad [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) para encontrar si el valor de la celda comienza con una comilla simple. Antes de esta propiedad, no había manera de distinguir entre cadenas como muestra y 'muestra, etc.

{{% /alert %}} 
## **Encontrar si el valor de la celda comienza con una comilla simple**
El siguiente código de ejemplo explica que las cadenas como muestra y 'muestra no se pueden diferenciar con la propiedad [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). Por lo tanto, debemos usar la propiedad [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) para distinguirlas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

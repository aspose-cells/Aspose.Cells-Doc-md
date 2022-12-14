---
title: Averigüe si el valor de la celda comienza con comillas simples
type: docs
weight: 610
url: /es/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells ahora proporciona el[Estilo.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) property para encontrar si el valor de la celda comienza con una comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como muestra y 'muestra, etc.

{{% /alert %}} 
## **Averigüe si el valor de la celda comienza con comillas simples**
El siguiente código de muestra explica que las cadenas como muestra y 'muestra no se pueden diferenciar con[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) propiedad. Por lo tanto debemos usar[Estilo.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)propiedad para distinguirlos.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}

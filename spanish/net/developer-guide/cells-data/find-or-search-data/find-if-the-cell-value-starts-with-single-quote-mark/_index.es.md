---
title: Averigüe si el valor de la celda comienza con comillas simples
type: docs
weight: 270
url: /es/net/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}}

 Aspose.Cells ahora proporciona el[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) property para encontrar si el valor de la celda comienza con una comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como muestra y 'muestra, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como muestra y 'muestra no se pueden diferenciar con[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) propiedad. Por lo tanto debemos usar[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)propiedad para distinguirlos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}

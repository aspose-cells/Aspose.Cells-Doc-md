---
title: Encuentre si el valor de la celda comienza con comillas simples
type: docs
weight: 270
url: /es/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprenda a saber si el valor de la celda comienza con una comilla simple hasta Aspose.Cells for .NET API.
keywords: Find cell value starts with a single quote mark, Search cell value starts with a single quote mark
---
{{% alert color="primary" %}}

 Aspose.Cells ahora proporciona la[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) propiedad para encontrar si el valor de la celda comienza con una comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como muestra y muestra, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como sample y 'sample no se pueden diferenciar con[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) propiedad. Por lo tanto debemos utilizar[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)propiedad para distinguirlos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}

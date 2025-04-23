---
title: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 270
url: /es/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprenda cómo encontrar si el valor de la celda comienza con un signo de comilla simple a través de la API Aspose.Cells for .NET.
keywords: Encontrar valor de celda que comienza con un signo de comilla simple, Buscar valor de celda que comienza con un signo de comilla simple
---

{{% alert color="primary" %}}

Ahora Aspose.Cells proporciona la propiedad [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) para encontrar si el valor de la celda comienza con un signo de comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como ejemplo y 'ejemplo, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como ejemplo y 'ejemplo no se pueden diferenciar con la propiedad [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). Por lo tanto, debemos usar la propiedad [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) para distinguirlas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
{{< app/cells/assistant language="csharp" >}}

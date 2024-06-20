---
title: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 270
url: /it/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Scopri come trovare se il valore della cella inizia con un singolo segno di citazione tramite l API Aspose.Cells for .NET.
keywords: Trova il valore della cella che inizia con un singolo segno di citazione, Cerca il valore della cella che inizia con un singolo segno di citazione
---

{{% alert color="primary" %}}

Aspose.Cells ora fornisce la proprietà [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) per trovare se il valore della cella inizia con un singolo segno di citazione. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come campione e 'campione ecc.

{{% /alert %}}

Il seguente codice di esempio spiega che le stringhe come campione e 'campione non possono essere differenziate con la proprietà [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). Pertanto, dobbiamo utilizzare la proprietà [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) per distinguerle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}

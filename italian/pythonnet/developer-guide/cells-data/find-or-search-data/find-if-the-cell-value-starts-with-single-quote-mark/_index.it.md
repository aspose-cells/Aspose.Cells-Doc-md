---
title: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 270
url: /it/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Scopri come trovare se il valore della cella inizia con un singolo apice attraverso l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Trova valore della cella che inizia con un singolo apice, Cerca valore della cella che inizia con un singolo apice in Python
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET ora fornisce la proprietà [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) per trovare se il valore della cella inizia con un singolo apice. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come campione e 'campione, ecc.

{{% /alert %}}

Il seguente codice di esempio spiega che le stringhe come campione e 'campione non possono essere differenziate con la proprietà [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). Pertanto, dobbiamo utilizzare la proprietà [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) per distinguerle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}

---
title: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 270
url: /it/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Impara come trovare se il valore di una cella inizia con un apostrofo tramite l’API Aspose.Cells for Node.js via C++.
keywords: Trova il valore della cella che inizia con un apostrofo Node.js tramite C++, Cerca il valore della cella che inizia con un apostrofo Node.js tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells ora fornisce il metodo [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) per trovare se il valore della cella inizia con un apostrofo. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come sample e 'sample' ecc.

{{% /alert %}}

Il seguente esempio di codice spiega che le stringhe come sample e 'sample' non possono essere differentiate con il metodo [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Pertanto, dobbiamo usare il metodo [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) per distinguerle.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}


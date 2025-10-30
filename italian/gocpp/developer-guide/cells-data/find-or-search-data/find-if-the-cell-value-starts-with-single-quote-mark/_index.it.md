---
title: Trova se il valore della cella inizia con un apostrofo singolo con Golang tramite C++
linktitle: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 270
url: /it/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Scopri come trovare se il valore della cella inizia con un simbolo di apice singolo tramite l API Aspose.Cells for C++.
keywords: Trova il valore della cella che inizia con un singolo segno di citazione, Cerca il valore della cella che inizia con un singolo segno di citazione
---

{{% alert color="primary" %}}

Aspose.Cells ora fornisce la proprietà [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) per trovare se il valore della cella inizia con un singolo segno di citazione. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come campione e 'campione ecc.

{{% /alert %}}

Il seguente codice di esempio spiega che le stringhe come campione e 'campione non possono essere differenziate con la proprietà [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Pertanto, dobbiamo utilizzare la proprietà [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) per distinguerle.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}

---
title: Ottieni il valore stringa della cella con e senza formattazione con Golang tramite C++
linktitle: Ottieni il valore stringa della cella
type: docs
weight: 240
url: /it/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Impara come ottenere il valore stringa della cella con e senza formattazione tramite l API Aspose.Cells for C++.
keywords: Ottieni il valore della stringa della cella con e senza formattazione, recuperare il valore della stringa della cella con e senza formattazione, ottenere il valore della stringa della cella con e senza formattazione
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) che può essere usato per ottenere il valore stringa della cella con o senza formattazione. Supponi di avere una cella con valore 0.012345 e di averla formattata per mostrare solo due decimali. Verrà visualizzata come 0.01 in Excel. Puoi recuperare i valori stringa come 0.01 e come 0.012345 usando il metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Richiede l'enumerazione [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) con i seguenti valori:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Il seguente codice di esempio spiega l'uso del metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}

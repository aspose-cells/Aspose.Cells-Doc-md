---
title: Ottieni il valore di una stringa della cella con o senza formattazione
type: docs
weight: 240
url: /it/net/get-cell-string-value-with-and-without-formatting/
description: Scopri come ottenere il valore della stringa della cella con e senza formattazione tramite l API Aspose.Cells for .NET.
keywords: Ottieni il valore della stringa della cella con e senza formattazione, recuperare il valore della stringa della cella con e senza formattazione, ottenere il valore della stringa della cella con e senza formattazione
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un metodo [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) che può essere utilizzato per ottenere il valore della stringa della cella con o senza alcuna formattazione. Supponiamo di avere una cella con valore 0.012345 e di averla formattata per visualizzare solo due posizioni decimali. Visualizzerà quindi come 0,01 in Excel. È possibile recuperare i valori delle stringhe sia come 0,01 che come 0,012345 utilizzando il metodo [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue). Assumi l'enumerazione [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) come parametro che ha i seguenti valori

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Il seguente codice di esempio spiega l'uso del metodo [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}

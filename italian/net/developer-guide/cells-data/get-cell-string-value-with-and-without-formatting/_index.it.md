---
title: Ottieni il valore stringa Cell con e senza formattazione
type: docs
weight: 240
url: /it/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce un metodo[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) che può essere utilizzato per ottenere il valore della stringa della cella con o senza alcuna formattazione. Supponiamo di avere una cella con valore 0,012345 e di averla formattata per visualizzare solo due cifre decimali. Verrà quindi visualizzato come 0,01 in Excel. È possibile recuperare valori di stringa sia come 0,01 che come 0,012345 utilizzando il[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) metodo. Ci vuole[**CellValueFormatStrategia**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum come parametro che ha i seguenti valori

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Il seguente codice di esempio spiega l'uso di[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}

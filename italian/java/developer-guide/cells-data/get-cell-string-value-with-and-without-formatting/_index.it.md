---
title: Ottieni il valore di una stringa della cella con o senza formattazione
type: docs
weight: 230
url: /it/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce un metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) che può essere utilizzato per ottenere il valore di stringa della cella con o senza formattazione. Supponiamo di avere una cella con valore 0.012345 e l'abbiamo formattata per visualizzare solo due cifre decimali. Lo visualizzerà come 0.01 in Excel. Puoi recuperare i valori delle stringhe sia come 0.01 sia come 0.012345 utilizzando il metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)). Prende come parametro l'enum [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) il quale ha i seguenti valori

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Ottieni il valore stringa della cella con e senza formattazione**
Il seguente codice di esempio spiega l'uso del metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) .

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Output della console**
Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}

---
title: Ottieni il valore di una stringa della cella con o senza formattazione
type: docs
weight: 230
url: /it/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce un metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) che può essere usato per ottenere il valore stringa della cella con o senza formattazione. Supponi di avere una cella con valore 0.012345 e di averla formattata per mostrare solo due decimali. Verrà mostrata come 0.01 in Excel. È possibile recuperare valori stringa sia come 0.01 che come 0.012345 usando il metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-). Accetta come parametro l’enum [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) che ha i seguenti valori.

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Ottieni il valore stringa della cella con e senza formattazione**
Il seguente esempio di codice spiega l’uso del metodo [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Output della console**
Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

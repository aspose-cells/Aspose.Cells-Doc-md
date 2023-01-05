---
title: Ottieni il valore stringa Cell con e senza formattazione
type: docs
weight: 230
url: /it/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells fornisce un metodo[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) che può essere utilizzato per ottenere il valore della stringa della cella con o senza alcuna formattazione. Supponiamo di avere una cella con valore 0,012345 e di averla formattata per visualizzare solo due cifre decimali. Verrà quindi visualizzato come 0,01 in Excel. È possibile recuperare valori di stringa sia come 0,01 che come 0,012345 utilizzando il[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) metodo. Ci vuole[CellValueFormatStrategia](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum come parametro che ha i seguenti valori

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Ottieni il valore stringa Cell con e senza formattazione**
 Il seguente codice di esempio spiega l'uso di[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Uscita console**
Di seguito è riportato l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}

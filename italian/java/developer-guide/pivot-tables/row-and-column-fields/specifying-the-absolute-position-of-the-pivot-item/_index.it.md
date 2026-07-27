---
title: Specificare la posizione assoluta dell elemento della tabella pivot
type: docs
weight: 40
url: /it/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

A volte, l'utente ha bisogno di specificare la posizione assoluta degli elementi della tabella pivot. Aspose.Cells API ha esposto alcune nuove proprietà e un metodo per soddisfare questo requisito dell'utente.

- Aggiunta la proprietà [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItems indipendentemente dal nodo genitore. Aggiunta la proprietà [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo genitore.
- Aggiunto il metodo [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) per spostare l'elemento su o giù in base al valore del conteggio, dove il conteggio è il numero di posizioni in cui spostare il PivotItem su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato su, mentre se il valore del conteggio è maggiore di zero, il PivotItem si sposterà giù, il parametro di tipo Booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo genitore o no.
- Obsoleto il metodo *PivotItem.move(int count)*, pertanto, si consiglia di utilizzare il nuovo metodo [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) al suo posto.

Si prega di notare che è necessario chiamare i metodi [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) e [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) prima di utilizzare le proprietà [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) e il metodo [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-).

{{% /alert %}}

## Codice di esempio

Il seguente codice di esempio crea una tabella pivot e poi specifica le posizioni dei Pivot Items nello stesso nodo genitore.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}

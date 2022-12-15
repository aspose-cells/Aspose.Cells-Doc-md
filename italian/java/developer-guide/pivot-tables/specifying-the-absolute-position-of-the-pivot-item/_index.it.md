---
title: Specificare la posizione assoluta dell'elemento pivot
type: docs
weight: 40
url: /it/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

A volte, l'utente deve specificare la posizione assoluta degli elementi pivot, l'API Aspose.Cells ha esposto alcune nuove proprietà e un metodo per soddisfare questo requisito dell'utente.

-  Aggiunto[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) proprietà che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItem indipendentemente dal nodo padre. Aggiunto[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) proprietà che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo padre.
-  Aggiunto[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)per spostare l'elemento verso l'alto o verso il basso in base al valore del conteggio, dove il conteggio è il numero di posizioni per spostare l'oggetto PivotItem verso l'alto o verso il basso. Se il valore del conteggio è minore di zero, l'elemento verrà spostato verso l'alto mentre se il valore del conteggio è maggiore di zero, il PivotItem si sposterà verso il basso, parametro di tipo booleano isSameParent che specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo padre o non.
-  Obsoleto il*PivotItem.move(int count)* metodo, pertanto, si suggerisce di utilizzare il metodo appena aggiunto[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) invece.

 Si prega di notare che è necessario chiamare il[**Tabella pivot.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) e[**Tabella pivot.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) metodi prima dell'uso[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) proprietà e[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) metodo.

{{% /alert %}}

## Codice di esempio

Il seguente codice di esempio crea una tabella pivot e quindi specifica le posizioni degli elementi pivot nello stesso nodo padre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}

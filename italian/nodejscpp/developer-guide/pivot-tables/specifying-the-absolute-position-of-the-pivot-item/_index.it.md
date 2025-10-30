---
title: Specificare la posizione assoluta dell elemento pivot
type: docs
weight: 50
url: /it/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

A volte, gli utenti devono specificare la posizione assoluta degli elementi pivot, l'API di Aspose.Cells for Node.js via C++ ha introdotto alcune nuove proprietà e un metodo per soddisfare questa esigenza.

- Aggiunta la proprietà [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItems indipendentemente dal nodo genitore. Aggiunta la proprietà [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo genitore.
- Aggiunta del metodo [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) per spostare l'elemento su o giù in base al valore del conteggio, dove il conteggio è il numero di posizioni per spostare l'elemento pivot su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato verso l'alto mentre se il valore del conteggio è maggiore di zero, l'elemento pivot si sposterà verso il basso, il parametro di tipo Boolean isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo padre o meno.
- Il metodo *PivotItem.move(int count)* è stato desueto, pertanto si consiglia di usare invece il nuovo metodo [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

Il seguente codice di esempio crea una tabella pivot e specifica quindi le posizioni degli elementi pivot nello stesso nodo padre. Puoi scaricare i file [Excel di origine](5112632.xlsx) e [Excel di output](5112619.xlsx) per il tuo riferimento. Se apri il file Excel di output, vedrai che l'elemento pivot "4H12" si trova nella posizione 0 nel padre "K11" e "DIF400" si trova nella terza posizione. Allo stesso modo, CA32 si trova nella posizione 1 e AAA3 è nella posizione 2

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Si prega di notare che è necessario chiamare i metodi PivotTable.RefreshData e PivotTable.CalculateData prima di utilizzare le proprietà [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) e il metodo [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}

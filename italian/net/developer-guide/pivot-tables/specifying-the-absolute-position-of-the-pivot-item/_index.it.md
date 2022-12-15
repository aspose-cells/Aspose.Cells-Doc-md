---
title: Specificare la posizione assoluta dell'elemento pivot
type: docs
weight: 50
url: /it/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

A volte, l'utente deve specificare la posizione assoluta degli elementi pivot, l'API Aspose.Cells ha esposto alcune nuove proprietà e un metodo per soddisfare i requisiti dell'utente.

-  Aggiunto[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) proprietà che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItem indipendentemente dal nodo padre. Aggiunto[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) proprietà che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo padre.
-  Aggiunto[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)metodo per spostare l'elemento in alto o in basso in base al valore di conteggio, dove conteggio è il numero di posizioni per spostare l'oggetto PivotItem in alto o in basso. Se il valore del conteggio è minore di zero, l'elemento verrà spostato verso l'alto dove, come se il valore del conteggio fosse maggiore di zero, il PivotItem si sposterà verso il basso, il parametro di tipo booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo padre o no.
-  Obsoleto il*PivotItem.Move(int count)* metodo pertanto si suggerisce di utilizzare il metodo appena aggiunto[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) invece.

{{% /alert %}}

 Il seguente codice di esempio crea una tabella pivot e quindi specifica le posizioni degli elementi pivot nello stesso nodo padre. Puoi scaricare il[fonte Excel](5112632.xlsx) e[uscita Excel](5112619.xlsx) file per il vostro riferimento. Se apri il file Excel di output, vedrai che l'elemento pivot "4H12" è in posizione 0 nel genitore "K11" e "DIF400" è in posizione 3. Allo stesso modo, CA32 è in posizione 1 e AAA3 è in posizione 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Si noti che è necessario chiamare i metodi PivotTable.RefreshData e PivotTable.CalculateData prima di utilizzare[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) proprietà e[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) metodo.

{{% /alert %}}

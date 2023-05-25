---
title: Elimina righe e colonne vuote in un foglio di lavoro
type: docs
weight: 300
url: /it/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

È possibile eliminare tutte le righe e le colonne vuote da un foglio di lavoro. Ciò è utile quando, ad esempio, si genera un file PDF da un file Excel Microsoft e si desidera convertire solo righe e colonne che contengono dati o oggetti correlati.

Utilizzare i seguenti metodi Aspose.Cells per eliminare righe e colonne vuote:

1.  Per eliminare le righe vuote, utilizzare il[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) metodo. Si prega di notare che per le righe vuote che verranno eliminate, non è solo necessario[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) dovrebbe essere vero, ma anche non dovrebbe esserci alcun commento visibile definito per nessuna cella in quelle righe e nessuna tabella pivot il cui intervallo si interseca con esse.
1.  Per eliminare le colonne vuote, utilizzare il[**Cells. Elimina colonne vuote ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) metodo.

{{% /alert %}}

##  C# codice per eliminare righe vuote

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  C# codice per eliminare colonne vuote

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}

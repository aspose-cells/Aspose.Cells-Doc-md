---
title: Eliminare Righe e Colonne Vuote in un Foglio di Lavoro
type: docs
weight: 300
url: /it/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

È possibile eliminare tutte le righe e le colonne vuote da un foglio di lavoro. Questo è utile, ad esempio, quando si genera un file PDF da un file Microsoft Excel e si desidera convertire solo le righe e le colonne che contengono dati o oggetti correlati.

Utilizzare i seguenti metodi Aspose.Cells per eliminare le righe e le colonne vuote:

1. Per eliminare le righe vuote, utilizzare il metodo [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). Si prega di notare che, per le righe vuote che verranno eliminate, non è solo richiesto che [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) sia vero, ma non deve essere definito alcun commento visibile per qualsiasi cella in quelle righe e non deve esserci alcuna tabella pivot il cui intervallo si sovrapponga con esse.
1. Per eliminare le colonne vuote, utilizzare il metodo [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## Codice C# per eliminare le righe vuote

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## Codice C# per eliminare le colonne vuote

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}

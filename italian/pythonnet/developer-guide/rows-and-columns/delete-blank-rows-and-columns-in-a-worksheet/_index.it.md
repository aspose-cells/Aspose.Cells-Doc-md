---
title: Eliminare Righe e Colonne Vuote in un Foglio di Lavoro
type: docs
weight: 300
url: /it/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Questo articolo descrive come eliminare le righe e le colonne vuote in un foglio di lavoro con la libreria Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, eliminare righe vuote in Python, rimuovere righe vuote in Python, eliminare colonne vuote in Python, rimuovere colonne vuote in Python, eliminare o rimuovere righe e colonne vuote.
---

{{% alert color="primary" %}}

È possibile eliminare tutte le righe e le colonne vuote da un foglio di lavoro. Questo è utile, ad esempio, quando si genera un file PDF da un file Microsoft Excel e si desidera convertire solo le righe e le colonne che contengono dati o oggetti correlati.

Utilizzare i seguenti metodi Aspose.Cells per eliminare le righe e le colonne vuote:

1. Per eliminare le righe vuote, utilizzare il metodo [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). Si prega di notare che, per le righe vuote che verranno eliminate, non è solo richiesto che [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) sia vero, ma non deve essere definito alcun commento visibile per qualsiasi cella in quelle righe e non deve esserci alcuna tabella pivot il cui intervallo si sovrapponga con esse.
1. Per eliminare le colonne vuote, utilizzare il metodo [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## Codice C# per eliminare le righe vuote

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## Codice C# per eliminare le colonne vuote

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}

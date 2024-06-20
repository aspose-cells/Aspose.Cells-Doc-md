---
title: Inserisci o elimina righe in un foglio Excel
type: docs
weight: 20
url: /it/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Questo articolo fornisce il codice python per inserire ed eliminare righe nel foglio Excel con la libreria Aspose.Cells for Python via .NET.
keywords: Libreria Excel di Python, inserisci o elimina righe nel foglio Excel, inserisci o elimina righe in Excel con Python, inserisci righe in Excel con Python, elimina righe in Excel con Python, inserisci o elimina righe nel foglio Excel con Python, inserisci o elimina righe in Excel con Python, inserisci righe in Excel con Python, elimina righe in Excel con Python
---

{{% alert color="primary" %}}

Quando si crea un nuovo foglio di lavoro, o si lavora con un foglio di lavoro esistente, potresti aver bisogno di aggiungere righe o colonne aggiuntive per ospitare i dati. Altre volte, potresti dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.

{{% /alert %}}

Aspose.Cells per Python via .NET offre due metodi per inserire ed eliminare righe: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) e [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.

Per inserire o rimuovere un numero di righe, ti consigliamo di utilizzare sempre i metodi [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) e [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) invece di usare i metodi [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) o [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) in un loop.

Aspose.Cells per Python via .NET funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso e verso destra. Quando vengono rimosse righe o colonne, il contenuto del foglio di lavoro viene spostato verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando vengono aggiunte o rimosse righe.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}

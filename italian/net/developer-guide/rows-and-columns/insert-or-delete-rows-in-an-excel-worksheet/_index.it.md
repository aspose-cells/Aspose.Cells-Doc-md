---
title: Inserisci o elimina righe in un foglio di lavoro Excel
type: docs
weight: 20
url: /it/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Questo articolo fornisce il codice C# per inserire ed eliminare righe nel foglio di lavoro di Excel
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

Quando si crea un nuovo foglio di lavoro o si lavora con un foglio di lavoro esistente, potrebbe essere necessario aggiungere ulteriori righe o colonne per contenere i dati. Altre volte, potrebbe essere necessario eliminare righe o colonne da posizioni specificate nel foglio di lavoro.

{{% /alert %}}

 Aspose.Cells offre due metodi per inserire ed eliminare righe:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) e[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.

 Per inserire o rimuovere più righe, si consiglia di utilizzare sempre il file[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) e[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) metodi invece di utilizzare il[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) o[**Elimina riga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)metodi in un ciclo.

Aspose.Cells funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso e verso destra. Quando vengono rimosse righe o colonne, il contenuto del foglio di lavoro viene spostato verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando le righe vengono aggiunte o rimosse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}

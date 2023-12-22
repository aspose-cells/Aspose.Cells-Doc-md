---
title: Ottieni tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico
type: docs
weight: 320
url: /it/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Scopri come ottenere tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico utilizzando Aspose.Cells for .NET API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **Possibili scenari di utilizzo**

Quando applichi il filtro automatico sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe darsi che alcune righe siano già nascoste manualmente dall'utente finale di Excel e non siano nascoste da un filtro automatico. Pertanto è difficile sapere quali righe sono nascoste dal filtro automatico e quali sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells affronta questo problema utilizzando l'int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metodo. Questo metodo restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico e non manualmente dall'utente finale di Excel.

##  **Ottieni tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico**

 Consulta il seguente codice di esempio che carica il file[file Excel di esempio](64716909.xlsx) che contiene alcune delle righe nascoste manualmente dall'utente finale di Excel. Il codice applica il filtro automatico e lo aggiorna utilizzando l'int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metodo che restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico. Quindi stampa gli indici delle righe nascoste sulla console insieme ai nomi e ai valori delle celle.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **Uscita della console**

{{< highlight "java" >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}

---
title: Ottieni tutti gli indici delle righe nascoste dopo l'aggiornamento del filtro automatico
type: docs
weight: 320
url: /it/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Possibili scenari di utilizzo**

Quando applichi il filtro automatico alle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe accadere che alcune righe siano già nascoste manualmente dall'utente finale di Excel e non siano nascoste da un filtro automatico. Rende quindi difficile sapere quali delle righe sono nascoste dal filtro automatico e quali di esse sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells affronta questo problema usando int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metodo. Questo metodo restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico e non manualmente dall'utente finale di Excel.

## **Ottieni tutti gli indici delle righe nascoste dopo l'aggiornamento del filtro automatico**

 Vedere il seguente codice di esempio che carica il file[esempio di file Excel](64716909.xlsx) che contiene alcune delle righe nascoste manualmente dall'utente finale di Excel. Il codice applica il filtro automatico e lo aggiorna utilizzando int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metodo che restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico. Quindi stampa gli indici delle righe nascoste sulla console insieme ai nomi e ai valori delle celle.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

## **Uscita console**

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

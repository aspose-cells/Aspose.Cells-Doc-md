---
title: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
type: docs
weight: 240
url: /it/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Possibili Scenari di Utilizzo**

Quando si applica un filtro automatico sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Tuttavia potrebbe accadere che alcune delle righe siano già state nascoste manualmente dall'utente finale di Excel e non siano nascoste dal filtro automatico. Questo rende difficile sapere quali righe sono nascoste dal filtro automatico e quali sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells affronta questo problema utilizzando il metodo int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)). Questo metodo restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico e non manualmente dall'utente finale di Excel.

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**

Consultare il seguente codice di esempio che carica il [file Excel di esempio](64716913.xlsx) che contiene alcune righe nascoste manualmente dall'utente di Excel. Il codice applica il filtro automatico e lo ricarica utilizzando il metodo int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) che restituisce gli indici delle righe nascoste dal filtro automatico. Poi stampa gli indici delle righe nascoste sulla console insieme ai nomi e valori delle celle.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Output della console**

{{< highlight java >}}

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

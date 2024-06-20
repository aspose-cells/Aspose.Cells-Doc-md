---
title: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
type: docs
weight: 320
url: /it/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Scopri come ottenere tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro utilizzando l API Aspose.Cells for .NET.
keywords: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro, Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro, Recupera tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
---

## **Possibili Scenari di Utilizzo**

Quando si applica l'autofiltro sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe essere il caso che alcune righe siano già state nascoste manualmente dall'utente finale di Excel e non sono nascoste da un autofiltro. Ciò rende difficile sapere quali delle righe sono nascoste dall'autofiltro e quali sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells affronta questo problema utilizzando il metodo int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1). Questo metodo restituisce gli indici di riga di tutte le righe nascoste dall'autofiltro e non manualmente dall'utente finale di Excel.

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](64716909.xlsx) che contiene alcune delle righe nascoste manualmente dall'utente finale di Excel. Il codice applica l'autofiltro e lo aggiorna utilizzando il metodo int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) che restituisce gli indici di riga di tutte le righe nascoste dall'autofiltro. Poi stampa gli indici delle righe nascoste sulla console insieme ai nomi e ai valori delle celle.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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

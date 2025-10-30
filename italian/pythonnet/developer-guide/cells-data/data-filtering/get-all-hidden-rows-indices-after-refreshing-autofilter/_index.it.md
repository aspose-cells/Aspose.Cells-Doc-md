---
title: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
type: docs
weight: 320
url: /it/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Scopri come ottenere tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro Python, Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro Python, Recupera tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro Python
---

## **Possibili Scenari di Utilizzo**

Quando si applica l'auto filtro sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe anche essere il caso che alcune delle righe siano già nascoste manualmente dall'utente finale di Excel e non siano nascoste da un filtro automatico. È quindi difficile sapere quali delle righe sono nascoste dal filtro automatico e quali sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells per Python via .NET affronta questo problema utilizzando il metodo [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). Questo metodo restituisce gli indici di riga di tutte le righe che sono nascoste dal filtro automatico e non manualmente dall'utente finale di Excel.

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](64716909.xlsx) che contiene alcune delle righe nascoste manualmente dall'utente finale di Excel. Il codice applica l'auto filtro e lo aggiorna utilizzando il metodo {0 che restituisce gli indici di riga di tutte le righe nascoste dal filtro automatico. Stampa quindi gli indici delle righe nascoste sulla console insieme ai nomi e ai valori delle celle.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
{{< app/cells/assistant language="python-net" >}}

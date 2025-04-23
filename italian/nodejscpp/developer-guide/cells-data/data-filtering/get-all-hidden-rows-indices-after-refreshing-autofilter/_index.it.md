---  
title: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro 
type: docs  
weight: 320  
url: /it/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Scopri come ottenere tutti gli indici delle righe nascoste dopo aver aggiornato AutoFilter usando l API Aspose.Cells for Node.js via C++.  
keywords: Ottieni tutti gli indici delle righe nascoste dopo aggiornamento AutoFilter Node.js tramite C++, Ottieni tutti gli indici delle righe nascoste dopo aggiornamento AutoFilter Node.js tramite C++, Recupera tutti gli indici delle righe nascoste dopo aggiornamento AutoFilter Node.js tramite C++  
---  

## **Possibili Scenari di Utilizzo**  

Quando applichi il filtro automatico sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe essere il caso che alcune righe siano già nascoste manualmente dall'utente Excel e non nascoste dal filtro automatico. Perciò è difficile sapere quali righe sono nascoste dal filtro automatico e quali sono nascoste manualmente dall'utente Excel. Aspose.Cells for Node.js via C++ affronta questo problema usando l’`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Questo metodo restituisce gli indici delle righe di tutte le righe che sono nascoste dal filtro automatico e non manualmente dall'utente Excel.  

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**  

Vedi il seguente esempio di codice che carica il [file Excel di esempio](64716909.xlsx) che contiene alcune righe nascoste manualmente dall'utente Excel. Il codice applica il filtro automatico e lo aggiorna usando il metodo `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) che restituisce gli indici di tutte le righe nascoste dal filtro automatico. Quindi stampa gli indici delle righe nascoste sulla console insieme ai nomi delle celle e ai valori.  

## **Codice di Esempio**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


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

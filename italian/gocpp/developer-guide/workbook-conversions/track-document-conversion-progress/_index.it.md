---
title: Traccia lo stato di avanzamento della conversione dei documenti con Golang via C++
linktitle: Monitora il progresso della conversione del documento
type: docs
weight: 970
url: /it/go-cpp/track-document-conversion-progress/
description: Impara come monitorare lo stato di avanzamento della conversione del documento in C++ usando Aspose.Cells per migliorare l usabilità dell applicazione.
---

## **Possibili Scenari di Utilizzo**

A volte la conversione di grandi file Excel può richiedere del tempo. Durante questo periodo, potresti voler mostrare lo stato di avanzamento della conversione invece di una semplice schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il tracciamento dello stato di avanzamento della conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) offre i metodi [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) e [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata `TestPageSavingCallback`.

## **Monitorare il progresso della conversione dei documenti**

Il seguente esempio di codice carica il [file Excel di origine](94896151.xlsx) e stampa il suo progresso di conversione nella console utilizzando la classe personalizzata `TestPageSavingCallback` che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Il seguente è il codice per la classe personalizzata `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
## **Output della console**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}

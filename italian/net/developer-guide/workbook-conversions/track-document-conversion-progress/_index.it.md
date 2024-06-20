---
title: Monitora il progresso della conversione del documento
type: docs
weight: 970
url: /it/net/track-document-conversion-progress/
---

## **Possibili Scenari di Utilizzo**

A volte la conversione di file di Excel di grandi dimensioni può richiedere del tempo. Durante questo periodo, potresti voler mostrare il progresso della conversione del documento invece di solo una schermata di caricamento per migliorare l'utilizzabilità della tua applicazione. Aspose.Cells supporta il monitoraggio del processo di conversione dei documenti fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) e [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) che è possibile implementare nella tua classe personalizzata. È inoltre possibile controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata T*estPageSavingCallback*.

## **Monitorare il progresso della conversione dei documenti**

Il seguente esempio di codice carica il [file excel di origine](94896151.xlsx) e stampa il progresso della conversione nella console usando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

Il seguente è il codice per la classe personalizzata *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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

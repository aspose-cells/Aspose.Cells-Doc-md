---
title: Monitora il progresso della conversione del documento
type: docs
weight: 120
url: /it/java/track-document-conversion-progress/
---

## **Possibili Scenari di Utilizzo**

A volte la conversione di grandi file Excel può richiedere del tempo. Durante questo periodo, potresti voler mostrare il progresso della conversione del documento anziché solo una schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il tracciamento del processo di conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) e [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.

## **Monitorare il progresso della conversione dei documenti**

Il seguente esempio di codice carica il *file Excel di origine](PagesBook1.xlsx) e stampa il progresso della conversione nella console utilizzando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Il seguente è il codice per la classe personalizzata *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

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
{{< app/cells/assistant language="java" >}}

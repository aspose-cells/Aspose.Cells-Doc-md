---
title: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 140
url: /it/java/track-conversion-progress-of-excel-to-tiff/
---

## **Possibili Scenari di Utilizzo**

A volte la conversione di grandi file Excel può richiedere del tempo. Durante questo periodo, potresti voler mostrare il progresso della conversione del documento anziché solo una schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il tracciamento del processo di conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs)) e [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs)) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestTiffPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

Il seguente esempio di codice carica il [file Excel di origine](sampleUseWorkbookRenderForImageConversion.xlsx) e stampa il progresso della conversione nella console utilizzando la classe personalizzata *TestTiffPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback). Il file di output generato è allegato per il tuo riferimento.

[File di Output](DocumentConversionProgressForTiff_out.tiff)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Di seguito è riportato il codice per la classe personalizzata *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Output della console**

{{< highlight java >}}
Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10

{{< /highlight >}}

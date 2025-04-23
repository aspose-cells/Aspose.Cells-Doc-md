---
title: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/net/track-conversion-progress-of-excel-to-tiff/
---

## **Possibili Scenari di Utilizzo**

A volte la conversione di file di Excel di grandi dimensioni può richiedere del tempo. Durante questo periodo, potresti voler mostrare il progresso della conversione del documento invece di solo una schermata di caricamento per migliorare l'utilizzabilità della tua applicazione. Aspose.Cells supporta il monitoraggio del processo di conversione dei documenti fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) e [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) che è possibile implementare nella tua classe personalizzata. È inoltre possibile controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata T*estPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

Il seguente esempio di codice carica il [file excel di origine](95584311.xlsx) e stampa il progresso della sua conversione nella console utilizzando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). Il file di output generato è allegato per il tuo riferimento.

[Output File](95584312.tiff)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Di seguito è riportato il codice per la classe personalizzata *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

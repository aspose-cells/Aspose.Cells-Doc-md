---
title: traccia il progresso della conversione da Excel a TIFF con Golang tramite C++
linktitle: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Impara come monitorare lo stato di avanzamento della conversione di file Excel in formato TIFF usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

 A volte, convertire grandi file Excel può richiedere del tempo. Durante questo periodo, potresti voler mostrare lo stato di avanzamento della conversione del documento invece di una semplice schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il monitoraggio dello stato di avanzamento della conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) fornisce i metodi [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) e [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

 Il seguente esempio di codice carica il file Excel di origine e stampa lo stato di avanzamento della conversione nel console utilizzando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Il file di output generato è allegato per riferimento.

[Output File](95584312.tiff)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Di seguito è riportato il codice per la classe personalizzata *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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

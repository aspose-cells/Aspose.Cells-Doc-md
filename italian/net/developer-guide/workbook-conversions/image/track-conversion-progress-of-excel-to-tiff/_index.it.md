---
title: Tieni traccia dell'avanzamento della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/net/track-conversion-progress-of-excel-to-tiff/
---
## **Possibili scenari di utilizzo**

 A volte la conversione di file Excel di grandi dimensioni può richiedere del tempo. Durante questo periodo, potresti voler mostrare l'avanzamento della conversione del documento anziché solo una schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il processo di conversione del documento di monitoraggio fornendo il file**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** interfaccia. Il**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**fornisce l'interfaccia**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**e**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**metodi che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono rese come mostrato nel T*estPageSavingCallback*classe personalizzata.

## **Tieni traccia dell'avanzamento della conversione di Excel in TIFF**

 L'esempio di codice seguente carica il file[file excel di origine](95584311.xlsx) e stampa l'avanzamento della conversione nella console utilizzando il file*TestPageSavingCallback* classe personalizzata che implementa il**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**interfaccia. Il file di output generato è allegato come riferimento.

[File di uscita](95584312.tiff)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Quello che segue è il codice per il*TestTiffPageSavingCallback*classe personalizzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **Uscita console**

Inizia a salvare l'indice della pagina 0 delle pagine 10</br>
Terminare il salvataggio dell'indice 0 delle pagine 10</br>
Inizia a salvare l'indice della pagina 1 delle pagine 10</br>
Terminare il salvataggio dell'indice 1 delle pagine 10</br>
Inizia a salvare l'indice della pagina 2 delle pagine 10</br>
Terminare il salvataggio dell'indice 2 delle pagine 10</br>
Inizia a salvare l'indice della pagina 3 delle pagine 10</br>
Terminare il salvataggio dell'indice 3 delle pagine 10</br>
Inizia a salvare l'indice della pagina 4 delle pagine 10</br>
Terminare il salvataggio dell'indice 4 delle pagine 10</br>
Inizia a salvare l'indice della pagina 5 delle pagine 10</br>
Terminare il salvataggio dell'indice 5 delle pagine 10</br>
Inizia a salvare l'indice della pagina 6 delle pagine 10</br>
Terminare il salvataggio dell'indice 6 delle pagine 10</br>
Inizia a salvare l'indice della pagina 7 delle pagine 10</br>
Terminare il salvataggio dell'indice 7 delle pagine 10</br>
Inizia a salvare l'indice della pagina 8 delle pagine 10</br>
Terminare il salvataggio dell'indice 8 delle pagine 10</br>


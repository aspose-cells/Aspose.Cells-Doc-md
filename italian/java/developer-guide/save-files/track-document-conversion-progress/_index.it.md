---
title: Tieni traccia dell'avanzamento della conversione del documento
type: docs
weight: 120
url: /it/java/track-document-conversion-progress/
---
## **Possibili scenari di utilizzo**

volte la conversione di file Excel di grandi dimensioni può richiedere del tempo. Durante questo periodo, potresti voler mostrare l'avanzamento della conversione del documento anziché solo una schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells supporta il processo di conversione del documento di monitoraggio fornendo il file**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaccia. Il**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**fornisce l'interfaccia**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**e**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** metodi che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono riprodotte come mostrato nel*TestPageSavingCallback*classe personalizzata.

## **Tieni traccia dell'avanzamento della conversione del documento**

L'esempio di codice seguente carica il file[file excel di origine](PagesBook1.xlsx)e stampa l'avanzamento della conversione nella console utilizzando il file*TestPageSavingCallback*classe personalizzata che implementa il**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interfaccia.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Quello che segue è il codice per il*TestPageSavingCallback*classe personalizzata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Uscita console**

Inizia a salvare l'indice della pagina 0 delle pagine 11</br>
Terminare il salvataggio dell'indice 0 delle pagine 11</br>
Inizia a salvare l'indice della pagina 1 delle pagine 11</br>
Terminare il salvataggio dell'indice 1 delle pagine 11</br>
Inizia a salvare l'indice della pagina 2 delle pagine 11</br>
Terminare il salvataggio dell'indice 2 delle pagine 11</br>
Inizia a salvare l'indice della pagina 3 delle pagine 11</br>
Terminare il salvataggio dell'indice 3 delle pagine 11</br>
Inizia a salvare l'indice della pagina 4 delle pagine 11</br>
Terminare il salvataggio dell'indice 4 delle pagine 11</br>
Inizia a salvare l'indice della pagina 5 delle pagine 11</br>
Terminare il salvataggio dell'indice 5 delle pagine 11</br>
Inizia a salvare l'indice della pagina 6 delle pagine 11</br>
Terminare il salvataggio dell'indice 6 delle pagine 11</br>
Inizia a salvare l'indice della pagina 7 delle pagine 11</br>
Terminare il salvataggio dell'indice 7 delle pagine 11</br>
Inizia a salvare l'indice della pagina 8 delle pagine 11</br>
Terminare il salvataggio dell'indice 8 delle pagine 11

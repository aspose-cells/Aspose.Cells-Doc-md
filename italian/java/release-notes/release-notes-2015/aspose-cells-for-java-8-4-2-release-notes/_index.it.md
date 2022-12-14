---
title: Aspose.Cells for Java 8.4.2 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-8-4-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.4.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSJAVA-41289) - Modo semplice per l'impostazione del grafico


## **Insetti**


 (CELLSJAVA-41323) - Le filigrane non vengono visualizzate correttamente

 (CELLSJAVA-41319) - Il filtro dei dati viene rimosso in Excel 2010/2013 dopo il salvataggio

 (CELLSJAVA-41317) - I caratteri maiuscoli creati tramite la funzionalità "Tutto maiuscolo" in Excel non vengono conservati in PDF

 (CELLSJAVA-41315) - Il rendering delle forme nella pagina 5 non è corretto

 (CELLSJAVA-41308) - La posizione della forma è errata durante il rendering del foglio di calcolo in formato PDF

 (CELLSJAVA-41282) - Le punte delle frecce vengono ingrandite durante la conversione del foglio di calcolo con disegni in PDF

(CELLSJAVA-41249) - WordArt non viene visualizzato correttamente nel file PDF di output

 (CELLSJAVA-41243) - Il testo orizzontale nelle forme viene reso verticale durante la conversione del foglio di calcolo in PDF

 (CELLSJAVA-41242) - Il disegno è incasinato durante il rendering del foglio di calcolo in PDF

 (CELLSJAVA-41241) - Le forme circolari vengono convertite in ovali durante il rendering del foglio di calcolo in PDF

 (CELLSJAVA-41233) - Gli oggetti e le forme del disegno nel modello Excel non vengono visualizzati correttamente nel PDF di output utilizzando Aspose.Cells

 (CELLSJAVA-41302) - L'ultima versione Aspose non riesce a salvare il file salvato tramite la versione precedente

 (CELLSJAVA-41299) - Il file viene danneggiato quando xls viene salvato nel formato xlsx

 (CELLSJAVA-41284) - Workbook.copy() corrompe il file excel di output

 (CELLSJAVA-41283) - Errore di calcolo con la funzione OR

 (CELLSJAVA-41281) - L'operazione di adattamento automatico delle colonne non ha effetto con alcune celle con l'opzione ShrinkToFit attivata

 (CELLSJAVA-41313) - Le linee continue vengono visualizzate come linee tratteggiate

(CELLSJAVA-41306) - Problema di conversione da Excel a PDF - parte destra tagliata

 (CELLSJAVA-41316) - Mancano alcune etichette dati nel file HTML sottoposto a rendering durante la copia della cartella di lavoro

 (CELLSJAVA-41314) - I DataLabel nel grafico non sono mostrati nell'immagine EMF renderizzata

 (CELLSJAVA-41311) - Etichette dell'asse del grafico mancanti durante la conversione in EMF

 (CELLSJAVA-41301) - I caratteri ebraici in "smart art" presenti in Excel sono rispecchiati nella versione PDF

 (CELLSJAVA-41300) - Dati del grafico a torta errati durante il rendering tramite Aspose

 (CELLSJAVA-41285) - L'altezza dell'area del tracciato del grafico aumenta dopo aver combinato le cartelle di lavoro

 (CELLSJAVA-41277) - Solo il rendering del grafico a torta genera un PDF vuoto

 (CELLSJAVA-41276) - Chart.toImage genera un'immagine vuota per il grafico a torta

 (CELLSJAVA-41275) - Mancano due delle etichette Axis nell'EMF risultante durante la conversione del grafico in immagine

 (CELLSJAVA-40606) - L'immagine di rendering del grafico non è corretta (da grafico a immagine)

(CELLSJAVA-40368) - Chart.calculate() posiziona in modo errato le etichette degli assi X e Y


## **Eccezioni**


 (CELLSJAVA-41310) - java.lang.IndexOutOfBoundsException: Indice: 2, Dimensione: 2, nella cartella di lavoro ctro

 (CELLSJAVA-41307) - java.lang.ArrayIndexOutOfBoundsException: -1 nella cartella di lavoro ctor durante il caricamento del file salvato con Aspose.Cells

 (CELLSJAVA-41280) - Si è verificata l'eccezione "java.lang.ArrayIndexOutOfBoundsException" per un formato di data personalizzato dispari

 (CELLSJAVA-41274) - java.lang.NullPointerException in Workbook.save dopo ripetute operazioni di caricamento e salvataggio


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge i metodi VbaModuleCollection.Add

 Aggiunge il modulo VBA.



 Aggiunge i metodi override Cells.CopyColumns().

 Copia alcune colonne.



Aggiunge le enumerazioni PasteType.Default e PasteType.DefaultExceptBorders.

 Viene utilizzato per copiare l'intervallo come "Tutto" e "Tutto tranne i bordi" in MS Excel.





 Nota

 Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.4.2 sono inclusi anche in questo Aspose.Cells for Java v8.4.2.

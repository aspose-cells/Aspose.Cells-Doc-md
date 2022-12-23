---
title: Aspose.Cells for Java 8.5.0 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-8-5-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.5.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.0/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSJAVA-41335) - Miglioramento del meccanismo PasteOptions/PasteType per consentire la copia delle altezze delle righe durante la copia degli intervalli

 (CELLSJAVA-41053) - Ricalcolo del fattore di ridimensionamento della configurazione della pagina


## **Miglioramenti**


 (CELLSJAVA-41334) - Formula/funzione HYPERLINK - Consenti all'utente di elaborare i parametri del collegamento ipertestuale

 (CELLSJAVA-41357) - CELLSJAVA-41225 Colore di sfondo errato restituito da Aspose.Cells


## **Insetti**


 (CELLSJAVA-41366) - Foglio di calcolo danneggiato dopo l'apertura e il salvataggio del file modello XLSX

 (CELLSJAVA-41355) - La conversione in HTML aggiunge # stringa alla fine dei valori per una colonna

(CELLSJAVA-41354) - Numbers nelle caselle di testo non vengono visualizzate all'interno

 (CELLSJAVA-41353) - Il posizionamento/allineamento delle arti intelligenti in PDF non corrisponde al file Excel di origine

 (CELLSJAVA-41343) - La linea di fondo è molto più lunga dell'originale nel file modello

 (CELLSJAVA-41342) - Dati spostati a destra nel file modello

 (CELLSJAVA-41341) - Il testo è sovrapposto a uno sfondo bianco nel file modello

 (CELLSJAVA-41340) - Cell l'allineamento è a sinistra anziché a destra nel file modello

 (CELLSJAVA-41339) - Il testo e l'allineamento del testo sono incasinati nel file modello

 (CELLSJAVA-41336) - Errore JavaScript durante l'esportazione in HTML

 (CELLSJAVA-41327) - Perdita di testo nel file modello

 (CELLSJAVA-41326) - Perdita di testo nel file modello

 (CELLSJAVA-41304) - Conversioni non riuscite da XLS a PDF con le API Aspose.Cells

(CELLSJAVA-41206) - Conversione di file Excel contenenti collegamenti ipertestuali in HTML - Cell i collegamenti ipertestuali di riferimento non funzionano

 (CELLSJAVA-40483) - Problema con la formattazione di una forma/oggetto freccia - Rendering da Excel a PDF

 (CELLSJAVA-41372) - Il diagramma di Gantt non viene visualizzato nel formato file di output PDF

 (CELLSJAVA-41363) - Problema con i valori restituiti dei parametri nel calcolo della funzione personalizzata

 (CELLSJAVA-41345) - La funzione personalizzata che coinvolge la formula di Excel (INDIRECT) ha esito negativo

 (CELLSJAVA-41320) - Problema con il valore ricevuto in una funzione personalizzata

 (CELLSJAVA-40734) - Problema con RefferedArea come risultato del calcolo del parametro

 (CELLSJAVA-41370) - Quando si crea un'istanza di una cartella di lavoro con un documento Excel danneggiato e LoadOptions, si verifica un blocco

 (CELLSJAVA-41369) - Problema con i filtri automatici sulle formule

 (CELLSJAVA-41348) - Il formato condizionale con formato numerico non funziona per XLS

(CELLSJAVA-41347) - Style.isDateTime restituisce false per una cella formattata come Data

 (CELLSJAVA-41338) - Il bordo sinistro appare quando non dovrebbe per una cella che ha una colonna nascosta adiacente

 (CELLSJAVA-41331) - Le formule non vengono aggiornate correttamente dopo l'inserimento delle righe

 (CELLSJAVA-41330) - Area di stampa dinamica interrotta quando si salva con nome / stampa PDF

 (CELLSJAVA-41365) - Alcuni caratteri ebraici nella casella di testo mancano nel file di output PDF

 (CELLSJAVA-41346) - Le etichette dell'asse dei valori e dell'asse delle categorie nel grafico sono oscurate (conversione da Excel a PDF)

 (CELLSJAVA-41312) - Il testo è troppo grande e si espande oltre il margine

 (CELLSJAVA-41305) - I caratteri di testo in grassetto si sovrappongono durante la conversione del foglio di lavoro in immagine

 (CELLSJAVA-40916) - Il testo al di fuori dell'interruzione di pagina viene visualizzato in PDF come testo a capo

 (CELLSJAVA-40791) - Problema con interruzione di pagina, rendering dei caratteri e margini in Excel per il rendering PDF

(CELLSJAVA-40605) - Aspose.Cells: il testo tagliato nella cella originale viene mostrato completamente quando convertito in PDF

 (CELLSJAVA-40479) - Problema di layout di pagina (RTL) rendering

 (CELLSJAVA-40448) - Il piè di pagina è incasinato nel file PDF generato

 (CELLSJAVA-41359) - Un piccolo punto appare al centro del grafico a torta durante il salvataggio come immagine

 (CELLSJAVA-41358) - Il grafico era in grado di accettare una formula di serie con valori vuoti ma ora genera un'eccezione

 (CELLSJAVA-41356) - Problemi di rendering durante la conversione del grafico in immagine

 (CELLSJAVA-41351) - Problema con la larghezza delle etichette dell'asse del grafico durante la conversione del foglio di lavoro Excel in immagine

 (CELLSJAVA-40607) - Problema relativo alle proprietà dell'etichetta dati del grafico

 (CELLSJAVA-40613) - Problema percentuale grafico a torta


## **Eccezioni**


 (CELLSJAVA-41377) - Eccezione quando viene chiamato cell.getPrecedents

 (CELLSJAVA-41361) - java.lang.NumberFormatException: per la stringa di input: "0,00" nella cartella di lavoro ctor

(CELLSJAVA-41344) - java.lang.NullPointerException a Cells.find


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge enum PasteType.RowHeights

 Viene utilizzato per copiare le altezze dell'intervallo.



 Aggiunge la proprietà SheetRender.PageScale.

 Viene utilizzato per ottenere la scala di pagina calcolata del foglio.



 Aggiunge il metodo Cell.GetStingValue(CellValueFormatStrategy).

 Viene utilizzato per ottenere il valore della stringa della cella mediante una strategia formattata specifica.



 Aggiunge la proprietà ExportTableOptions.FormatStrategy.

 Ottiene e imposta la strategia di formato durante l'esportazione del valore come valore stringa.



 Aggiunge la classe CalculationOptions.

 Rappresenta le opzioni per il calcolo delle formule.



Aggiunge metodi per il calcolo delle formule con CalculationOptions: Cell.Calculate(CalculationOptions),
 Workbook.CalculateFormula(CalculationOptions), Worksheet.CalculateFormula(CalculationOptions options, bool recursive).

 Consenti all'utente di calcolare formule con opzioni più flessibili ed estensibili.



Aggiunge metodi: ReferredArea.GetValues(),ReferredArea.GetValue(int rowOffset, int colOffset)

 Consenti all'utente di recuperare i dati da un riferimento.



 Modifiche per i parametri di ICustomFunction.CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

 Ora aggiungiamo l'oggetto ReferredArea in "paramsList" invece il valore o l'array di valori dell'area a cui si fa riferimento quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. E rimuoviamo ReferredAreaCollection da contextObjexts.





 Nota

 Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.5.0 sono inclusi anche in questo Aspose.Cells for Java v8.5.0.

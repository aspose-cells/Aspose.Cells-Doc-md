---
title: Aspose.Cells for Java 8.6.2 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-8-6-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.6.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.6.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSJAVA-41144) - Possibilità di eliminare Style da StyleCollection


## **Insetti**


 (CELLSJAVA-41554) - Immagine mancante durante la conversione da HTML a formato EXCEL

 (CELLSJAVA-41549) - XLSB danneggiato in Excel 2010 dopo il salvataggio di Aspose.Cells v8.6.1

 (CELLSJAVA-41530) - Impostazione del layout della tabella pivot classica persa quando si salvava nuovamente il file XLSB del modello

 (CELLSJAVA-41558) - Formati condizionali medi Ottieni formule aggiunte

 (CELLSJAVA-41546) - I metodi Workbook.calculateFormula si bloccano per un tempo indefinito

(CELLSJAVA-41544) - Problema relativo al formato della data giapponese durante la conversione da "XML Spreadsheet 2003" a XLSX

 (CELLSJAVA-41543) - Problema con la funzione CODE() per le lettere russe

 (CELLSJAVA-41541) - La dimensione del carattere non viene conservata durante la conversione del foglio di calcolo XML 2003 in altri formati

 (CELLSJAVA-41538) - Il nuovo salvataggio del foglio di calcolo rimuove alcune proprietà dal foglio1.xml per il tag controlPr

 (CELLSJAVA-41567) - Problema con i caratteri webdings nei rendering da Excel a PDF

 (CELLSJAVA-41559) - Il salvataggio in PDF genera colori Colorscale errati

 (CELLSJAVA-41556) - La stampa del PDF generato Aspose.Cells modifica in una certa misura il codice a barre incorporato

 (CELLSJAVA-41552) - La larghezza e l'altezza di un valore di testo ruotato sembrano non essere corrette

 (CELLSJAVA-41578) - Il grafico in PDF non viene generato subito dopo l'esecuzione del metodo chart.toPdf(fileName)

 (CELLSJAVA-41574) - Problema di spaziatura tra l'asse Y e le legende

 (CELLSJAVA-41557) - La differenza tra i segni di graduazione dell'etichetta dell'asse è stata modificata da 10 a 20 durante il rendering del grafico in PDF

(CELLSJAVA-41553) - I colori del grafico mostrano un cambiamento importante nell'output PDF

 (CELLSJAVA-41539) - l'intervallo dell'asse verticale non corrisponde al grafico di origine durante il rendering del foglio di calcolo in PDF

 (CELLSJAVA-41536) - Problema riguardante le forme della linea della serie nel grafico secondo MS Excel 2010/2013

 (CELLSJAVA-41533) - La spaziatura tra la legenda e le etichette degli assi del grafico è inferiore al previsto

 (CELLSJAVA-41520) - L'immagine del grafico viene tagliata dai lati superiore e destro

 (CELLSJAVA-41509) - Problemi con i bordi del grafico durante il rendering del grafico in PDF

 (CELLSJAVA-41505) - I bordi destro e inferiore vengono tagliati durante il rendering del grafico in PDF

 (CELLSJAVA-41560) - Come ottenere il colore predefinito del foglio di lavoro

 (CELLSJAVA-41542) - Problema con il nome della casella di controllo quando le caselle di controllo vengono create con Aspose.Cells

 (CELLSJAVA-41469) - Supporta marcatori intelligenti nidificati


## **Eccezioni**


 (CELLSJAVA-41550) - java.lang.NullPointerException su Workbook.combine

(CELLSJAVA-41564) - NullPointerExceptions che chiama com.aspose.cells.Row



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSJAVA-41566) - La dimensione del carattere è inferiore rispetto all'altra cella


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge la proprietà WorkbookDesigner.CallBack e l'interfaccia ISmartMarkerCallBack.

 Rappresenta l'interfaccia di richiamata dell'elaborazione del marcatore intelligente.



 Aggiunge la proprietà Cells.Style.

 Ottiene e imposta lo stile predefinito del foglio di lavoro.



 Aggiunge il metodo Chart.ToPdf(string fileName).

 Salva il grafico in un file pdf.



 Aggiunge il metodo Workbook.RemoveUnusedStyles().

 Rimuove tutti gli stili inutilizzati dal pool di stili della cartella di lavoro.



 Aggiunge l'evento AjaxCallFinished in GridWeb

 Si attiva quando l'aggiornamento Ajax del controllo è terminato. (EnableAJAX deve essere impostato su true).



 Aggiunge l'evento CellModifiedOnAjax in GridWeb

 Si attiva quando la cella viene modificata in ajaxcall.





 Nota

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.6.2 sono inclusi anche in questo Aspose.Cells for Java v8.6.2.

---
title: Aspose.Cells for .NET 8.0.2 Note di rilascio
type: docs
weight: 70
url: /it/net/aspose-cells-for-net-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.0.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.0.2/)

{{% /alert %}} 

 Aspose.Cells for .NET è stato aggiornato alla versione 8.0.2 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 30 nuovi utili miglioramenti.
Usando Aspose.Cells for .NET puoi lavorare con XLS, SpreadsheetML,OOXML,XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche visualizzare, generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for .NET.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells.

\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-42585) - Modifica direzione testo commento


## **Prestazione**


 (CELLSNET-42278) - System.OutOfMemoryException durante il salvataggio da XLSX a PDF dove XLSX ha molte celle vuote con formattazione


## **Insetti**


(CELLSNET-42524) - Funzione CalculateTextSize dei problemi dell'oggetto Shape

 (CELLSNET-42401) - CalculateTextSize() non restituisce l'altezza corretta

 (CELLSNET-42235) - Problema con il ridimensionamento automatico della casella di testo

 (CELLSNET-42104) - CalculateTextSize non restituisce l'altezza corretta

 (CELLSNET-42612) - La funzione di adattamento automatico delle colonne non funziona per le colonne a discesa filtrate di Pivot

 (CELLSNET-42562) - Le formule non funzionano con la valuta estera

 (CELLSNET-42269) - La formattazione della tabella pivot nell'output XPS non è corretta

 (CELLSNET-42597) - AutoFitRows sta facendo nascondere il testo a capo nel risultante PDF

 (CELLSNET-42615) - SheetRender non esegue correttamente il rendering dell'apice

 (CELLSNET-42594) - La giustificazione verticale del testo non funziona correttamente in SheetRender

 (CELLSNET-42580) - Il salvataggio del file Excel in PDF ignora le impostazioni del colore nell'intestazione

 (CELLSNET-42579) - Problema di interruzione di pagina durante il rendering in PDF

(CELLSNET-42498) - Il bordo viene copiato nella pagina successiva durante la conversione da XLSX a PDF

 (CELLSNET-42495) - Il rendering del pdf contiene righe indesiderate nelle pagine 2 e 3

 (CELLSNET-42567) - Il grafico scompare quando viene convertito in PDF

 (CELLSNET-42527) - Il grafico a linee e il grafico a barre nello stesso grafico non sono nella posizione corretta

 (CELLSNET-42595) - Le griglie vengono visualizzate nell'anteprima di stampa di MS-Excel quando la cartella di lavoro viene salvata in formato Xlsb

 (CELLSNET-42591) - AutoFitColumns non funziona con ListObjects quando vengono aggiunte nuove righe.

 (CELLSNET-42590) - Attributo xml:space="preserve" perso per il nodo OpenXML v (valore) di Excel Cell

 (CELLSNET-42588) - Impossibile inserire una tabella nel file XLSB

 (CELLSNET-42586) - L'allineamento del testo dei commenti quando è impostato a destra non funziona

 (CELLSNET-42582) - Excel ha trovato un errore di contenuto illeggibile all'apertura di Aspose.Cells convertito XLSM da XLSB

(CELLSNET-42581) - ArgumentOutOfRangeException - all'apertura del file Excel XLSX

 (CELLSNET-42570) - Le formule Cell nei marcatori intelligenti non si espandono

 (CELLSNET-42568) - La colonna Dimensione setaccio mostra #N/D


## **Eccezioni**


 (CELLSNET-42576) - Eccezione di riferimento nulla al salvataggio di xls come pdf

 (CELLSNET-42628) - System.NullReferenceException durante il caricamento di un foglio di calcolo MHTML

 (CELLSNET-42609) - Cell.GetDispalyStyle() non riesce per alcune regole di formattazione condizionale

 (CELLSNET-42587) - System.NullReferenceException all'apertura del file

 (CELLSNET-42577) - NullReferenceException - durante il recupero dello stile condizionale per una cella





 \2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-42572) - Il colore della scheda del foglio non viene mantenuto all'interno di GridWeb

 (CELLSNET-42302) - Menu contestuale WebGrid - FIND non riesce su IE11 con errore JS: impossibile ottenere la proprietà 'acwFindReplaceDialog_Element' di riferimento non definito o nullo

 (CELLSNET-40531) - Problema relativo alla formula durante il caricamento del file modello in GridWeb

(CELLSNET-42571) - Formato numerico sulla colonna H all'interno di GridWeb non conservato

 (CELLSNET-42553) - Elenco oggetti/formattazione tabelle/stile perso durante l'importazione di file Excel in GridWeb

 (CELLSNET-42623) - Errore durante la creazione del controllo per GridWeb




## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge la proprietà Shape.TextDirection

 Ottiene/imposta la direzione del flusso di testo per Shape.



 Aggiunge la proprietà HTMLLoadOptions.ConvertFormulasData

 Indica se convertire o meno la stringa in formula quando il valore della stringa che inizia con il carattere '=' è la stringa della formula, il valore predefinito è false.



 Aggiunge la proprietà HtmlSaveOptions.ImageOptions

 Ottiene/imposta le opzioni per il rendering durante il salvataggio dei file html.



 Proprietà HtmlSaveOptions.ExportChartImageFormat obsoleta

 Utilizza invece HtmlSaveOptions.ImageOptions per le impostazioni del formato immagine durante il salvataggio di file html.



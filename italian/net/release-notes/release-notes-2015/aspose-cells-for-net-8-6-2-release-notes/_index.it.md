---
title: Aspose.Cells for .NET 8.6.2 Note di rilascio
type: docs
weight: 20
url: /it/net/aspose-cells-for-net-8-6-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.6.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43934) - Supporta marcatori intelligenti per accettare un elenco generico come oggetto nidificato


## **Insetti**


 (CELLSNET-44044) - PivotTable.ShowValuesRow non ha alcun effetto dopo lo spostamento di DataField nelle colonne

 (CELLSNET-44043) - L'apertura e il nuovo salvataggio di file Excel di grandi dimensioni danneggiano il documento

 (CELLSNET-44031) - XLSB danneggiato in Excel 2010 dopo il salvataggio in v8.6.1

(CELLSNET-43990) - AutoShape fuori posto durante il rendering del foglio di calcolo in PDF

 (CELLSNET-43989) - Lo spazio tra le righe all'interno di una casella di testo è stato ridotto

 (CELLSNET-43901) - La tabella pivot non avvolge il testo durante l'aggiornamento

 (CELLSNET-43808) - Lo stile della tabella pivot viene perso quando i fogli di lavoro vengono copiati in un'altra cartella di lavoro e sottoposti a rendering in PDF

 (CELLSNET-43786) - Il file è danneggiato dopo l'aggiornamento della tabella pivot nel file modello

 (CELLSNET-43421) - La freccia non viene visualizzata correttamente durante la conversione del foglio di calcolo in PDF

 (CELLSNET-43391) - Problema con il rendering HTML per una tabella con una colonna nascosta

 (CELLSNET-44045) - I metodi Workbook.CalculateFormula si bloccano per un tempo indefinito

 (CELLSNET-44051) - Icone di formattazione condizionale mancanti dal PDF

 (CELLSNET-44047) - Le pagine vengono ingrandite nel PDF di output

 (CELLSNET-44025) - Lo spessore del bordo non viene mantenuto in base all'area di stampa

 (CELLSNET-44002) - L'immagine viene ridimensionata a causa di qualche problema nel codice

 (CELLSNET-43960) - Impossibile leggere alcuni file protetti da password

(CELLSNET-44062) - La voce della legenda del grafico non viene rimossa quando la colonna dell'origine dati è nascosta

 (CELLSNET-44026) - Tutte le linee guida vengono mostrate nell'immagine di output per un grafico personalizzato

 (CELLSNET-44020) - Mancano alcune etichette dati durante l'esportazione del grafico in immagine

 (CELLSNET-44010) - Il testo TickLabel inclinato sull'asse delle categorie del grafico viene tagliato quando viene convertito in immagine

 (CELLSNET-44000) - DataLabel non viene visualizzato durante il rendering del grafico nell'immagine

 (CELLSNET-43978) - Il grafico all'immagine viene generato con valori extra

 (CELLSNET-43874) - Il formato numerico Chart.NSeries.DataLabels non viene mantenuto durante il nuovo salvataggio

 (CELLSNET-44038) - Chart.ToImage() modifica l'allineamento del testo dell'etichetta

 (CELLSNET-44009) - Il nome della serie di grafici viene modificato se i dati provengono da una cella unita

 (CELLSNET-44060) - Colore del carattere della forma errato dopo la copia del foglio

 (CELLSNET-44056) - Salva in PDF perde i bordi verticali

 (CELLSNET-44049) - Le colonne nascoste perdono la loro larghezza

(CELLSNET-44039) - Impossibile calcolare la formula in base ai valori filtrati nel foglio di lavoro

 (CELLSNET-44037) - La funzione di aggregazione genera un errore #NAME fino a quando l'utente non accede alla barra della formula

 (CELLSNET-44034) - Le convalide non funzionano nel formato XLSB

 (CELLSNET-44030) - La funzione SOMMA.PIÙ.SE di Excel non funziona nel formato XLSB

 (CELLSNET-44007) - Duplicazione di oggetti telecamera nel foglio di calcolo risultante durante il nuovo salvataggio in XLSB

 (CELLSNET-44006) - Errore di visualizzazione protetta durante l'apertura di XLS risalvati

 (CELLSNET-44001) - La formula NOW() non viene visualizzata correttamente nella conversione da SpreadsheetML(XML) a PDF

 (CELLSNET-43894) - Impossibile aggiornare ObjectSourceFullName del collegamento OLE

 (CELLSNET-43845) - Sono stati nascosti due campi a sinistra del grafico che riappaiono successivamente


## **Eccezioni**


 (CELLSNET-44008) - CellsException in SheetRender.ToImage

 (CELLSNET-43926) - CellsException in Workbook.CalculateFormula

 (CELLSNET-44052) - Si è verificata un'eccezione su Workbook.Save() nella conversione da Excel a PDF

 (CELLSNET-44050) - System.FormatException nella cartella di lavoro ctor



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


(CELLSNET-44036) - Il colore del carattere è lo stesso per l'intero testo anche se la cella contiene testi con colori diversi

 (CELLSNET-44033) - Ottieni celle modificate in modalità Ajax sul lato server

 (CELLSNET-44014) - Il metodo GridWorkSheet.SetEditableRange non è disponibile in 8.6.1


## **Insetti**


 (CELLSNET-43955) - Metodo GridWeb.SaveCustomStyleFile mancante in 8.6.0

 (CELLSNET-44017) - Errore di serializzazione durante l'utilizzo della modalità SessionState su "StateServer" nel file web.config - GridWeb


## **Eccezioni**


 (CELLSNET-43185) - SerializationException quando la modalità Session-State passa a StateServer


## **API pubblica e modifiche non compatibili con le versioni precedenti**


 Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.



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



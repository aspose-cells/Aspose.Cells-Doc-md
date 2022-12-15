---
title: Aspose.Cells for .NET 8.2.0 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-8-2-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.2.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.2.0/)

{{% /alert %}} 

 Aspose.Cells for .NET è stato aggiornato alla versione 8.2.0 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 40 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for .NET puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. È inoltre possibile visualizzare, generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for .NET.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells.

\1) Aspose.Cells 
## **Altri miglioramenti e modifiche**

## **Miglioramenti**


 (CELLSNET-42892) - È necessario un sovraccarico di AutoFitRows

 (CELLSNET-42868) - L'elenco del validatore dati non restituisce i valori previsti

 (CELLSNET-42862) - Funzione Excel 2013 non supportata - Giorni


## **Prestazione**


(CELLSNET-42876) - Aspose.Cells si blocca sul metodo Workbook.Save()

 (CELLSNET-42840) - Il file Excel di grandi dimensioni viene danneggiato quando vengono aggiunte più di 45.000 righe


## **Insetti**


 (CELLSNET-42866) - Il testo verticale nel foglio di calcolo manca nel PDF risultante

 (CELLSNET-42835) - Il testo non è allineato a lato della forma quando XLS viene convertito in PDF

 (CELLSNET-42787) - L'immagine renderizzata non è chiara nel pdf di output

 (CELLSNET-42526) - Gli oggetti freccia non sono posizionati correttamente nel pdf di output

 (CELLSNET-42322) - L'eliminazione di righe e l'aggiornamento della tabella pivot causano l'arresto anomalo del file di output

 (CELLSNET-42827) - Problema con i valori di lettura multi-thread delle celle nel foglio di lavoro

 (CELLSNET-42898) - Problema con il piè di pagina con stile quando il foglio di calcolo viene visualizzato come PDF

 (CELLSNET-42880) - Il numero di pagine salvate da Aspose.Cells PDF è 3.

 (CELLSNET-42841) - Immagine Tiff che si estende su 4 pagine invece di 2

 (CELLSNET-42833) - Forma sovrapposta al testo nel PDF risultante

(CELLSNET-42829) - Le caselle di controllo non sono allineate correttamente nel PDF risultante

 (CELLSNET-42776) - La qualità dell'immagine è diminuita durante il salvataggio dei fogli di calcolo in PDF

 (CELLSNET-42620) - Il carattere e nel grafico non è riempito di colore nero

 (CELLSNET-42856) - #RIF! errore nel riferimento all'origine dati del grafico

 (CELLSNET-42847) - Il grafico viene perso al nuovo salvataggio del file ODS

 (CELLSNET-42831) - La forma è stata spostata nel PDF risultante

 (CELLSNET-42830) - Modifica della direzione della freccia nel PDF risultante

 (CELLSNET-42828) - Il PDF risultante ha una forma ritagliata con una parte della croce non mostrata

 (CELLSNET-42798) - L'immagine del grafico a bolle non viene creata correttamente (dal grafico all'immagine)

 (CELLSNET-42920) - Il salvataggio di un file XLSM di Excel crea un errore di contenuto illeggibile

 (CELLSNET-42909) - Le linee direttrici vengono nascoste quando si salva nuovamente il file XLSX del modello

 (CELLSNET-42908) - La posizione della cella finale cambia da E9 a F9

 (CELLSNET-42907) - Aspose.Cells rimosso i filtri del periodo di tempo

(CELLSNET-42904) - Problema di DeleteRange con la raccolta di collegamenti ipertestuali

 (CELLSNET-42900) - Le proprietà del documento predefinite e personalizzate vengono perse

 (CELLSNET-42899) - Name.GetRange restituisce null anziché l'intervallo effettivo

 (CELLSNET-42897) - Valore errato calcolato per la formula COUNTIF durante il rendering in PDF

 (CELLSNET-42889) - I valori non sono stati calcolati correttamente da Workbook.CalculateFormula

 (CELLSNET-42874) - Worksheet.Copy non conserva correttamente il grafico

 (CELLSNET-42872) - Valori errati durante la lettura del grafico a linee dalla cartella di lavoro

 (CELLSNET-42851) - La funzione CERCA.VERT viene valutata come 0 rispetto a MS Excel

 (CELLSNET-42849) - Mappature XML perse durante il nuovo salvataggio di un file Excel

 (CELLSNET-42848) - Il carattere del commento cambia al nuovo salvataggio del file ODS

 (CELLSNET-42806) - Modifiche alla formula della serie del grafico

 (CELLSNET-42755) - Le etichette dei grafici hanno cambiato posizione/disposizione


## **Eccezioni**


(CELLSNET-41952) - "Eccezione di memoria insufficiente" durante il salvataggio della cartella di lavoro come PDF

 (CELLSNET-42891) - CellsException: tale intestazione o piè di pagina non è ancora supportato!

 (CELLSNET-42875) - NullReferenceException all'apertura della cartella di lavoro dal flusso di memoria

 (CELLSNET-42863) - NullReferenceException all'apertura della cartella di lavoro



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-42895) - Page.IsPostBack è sempre false all'interno di GridWeb

 (CELLSNET-42881) - GridWeb mostra la stessa immagine in tutti i fogli di lavoro web


## **Eccezioni**


 (CELLSNET-42879) - Eccezione al salvataggio di Excel con immagine in GridWeb


## **API pubblica e modifiche non compatibili con le versioni precedenti**


 Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.



 Aggiunge la proprietà Cells.MultiThreadReading

 Indica se il modello di dati delle celle deve supportare la lettura multithread.



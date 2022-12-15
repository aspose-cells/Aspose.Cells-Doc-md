---
title: Aspose.Cells for .NET 8.2.1 Note di rilascio
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.2.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.2.1/)

{{% /alert %}} 

 Aspose.Cells for .NET è stato aggiornato alla versione 8.2.1 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 30 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for .NET puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. È inoltre possibile visualizzare, generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for .NET.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells.

\1) Aspose.Cells 
## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-42923) - Supporta l'opzione di mostrare la legenda senza sovrapposizioni

 (CELLSNET-42935) - Verificare che il valore della cella soddisfi le regole di convalida dei dati

 (CELLSNET-42911) - Disabilita la disposizione del testo per le etichette dati del grafico


## **Insetti**


 (CELLSNET-42941) - Genera un errore di contenuto illeggibile nel file XLSM

(CELLSNET-42933) - Impossibile evitare le etichette di riga quando viene creato il pivot utilizzando aspose

 (CELLSNET-42857) - Il file viene danneggiato all'apertura e al salvataggio

 (CELLSNET-42816) - La casella di testo diagonale appare orizzontale quando il foglio di calcolo viene convertito in PDF

 (CELLSNET-42815) - La casella di testo diagonale appare orizzontale quando il foglio di calcolo viene convertito in HTML

 (CELLSNET-42676) - Lo spessore delle linee freccia del diagramma Visio è errato nel pdf di output

 (CELLSNET-41568) - Da Excel a immagine con forma ruotata non visualizzata correttamente

 (CELLSNET-40931) - Forme errate esportate nell'immagine

 (CELLSNET-42802) - Problema di rendering grafico durante la conversione di Xls in PDF

 (CELLSNET-42980) - Interruzione di pagina errata durante il rendering del foglio di calcolo in PDF

 (CELLSNET-42979) - Estensione indesiderata del bordo durante il rendering del foglio di calcolo in PDF

 (CELLSNET-42970) - L'operazione di addizione nel piè di pagina di Excel non funziona nel rendering PDF

 (CELLSNET-42936) - Stampa su entrambi i lati della pagina

(CELLSNET-42938) - Collegamenti ipertestuali per le forme perse nel formato file PDF renderizzato

 (CELLSNET-42966) - Contenuto illeggibile dopo l'apertura e il salvataggio del file xlsx

 (CELLSNET-42964) - Excel ha rilevato un errore di contenuto illeggibile durante la generazione di collegamenti ipertestuali

 (CELLSNET-42946) - Il valore della cella L45 non è corretto dopo il calcolo della formula

 (CELLSNET-42943) - Limitazione di Excel relativa al numero di collegamenti ipertestuali in Aspose.Cells

 (CELLSNET-42934) - Lettura errata del tipo di grafico a dispersione e dei riferimenti all'intervallo di nomi

 (CELLSNET-42926) - Il piè di pagina non è corretto durante la conversione dal documento SpreadsheetML

 (CELLSNET-42837) - Mostra tabella dati con chiave legenda chatt

 (CELLSNET-41129) - Logo scomparso nel file PDF di output

 (CELLSNET-42986) - Formula errata copiata nelle celle durante l'inserimento di righe nelle tabelle

 (CELLSNET-42974) - Aspose.Cells foglio di calcolo corrotto contenente dati esterni

 (CELLSNET-42802) - torta, ciambella. Calcola formula

 (CELLSNET-42940) - Collegamento ipertestuale in PDF di XLS

(CELLSNET-42738) - La linea smussata sul grafico a dispersione contiene loop

 (CELLSNET-42739) - L'immagine del grafico a dispersione mostra marcatori della griglia dell'asse X errati


## **Eccezioni**


 (CELLSNET-42929) - IndexOutOfRangeException generata in PivotTable.CalculateData

 (CELLSNET-42213) - Conversione in PDF di un file XLS contenente una forma con uno sfondo sfumato

 (CELLSNET-42962) - Eccezione su Workbook.RemoveExternalLinks()

 (CELLSNET-42951) - CellsHelper.ConvertA1FormulaToR1C1 genera un'eccezione

 (CELLSNET-42930) - System.ArgumentException in Workbook.Save

 (CELLSNET-42002) - Eccezione System.ArgumentException nella pagina 9110

 (CELLSNET-42977) - Eccezione dell'immagine del disegno


## **API pubblica e modifiche non compatibili con le versioni precedenti**


 Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.



 Aggiunge il metodo Cell.GetValidation()

 Ottiene la convalida che si applica alla cella.



 Aggiunge il metodo Cell.GetValidationValue()

 Indica se il valore della cella è valido.



 Aggiunge il metodo WorkbookRender.ToPrinter(PrinterSettings PrinterSettings).

 Renderizza la cartella di lavoro sulla stampante tramite PrinterSettings.



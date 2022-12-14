---
title: Aspose.Cells for .NET 8.1.0 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-8-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.1.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.1.0/)

{{% /alert %}} 

 Aspose.Cells for .NET è stato aggiornato alla versione 8.1.1 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 20 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for .NET puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche visualizzare, generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for .NET.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells.

\1) Aspose.Cells 
## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


(CELLSNET-42761) - Rimuovere gli scenari dai fogli di lavoro


## **Insetti**


 (CELLSNET-42523) - SheetRender non riesce quando viene utilizzato UpdateSelectedValue

 (CELLSNET-42387) - Il testo viene spostato fuori dal banner.

 (CELLSNET-42385) - La forma del connettore curvo non viene visualizzata durante il rendering di XLSX in PDF

 (CELLSNET-42379) - Il testo nella matrice viene visualizzato in modo diverso

 (CELLSNET-42752) - I totali parziali della tabella pivot presentano un'unione di celle errata

 (CELLSNET-42703) - La conversione del foglio di calcolo con tabella pivot in PDF presenta problemi relativi allo stile

 (CELLSNET-42386) - La funzione GetPivotData calcola il valore errato

 (CELLSNET-42742) - Aspose.Cells Incorpora caratteri errati nel PDF

 (CELLSNET-42697) - L'intestazione viene duplicata nel pdf di output

 (CELLSNET-42759) - Le etichette dell'asse X del grafico sono tagliate

 (CELLSNET-42756) - I punti elenco non vengono visualizzati correttamente se si trovano all'interno di una casella di testo

 (CELLSNET-42750) - Le frecce vengono visualizzate speculari su un asse verticale

(CELLSNET-42748) - Le linee della legenda sono più sottili che in Excel

 (CELLSNET-42730) - Da XLSM a PDF tende a bloccarsi quando vengono apportate modifiche al valore e al formato Cell

 (CELLSNET-42381) - L'elenco puntato non viene stampato correttamente sotto l'intestazione dell'elenco

 (CELLSNET-42375) - L'elenco puntato sotto l'intestazione Ciclo non è correttamente convertito in pdf

 (CELLSNET-42779) - Il file Xlam non si apre in Excel dopo averlo aperto e salvato di nuovo

 (CELLSNET-42766) - L'apertura e il salvataggio del file provocano un errore nelle visualizzazioni personalizzate

 (CELLSNET-42725) - L'immagine inserita perde le dimensioni originali

 (CELLSNET-42716) - Nastri XLSM persi dopo aver salvato nuovamente il file XLSM

 (CELLSNET-42711) - Row.ApplyStyle non funziona correttamente

 (CELLSNET-42708) - Il colore di sfondo verde delle celle scompare nell'HTML

 (CELLSNET-42695) - Errore di visualizzazione protetta nel file MS Excel - È richiesta un'indagine


## **Eccezioni**


 (CELLSNET-42782) - System.FormatException durante la lettura del file xlsx

(CELLSNET-42758) - Il cast specificato non è un'eccezione valida in Cell.GetDisplayStyle()

 (CELLSNET-42724) - StackOverflowException si è verificata durante la chiamata al metodo Worksheet/Workbook.CalculateFormula()

 (CELLSNET-42710) - Formula non valida durante il caricamento di un foglio di calcolo eventualmente danneggiato

 (CELLSNET-42706) - System.OutOfMemoryException in DetectFileFormat


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunta della proprietà HtmlSaveOptions.PresentationPreference

 Indica se il file html o mht è la preferenza di presentazione. Il valore predefinito è false. Se vuoi ottenere una presentazione più bella, imposta il valore su true.



Classi Pubbliche ScenarioCollection, Scenario,ScenarioInputCellCollection , ScenarioInputCell e proprietà Worksheet.Scenarios.

 Supporta l'aggiunta, la modifica e l'eliminazione delle impostazioni dello scenario.



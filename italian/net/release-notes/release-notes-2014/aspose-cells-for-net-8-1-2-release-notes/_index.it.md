---
title: Aspose.Cells for .NET 8.1.2 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-8-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.1.2/)

{{% /alert %}} 

Aspose.Cells for .NET è stato aggiornato alla versione 8.1.2 e siamo lieti di annunciare che questa versione apporta l'aggiunta di oltre 20 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for .NET puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche visualizzare, generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for .NET.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells.

\1) Aspose.Cells 
## **Altri miglioramenti e modifiche**

## **Prestazione**


 (CELLSNET-42820) - FileFormatUtil.DetectFileFormat utilizza tutta la memoria disponibile del sistema durante il rilevamento di un foglio di calcolo danneggiato


## **Insetti**


 (CELLSNET-42801) - Mancano dati quando la tabella pivot viene convertita in PDF

 (CELLSNET-42800) - Titolo totale mancante quando la tabella pivot viene convertita in PDF

(CELLSNET-42799) - Cell Problema di unione quando la tabella pivot viene convertita in PDF

 (CELLSNET-42775) - Bug della tabella pivot relativo ai subtotali

 (CELLSNET-42749) - Le linee delle frecce sono troppo spesse rispetto a Excel

 (CELLSNET-42438) - Il contenuto delle celle unite scompare quando le righe vengono filtrate e il foglio di calcolo viene convertito in HTML

 (CELLSNET-42353) - Aspose.Cells produce frecce di spessore doppio mentre converte XLS in PDF

 (CELLSNET-42747) - Il risultato stampato non è centrato correttamente e l'ultima riga va persa

 (CELLSNET-42744) - Il testo nelle celle unite non viene visualizzato durante la conversione in PDF

 (CELLSNET-42781) - Errore da forma a immagine durante la conversione di ExcelShapeToImageRedactedEx.xls in Tiff

 (CELLSNET-42780) - Errore da forma a immagine durante la conversione di ExcelShapeToImageError.xls in Tiff

 (CELLSNET-42760) - La linea è molto spessa se salvata come pdf utilizzando Aspose celle

 (CELLSNET-42622) - Le etichette dei grafici di Excel si sovrappongono dopo l'apertura e il salvataggio del file xlsm

(CELLSNET-42836) - La formula di corrispondenza non viene calcolata correttamente con Workbook.CalculateFormula

 (CELLSNET-42818) - #NUM! errore durante la lettura di determinate celle

 (CELLSNET-42811) - Indicatori intelligenti - Cells Formattazione non mantenuta in Gruppo:Unisci, Salta:1


## **Eccezioni**


 (CELLSNET-42635) - MonoDevelop provoca un errore SIGSEGV

 (CELLSNET-42812) - CellsException durante la conversione del foglio di calcolo in PDF

 (CELLSNET-42788) - System.NullReferenceException al salvataggio del file ods


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 WarningInfo pubblico, classi WarningType, interfaccia IWarningCallback e proprietà SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback.

 Supporta avvisi quando il carattere è stato sostituito.



 Elimina la proprietà PdfSaveOptions.ChartImageType obsoleta.



---
title: Aspose.Cells for Java 8.1.2 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-8-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.1.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.1.2/)

{{% /alert %}} 

Aspose.Cells for Java è stato aggiornato alla versione 8.1.2 e siamo lieti di annunciare che questa versione apporta l'aggiunta di oltre 20 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for Java puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche generare, modificare, convertire, visualizzare e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for Java.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells for Java.

\1) Aspose.Cells

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-40875) - Ricevi avvisi per la sostituzione dei caratteri durante il rendering dei fogli di calcolo

Miglioramenti

(CELLSJAVA-40900) - Offuscamento di metodi pubblici API
(CELLSJAVA-40891) - Il processo si blocca durante il caricamento di un foglio di calcolo completamente danneggiato
(CELLSJAVA-40883) - Problema con il formato della data durante l'importazione di CSV
(CELLSJAVA-40872) - worksheet.getCells().importResultSet, l'ora dalla colonna della data è sempre 00:00

Insetti

(CELLSJAVA-40866) - La conversione in HTML non rispetta ImageFormat in SaveOptions
(CELLSJAVA-40854) - HtmlHiddenRowDisplayType.HIDDEN provoca lo spostamento delle celle nell'HTML risultante (problema di spanning)
(CELLSJAVA-40835) - Problema di esportazione delle colonne nascoste nel file HTML sottoposto a rendering
(CELLSJAVA-40879) - Problema nella creazione dell'immagine dell'intervallo di dati (da foglio a immagine)
(CELLSJAVA-40878) - L'impostazione della risoluzione verticale e orizzontale durante il salvataggio del foglio di calcolo nell'immagine Jpeg non ha effetto
(CELLSJAVA-40877) - Da Excel a PDF - Scarsa qualità dell'immagine resa da Aspose Cells 8.xx
(CELLSJAVA-40910) - Le immagini vengono perse quando viene eseguito il rendering del PDF utilizzando PdfSaveOptions.setImageType(ImageFormat.getPng())
(CELLSJAVA-40907) - Nel grafico mancano gli indicatori dei punti dati quando un file Excel modello viene salvato come HTML
(CELLSJAVA-40904) - Alcuni grafici non vengono visualizzati correttamente nel formato di file HTML
(CELLSJAVA-40899) - Problema di dati troncati nel foglio18
(CELLSJAVA-40898) - Problema di dati troncati nel foglio17
(CELLSJAVA-40886) - Contrassegni di serie interrotti durante il nuovo salvataggio di un file Excel
(CELLSJAVA-40885) - Il grafico esporta la forma del punto dati mancante nel formato dell'immagine di output
(CELLSJAVA-40869) - Nelle equazioni mancano glifi e alcuni testi formattati vengono troncati nel file PDF sottoposto a rendering
(CELLSJAVA-40865) - L'immagine non è chiara nel pdf di output
(CELLSJAVA-40860) - Le proprietà della bolla sono state modificate nel grafico durante il nuovo salvataggio del file XLSX del modello
(CELLSJAVA-40859) - Le proprietà della bolla sono state modificate nel grafico durante il nuovo salvataggio del file XLSX del modello
(CELLSJAVA-40858) - La proprietà Column100PercentStacked o Bar label è stata persa
(CELLSJAVA-40817) - L'immagine nel pdf di output diventa sfocata
(CELLSJAVA-40880) - Il tipo DateTime non viene rilevato quando si aggiunge un valore DateTime in fase di esecuzione tramite Aspose.Cells
(CELLSJAVA-40851) - Larghezza delle forme modificata e altre formattazioni perse nella cartella di lavoro copiata

Eccezioni

(CELLSJAVA-40901) - Eccezione: "Errore da forma a immagine!" durante il rendering in formato file PDF


Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

 WarningInfo pubblico, classi WarningType, interfaccia IWarningCallback e proprietà SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback.
Supporta avvisi quando il carattere è stato sostituito.

Elimina la proprietà PdfSaveOptions.ChartImageType obsoleta.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.1.2 sono inclusi anche in questo Aspose.Cells for Java v8.1.2.

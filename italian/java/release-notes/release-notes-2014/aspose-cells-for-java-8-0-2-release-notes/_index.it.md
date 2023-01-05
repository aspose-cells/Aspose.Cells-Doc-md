---
title: Aspose.Cells for Java 8.0.2 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-8-0-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.0.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.0.2/)

{{% /alert %}} 

 Aspose.Cells for Java è stato aggiornato alla versione 8.0.2 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 10 nuovi utili miglioramenti.
Usando Aspose.Cells for Java puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche generare, modificare, convertire, visualizzare e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for Java.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells for Java.


Altri miglioramenti e modifiche

Miglioramenti

(CELLSJAVA-40788) - Supporta il tema personalizzato per le proprietà delle forme
(CELLSJAVA-40803) - Imposta i suggerimenti di rendering per le immagini durante l'esportazione dei fogli di calcolo su HTML

Insetti

(CELLSJAVA-40793) - L'intervallo non si riferisce all'area corretta
(CELLSJAVA-40768) - Il metodo WorkbookRender.toPrinter() non stampa l'immagine
(CELLSJAVA-40669) - Problema di rotazione della colonna principale durante il rendering da XLTX a PDF
(CELLSJAVA-40801) - Cell problemi di allineamento nel file PDF sottoposto a rendering
(CELLSJAVA-40406) - Conversione di file Excel con un numero elevato di colonne nel file PDF
(CELLSJAVA-40794) - AutoFitColumns non funziona se utilizzato con impostazioni di carattere diverse
(CELLSJAVA-40816) - Il cursore si sposta ancora sull'ultima colonna dopo aver utilizzato Cells.DeleteColumn() per eliminarlo
(CELLSJAVA-40786) - La forma della fem generata non è la stessa dell'originale
(CELLSJAVA-40806) - Segnalibri di Excel non generati durante la conversione in PDF


Eccezioni

(CELLSJAVA-40797) - Cell.getDependents() genera NullPointerException
(CELLSJAVA-40800) - CellsException durante la conversione del foglio di calcolo in PDF su MAC OS

Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Aggiunge la proprietà Shape.TextDirection
Ottiene/imposta la direzione del flusso di testo per Shape.

Aggiunge la proprietà HTMLLoadOptions.ConvertFormulasData
Indica se convertire o meno la stringa in formula quando il valore della stringa che inizia con il carattere '=' è la stringa della formula, il valore predefinito è false.

Aggiunge la proprietà HtmlSaveOptions.ImageOptions
Ottiene/imposta le opzioni per il rendering durante il salvataggio dei file html.

Proprietà HtmlSaveOptions.ExportChartImageFormat obsoleta
Utilizza invece HtmlSaveOptions.ImageOptions per le impostazioni del formato immagine durante il salvataggio di file html.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.0.2 sono inclusi anche in questo Aspose.Cells for Java v8.0.2.

---
title: Aspose.Cells for Java 8.2.1 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.2.1/)

{{% /alert %}} 

 Aspose.Cells for Java è stato aggiornato alla versione 8.2.1 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 30 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for Java puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche generare, modificare, convertire, eseguire il rendering e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for Java.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells for Java.

\1) Aspose.Cells

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-40955) - Posizionamento assoluto della forma
(CELLSJAVA-40943) - Aggiunta un'opzione a PasteOptions per incollare solo le celle visibili dall'intervallo

Insetti

(CELLSJAVA-40977) - La formattazione condizionale non funziona quando il file Excel viene convertito in HTML
(CELLSJAVA-40959) - Attributo di allineamento aggiuntivo nell'output HTML.
(CELLSJAVA-40954) - Le colonne non corrispondono nell'output HTML
(CELLSJAVA-40953) - Alcuni bordi delle celle sono stati leggermente estesi durante la conversione da excel a html
(CELLSJAVA-40980) - Il valore della cella collegata non viene aggiornato dalla cartella di lavoro esterna
(CELLSJAVA-40957) - La protezione del foglio di lavoro in modalità con licenza causa l'arresto anomalo di MS Excel durante l'anteprima
(CELLSJAVA-40956) - Chart.getName() restituisce un nome grafico errato
(CELLSJAVA-40952) - Series.hasLeaderLines() non restituisce il valore corretto
(CELLSJAVA-40944) - Il PDF incorporato viene danneggiato dopo l'unione delle cartelle di lavoro
(CELLSJAVA-40979) - Alcuni quadrati sono allegati alle etichette dei dati nel grafico a torta nel PDF renderizzato
(CELLSJAVA-40975) - Conversione da XLSX a Jpeg - Prestazioni
(CELLSJAVA-40973) - Disabilita setExtractContentPermission - L'opzione "Autorizzazione a copiare o estrarre contenuto" non funziona
(CELLSJAVA-40965) - Cells si incontrano nel PDF
(CELLSJAVA-40962) - Aspose.Cells esegue il rendering del valore #N/D in modo diverso rispetto a MS Excel
(CELLSJAVA-40926) - Il bordo della tabella è normale anziché in grassetto al 100% di zoom
(CELLSJAVA-40833) - La qualità dell'immagine del grafico è bassa - Conversione da grafico a immagine
(CELLSJAVA-40949) - L'asse orizzontale non viene visualizzato nell'immagine del grafico
(CELLSJAVA-40948) - L'immagine personalizzata nei punti dati non viene visualizzata nell'immagine del grafico
(CELLSJAVA-40947) - I caratteri cinesi non vengono visualizzati nell'immagine del grafico
(CELLSJAVA-40946) - Le etichette dei dati sono nella posizione errata all'interno dell'immagine del grafico
(CELLSJAVA-40821) - Casella di testo mancante quando il grafico viene salvato come EMF utilizzando ToImage
(CELLSJAVA-40819) - Valori dell'asse errati quando il grafico viene salvato come EMF utilizzando ToImage
(CELLSJAVA-40818) - Titolo dell'asse mancante quando il grafico viene salvato come EMF utilizzando ToImage
(CELLSJAVA-40830) - Z-index invertito nell'area in pila e nel grafico a barre durante l'esportazione in PDF

Eccezioni

(CELLSJAVA-40985) - CellsException: fine del file raggiunta in Workbook.save
(CELLSJAVA-40983) - java.lang.NullPointerException su Workbook.save
(CELLSJAVA-40981) - Aspose.Cells non riesce a leggere i file Excel 2013 protetti da password
(CELLSJAVA-40976) - Sparkline genererà NullPointerException quando si utilizza insertRows
(CELLSJAVA-40969) - Eccezione: "java.lang.StringIndexOutOfBoundsException: Indice stringa fuori intervallo" durante l'aggiornamento del valore di una forma
(CELLSJAVA-40967) - Impossibile trasmettere a LineShape

API pubblica e modifiche non compatibili con le versioni precedenti

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

 Aggiunge il metodo Cell.GetValidation()
Ottiene la convalida che si applica alla cella.

 Aggiunge il metodo Cell.GetValidationValue()
Indica se il valore della cella è valido.

 Aggiunge il metodo WorkbookRender.ToPrinter(PrinterSettings PrinterSettings).
Renderizza la cartella di lavoro sulla stampante tramite PrinterSettings.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.2.1 sono inclusi anche in questo Aspose.Cells for Java v8.2.1.

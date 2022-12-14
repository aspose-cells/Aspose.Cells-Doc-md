---
title: Aspose.Cells for Java 8.0.0 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-8-0-0-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.0.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.0.0/)

{{% /alert %}}

Aspose.Cells for Java è stato aggiornato alla versione 8.0.0 e siamo lieti di annunciare che questa versione porta l'aggiunta di oltre 30 nuovi utili miglioramenti.
Utilizzando Aspose.Cells for Java puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche generare, modificare, convertire, visualizzare e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for Java.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells for Java.

Caratteristiche principali

L'opzione di utilizzo della memoria può essere utilizzata per considerazioni sulle prestazioni.
Quando si crea una cartella di lavoro con set di dati di celle di grandi dimensioni, l'opzione MemorySetting.MEMORY_PREFERENCE può ottimizzare l'utilizzo della memoria per i dati delle celle per ridurre il costo della memoria.

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-40749) - Ottieni gli indici riga/colonna iniziale e riga/colonna finale per una pagina del foglio di lavoro
(CELLSJAVA-40744) - Supporto per la funzione Mostra formule MS Excel
(CELLSJAVA-40423) - Dipendenze Aspose.Cells e Maven
(CELLSJAVA-40770) - Imposta l'ora di creazione nel PDF generato

Miglioramenti

(CELLSJAVA-40751) - Errore di battitura nel nome del metodo - SeriesCollection.setSecondCategoryData
(CELLSJAVA-40753) - Separatore etichetta dati serie personalizzata
(CELLSJAVA-40764) - Cell.DisplayStringValue non ha calcolato accuratamente gli spazi determinati dalla larghezza della colonna e '*' nella personalizzazione dello stile

Insetti

(CELLSJAVA-40738) - setExportActiveWorksheet Modifica solo l'allineamento della tabella in HTML
(CELLSJAVA-40747) - L'immagine di sfondo non viene copiata nella cartella di lavoro di destinazione quando si chiama Workbook.copy
(CELLSJAVA-40276) - Il testo all'interno di un'immagine sembra essere rispecchiato durante il salvataggio di una cartella di lavoro Excel come PDF
(CELLSJAVA-40573) - Alcune parole vengono separate durante il salvataggio in PDF
(CELLSJAVA-40743) - Il filtro automatico della tabella non funziona nel formato xls ma funziona correttamente nel formato xlsx
(CELLSJAVA-40750) - Durante l'esportazione in HTML, le celle coperte dall'immagine perdono il colore di sfondo
(CELLSJAVA-40748) - Il percorso dell'immagine di sfondo non è corretto
(CELLSJAVA-40731) - Problema di testo verticale
(CELLSJAVA-40737) - Problema di formattazione di forme/controlli nella conversione da Excel a PDF
(CELLSJAVA-40742) - Disposizione errata delle etichette Axis durante la conversione di XLSX in PDF
(CELLSJAVA-40757) - Colonne DateTime lette in modo errato da CSV con locale europeo
(CELLSJAVA-40282) - Output dell'immagine speculare durante la trasformazione di un foglio di lavoro Excel in PDF
(CELLSJAVA-40585) - Aspose.Cells: grafico grafico sigma incorporato non visualizzato correttamente in PDF/immagini
(CELLSJAVA-40742) - Disposizione errata delle etichette Axis durante la conversione di XLSX in PDF
(CELLSJAVA-40758) - I dati non sono corretti nel pdf di output
(CELLSJAVA-40762) - Cell.getDependents(true) problema - Cells da altri fogli che non dovrebbero essere nell'elenco
(CELLSJAVA-40756) - CellsException: null in Workbook.calculateFormula(false)
(CELLSJAVA-40748) - Il percorso dell'immagine di sfondo non è corretto
(CELLSJAVA-40754) - Esporta forme in html con colore di sfondo di errore
(CELLSJAVA-40766) - Da XLSX a HTML: problema con hideColumn che produce valori Null in HTML
(CELLSJAVA-40769) - Ricalcolo della formula della cella

(CELLSJAVA-40771) - Riga nascosta e problema relativo all'altezza della riga


Eccezioni

(CELLSJAVA-40736) - com.aspose.cells.CellsException: nome cella non valido
(CELLSJAVA-40767) - NullpointerException durante il salvataggio di un libro
(CELLSJAVA-40755) - CellsException: overflow nella conversione da stringa a int. Valore stringa: #N/D.
(CELLSJAVA-40761) - CellsException: errore da forma a immagine!

Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Proprietà AutoFilter.FilterColumnCollection obsoleta
Utilizza invece AutoFilter.FilterColumns.

Aggiunge la proprietà Worksheet.ShowFormulas
Indica se visualizzare le formule o il valore delle formule.

Aggiunge la proprietà PdfSaveOptions.CreatedTime
Ottiene e imposta l'ora di generazione del documento pdf.

Aggiunge l'enumerazione FileFormatType.Ooxml
Rappresenta il file xml aperto dell'ufficio crittografato (come XLSX, DOCX, PPTX, ecc.).

Aggiunge la proprietà LoadOptions.MemorySetting e la proprietà WorkbookSettings.MemorySetting
Da questa versione forniamo l'opzione di utilizzo della memoria per l'utente per considerazione delle prestazioni. L'opzione predefinita MemorySetting.NORMAL viene applicata a tutte le versioni. Per alcune situazioni, ad esempio la creazione di una cartella di lavoro con set di dati di grandi dimensioni per le celle, l'opzione MemorySetting.MEMORY_PREFERENCE può ottimizzare l'utilizzo della memoria e ridurre il costo della memoria per l'applicazione dell'utente. Tuttavia, questa opzione può ridurre le prestazioni in alcuni casi speciali, come l'accesso casuale e ripetuto alle celle.

Rende obsoleta la proprietà SeriesCollection.SecondCatergoryData e aggiunge la proprietà SeriesCollection.SecondCategoryData
Utilizza SeriesCollection.SecondCategoryData per sostituire SeriesCollection.SecondCatergoryData.

Le implementazioni di Row/Cell/RowCollection sono state modificate
Nelle vecchie versioni, gli oggetti Row e Cell sono tenuti in memoria per rappresentare la riga e la cella corrispondenti in un foglio di lavoro. La stessa istanza verrà restituita ogni volta che l'utente chiama metodi come RowCollection[int index], Cells[int, int]e così via. Per considerazioni sulle prestazioni della memoria, da questa versione in poi solo le proprietà e i dati di Row e Cell verranno conservati in memoria. L'oggetto Row/Cell diventa il wrapper di tali proprietà e dati per comodità dell'utente per manipolare il modello di celle e verrà nuovamente istanziato quando l'utente chiama quei metodi. Quindi, ora l'utente otterrà oggetti diversi quando chiama lo stesso metodo per ottenere Row/Cell molte volte anche se questi oggetti diversi fanno tutti riferimento alla stessa riga/cella nel foglio di lavoro. Questa modifica può influire sull'applicazione dell'utente per le seguenti situazioni: 1. Se l'utente ha utilizzato il codice likeif(row1==row2)...if(cell1==cell2)...per verificare la stessa riga/Cell, con le nuove versioni tali controlli potrebbero non riuscire. Si prega di utilizzare row1.equals(row2) e cell1.equals(cell2) invece.2. Poiché gli oggetti Row/Cell vengono istanziati di recente in base all'invocazione dell'utente, non verranno conservati e gestiti in memoria dal componente delle celle. Dopo alcune operazioni di inserimento/eliminazione, la loro posizione (indice di riga/colonna) potrebbe non essere aggiornata o anche peggio, quegli oggetti diventano non validi. Ad esempio, per il seguente codice:Cell cell = cells.get("A2");System.out.println(cell.getName() + ":" + cell.getValue());cells.insertRange(CellArea.createCellArea( "A1", "A1"), ShiftType.DOWN);System.out.println(cell.getName() + ":" + cell.getValue());con le vecchie versioni, la cella farà riferimento ad A3 dopo l'inserimento operazione e il suo valore è uguale a quello precedente all'inserimento. Tuttavia, con la nuova versione l'oggetto cella non sarà più valido o farà ancora riferimento ad A2 con un altro valore. Per questo tipo di situazione, l'utente deve ottenere nuovamente l'oggetto Row/Cell dalla raccolta di celle per ottenere il risultato corretto: Cell cell = cells.get("A2");System.out.println(cell.getName() + ": " + cell.getValue());cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);cell = cells.get("A3");System.out.println(cell. getName() + ":" + cell.getValue());3. RowCollection ora non eredita CollectionBase perché non c'è più alcun oggetto Row nel suo elenco interno.

Cell.StringValue viene modificato per un modello di formattazione speciale con '*' e '_'
Nelle vecchie versioni, modello speciale '* verrà ignorato durante la formattazione del valore della cella per Cell.StringValue e '** produce sempre un carattere nel risultato formattato. Da questa versione cambiamo la logica del fare con '* e '**' per rendere il risultato formattato uguale a quello che puoi ottenere da ms excel quando copi una cella come testo (come copiare una cella in un editor di testo o esportare la cella in csv). Ad esempio, utilizza il carattere personalizzato "*($* #,##0.00*)" per formattare il valore della cella 123, con le versioni precedenti Cell.StringValue darà come risultato "$ 123.00". Ora con le nuove versioni Cell.StringValue darà come risultato "$ 123,00", che è lo stesso con quello che puoi ottenere da ms excel copiando questa cella nel testo.

Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.0.0 sono inclusi anche in questo Aspose.Cells for Java v8.0.0.

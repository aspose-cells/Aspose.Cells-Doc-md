---
title: Aspose.Cells for Android via Java 19.6 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 19.6.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42914|I formati condizionali di grandi dimensioni causano un'eccezione OOM|Aumento|
|CELLSJAVA-42916|Problema relativo al formato dei dati dopo Workbook.save()|Aumento|
|CELLSJAVA-42930|Errore di caricamento di Excel95|Aumento|
|CELLSJAVA-42927|Il file salvato si apre lentamente in Excel dopo aver eliminato le colonne|Aumento|
|CELLSJAVA-42857|Valore errato visualizzato per le forme nel PDF esportato|Insetto|
|CELLSJAVA-42890|L'immagine è opaca e non trasparente dopo la conversione: rendering da Excel a HTML|Insetto|
|CELLSJAVA-42893|Il grafico non è presente nel rendering da Excel a HTML|Insetto|
|CELLSJAVA-42899|Problema da Excel a HTML|Insetto|
|CELLSJAVA-42903|Problema di rendering da Excel a HTML su CentOS|Insetto|
|CELLSJAVA-42882|Impossibile estrarre i dati da un file MS Excel 95 XLS|Insetto|
|CELLSJAVA-42887|Differenza di calcolo tra MS Excel e Aspose.Cells|Insetto|
|CELLSJAVA-42891|La funzione XIRR restituisce un errore numerico se esiste un valore nullo nell'intervallo|Insetto|
|CELLSJAVA-42909|Problema con la funzione DATEVALUE|Insetto|
|CELLSJAVA-42910|Problema con la funzione VLOOKUP quando un carattere è presente nella stringa|Insetto|
|CELLSJAVA-42911|Problema durante l'utilizzo della funzione TESTO per le date|Insetto|
|CELLSJAVA-42896|La conversione in PDF trasforma i numeri di telefono|Insetto|
|CELLSJAVA-42900|La conversione in PDF modifica l'ordine del testo|Insetto|
|CELLSJAVA-42932|Errore di formattazione condizionale con il metodo Style.getDisplayStyle|Insetto|
|CELLSJAVA-42928|Alcune righe non si riflettono nella conversione da XLSX a PDF|Insetto|
|CELLSJAVA-42904|L'immagine dell'intestazione sembra corrompere il file|Insetto|
|CELLSJAVA-42907|Filtro perso dopo aver salvato la cartella di lavoro|Insetto|
|CELLSJAVA-42915|I filtri vengono modificati dopo aver aggiunto un foglio alla cartella di lavoro|Insetto|
|CELLSJAVA-42918|Grafico del file convertito appiattito (conversione da XLS a XLSX)|Insetto|
|CELLSJAVA-42938|Il caricamento del file XLSX interrompe l'applicazione|Insetto|
|CELLSJAVA-42881|Eccezione "java.lang.IllegalStateException: codifica non valida: null " durante il caricamento di un file XLS di MS Excel 5.0/95|Eccezione|
|CELLSJAVA-42884|Eccezione "java.lang.ArrayIndexOutOfBoundsException" durante il caricamento di un file XLS MS Excel 5.0/95|Eccezione|
|CELLSJAVA-42859|CellsException per il caricamento del nome dal file ODS|Eccezione|
|CELLSJAVA-42908|Eccezione durante la chiamata a Name.getRefersTo()|Eccezione|
|CELLSJAVA-42926|IllegalStateException durante il caricamento della cartella di lavoro|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. sul forum di supporto Aspose.Cells.
### **Aggiunge il costruttore StreamProviderOptions**
Nuove opzioni StreamProvider.
### **Aggiunge l'enumerazione FileFormatType.GraphChart**
Rappresenta il file grafico del grafico incorporato.
### **Aggiunge le proprietà ImportTableOptions.CheckMergedCells**
Indica se controllare le celle unite durante l'importazione dei dati.
### **Aggiunge le classi ODSCellFieldCollection, ODSCellField e ODSCellFieldType enum**
Rappresenta il campo cellulare di ODS.
### **Aggiunge le proprietà Cells.ODSCellFields**
Ottiene l'elenco dei campi cella di ODS.
### **Aggiunge la classe ODSPageBackground e la proprietà PageSetup.ODSPageBackground**
Rappresenta lo sfondo di ODS.
### **Aggiunge enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS e SaveFormat.SXC**
Rappresenta i tipi di formato file .FODS e .SXC.
### **Aggiunge enum WarningType.UnsupportedFileFormat**
Rappresenta il formato di file non supportato per i tipi di avviso.
### **Aggiunge enum ODSGeneratorType**
Rappresenta il tipo di generatore di od.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Indica se incorporare il file OOXML come OleObject.
### **Aggiunge Row.CopySettings(Aspose.Cells.Row,System.Boolean)**
Copia le impostazioni della riga, come stile, altezza, visibilità, ...ecc.

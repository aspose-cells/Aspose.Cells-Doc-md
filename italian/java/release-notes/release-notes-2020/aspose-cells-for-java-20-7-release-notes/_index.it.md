---
title: Aspose.Cells for Java 20.7 Note di rilascio
type: docs
weight: 9
url: /it/java/aspose-cells-for-java-20-7-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.7/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43221|Eccezione "java.lang.NullPointerException" durante il caricamento del file XLT|Aumento|
|CELLSJAVA-43222|Eccezione "com.aspose.cells.CellsException: i dati della formula dovrebbero essere stati danneggiati..." durante il caricamento di un file XLS|Aumento|
|CELLSJAVA-43223|Eccezione "java.lang.IllegalStateException: codifica non valida: null" durante il caricamento di un file XLS|Aumento|
|CELLSJAVA-43226|Eccezione "java.lang.ArrayIndexOutOfBoundsException" durante il recupero dei dati dell'immagine|Aumento|
|CELLSJAVA-43234|I dati precedenti al 2014 non vengono letti dalla tabella pivot|Insetto|
|CELLSJAVA-43210|Valore errato #Valore letto da Aspose.Cells|Insetto|
|CELLSJAVA-43215|Impossibile trasformare il file XLSM in PDF|Insetto|
|CELLSJAVA-43219|L'aggiunta del riferimento alla formula a fogli diversi risulta in una cartella di lavoro di Excel danneggiata|Insetto|
|CELLSJAVA-43232|Problema con la funzione ROUNDUP|Insetto|
|CELLSJAVA-43243|Impossibile recuperare la formula durante la modifica della formula della cella adiacente|Insetto|
|CELLSJAVA-43217|La stampa da XLSX a XPS perde la formattazione in background|Insetto|
|CELLSJAVA-43224|Problema durante la stampa su una stampante fisica|Insetto|
|CELLSJAVA-43241|Problema con l'altezza della linea e il bordo durante la creazione di un'immagine dall'area di Excel|Insetto|
|CELLSJAVA-43209|setRepeatFormulaWithSubtotal(true) non genera i risultati previsti durante l'utilizzo di SmartMarkers|Insetto|
|CELLSJAVA-43213|Aspose.Cells 20.6 non funziona correttamente con i controlli dei moduli in Office 365 (versione 2005 Build 12827.20268)|Insetto|
|CELLSJAVA-43214|Quando si traduce XLS in XLSX, produce un file XLSX danneggiato|Insetto|
|CELLSJAVA-43216|Conversione da XLS a XLSX: l'audacia e il posizionamento dei caratteri vengono modificati per la forma|Insetto|
|CELLSJAVA-43228|L'XLS generato è in visualizzazione protetta|Insetto|
|CELLSJAVA-43231|Errore nel file di output dopo le sostituzioni|Insetto|
|CELLSJAVA-43225|Eccezione "java.lang.NullPointerException" durante il recupero del valore stringa dalla cella|Eccezione|
|CELLSJAVA-43229|Eccezione durante il caricamento del file XLSM con l'opzione setKeepUnparsedData(false)|Eccezione|
|CELLSJAVA-43238|Il calcolo non riesce con NPE (java.lang.NullPointerException)|Eccezione|
|CELLSJAVA-43199|Eccezione "java.lang.NegativeArraySizeException" al salvataggio in HTML|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cells.RemoveDuplicates().**

Metodo sovraccarico di Cells.RemoveDuplicates(...) per comodità dell'utente per rimuovere le righe duplicate nell'intero foglio.

### **Aggiunge la proprietà TickLabels.DisplayNumberFormat.**

Ottiene e imposta il formato del numero di visualizzazione delle etichette dei segni di graduazione.

### **Aggiunge il metodo Cells.GetViewRowHeight() e Cells.GetViewRowHeightInch().**

Ottiene l'altezza della riga della vista.

### **Aggiunge enum SheetType.InternationalMacro.**

Aggiunge un nuovo tipo di foglio: macro internazionale.

### **Aggiunge il metodo PivotFieldCollection.iterator().**

Ottiene un enumeratore sugli elementi di questa raccolta nella sequenza corretta.

### **Aggiunge il metodo PivotItemCollection.iterator().**

Ottiene un enumeratore sugli elementi di questa raccolta nella sequenza corretta.

### **Aggiunge la proprietà Workbook.IsWorkbookProtectedWithPassword.**

Indica se la struttura e la finestra sono protette da password.

### **Aggiungere le classi PowerQueryFormulaParameters e PowerQueryFormulaParameter**

Rappresenta i parametri della formula di query avanzata.

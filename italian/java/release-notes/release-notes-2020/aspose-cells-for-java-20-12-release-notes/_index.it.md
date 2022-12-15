---
title: Aspose.Cells for Java 20.12 Note di rilascio
type: docs
weight: 1
url: /it/java/aspose-cells-for-java-20-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.12](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.12/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43367|Supporta il calcolo della funzione ISFORMULA|
|CELLSJAVA-43338|Differenza nell'output durante la conversione di file Excel in PDF|
|CELLSJAVA-43346|Il file di output è danneggiato quando si aggiungono più di 12 campi nei filtri della pagina della tabella pivot|
|CELLSJAVA-43351|Il colore di sfondo della tabella di intestazione non è corretto durante la conversione in pdf|
|CELLSJAVA-43358|Manca il testo durante la conversione da HTML a Excel|
|CELLSJAVA-43341|Colonne extra vuote durante l'esportazione CSV con LightCellsDataProvider|
|CELLSJAVA-43352|Il file Excel convertito in PDF produce un problema di grandi numeri|
|CELLSJAVA-43339|L'immagine è fuori posto durante la conversione del file sorgente in pdf|
|CELLSJAVA-43340|Contenuti mancanti nella conversione da XLS a PDF|
|CELLSJAVA-43336| Le voci della legenda del grafico sono visualizzate troppo a sinistra|
|CELLSJAVA-43356|I valori/spazi vuoti su un grafico non vengono rispettati quando si trovano tra 2 valori|
|CELLSJAVA-43344|Il nome utente corrente viene visualizzato come autore dell'ultimo commento|
|CELLSJAVA-43349|Le righe nascoste non vengono mantenute dalla conversione da XML a XLS/XLSX|
|CELLSJAVA-43361|Colore della cella errato nella conversione da xls a xlsx|
|CELLSJAVA-43366|La proprietà SetAsTotal non viene aggiornata|
|CELLSJAVA-43348|Conversione da XLSB a PDF: CellsException: -2147483648|
|CELLSJAVA-43343|Eccezione durante l'esportazione di un file in PDF che non ha un elemento selezionato per una forma|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cell.SetDynamicArrayFormula(string arrayFormula, Opzioni FormulaParseOptions, bool calcola).**

Supporta l'impostazione della formula dell'array dinamico e la diffusione nelle celle adiacenti, se possibile.

### **Aggiunge il metodo Workbook.RefreshDynamicArrayFormulas(boolcalculate).**

Supporta l'aggiornamento delle formule di matrice dinamica e la diffusione nelle celle adiacenti in base ai dati correnti.

### **Aggiunge la proprietà Cell.Comment.**

Ottiene il commento della cella.

### **Aggiunge la proprietà HtmlSaveOptions.ExportExtraHeadings**

Indica se esportare intestazioni aggiuntive quando la lunghezza del testo è maggiore della colonna di visualizzazione massima.
Il valore predefinito è falso. Se desideri importare il file html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà HtmlSaveOptions.ExportFormula**

Indica se esportare la formula durante il salvataggio del file in html. Il valore predefinito è vero.
Se desideri importare l'output html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà HtmlSaveOptions.MergeEmptyTdForcely**

Indica se l'unione forzata dell'elemento TD vuoto durante l'esportazione del file in html.
La dimensione del file html verrà ridotta in modo significativo dopo aver impostato il valore su true. Il valore predefinito è falso.
Se vuoi importare il file html per eccellere o esportare le linee della griglia perfette quando salvi il file in html,
si prega di mantenere il valore predefinito.

### **Aggiunge la proprietà LoadOptions.AutoFilter**

Indica se filtrare automaticamente i dati durante il caricamento dei file.
A volte, sebbene sia impostato il filtro automatico, le righe corrispondenti non sono nascoste nel file. Ora funziona solo per il file SpreadSheetML.

### **Aggiunge la proprietà WorkbookSettings.Author**

Ottiene e imposta l'autore della cartella di lavoro.

### **Aggiunge il metodo MultipleFilterCollection.Add().**

Aggiunge la stringa del filtro del filtro automatico.

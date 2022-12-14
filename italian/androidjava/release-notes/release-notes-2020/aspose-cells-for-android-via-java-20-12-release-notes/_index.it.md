---
title: Aspose.Cells per Android tramite Java 20.12 Note di rilascio
type: docs
weight: 8
url: /it/java/aspose-cells-for-android-via-java-20-12-release-notes/
---
{{% alert color="primary" %}}

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 20.12.

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43322|Proprietà Shape.getWorksheet() obbligatoria|Nuova caratteristica|
|CELLSJAVA-43367|Supporta il calcolo della funzione ISFORMULA|
|CELLSJAVA-43191|Fornire mezzi per gestire gli scenari quando si specificano tipi di carattere errati|Aumento|
|CELLSJAVA-40913|La direzione della freccia è cambiata nel PDF risultante|Insetto|
|CELLSJAVA-43282|Il pivot di aggiornamento non funziona e corrompe il file di output|Insetto|
|CELLSJAVA-43286|Aspose.Cells è in conflitto con le impostazioni HtmlHiddenRowDisplayType.REMOVE|Insetto|
|CELLSJAVA-43302|Problema con l'ottenimento del valore Cells|Insetto|
|CELLSJAVA-43308|Conversione da HTML a Excel con proprietà wrapText|Insetto|
|CELLSJAVA-43318|Cell problema di valore dopo l'aggiornamento della tabella pivot|Insetto|
|CELLSJAVA-43299|Problema con l'ottenimento del valore Cell|Insetto|
|CELLSJAVA-43284|Grafico non stampato durante l'utilizzo di Aspose.Cells per una particolare stampante fisica|Insetto|
|CELLSJAVA-43273|Il testo negli elementi della legenda viene ritagliato nell'immagine di output|Insetto|
|CELLSJAVA-43274|Differenza nel colore del contorno della barra del grafico|Insetto|
|CELLSJAVA-43276|Problemi di interruzione di riga durante la conversione di XLSX in PDF|Insetto|
|CELLSJAVA-43278|Il barrato in Excel non viene visualizzato nel file PDF|Insetto|
|CELLSJAVA-43304|Alcune etichette dati del grafico mancano nel PDF di output|Insetto|
|CELLSJAVA-43311|Le etichette dell'asse X del grafico sono verticali anziché diagonali quando vengono convertite in immagine|Insetto|
|CELLSJAVA-40992|Problema con la posizione del testo del grafico durante il nuovo salvataggio di un file Excel|Insetto|
|CELLSJAVA-43294|Il tema colore della formattazione condizionale non funziona correttamente|Insetto|
|CELLSJAVA-43307|Problema di ridimensionamento con l'oggetto OLE incorporato durante la copia del foglio di lavoro|Insetto|
|CELLSJAVA-43319|Problema di ottenere il valore della cella con la formula|Insetto|
|CELLSJAVA-43330|Problema dopo aver salvato nuovamente il file XLSB: file danneggiato|Insetto|
|CELLSJAVA-43333|Immagini e posizionamento del testo errato durante il rendering di Excel come HTML|Insetto|
|CELLSJAVA-43321|Problema con il filtro automatico: vengono visualizzate righe vuote|Insetto|
|CELLSJAVA-43335|Si è verificato un deadlock durante il calcolo delle formule sulla cartella di lavoro|Insetto|
|CELLSJAVA-43313|L'etichetta del grafico cambia posizione quando viene stampata|Insetto|
|CELLSJAVA-43314|Riga 0/100% non stampata per grafici a torta 100%.|Insetto|
|CELLSJAVA-43316| Vari problemi durante la stampa dei grafici|Insetto|
|CELLSJAVA-40582|Il testo Smart Art non viene visualizzato correttamente in PDF/immagine|Insetto|
|CELLSJAVA-41639|Le larghezze delle colonne non vengono mantenute durante la conversione dal formato "XML Spreadsheet 2003" al formato XLSX|Insetto|
|CELLSJAVA-43315|La conversione di XLS in XLSX danneggia il file e genera l'errore "Shape to Image" durante la conversione dell'output XLSX in PDF|Insetto|
|CELLSJAVA-43334|Filtro automatico sul problema della tabella|Insetto|
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
|CELLSJAVA-43296|ArrayIndexOutOfBoundsException durante l'aggiornamento della tabella pivot|Eccezione|
|CELLSJAVA-43298|Aspose.Cells 20.8: Eccezione quando si salva in PDF.|Eccezione|
|CELLSJAVA-43348|Conversione da XLSB a PDF: CellsException: -2147483648|
|CELLSJAVA-43343| Eccezione durante l'esportazione di un file in PDF che non ha un elemento selezionato per una forma|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.

### **Aggiunge ExceptionType.Permission enum**

Rappresenta ExceptionType.Permission.

### **Aggiunge la proprietà ExternalConnection.PowerQueryFormula.**

Ottiene la definizione della formula di query di alimentazione.

### **Aggiunge il metodo FileFormatUtil.VerifyPassword.**

Verifica se la password è valida per il file.

### **Aggiunge il metodo VbaProject.Copy().**

Copia il progetto VBA.

### **Aggiunge la proprietà XlsSaveOptions.MatchColor.**

Indica se corrispondere al colore se il colore non è nella tavolozza durante il salvataggio del file .xls.

### **Elimina la proprietà Series.Line obsoleta.**

Utilizzare invece la proprietà Series.Border.

### **Elimina il metodo CellsHelper.IsProtectedByRMS() obsoleto**

Usare invece la proprietà FileFormatUtil.DetectFileFormat().IsProtectedByRMS.

### **Elimina il metodo CellsHelper.DetectLoadFormat() e CellsHelper.DetectFileFormat() obsoleto**

Utilizzare invece FileFormatUtil.DetectFileFormat().

### **Elimina la proprietà CellsHelper.FontDir obsoleta.**

Usare invece FontConfigs.SetFontsFolder(string, bool).

### **Elimina la proprietà CellsHelper.FontDirs obsoleta.**

Usare invece FontConfigs.SetFontFolders(string[], bool).

### **Elimina la proprietà CellsHelper.FontFiles obsoleta.**

Usare invece FontConfigs.SetFontSources(FontSourceBase[]).

### **Aggiunge la proprietà CellsHelper.IsCloudPlatform.**

Indica se è in esecuzione sulla piattaforma could.

### **Aggiunge la proprietà Shape.Worksheet.**

Ottiene il foglio di lavoro che contiene questa forma.

### **Aggiunge la proprietà SaveOptions.SortExternalNames.**

Indica se ordinare i nomi esterni durante il salvataggio dei file .xlsx.

### **Aggiunge il metodo ListObject.Filter().**

Filtra la tabella.

### **Aggiunge il metodo override XmlMapCollection.Clear().**

Cancella tutte le mappe xml.

### **Aggiunge l'enumerazione SaveFormat.Docx.**

Rappresenta il salvataggio come file .docx.

### **Aggiunge ImageType.OfficeCompatibleEmf enum.**

Windows Enhanced Metafile che è più compatibile con Office.

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

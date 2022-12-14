---
title: Aspose.Cells per Android tramite Java 19.12 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-android-via-java-19-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 19.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41814|Supporta l'ordinamento personalizzato dei dati per l'area specifica nel rapporto di tabella pivot|Nuova caratteristica|
|CELLSJAVA-43032|Aggiungere Validation.addArea (CellArea cellArea, boolean skipArea) o Validation.setAreas() metodo/overload alle API|Nuova caratteristica|
|CELLSJAVA-42851|Ottieni i dettagli della connessione ODATA|Nuova caratteristica|
|CELLSJAVA-43047|Aggiunta del testo del suggerimento alla cella per l'esportazione in HTML|Nuova caratteristica|
|CELLSJAVA-42988|Problema di prestazioni con calcolaFormula()|Aumento|
|CELLSJAVA-43018|Esporta l'intervallo dell'area di stampa in HTML senza modificare implicitamente alcuni stati della stessa cartella di lavoro|Aumento|
|CELLSJAVA-43041|Cells.importCSV genera un'eccezione "il valore della stringa non può superare i 255 caratteri"|Aumento|
|CELLSJAVA-43043|Cells.removeDuplicates richiede più tempo per set di dati di grandi dimensioni|Aumento|
|CELLSJAVA-43002|Hot spot CPU imprevisto in ZipOutputStream all'apertura di XSLB|Aumento|
|CELLSJAVA-43008|Opzione per disabilitare il caricamento dell'oggetto OLE durante l'apertura di una cartella di lavoro|Aumento|
|CELLSJAVA-43019|Grafico radiale non visualizzato correttamente in HTML|Insetto|
|CELLSJAVA-43027|Dopo il rendering in PNG, il ridimensionamento dell'asse è diverso.|Insetto|
|CELLSJAVA-42474|La tabella pivot non viene aggiornata e danneggiata dopo l'aggiornamento dei dati di origine|Insetto|
|CELLSJAVA-43033|La conversione in PDF non finisce.|Insetto|
|CELLSJAVA-43034|Viene recuperato un output in formato di data russo (personalizzato) non valido|Insetto|
|CELLSJAVA-43040|LoadFilter non considera il foglio richiesto|Insetto|
|CELLSJAVA-43035|I bordi vengono persi durante la conversione del file Excel in EMF|Insetto|
|CELLSJAVA-43016|Conteggio pagine non valido da SheetRender|Insetto|
|CELLSJAVA-43026|Dopo aver eseguito il rendering del grafico sull'immagine, le etichette dei dati cambiano stile e i valori non sono gli stessi|Insetto|
|CELLSJAVA-43038|I collegamenti ipertestuali non vengono esportati utilizzando Cell.setHtmlString()|Insetto|
|CELLSJAVA-43039|Cell.setHtmlString() non esegue il rendering di determinati tag/script HTML nell'esportazione in Excel|Insetto|
|CELLSJAVA-41103|La colorazione e la formattazione dei dati della tabella pivot non vengono visualizzate correttamente|Insetto|
|CELLSJAVA-43007|Il PDF non viene generato come previsto|Insetto|
|CELLSJAVA-43025|Cell.getStyle.getCustom restituisce un formato errato per la locale tedesca|Insetto|
|CELLSJAVA-42793|Oggetto Fontwork SmartArt perso durante la conversione da ODS a XLSX|Insetto|
|CELLSJAVA-43020|Grafico radiale distorto dopo aver chiamato Chart.Calcluate()|Insetto|
|CELLSJAVA-43022|Errore da forma a immagine per i file XLS|Insetto|
|CELLSJAVA-43046|LoadOptions.setParsingFormulaOnOpen(false) provoca risultati indesiderati durante la chiamata a getFormula()|Insetto|
|CELLSJAVA-43052|Problema di convalida per i valori booleani|Insetto|
|CELLSJAVA-43054|Problema con CSV Merge nelle impostazioni portoghesi|Insetto|
|CELLSJAVA-43056|Cell.setFormula() non si aggiorna per i collegamenti esterni|Insetto|
|CELLSJAVA-42767|Immagine persa durante la conversione da Excel a PDF|Insetto|
|CELLSJAVA-42913|Oggetti Visio incorporati visualizzati in modo errato in PDF|Insetto|
|CELLSJAVA-42883|Problema durante l'estrazione del testo del grafico dal file in formato Aspose.Cells for Java 95|Insetto|
|CELLSJAVA-42931|Allegati/Oggetti non recuperati da Excel95|Insetto|
|CELLSJAVA-43051|Proporzioni non mantenute per l'immagine|Insetto|
|CELLSJAVA-43057|Problema con l'aggiunta dell'immagine dell'intestazione alla prima pagina nell'output di Excel|Insetto|
|CELLSJAVA-43069|MS Excel fornisce un messaggio di riparazione quando si apre il file risalvato da Aspose.Cells|Insetto|
|CELLSJAVA-43013|ArrayIndexOutOfBoundsException durante il caricamento del file Excel|Eccezione|
|CELLSJAVA-43060|Eccezione "java.lang.NullPointerException" su Workbook.save dopo aver impostato l'origine dati esterna come vuota|Eccezione|
|CELLSJAVA-42923|Eccezioni durante il caricamento del documento XLS|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.
### **Aggiunge il metodo Cells.RemoveDuplicates()**
Rimuove i dati duplicati dell'intervallo.
### **Aggiunge la proprietà OleObject.FullObjectBin**
Ottiene i dati binari dell'oggetto ole incorporati completi nel file modello.
### **Aggiunge la proprietà ContentTypeProperty.IsNillable**
Indica se la proprietà può essere nulla.
### **Aggiungere il metodo WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Imposta l'origine dati per Smart Marker Designer.
### **Aggiunge la proprietà ImageOrPrintOptions.PageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
### **Aggiunge la proprietà ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Indica se sostituire solo il carattere del carattere quando il carattere della cella non è compatibile con esso.
### **Rimuove la classe obsoleta HTMLLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
### **Rimuove la classe obsoleta ODSLoadOptions**
Utilizzare invece la classe OdsLoadOptions.
### **Rimuove la classe obsoleta JSONUtility**
Utilizzare invece la classe JsonUtility.
### **Aggiunge metodi: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Aggiunge/rimuove le impostazioni di convalida da determinate aree tenendo conto delle prestazioni.
### **Aggiunge il metodo Workbook.ImportXml(Stream stream, string sheetName, int row, int col).**
Importa un flusso di file XML nella cartella di lavoro.
### **Aggiunge il metodo Workbook.ExportXml(string mapName, Stream stream).**
Esporta i dati XML in un flusso.
### **Aggiunge la proprietà HtmlSaveOptions.ExportArea**
Ottiene o imposta la CellArea di esportazione del foglio di lavoro attivo corrente. Se si imposta questo attributo, l'area di stampa del foglio di lavoro attivo corrente verrà omessa. Solo l'area specificata verrà esportata durante il salvataggio del file in HTML.
### **Aggiunge classi: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem e PowerQueryFormulaItemCollection**
Ottiene informazioni nel DataMashup.
### **Aggiunge la proprietà DBConnection.SeverCommand.**
Ottiene e imposta una seconda stringa di testo del comando che viene resa persistente quando sono in uso i campi della pagina basata sul server della tabella pivot.
### **Aggiunge il metodo CellsHelper.GetTextWidth().**
Ottiene la larghezza del testo nell'unità di punti.
### **Elimina la proprietà DataLabels.BaseField obsoleta**
Utilizzare invece PivotField.BaseFieldIndex.
### **Elimina la proprietà DataLabels.BaseItem obsoleta**
Utilizzare invece PivotField.BaseItemIndex.
### **Elimina la proprietà DataLabels.IsValueShown obsoleta**
Usare invece la proprietà DataLabels.ShowValue.
### **Elimina la proprietà DataLabels.IsPercentageShown obsoleta**
Utilizzare invece la proprietà DataLabels.ShowPercentage.
### **Elimina la proprietà DataLabels.IsBubbleSizeShown obsoleta**
Usare invece la proprietà DataLabels.ShowBubbleSize.
### **Elimina la proprietà DataLabels.IsCategoryNameShown obsoleta**
Usare invece la proprietà DataLabels.ShowCategoryName.
### **Elimina la proprietà DataLabels.IsSeriesNameShown obsoleta**
Utilizzare invece la proprietà DataLabels.ShowSeriesName.
### **Elimina la proprietà DataLabels.IsLegendKeyShown obsoleta**
Usare invece la proprietà DataLabels.ShowLegendKey.
### **Aggiunge l'opzione LoadOptions.KeepUnparsedData**
L'opzione indica se conservare i dati non analizzati in memoria per la cartella di lavoro quando viene caricata da un file modello. Se gli utenti non hanno bisogno di salvare completamente la cartella di lavoro, specialmente quando hanno solo bisogno di leggere alcuni contenuti speciali della cartella di lavoro (come da qualche tipo di LoadFilter), i dati non analizzati non sono più necessari e possono impostare questa proprietà come false per ottenere prestazioni migliori. Per le versioni precedenti, durante il caricamento della cartella di lavoro da un file modello con LoadFilter specificato dall'utente, per motivi di prestazioni i dati non analizzati non venivano conservati. Ora forniamo questa opzione e rendiamo vero il suo valore predefinito, potrebbe influenzare le prestazioni dei casi di utilizzo di LoadFilter da parte degli utenti. In tal caso, gli utenti devono impostare questa proprietà come false in modo esplicito nella loro applicazione.
### **Aggiunge l'opzione LoadDataFilterOptions.Picture**
L'opzione che indica se l'immagine deve essere caricata.
### **Aggiunge l'opzione LoadDataFilterOptions.OleObject**
L'opzione che indica se OleObject deve essere caricato.
### **Aggiunge l'opzione LoadDataFilterOptions.Drawing**
L'opzione che indica se gli oggetti di disegno (inclusi Grafico, Immagine, OleObject e tutti gli altri oggetti di disegno) devono essere caricati.
### **Opzione LoadDataFilterOptions.Shape obsoleta**
Utilizzare (LoadDataFilterOptions.Drawing & ~LoadDataFilterOptions.Chart) invece di LoadDataFilterOptions.Shape.
### **Aggiunge la classe FormulaParseOptions**
Fornisce opzioni utente per l'impostazione delle formule.
### **Aggiunge metodi: Cell.SetFormula(string formula,FormulaParseOptions options,object value),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,FormulaParseOptions options),SetSharedFormula(string sharedFormula,int rowNumber,int columnNumber,FormulaParseOptions options)**
Imposta le formule con le opzioni.
### **Metodi obsoleti: Cell.SetFormula(string formula,bool isR1C1,bool isLocal,object value),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,bool isR1C1,bool isLocal),SetSharedFormula(string sharedFormula,int rowNumber,int columnNumber,bool isR1C1,bool isLocal)**
Utilizzare invece i metodi corrispondenti con FormulaParseOptions.
### **Aggiunge l'enumerazione FileFormatType.OTP**
Supporta il rilevamento del formato file .OTP.
### **Aggiunge la proprietà AutoFitterOptions.AutoFitWrappedTextType e l'enumerazione AutoFitWrappedTextType.**
Ottiene e imposta il tipo di testo a capo con adattamento automatico.
### **Aggiunge la classe EmfRenderSetting**
Imposta per il rendering del metafile EMF.
### **Aggiunge la proprietà PdfSaveOptions.EmfRenderSetting**
Imposta per il rendering del metafile EMF durante il rendering in un file PDF.
### **Aggiunge il metodo ShapeCollection.AddSvg()**
Aggiunge un'immagine svg.
### **Aggiunge la proprietà WorkbookSettings.QuotePrefixToStyle**
Indica se impostare la proprietà Style.QuotePrefix quando si immette il valore della stringa (che inizia con virgolette singole) nella cella
### **Aggiunge la proprietà HtmlSaveOptions.AddTooltipText**
Indica se aggiungere il testo della descrizione comandi quando i dati non possono essere visualizzati completamente. Il valore predefinito è falso.

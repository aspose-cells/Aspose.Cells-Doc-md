---
title: Aspose.Cells for Java Note sulla versione 19.12
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-19-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43047|Aggiunta del testo del suggerimento alla cella per l'esportazione in HTML|Nuova caratteristica|
|CELLSJAVA-43002|Hot spot CPU imprevisto in ZipOutputStream all'apertura di XSLB|Aumento|
|CELLSJAVA-43008|Opzione per disabilitare il caricamento dell'oggetto OLE durante l'apertura di una cartella di lavoro|Aumento|
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
|CELLSJAVA-43060|Eccezione "java.lang.NullPointerException" su Workbook.save dopo aver impostato l'origine dati esterna come vuota|Eccezione|
|CELLSJAVA-42923|Eccezioni durante il caricamento del documento XLS|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
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

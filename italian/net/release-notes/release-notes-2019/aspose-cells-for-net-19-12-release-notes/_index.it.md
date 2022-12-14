---
title: Aspose.Cells for .NET Note sulla versione 19.12
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-19-12-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.12](https://www.nuget.org/packages/Aspose.Cells/19.12.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-44451|Applica l'ordinamento dei dati per il campo dati rispetto al campo Riga nella tabella pivot: simula i risultati in base al file previsto dall'utente|Nuova caratteristica|
|CELLSNETCORE-45|Carica i dati da Datasource con l'opzione per saltare alcuni caratteri come Apostrophe|Nuova caratteristica|
|CELLSNET-47018|Il calcolo di alcuni grafici combinati può generare un'eccezione|Aumento|
|CELLSNET-47016|Il testo a capo è diverso nell'ultima versione di Aspose.Cells|Aumento|
|CELLSNET-47023|Grafico perso durante il caricamento e il salvataggio del file ODS|Aumento|
|CELLSNET-47056|Grafici non visualizzati durante il caricamento e il salvataggio del file ODS|Aumento|
|CELLSNET-46679|Rendering errato durante l'esportazione di XLSX in PDF|Insetto|
|CELLSNET-46680|Il simbolo Wingding non è presente durante la conversione di XLSX in PDF|Insetto|
|CELLSNET-46740|Errore nelle immagini durante la conversione del file Excel in PDF|Insetto|
|CELLSNET-46901|La posizione del modello 3D si sposta|Insetto|
|CELLSNET-46936|Carattere non reso correttamente in HTML|Insetto|
|CELLSNET-47013|I numeri sul grafico a imbuto scompaiono durante la conversione del file Excel in PDF|Insetto|
|CELLSNET-43846|La tabella pivot perde i nomi dei campi personalizzati e l'impostazione "Mostra valore come..."|Insetto|
|CELLSNET-46444|Il valore della tabella pivot è stato modificato dopo aver chiamato PivotTable.CalculateData|Insetto|
|CELLSNET-46484|RefreshData non ordina i dati prima di aprire il file in Excel|Insetto|
|CELLSNET-47010|Un problema con la formattazione delle intestazioni dei gruppi di tabelle pivot|Insetto|
|CELLSNET-47024|Ordinamento delle righe errato nelle tabelle pivot con riga Valori|Insetto|
|CELLSNET-47034|Larghezze delle colonne e altezza delle righe ridotte durante la conversione da HTML a Excel|Insetto|
|CELLSNET-47007|L'errore di valore viene visualizzato durante la valutazione della formula|Insetto|
|CELLSNET-47029|Valore errato TRUE recuperato da Cell invece del valore FALSE|Insetto|
|CELLSNET-47052|DateTimeFormat danneggiato durante la conversione di Excel in PDF|Insetto|
|CELLSNET-46757|Problemi durante la conversione di XLSX in PDF|Insetto|
|CELLSNET-46976|Alcune linee di confine scompaiono nel rendering da Excel a PDF|Insetto|
|CELLSNET-47000|Immagine del risultato inappropriata di SheetRender dal file .ods protetto da password|Insetto|
|CELLSNET-47025|Macro per XLSM non rilevate|Insetto|
|CELLSNET-47038|I grafici a linee nel file ODS non vengono visualizzati correttamente quando vengono aperti o salvati tramite Aspose.Cells|Insetto|
|CELLSNET-47045|La modifica del nome del modulo VBA si arresta in modo anomalo|Insetto|
|CELLSNET-47051|Il grafico è ancora legato al primo foglio di lavoro dopo la copia|Insetto|
|CELLSNET-47053|Rilevamento errato del formato file e processo bloccato durante l'apertura del file|Insetto|
|CELLSNET-46922|Eccezione durante il caricamento del file XLS|Eccezione|
|CELLSNET-46999|Viene generata un'eccezione durante il rendering del file .ods "Parametro non valido".|Eccezione|
|CELLSNET-47017|OpenXML SDK genera un'eccezione all'apertura del file convertito|Eccezione|
|CELLSNET-47022|Eccezione durante il caricamento di un formato di file XLSX|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Elimina la proprietà DataLabels.BaseField obsoleta**
Utilizzare invece PivotField.BaseFieldIndex.
#### **Elimina la proprietà DataLabels.BaseItem obsoleta**
Utilizzare invece PivotField.BaseItemIndex.
#### **Elimina la proprietà DataLabels.IsValueShown obsoleta**
Usare invece la proprietà DataLabels.ShowValue.
#### **Elimina la proprietà DataLabels.IsPercentageShown obsoleta**
Utilizzare invece la proprietà DataLabels.ShowPercentage.
#### **Elimina la proprietà DataLabels.IsBubbleSizeShown obsoleta**
Usare invece la proprietà DataLabels.ShowBubbleSize.
#### **Elimina la proprietà DataLabels.IsCategoryNameShown obsoleta**
Usare invece la proprietà DataLabels.ShowCategoryName.
#### **Elimina la proprietà DataLabels.IsSeriesNameShown obsoleta**
Utilizzare invece la proprietà DataLabels.ShowSeriesName.
#### **Elimina la proprietà DataLabels.IsLegendKeyShown obsoleta**
Usare invece la proprietà DataLabels.ShowLegendKey.
#### **Aggiunge l'opzione LoadOptions.KeepUnparsedData**
L'opzione indica se mantenere i dati non analizzati in memoria per la cartella di lavoro quando viene caricata dal file modello. Se gli utenti non hanno bisogno di salvare completamente la cartella di lavoro, specialmente quando hanno solo bisogno di leggere alcuni contenuti speciali della cartella di lavoro (come da qualche tipo di LoadFilter), quei dati non analizzati non sono più necessari e possono impostare questa proprietà come false per ottenere prestazioni migliori. Per le versioni precedenti, durante il caricamento della cartella di lavoro da un file modello con LoadFilter specificato dall'utente, per motivi di prestazioni i dati non analizzati non venivano conservati. Ora forniamo questa opzione e rendiamo vero il suo valore predefinito, potrebbe influenzare le prestazioni dei casi di utilizzo di LoadFilter da parte degli utenti. In tal caso, gli utenti devono impostare questa proprietà come false in modo esplicito nella loro applicazione.
#### **Aggiunge l'opzione LoadDataFilterOptions.Picture**
L'opzione che indica se l'immagine deve essere caricata.
#### **Aggiunge l'opzione LoadDataFilterOptions.OleObject**
L'opzione che indica se OleObject deve essere caricato.
#### **Aggiunge l'opzione LoadDataFilterOptions.Drawing**
L'opzione che indica se gli oggetti di disegno (inclusi Grafico, Immagine, OleObject e tutti gli altri oggetti di disegno) devono essere caricati.
#### **Opzione LoadDataFilterOptions.Shape obsoleta**
Utilizzare (LoadDataFilterOptions.Drawing & ~LoadDataFilterOptions.Chart) invece di LoadDataFilterOptions.Shape.
#### **Aggiunge la classe FormulaParseOptions**
Fornisce opzioni utente per l'impostazione delle formule.
#### **Aggiunge metodi: Cell.SetFormula(string formula,FormulaParseOptions options,object value),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,FormulaParseOptions options),SetSharedFormula(string sharedFormula,int rowNumber,int columnNumber,FormulaParseOptions options)**
Imposta le formule con le opzioni.
#### **Metodi obsoleti: Cell.SetFormula(string formula,bool isR1C1,bool isLocal,object value),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,bool isR1C1,bool isLocal),SetSharedFormula(string sharedFormula,int rowNumber,int columnNumber,bool isR1C1,bool isLocal)**
Usa invece i metodi corrispondenti con FormulaParseOptions.
#### **Aggiunge l'enumerazione FileFormatType.OTP**
Supporta il rilevamento del formato file .OTP.
#### **Aggiunge la proprietà AutoFitterOptions.AutoFitWrappedTextType e l'enumerazione AutoFitWrappedTextType.**
Ottiene e imposta il tipo di testo a capo con adattamento automatico.
#### **Aggiunge la classe EmfRenderSetting**
Imposta per il rendering del metafile Emf.
#### **Aggiunge la proprietà PdfSaveOptions.EmfRenderSetting**
Imposta per il rendering del metafile EMF durante il rendering in un file PDF.
#### **Aggiunge il metodo ShapeCollection.AddSvg()**
Aggiunge l'immagine SVG.
#### **Aggiunge la proprietà WorkbookSettings.QuotePrefixToStyle**
Indica se impostare la proprietà Style.QuotePrefix quando si immette il valore della stringa (che inizia con virgolette singole) nella cella
#### **Aggiunge la proprietà HtmlSaveOptions.AddTooltipText**
Indica se aggiungere il testo della descrizione comandi quando i dati non possono essere visualizzati completamente. Il valore predefinito è falso.

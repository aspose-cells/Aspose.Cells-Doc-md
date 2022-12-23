---
title: Aspose.Cells for .NET 19.4 Note di rilascio
type: docs
weight: 90
url: /it/net/aspose-cells-for-net-19-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.4](https://www.nuget.org/packages/Aspose.Cells/19.4.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46619|Supporta il salvataggio del documento in formato Markdown|Nuova caratteristica|
|CELLSNET-46124|Supporta l'aggiunta di forme WebExtension|Nuova caratteristica|
|CELLSNET-46553|Supporta l'importazione di file JSON|Nuova caratteristica|
|CELLSNET-46653|Supporta l'aggiunta del riquadro attività WebExtension|Nuova caratteristica|
|CELLSNET-46656|Supporta i commenti in thread|Nuova caratteristica|
|CELLSNET-46657|Supporta le celle di taglio e incolla|Nuova caratteristica|
|CELLSNET-46686|Supporta l'utilizzo di spazi bianchi (codice carattere 20) come separatore di gruppi di numeri per la lingua francese|Aumento|
|CELLSNET-46649|Grande PDF generato rispetto allo strumento online iLovePDF|Aumento|
|CELLSNET-46093|I grafici non rispettano l'impostazione della pagina in bianco e nero|Aumento|
|CELLSNET-46677|L'esportazione di Excel in PDF non esegue il rendering preciso dei testi arabi nei grafici|Aumento|
|CELLSNET-46639|Supporta l'interruzione di pagina verticale per il file ODS.|Aumento|
|CELLSNET-46631|Eccezione OutOfMemoryException durante il rendering|Prestazione|
|CELLSNET-46596|Etichette mancanti nelle forme|Insetto|
|CELLSNET-46615|Shape.ToImage() esporta immagini di dimensioni diverse|Insetto|
|CELLSNET-46637|Errori di formattazione nel codice HTML generato|Insetto|
|CELLSNET-46650|PivotTable.ShowValuesRow non impostato su false a livello di codice|Insetto|
|CELLSNET-46652|Le affettatrici della tabella pivot vengono rimosse dopo il caricamento e il salvataggio|Insetto|
|CELLSNET-46678|PivotField.IsRepeatItemLabels non viene mantenuto nell'output XLSB|Insetto|
|CELLSNET-46671|Range.Copy dopo Range.CopyData corrompe la cartella di lavoro|Insetto|
|CELLSNET-42423|Il salvataggio in PDF taglia i dati della riga|Insetto|
|CELLSNET-45698|Il metodo Worksheet.AutoFitColumns taglia il testo lungo durante il rendering su PDF|Insetto|
|CELLSNET-46661|Meno numero di pagine visualizzate in PDF rispetto a Excel 365|Insetto|
|CELLSNET-46673|Problema di dimensione del file durante la conversione di Excel in PDF|Insetto|
|CELLSNET-46632|ChartPoint.Datalabels.ShowValue non funziona come previsto|Insetto|
|CELLSNET-46655|Etichette dell'asse delle categorie multilivello perse durante il salvataggio con RefreshChartCache = true|Insetto|
|CELLSNET-46665|Il file Excel è danneggiato dopo aver chiamato NSeries.Clear() sui grafici Surface|Insetto|
|CELLSNET-46672|Dati della serie mancanti durante l'esportazione del grafico in un'immagine|Insetto|
|CELLSNET-46627|Un problema con il puntamento del grafico pivot|Insetto|
|CELLSNET-46640|L'interruzione di pagina orizzontale viene persa se la riga è vuota durante il salvataggio del file ODS|Insetto|
|CELLSNET-46643|Gli intervalli denominati non vengono copiati durante la copia di una colonna|Insetto|
|CELLSNET-46644|I tag HeadingPairs e TitlesOfParts vengono persi|Insetto|
|CELLSNET-46651|File Excel danneggiato durante l'apertura e il salvataggio|Insetto|
|CELLSNET-46654|Supporta l'aggiunta di WebExtension|Insetto|
|CELLSNET-46662|Problema nell'ottenere BuiltInDocumentProperties|Insetto|
|CELLSNET-46663|La dimensione dell'immagine è cambiata durante la conversione da XLS a PDF|Insetto|
|CELLSNET-46667|Le righe nascoste vengono recuperate mentre PlotVisibleRows = true|Insetto|
|CELLSNET-46668|La linea tratteggiata diventa continua quando XLSX viene salvato come ODS|Insetto|
|CELLSNET-46669|Shape to image Errore durante il rendering di un file Excel in PDF|Eccezione|
|CELLSNET-46645|Eccezione sollevata durante la chiamata a PivotTable.GetChildrens()|Eccezione|
|CELLSNET-46675|Eccezione all'apertura di un file XLSX|Eccezione|
|CELLSNET-46646|Eccezione sollevata aprendo il file Excel dopo aver aggiornato il grafico|Eccezione|
|CELLSNET-46660|La proprietà Style.ForegroundColor genera un'eccezione per determinati scenari|Eccezione|
|CELLSNET-46688|Eccezioni sollevate durante l'applicazione dinamica degli stili|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge le API per il salvataggio del documento Markdown: SaveFormat.Markdown, FileFormatType.Markdown, MarkdownSaveOptions**
Supporta il salvataggio del contenuto delle celle come tabella markdown. Con il metodo Workbook.Save(), tutto il contenuto delle celle nel foglio attivo verrà esportato come tabella nel documento markdown.
#### **Rimuove le proprietà obsolete di TxtLoadOptions**
Utilizzare la proprietà LoadStyleStrategy invece di KeepExactFormat.
#### **Rimuove la classe obsoleta LoadDataOption**
Utilizzare invece la classe LoadFilter e la proprietà LoadOptions.LoadFilter.
#### **Rimuove le proprietà obsolete di LoadOptions**
LoadOptions.ConvertNumericData: utilizzare questa proprietà con la sottoclasse corrispondente di LoadOptions, ad esempio TxtLoadOptions.
LoadOptions.LoadDataOptions: utilizzare la proprietà LoadOptions.LoadFilter con l'implementazione personalizzata di LoadFilter.
LoadOptions.LoadDataFilterOptions: utilizzare invece LoadOptions.LoadFilter.LoadDataFilterOptions.
LoadOptions.OnlyLoadDocumentProperties: utilizzare LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting/LoadDataOnly: utilizzare LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
#### **Aggiunge la proprietà PdfSaveOptions.ExportDocumentStructure**
Ottiene o imposta un valore che determina se esportare o meno la struttura del documento.
#### **Aggiunge le classi dello spazio dei nomi Aspose.Cells.WebExtensions**
Rappresenta WebExtensions e WebExtensionTasks.
#### **Aggiunge le proprietà WorksheetCollection.WebExtensions e WorksheetCollection.WebExtensionTaskPanes.**
Rappresenta tutte le WebExtensions e WebExtensionTasks.
#### **Aggiunge la classe WebExtensionShape.**
Rappresenta la forma di WebExtension.
#### **Aggiunge il metodo Cells.InsertCutCells().**
Inserisce celle tagliate.
#### **Aggiunge il metodo Cells.SetViewColumnWidthPixel.**
Imposta la larghezza della vista della colonna.
#### **Aggiunge le classi ThreadedCommentCollection e ThreadedComment.**
Rappresenta il commento con thread.
#### **Aggiunge la proprietà WorksheetCollection.ThreadedCommentAuthors.**
Ottiene e imposta gli autori dei commenti in thread.
#### **Aggiunge la proprietà Comment.ThreadedComments.**
Rappresenta i commenti in thread sul commento.
#### **Aggiungere i metodi CommentCollection.AddThreadedComment() e CommentCollection.GetThreadedComments().**
Aggiunge e ottiene i commenti in thread.
#### **Aggiungere la proprietà Chart.SubTitle.**
Ottiene il sottotitolo del grafico. Solo per file in formato ODS.

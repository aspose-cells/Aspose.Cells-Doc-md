---
title: Aspose.Cells for Java 19.4 Note di rilascio
type: docs
weight: 90
url: /it/java/aspose-cells-for-java-19-4-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.4.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42838|Disattivazione della proprietà del riquadro delle attività di visualizzazione automatica.|Nuova caratteristica|
|CELLSJAVA-42853|Problema di prestazioni durante la conversione da XLSX a HTML|Aumento|
|CELLSJAVA-42852|L'etichetta su entrambi gli assi non viene visualizzata|Insetto|
|CELLSJAVA-42856|Problema di conversione da Excel a HTML|Insetto|
|CELLSJAVA-42872|Immagine del foglio, mancano le righe destra e inferiore|Insetto|
|CELLSJAVA-42873|Il foglio precondizionato presenta diversi sfondi di celle e testo mancante ed è nascosto.|Insetto|
|CELLSJAVA-42874|Perdita di colonne durante l'esportazione del file in HTML|Insetto|
|CELLSJAVA-42875|La larghezza è sbagliata e il display è fuori forma|Insetto|
|CELLSJAVA-42878|Il risultato del calcolo delle formule non è corretto|Insetto|
|CELLSJAVA-40419|Impossibile creare PDF con tag durante l'esportazione da Excel a PDF|Insetto|
|CELLSJAVA-40570|Conversione errata in PDF e JPG per pagine di dimensioni diverse|Insetto|
|CELLSJAVA-42833|Problema durante l'incorporamento dello stesso file PDF in più fogli in una cartella di lavoro|Insetto|
|CELLSJAVA-42858|Problema durante l'aggiunta di un'immagine alle celle unite utilizzando marcatori intelligenti con l'opzione Picture:FitToCell|Insetto|
|CELLSJAVA-42862|Il nome del foglio viene rinominato nelle formule dopo l'importazione CSV|Insetto|
|CELLSJAVA-42865|Ora errata letta da una cella nel file ODS|Insetto|
|CELLSJAVA-42879|Il file Excel viene danneggiato dopo il salvataggio da parte di Aspose.Cells|Insetto|
|CELLSJAVA-42860|java.lang.NullPointerException durante il caricamento di un formato di file ODS|Eccezione|
|CELLSJAVA-42871|java.lang.Exception: clone non supportato per il flusso di backup durante la conversione da XLSX a PDF|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge le API per il salvataggio del documento Markdown: SaveFormat.Markdown, FileFormatType.Markdown, MarkdownSaveOptions**
Supporta il salvataggio del contenuto delle celle come tabella markdown. Con il metodo Workbook.Save(), tutto il contenuto delle celle nel foglio attivo verrà esportato come tabella nel documento markdown.
### **Rimuove le proprietà obsolete di TxtLoadOptions**
Utilizzare la proprietà LoadStyleStrategy invece di KeepExactFormat.
### **Rimuove la classe obsoleta LoadDataOption**
Utilizzare invece la classe LoadFilter e la proprietà LoadOptions.LoadFilter.
### **Rimuove le proprietà obsolete di LoadOptions**
LoadOptions.ConvertNumericData: utilizzare questa proprietà con la sottoclasse corrispondente di LoadOptions, ad esempio TxtLoadOptions.
LoadOptions.LoadDataOptions: utilizzare la proprietà LoadOptions.LoadFilter con l'implementazione personalizzata di LoadFilter.
LoadOptions.LoadDataFilterOptions: utilizzare invece LoadOptions.LoadFilter.LoadDataFilterOptions.
LoadOptions.OnlyLoadDocumentProperties: utilizzare LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting/LoadDataOnly: utilizzare LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
### **Aggiunge la proprietà PdfSaveOptions.ExportDocumentStructure**
Ottiene o imposta un valore che determina se esportare o meno la struttura del documento.
### **Aggiunge le classi dello spazio dei nomi Aspose.Cells.WebExtensions**
Rappresenta WebExtensions e WebExtensionTasks.
### **Aggiunge le proprietà WorksheetCollection.WebExtensions e WorksheetCollection.WebExtensionTaskPanes.**
Rappresenta tutte le WebExtensions e WebExtensionTasks.
### **Aggiunge la classe WebExtensionShape.**
Rappresenta la forma di WebExtension.
### **Aggiunge il metodo Cells.InsertCutCells().**
Inserisce celle tagliate.
### **Aggiunge il metodo Cells.SetViewColumnWidthPixel.**
Imposta la larghezza della vista della colonna.
### **Aggiunge le classi ThreadedCommentCollection e ThreadedComment.**
Rappresenta il commento con thread.
### **Aggiunge la proprietà WorksheetCollection.ThreadedCommentAuthors.**
Ottiene e imposta gli autori dei commenti in thread.
### **Aggiunge la proprietà Comment.ThreadedComments.**
Rappresenta i commenti in thread sul commento.
### **Aggiunge i metodi CommentCollection.AddThreadedComment() e CommentCollection.GetThreadedComments().**
Aggiunge e ottiene i commenti in thread.
### **Aggiunge la proprietà Chart.SubTitle.**
Ottiene il sottotitolo del grafico. Solo per file in formato ODS.

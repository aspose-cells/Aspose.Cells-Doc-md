---
title: Aspose.Cells per Android tramite Java 20.6 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-android-via-java-20-6-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 20.6.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43153|Visualizza la legenda del grafico a cascata in turco simile a MS Excel|Aumento|
|CELLSJAVA-43173|Quando il campo gruppo ha un valore nullo, il risultato di subtotalN perde il subtotale per il gruppo nullo|Aumento|
|CELLSJAVA-43186|Calcola il totale complessivo per ogni riga con colonna espansa|Aumento|
|CELLSJAVA-43191|Fornire un mezzo per gestire gli scenari quando si specificano tipi di carattere errati|Aumento|
|CELLSJAVA-43187|Eccezione durante il caricamento di file XLS "Microsoft Excel 5.0 / 95 Workbook"|Aumento|
|CELLSJAVA-43142|Rendering da Excel a HTML: alcune celle non sono allineate dopo la conversione|Insetto|
|CELLSJAVA-43155|Il testo ruotato viene impostato fuori dalla cella quando viene visualizzato come HTML|Insetto|
|CELLSJAVA-43161|Rappresentazione errata dell'equazione|Insetto|
|CELLSJAVA-43130|Problema di trasparenza del grafico a cascata|Insetto|
|CELLSJAVA-43131|Da Excel a PDF: forme con testo non convertito correttamente|Insetto|
|CELLSJAVA-43133|Chart.toImage non include etichette di dati nell'immagine di output|Insetto|
|CELLSJAVA-43138|Immagine generata con problemi di rendering.|Insetto|
|CELLSJAVA-43151|Modifica dello stile dopo la conversione del file XLS|Insetto|
|CELLSJAVA-43162|Rendering da Excel a HTML: il processo di conversione richiede molto tempo|Insetto|
|CELLSJAVA-43164|Conversione da HTML a Excel che non conserva i formati RTF nell'output|Insetto|
|CELLSJAVA-43166|Il testo ruotato non viene visualizzato correttamente nella conversione da XLSX a HTML|Insetto|
|CELLSJAVA-43178|Le formattazioni RichText vengono perse durante l'esportazione del file in HTML|Insetto|
|CELLSJAVA-43165|Stringa "20TT1" sostituita con il numero 43850 durante la conversione da CSV a XLSB|Insetto|
|CELLSJAVA-43026|Dopo aver eseguito il rendering del grafico in un'immagine, le etichette dati cambiano lo stile e i valori non sono gli stessi|Insetto|
|CELLSJAVA-43154|Alcuni punti del grafico si sovrappongono per etichetta|Insetto|
|CELLSJAVA-43089|Il grafico radar è capovolto e i valori degli assi non sono identici al grafico originale nella conversione da XLS a PDF|Insetto|
|CELLSJAVA-43171|Il documento è rotto dopo aver copiato i fogli|Insetto|
|CELLSJAVA-43172|Un problema con i marcatori intelligenti nelle celle unite|Insetto|
|CELLSJAVA-43180|Conversione da HTML a Excel creando un foglio di lavoro nero|Insetto|
|CELLSJAVA-43181|C'è una differenza nell'altezza della riga nella conversione di Excel in HTML|Insetto|
|CELLSJAVA-43188|Lo stile del colore di sfondo non viene mantenuto durante la conversione da HTML a Excel|Insetto|
|CELLSJAVA-43196|Esiste un numero diverso di moduli VBA rilevati utilizzando Aspose.Cells for Java 20.4 e 20.5|Insetto|
|CELLSJAVA-43202|Le risorse non vengono rilasciate al completamento della creazione della cartella di lavoro|Insetto|
|CELLSJAVA-43203|Impossibile elaborare alcuni elenchi di convalida di Excel basati sugli intervalli denominati con nomi Unicode|Insetto|
|CELLSJAVA-43185|La qualità JPEG è sempre 75 su setImageResample su Linux|Insetto|
|CELLSJAVA-43192|Carica la cartella dei font /Sistema/Libreria/Fonts su macOS per impostazione predefinita|Insetto|
|CELLSJAVA-43157|Il colore delle serie di dati personalizzate non viene mantenuto durante la creazione di un grafico a cascata|Insetto|
|CELLSJAVA-43175|Un problema con il nome della serie di grafici quando si fa riferimento alla cartella di lavoro ad altre cartelle di lavoro|Insetto|
|CELLSJAVA-43158|IllegalArgumentException: Map size(0) deve essere >= 1|Eccezione|
|CELLSJAVA-43149|Eccezione sollevata durante il salvataggio di XLSM dopo la rimozione del foglio di lavoro|Eccezione|
|CELLSJAVA-43150|Eccezione "java.lang.NumberFormatException" al caricamento del file|Eccezione|
|CELLSJAVA-43183|Eccezione "ClassCastException: ...." durante il calcolo della tabella pivot|Eccezione|
|CELLSJAVA-43177|La nuova cartella di lavoro con file CSV restituisce "java.lang.IndexOutOfBoundsException: millisecond"|Eccezione|
|CELLSJAVA-43168|Eccezione "IllegalStateException: questo non è un file di archiviazione strutturato" durante l'unione di file Excel|Eccezione|
|CELLSJAVA-43179|Eccezione NumberFormatException: per la stringa di input: "preserve"|Eccezione|
|CELLSJAVA-43182|Eccezione "lang.IllegalStateException: codifica non valida: null" durante il caricamento del file XLS|Eccezione|
|CELLSJAVA-43201|Eccezione "java.util.EmptyStackException" al salvataggio in HTML|Eccezione|
|CELLSJAVA-43204|NegativeArraySizeException si verifica quando si utilizza Cell.getDisplayStringValue()|Eccezione|
|CELLSJAVA-43189|Eccezione sollevata durante il caricamento del file XLS|Eccezione|
|CELLSJAVA-43193|NullPointerException si è verificata durante il caricamento di alcuni file XLSX|Eccezione|
|CELLSJAVA-43200|Eccezione "java.lang.ArrayIndexOutOfBoundsException" al caricamento del file|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.
### **Aggiunge la proprietà ChartTextFrame.DirectionType.**
Ottiene e imposta la direzione del testo nel grafico.
### **Aggiunge ChartTextFrame.ReadingOrder e rende obsoleta la proprietà ChartTextFrame.TextDirection.**
Usare invece la proprietà ChartTextFrame.ReadingOrder.
### **Aggiunge classi per le funzionalità avanzate di Revisioni.**
Ottiene le informazioni sulla revisione.
### **Modifica il valore predefinito della proprietà TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
Per rendere il comportamento predefinito del salvataggio di CSV lo stesso con ms excel, abbiamo modificato il valore predefinito e il comportamento di questa proprietà. Per le vecchie versioni, il suo valore predefinito era "**falso**". Da 20.4, il suo valore predefinito diventa "**VERO**".
### **Modifica il comportamento per il rilevamento di righe/colonne vuote per il salvataggio di CSV.**
Per le vecchie versioni, abbiamo preso quelle righe/colonne che non hanno dati ma hanno impostazioni personalizzate (visibilità, formattazione, ... ecc.) come vuote. Dalla 20.4 non li prendiamo più come vuoti, il nuovo comportamento è lo stesso con ms excel.
### **Aggiunge la proprietà TxtSaveOptions.ExportArea.**
Specifica l'intervallo di dati delle celle da esportare. Gli utenti possono utilizzare questa opzione per ottenere lo stesso risultato con le versioni precedenti per il comportamento modificato di TxtSaveOptions.TrimLeadingBlankRowAndColumn e righe/colonne vuote.
### **Aggiunge la classe UnionRange.**
Rappresenta l'intervallo di unione.
### **Elimina la proprietà DrawObject.Image obsoleta.**
Usare invece la proprietà DrawObject.ImageBytes.
### **Aggiunge la proprietà Bullet.FontName**
Ottiene e imposta il nome del carattere del punto elenco.
### **Aggiunge il metodo WorksheetCollection.CreateUnionRange().**
Crea un intervallo di unione.
### **Elimina l'enumerazione SaveType obsoleta.**
È inutilizzato.
### **Elimina le proprietà OleObject.ImageFormat e Pictuer.ImageFormat obsolete.**
Usare invece le proprietà OleObject.ImageType e Picture.ImageType.
### **Aggiunge il metodo WorkbookSettings.GetThemeFont().**
Ottiene il carattere del tema.
### **Aggiunge la proprietà DataLabels.LinkedSource.**
Ottiene e imposta l'origine collegata.
### **Aggiunge l'enumerazione DefaultEditLanguage.**
Rappresenta la lingua di modifica predefinita.
### **Aggiunge la proprietà ImageOrPrintOptions.DefaultEditLanguage.**
Ottiene o imposta la lingua di modifica predefinita.
Può visualizzare/renderizzare diversi layout per i paragrafi di testo quando sono impostate diverse lingue di modifica.
### **Aggiunge la proprietà PdfSaveOptions.DefaultEditLanguage.**
Ottiene o imposta la lingua di modifica predefinita.
Può visualizzare/renderizzare diversi layout per i paragrafi di testo quando sono impostate diverse lingue di modifica.
### **Aggiunge il metodo ReferredArea.GetValues(boolcalculateFormulas)/GetValue(introwOffset, int colOffset, boolcalculateFormulas).**
Offre all'utente la possibilità di controllare se le formule devono essere calcolate in modo ricorsivo nell'implementazione di AbstractCalculationEngine.
### **Aggiunge l'enumerazione WarningType.InvalidFontName e WarningType.InvalidTextOfDefinedName.**
Rappresenta il tipo di avviso.
### **Aggiunge le proprietà WarningInfo.CorrectedObject e WarningInfo.ErrorObject.**
Rappresenta i dati errati e i dati aggiornati quando viene generato un avviso.
### **Aggiunge le proprietà WorkbookDesigner.RepeatFormulasWithSubtotal.**
Indica se si ripetono formule con righe di totale parziale.
### **Aggiunge la proprietà PlotArea.IsAutomaticSize.**
Indica se la dimensione dell'area del tracciato è automatica.
### **Elimina la proprietà Style.Rotation obsoleta.**
Utilizzare invece la proprietà Style.RotationAngle.
### **Aggiunge il metodo Gridweb.SetFontFolder(string fontFolder, bool recursive)/SetFontFolders(string[] fontFolders, bool recursive).**
Imposta la cartella/le cartelle dei font

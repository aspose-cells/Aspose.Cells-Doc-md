---
title: Aspose.Cells for Android via Java 9.0.0 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-android-via-java-9-0-0-release-notes/
---
|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41925|Il tempo di calcolo è aumentato con le recenti revisioni dell'API|Nuova caratteristica|
|CELLSJAVA-40958|È necessario un meccanismo di sostituzione dei caratteri configurabile dall'utente|Nuova caratteristica|
|CELLSJAVA-41925|Il tempo di calcolo è aumentato con le recenti revisioni dell'API|Nuova caratteristica|
|CELLSJAVA-41947|Capacità di rilevare se un DataPoint è in torta o barra|Nuova caratteristica|
|CELLSJAVA-41936|Il metodo Workbook.calculateFormula() non termina mai per il file Excel di origine|Aumento|
|CELLSJAVA-41827|Il foglio di calcolo impiega più di 3 minuti per calcolare le formule con il metodo Workbook.calculateFormula()|Aumento|
|CELLSJAVA-41928|Impossibile rilevare la risorsa immagine durante il rendering del foglio di calcolo in HTML con IStreamProvider|Insetto|
|CELLSJAVA-41841|Problema con il rendering delle caselle di controllo in HTML|Insetto|
|CELLSJAVA-41932|Problema con getDisplayStringValue() per i valori formattati Data|Insetto|
|CELLSJAVA-41930|Utilizzando le API Light Cells per elaborare un file XLS, la prima cella del primo foglio viene sempre elaborata|Insetto|
|CELLSJAVA-41931|Spaziatura e interruzione dei caratteri non corrette per il testo verticale durante il rendering del foglio di calcolo in PDF|Insetto|
|CELLSJAVA-41709|Le larghezze delle colonne sono diverse su CentOS rispetto a Windows|Insetto|
|CELLSJAVA-41933|La scala del grafico è stata spostata durante il rendering del foglio di calcolo in PDF|Insetto|
|CELLSJAVA-41934|Problema di allineamento durante il rendering di un file Excel in PDF|Insetto|
|CELLSJAVA-41935|La formattazione delle voci della legenda è disturbata durante il rendering del foglio di calcolo in PDF|Insetto|
|CELLSJAVA-41943|Le etichette dell'asse orizzontale non sono state renderizzate completamente, cioè; a tutte le etichette mancano alcuni contenuti nell'immagine renderizzata.|Insetto|
|CELLSJAVA-41940|Il file è danneggiato dopo il calcolo della formula e il salvataggio|Insetto|
|CELLSJAVA-41952|Il risultato del calcolo non è corretto|Insetto|
|CELLSJAVA-41941|La formula di matrice non viene calcolata correttamente|Insetto|
|CELLSJAVA-41937|Alcuni valori del file Excel mancano nell'output HTML - Conversione da XLS a HTML|Insetto|
|CELLSJAVA-41969|Manca l'ombreggiatura Cell durante la conversione da HTML a XLSX|Insetto|
|CELLSJAVA-41955|La cartella di lavoro in HTML mostra '#' nelle celle|Insetto|
|CELLSJAVA-41942|Bordi mancanti, ombreggiatura delle celle e immagini: rendering da HTML a Excel|Insetto|
|CELLSJAVA-41967|Cells mancante nel PDF quando sono definite più aree di stampa in un unico foglio|Insetto|
|CELLSJAVA-41958|La legenda del lato destro viene troncata nell'immagine del grafico|Insetto|
|CELLSJAVA-41953|Testo fuori posto nel diagramma dopo la conversione in formato HTML|Insetto|
|CELLSJAVA-41948|Il grafico viene modificato durante la conversione del foglio di calcolo in HTML|Insetto|
|CELLSJAVA-41981|Posizione errata della linea verticale nel PDF del grafico|Insetto|
|CELLSJAVA-41964|L'adattamento automatico non considera il livello di rientro|Insetto|
|CELLSJAVA-40260|Modifica del testo di una WordArt esistente in un file Excel|Insetto|
|CELLSJAVA-41927|Eccezione: "java.lang.OutOfMemoryError" durante il salvataggio nel formato di file HTML|Eccezione|
|CELLSJAVA-41945|CellsException: errore nel calcolo di Cell[0Sheet1!E5] in Workbook.calculateFormula durante il calcolo della funzione TREND|Eccezione|
|CELLSJAVA-41946|L'apertura del file Excel causa java.lang.NumberFormatException: per la stringa di input: "80000020"|Eccezione|
|CELLSJAVA-41922|IndexOutOfBoundsException durante la copia delle celle|Eccezione|
|CELLSJAVA-41971|Cell.getValidationValue() genera NullPointerException per il tipo di convalida personalizzato|Eccezione|
|CELLSJAVA-41963|Si verifica un'eccezione di dimensione della chiave illegale durante l'apertura della sorgente a5.xlsx|Eccezione|
|CELLSJAVA-41962|L'eccezione ArrayIndexOutOfBoundsException si verifica durante l'apertura dell'origine a4.xls|Eccezione|
|CELLSJAVA-41961|Stringa non valida nell'eccezione del file si verifica durante l'apertura del sorgente a3.xls|Eccezione|
|CELLSJAVA-41960|L'eccezione NegativeArraySizeException si verifica durante l'apertura dell'origine a2.xls|Eccezione|
|CELLSJAVA-41959|L'eccezione NullPointerException si verifica durante l'apertura dell'origine a1.xlsx|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà CopyOptions.ReferToDestinationSheet e il metodo Cells.CopyRows(Cells sourceCells, int sourceRowIndex, int destinationRowIndex, int rowNumber, CopyOptions copyOptions)**
Quando si copia l'intervallo e il grafico fa riferimento al foglio di origine, False significa che l'origine dati del grafico copiato non verrà modificata. True significa che l'origine dati del grafico copiato fa riferimento al foglio di destinazione.
### **Aggiunge la proprietà HtmlSaveOptions.FilePathProvider**
Ottiene o imposta IFilePathProvider per l'esportazione separata di Worksheet in HTML.
### **Aggiunge l'interfaccia IFilePathProvider**
Rappresenta il provider del percorso del file esportato.
### **Aggiunge la classe FontConfigs**
Specifica le impostazioni dei caratteri.
### **Aggiunge la classe FontSourceBase**
Questa è una classe base astratta per le classi che consentono all'utente di specificare varie fonti di font.
### **Aggiunge la classe FileFontSource**
Rappresenta il singolo file di carattere TrueType archiviato nel file system.
### **Aggiunge la classe FolderFontSource**
Rappresenta la cartella che contiene i file dei caratteri TrueType.
### **Aggiunge la classe MemoryFontSource**
Rappresenta il singolo file di font TrueType archiviato in memoria.
### **Aggiunge l'enumerazione FontSourceType**
Specifica il tipo di un'origine font.
### **Aggiunge la proprietà CalculationOptions.Recursive**
Specifica se calcolare le celle dipendenti in modo ricorsivo durante il calcolo di una cella e dipende da altre celle.
### **Proprietà CellsHelper.FontDir obsoleta**
Utilizzare invece il metodo FontConfigs.SetFontFolder(string, bool) con la cartella ricorsiva su false.
### **Proprietà CellsHelper.FontDirs obsoleta**
Utilizzare invece il metodo FontConfigs.SetFontFolders(string[], bool) con la cartella ricorsiva su false.
### **Proprietà CellsHelper.FontFiles obsoleta**
Usare invece FontConfigs.SetFontSources(FontSourceBase[]).
### **Rende obsoleta la proprietà Shape.LineFormat e aggiunge la proprietà Shape.Line**
Utilizzare invece la proprietà Shape.Line.
### **Rende obsoleta la proprietà Shape.FillFormat e aggiunge la proprietà Shape.Fill**
Utilizzare invece la proprietà Shape.Fill.
### **Obsolete la classe ShapeFormat e la proprietà Shape.Format**
Utilizzare direttamente le proprietà Shape.Fill e Shape.Line.
### **Obsoleta la classe ShapeFont e aggiunta la classe TextOptions**
Utilizzare invece la classe TextOptions.
### **Aggiunge le proprietà TextOptions.Fill, TextOptions.Outline e TextOptions.Shadow**
Rappresenta il riempimento, il contorno e l'ombreggiatura del testo.
### **Rende obsoleta la proprietà FontSetting.ShapeFont e aggiunge la proprietà FontSetting.TextOptions**
Utilizzare invece la proprietà FontSetting.TextOptions.
### **Aggiunge la proprietà Shape.TextOptions.**
Rappresenta le opzioni di testo della forma.
### **Metodo Worksheet.SetBackground obsoleto.**
Utilizzare invece la proprietà Worksheet.BackgroundImage.
### **LineShape.BeginArrowheadStyle e ArcShape.BeginArrowheadStyle obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadStyle.
### **LineShape.BeginArrowheadWidth e ArcShape.BeginArrowheadWidth obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadWidth.
### **LineShape.BeginArrowheadLength e ArcShape.BeginArrowheadLength obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadLength.
### **LineShape.EndArrowheadStyle e ArcShape.EndArrowheadStyle obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadStyle.
### **LineShape.EndArrowheadWidth e ArcShape.EndArrowheadWidth obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadWidth.
### **LineShape.EndArrowheadLength e ArcShape.EndArrowheadLength obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadLength.
### **Elimina il metodo Worksheet.CopyConditionalFormatting() obsoleto.**
### **Elimina il metodo Workbook.CheckWriteProtectedPassword() obsoleto.**
Utilizzare invece il metodo WorkbookSettings.WriteProtection.ValidatePassword.
### **Rinomina Workbook.RemoveDigitallySign come metodo Workbook.RemoveDigitalSignature.**
### **Il metodo Obsoletes WorksheetCollection.ClearPivots aggiunge il metodo WorksheetCollection.ClearPivottables.**
Utilizzare il metodo WorksheetCollection.ClearPivottables.
### **Aggiunge la proprietà ChartSplitType.Auto.**
Rappresenta i punti dati che devono essere divisi utilizzando il meccanismo predefinito per questo tipo di grafico.
### **Aggiunge la proprietà ChartPoint.IsInSecondaryPlot.**
Ottiene o imposta un valore che indica se questi punti dati si trovano nella seconda torta o barra di un grafico a torta o a barre del grafico a torta.
### **Aggiunge la proprietà OleObject.ClassIdentifier.**
Ottiene o imposta l'identificatore di classe dell'oggetto incorporato.

{{% alert color="primary" %}} 

Since the code base of Aspose.Cells for Android matches the code of relevant .NET and Java version, most of the changes, enhancements and fixes included in the Aspose.Cells for .NET v8.9.1, Aspose.Cells for .NET v8.9.2, Aspose.Cells for .NET v9.0.0, Aspose.Cells for Java v8 .9.1, Aspose.Cells for Java v8.9.2 e Aspose.Cells for Java v9.0.0 sono inclusi anche in questo Aspose.Cells for Android v9.0.0.

{{% /alert %}}

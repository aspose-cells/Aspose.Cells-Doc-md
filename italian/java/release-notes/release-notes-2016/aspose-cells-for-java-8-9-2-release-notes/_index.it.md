---
title: Aspose.Cells for Java 8.9.2 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-8-9-2-release-notes/
---
## **1) Aspose.Cells**

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41925|Il tempo di calcolo è aumentato con le recenti revisioni API|Nuova caratteristica|
|CELLSJAVA-40958|È necessario un meccanismo di sostituzione dei caratteri configurabile dall'utente|Nuova caratteristica|
|CELLSJAVA-41936|Il metodo Workbook.calculateFormula() non termina mai per il file Excel di origine|Aumento|
|CELLSJAVA-41928|Impossibile rilevare la risorsa immagine durante il rendering del foglio di calcolo in HTML con IStreamProvider|Insetto|
|CELLSJAVA-41841|Problema con il rendering di CheckBox in HTML|Insetto|
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
|CELLSJAVA-41941|La formula matrice non viene calcolata correttamente|Insetto|
|CELLSJAVA-41937|Alcuni valori del file Excel mancano nell'output HTML - Conversione da XLS a HTML|Insetto|
|CELLSJAVA-41927|Eccezione: "java.lang.OutOfMemoryError" durante il salvataggio nel formato di file HTML|Eccezione|
|CELLSJAVA-41945|CellsException: errore nel calcolo di Cell[0Sheet1!E5]in Workbook.CalculateFormula durante il calcolo della funzione TREND|Eccezione|
|CELLSJAVA-41946|L'apertura del file excel provoca java.lang.NumberFormatException: per la stringa di input: "80000020"|Eccezione|
|CELLSJAVA-41922|IndexOutOfBoundsException durante la copia delle celle|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà CopyOptions.ReferToDestinationSheet e il metodo Cells.CopyRows(Cells sourceCells, int sourceRowIndex, int destinationRowIndex, int rowNumber, CopyOptions copyOptions)**
Specifica se fare riferimento al foglio di lavoro di destinazione (come origine dati per il grafico) durante la copia di righe/intervallo.
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

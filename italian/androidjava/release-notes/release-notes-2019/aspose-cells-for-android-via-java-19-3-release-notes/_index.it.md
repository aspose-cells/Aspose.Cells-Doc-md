---
title: Aspose.Cells for Android via Java 19.3 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-android-via-java-19-3-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 19.3.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41026|Supporta Excel 95/5.0 (file XLS)|Nuova caratteristica|
|CELLSJAVA-42827|Inserisci riga con InsertOptions simile a MS Excel|Nuova caratteristica|
|CELLSJAVA-42845|Mantieni i separatori per le righe vuote durante l'esportazione di un file XLS in CSV|Nuova caratteristica|
|CELLSJAVA-42778|Eccezione "style textRotation deve essere compreso tra 0 e 180" durante il caricamento di XLSM|Aumento|
|CELLSJAVA-42712|Migliora JavaDocs per Aspose.Cells for Java|Aumento|
|CELLSJAVA-42823|L'utilizzo di FontUnderlineType.WORDS genera un'eccezione|Aumento|
|CELLSJAVA-42846|I risultati dell'estrazione del testo sono diversi|Aumento|
|CELLSANDROID-85|Problemi nella conversione da foglio a immagine con immagini trasparenti sopra altre immagini|Insetto|
|CELLSJAVA-42290|Mdashes e ndash inseriti in TextBox nei grafici non vengono visualizzati correttamente nel grafico PDF|Insetto|
|CELLSJAVA-42750|Impossibile recuperare gli elementi dei campi della pagina nel rapporto di tabella pivot|Insetto|
|CELLSJAVA-42783|Problema con il testo barrato nel formato file HTML generato|Insetto|
|CELLSJAVA-42784|I dati in alcune celle (ad es. G7, H7, ecc.) non vengono visualizzati allo stesso modo del file originale in Excel in HTML/conversione immagine|Insetto|
|CELLSJAVA-42797|Alcuni stili non vengono visualizzati nell'input HTML|Insetto|
|CELLSJAVA-42807|Il calcolo della formula/funzione "ISOWEEKNUM" non è lo stesso di MS Excel|Insetto|
|CELLSJAVA-42794|Da ODS a XLSX - Il colore del testo è cambiato|Insetto|
|CELLSJAVA-42795|Da ODS a XLSX - Carattere barrato non conservato correttamente|Insetto|
|CELLSJAVA-42796|Da ODS a XLSX - Le dimensioni della casella di testo sono state modificate|Insetto|
|CELLSJAVA-42798|ODS -> XLSX - Il collegamento ipertestuale è funzionale ma mostrato come testo normale|Insetto|
|CELLSJAVA-42802|Da ODS a XLSX, le percentuali vengono perse nel grafico a barre|Insetto|
|CELLSJAVA-42803|Contorno "SummaryRowBelow" non influenzato durante il salvataggio nel formato file XLSB|Insetto|
|CELLSJAVA-42826|Dati con formattazione condizionale omessi durante la conversione da XLSX a HTML|Insetto|
|CELLSJAVA-42815|L'aggiunta di un riferimento complesso a un nome definito risulta in una cartella di lavoro MS Excel corrotta|Insetto|
|CELLSJAVA-42822|Cell.getValidationValue restituisce un valore errato per il valore specificato|Insetto|
|CELLSJAVA-42829|Nome della funzione personalizzata all'interno delle formule condivise sostituito da un altro nome|Insetto|
|CELLSJAVA-42824|Titoli degli assi mancanti e altra formattazione è errata dei grafici nella conversione da Excel a PDF/A|Insetto|
|CELLSJAVA-42814|Le frecce nell'output PNG non corrispondono alle frecce nel grafico di Excel|Insetto|
|CELLSJAVA-42777|Modifica dell'altezza delle righe errata durante l'utilizzo dell'operazione di adattamento automatico delle righe|Insetto|
|CELLSJAVA-42813|L'impostazione della cartella di lavoro "ReCalculateOnOpen" non è stata mantenuta|Insetto|
|CELLSJAVA-42816|Visualizzazione incompleta per AutoFitterOptions.setAutoFitMergedCells(true)|Insetto|
|CELLSJAVA-42817|Il colore di sfondo delle caselle di testo viene modificato in modo imprevisto|Insetto|
|CELLSJAVA-42821|Quando si elimina la prima riga di un intervallo, l'intervallo viene aggiornato in modo errato|Insetto|
|CELLSJAVA-42828|Quando si utilizza Cell.setHtmlString viene aggiunta una nuova riga alla fine del testo|Insetto|
|CELLSJAVA-42844|Il testo non è correttamente allineato nell'output PDF|Insetto|
|CELLSJAVA-42834|Cambia il colore del testo nero in rosso|Insetto|
|CELLSJAVA-42839|Il grafico a dispersione non viene visualizzato nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-42840|Le etichette dell'asse orizzontale non vengono visualizzate correttamente per i grafici in Excel fino al rendering PDF|Insetto|
|CELLSJAVA-42842|Il grafico a bolle 2D non viene visualizzato nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-42833|Problema durante l'incorporamento dello stesso file PDF in più fogli in una cartella di lavoro|Insetto|
|CELLSJAVA-42836|Workbook.hasExernalLinks() non restituisce true per i collegamenti DDE|Insetto|
|CELLSJAVA-42848|Impostazione dei caratteri e altri oggetti non copiati utilizzando la funzione Range.copy()|Insetto|
|CELLSJAVA-42757|CellsException durante la conversione dei file|Eccezione|
|CELLSJAVA-42799|Eccezione "java.lang.ArrayIndexOutOfBoundsException: -32768" durante il caricamento di un formato di file XLSX|Eccezione|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException durante il caricamento di una cartella di lavoro|Eccezione|
|CELLSJAVA-42820|Eccezione "Valore stringa IMEModeType non valido" durante il caricamento di un formato di file XLSX|Eccezione|
|CELLSJAVA-42849|Eccezione IndexOutOfBoundsException durante la conversione da XLSX a HTML|Eccezione|
|CELLSJAVA-42831|Eccezione sollevata da Excel dopo l'applicazione dello stile all'intervallo di celle di intestazione|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo sul forum di supporto Aspose.Cells.

**Aggiunge il metodo PivotTable.ShowReportFilterPageByName(string fieldName).**

Mostra tutte le pagine del filtro del report in base al nome del PivotField, il PivotField deve trovarsi nei PageField.
### **Aggiunge il metodo PivotTable.ShowReportFilterPageByIndex(int posIndex).**
Mostra tutte le pagine del filtro del report in base all'indice di posizione nei PageField.
### **Aggiunge il metodo PivotTable.ShowReportFilterPage(PivotField pageField).**
Mostra tutte le pagine del filtro del report in base a PivotField, il PivotField deve trovarsi nei PageField.
### **Aggiunge la classe DataSorterKey e DataSorterKeyCollection**
Rappresenta la chiave dell'ordinatore di dati.
### **Aggiunge il metodo DataSorter.AddKey(Int32,SortOnType,SortOrder,Object)**
Aggiunge la chiave di ordinamento come il colore di sfondo della cella, il colore del carattere.
### **Aggiunge la proprietà Aspose.Cells.DataSorter.Keys**
Ottiene tutte le chiavi dell'ordinatore dati.
### **Aggiunge l'enumerazione SortOnType**
Rappresenta il tipo di dati ordinati.
### **Aggiunge la classe ODSLoadOptions**
Rappresenta le opzioni di caricamento del file ODS.
### **Aggiunge la proprietà HTMLLoadOptions.ProgId**
Ottiene l'ID del programma di creazione del file. utilizzato solo per i file MHT.
### **Aggiunge la proprietà PdfSaveOptions.TextCrossType**
Ottiene o imposta la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
### **Aggiunge la classe enum TextCrossType**
Enumera la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
### **Aggiunge i metodi WorksheetCollection.RegisterAddInFunction()**
Sostituzione di Cell.SetAddInFormula(), un modo più conveniente ed efficiente per gli utenti di aggiungere e utilizzare funzioni aggiuntive.
### **Metodo Cell.SetAddInFormula() obsoleto**
Si prega di registrare le funzioni addin in primo luogo da WorksheetCollection.RegisterAddInFunction() e quindi impostare la formula per Cell da Cell.Formula/Cell.SetFormula() invece.
### **Aggiunge la proprietà Cells.CountLarge**
Dal punto di vista funzionale è uguale alla proprietà Count, ad eccezione del fatto che la proprietà Count può generare un errore di overflow quando sono presenti troppe istanze di oggetti Cell.
### **Aggiunge il metodo Hyperlink.Delete()**
Elimina questo collegamento ipertestuale.
### **Aggiunge la proprietà Range.Hyperlinks**
Ottiene tutti i collegamenti ipertestuali nell'intervallo.
### **Aggiunge enum CopyFormatType**
Rappresenta il tipo di formato di copia durante l'inserimento delle righe.
### **Aggiunge la classe InsertOptions e il metodo Cells.InsertRows(int, int , InsertOptions)**
Inserimento di righe con alcune opzioni.
### **Aggiunge i metodi FileFormatUtil.DetectFileFormat(Stream,String) e FileFormatUtil.DetectFileFormat(String,String)**
Rileva il formato file del file OOXML crittografato.
### **Aggiunge le proprietà ListObject.AlternativeDescription e ListObject.AlternativeText**
Ottiene e imposta il testo alternativo e la descrizione della tabella.
### **Aggiunge la proprietà Line.ThemeColor**
Ottiene e imposta il colore del tema della linea.
### **Aggiunge la classe Mode3d e MsoModel3dFormat**
Incapsula l'oggetto che rappresenta un singolo modello 3D in un foglio di calcolo.
### **Aggiunge l'enumerazione ImageType.Gltf**
Rappresenta il tipo di modello 3D.
### **Modifiche per il carattere predefinito del file modello XLS caricato**
Nelle versioni precedenti, non supportavamo l'applicazione del carattere definito nel tema (funzionalità avanzata in MS Excel 2007 e versioni successive) in base alla regione durante il caricamento dei file modello XLS. Su richiesta di alcuni utenti, lo abbiamo supportato dalla v19.3. Se la regione è stata specificata nel file modello XLS, applicheremo il carattere definito nel tema in base al valore della regione specificato salvato. Altrimenti applicheremo il carattere definito nel tema in base alle impostazioni regionali dell'ambiente dell'applicazione. Ciò causerà la modifica del carattere predefinito della cartella di lavoro (caricato dal file modello XLS che ha specificato i dati del tema) e quindi influenzerà altre funzionalità, come la larghezza della colonna, la dimensione della forma, l'effetto di rendering, ... ecc.
### **Aggiunge il metodo Name.GetReferredAreas(bool recalculate).**
Fornisce i riferimenti a cui fa riferimento il nome definito come metodo GetRanges(bool recalculate). Ma i riferimenti restituiti sono rappresentati dall'oggetto ReferredArea che fornisce funzionalità più ricche, inclusi collegamenti esterni.
### **Aggiunge la proprietà TxtSaveOptions.KeepSeparatorsForBlankRow**
Indica se i separatori devono essere emessi per la riga vuota. Il valore predefinito è false, il che significa che il contenuto della riga vuota sarà vuoto.
### **Aggiunge enum AutoFitMergedCellsType**
Rappresenta il tipo di celle unite con adattamento automatico.
### **Obsoleta la proprietà AutoFitterOptions.AutoFitMergedCells e aggiunge la proprietà AutoFitterOptions.AutoFitMergedCellsType**
Ottiene e imposta il tipo di altezza della riga di adattamento automatico.
### **Aggiunge le classi JSONUtility e JsonLayoutOptions**
È usato per importare file json.
### **Aggiunge la classe TableToRangeOptions e il metodo ListObject.ConvertToRange(TableToRangeOptions options)**
Converte la tabella in un intervallo con opzioni.

{{% alert color="primary" %}} 

Since the code base of Aspose.Cells for Android via Java matches the code of relevant .NET and Java version(s), most of the changes, enhancements and fixes included in the Aspose.Cells for .NET v19.1, Aspose.Cells for .NET v19.2, Aspose.Cells for .NET v19.3, Aspose.Cells for Java v19.1, Aspose.Cells for Java v19.2 e Aspose.Cells for Java v19.3 sono inclusi anche in questo Aspose.Cells for Android via Java v19.3.

{{% /alert %}}

---
title: Aspose.Cells for Android via Java 21.6 Note di rilascio
type: docs
weight: 7
url: /it/java/aspose-cells-for-android-via-java-21-6-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 21.6.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43396|La conversione di un foglio Excel in un file di testo rimuove le virgolette dall'inizio|
|CELLSJAVA-43386|L'ordinamento non funziona quando i dati contengono caratteri non alfanumerici|
|CELLSJAVA-43452|Il calendario giapponese che utilizza una funzione di Excel non viene letto correttamente|
|CELLSJAVA-43466|CellsException: errore per ZipFile durante l'importazione di ods|
|CELLSJAVA-43403|Posizionamento del testo spostato a sinistra durante il salvataggio come HTML|
|CELLSJAVA-43421|caratteri di escape e di interruzione di riga non vengono visualizzati correttamente durante la conversione di HTML in Excel|
|CELLSJAVA-43427|Il formato condizionale con le barre dei dati mostra i valori nell'esportazione HTML|
|CELLSJAVA-43428| Il formato contabile combinato con il carattere a 6 punti distorce i numeri in HTML|
|CELLSJAVA-43429|Il testo con allineamento verticale del testo scompare in HTML|
|CELLSJAVA-43407|Le formule di Excel vengono saltate/modificate dopo il salvataggio del file|
|CELLSJAVA-43419| Formato numerico personalizzato non visualizzato correttamente in PDF|
|CELLSJAVA-43374|Etichette del grafico ripetute durante la conversione dei file Excel allegati in PDF|
|CELLSJAVA-43409| Le etichette dei dati imprevisti sono apparse nell'immagine di output del grafico|
|CELLSJAVA-43411|Gli avvisi di sostituzione dei caratteri non funzionano nella conversione da grafico a immagine|
|CELLSJAVA-43414|Problema di conversione da Xls a Pdf|
|CELLSJAVA-43425|Intestazione-Piè di pagina non disponibile nella prima pagina se esportato in Excel|
|CELLSJAVA-43433|L'immagine di riferimento non è renderizzata in PDF|
|CELLSJAVA-43434|La formula dinamica SmartMarker ha uno stile di cella in espansione errato|
|CELLSJAVA-43435| La formula dinamica degli indicatori intelligenti inserisce le celle in base alla colonna espansa a sinistra ma non in base alle colonne nella formula|
|CELLSJAVA-43450|Problema di aggiornamento della tabella pivot|
|CELLSJAVA-43444|Regressione: getLastSavedUniversalTime restituisce una data errata|
|CELLSJAVA-43446|Cells Eccezione modifiche alla traccia|
|CELLSJAVA-43448|Regressione: riferimento non valido per l'elenco|
|CELLSJAVA-43457|Ciclo infinito durante il salvataggio della cartella di lavoro copiata|
|CELLSJAVA-43442|Problema con l'ordinamento dei dati quando si fa clic sui collegamenti di intestazione nella demo primaverile di GridWeb|
|CELLSJAVA-43443|Problema con la modalità di modifica in GridWeb Java|
|CELLSJAVA-43455|I caratteri non sono incorporati in PDF per i caratteri non ASCII durante l'impostazione di EmbedStandardWindowsFonts su false|
|CELLSJAVA-43449|Impossibile cambiare la famiglia di caratteri degli elementi del grafico da "Calibri" ad "Aktiv Grotesk"|
|CELLSJAVA-43454|Le etichette dell'asse X sono tagliate|
|CELLSJAVA-43445|Regressione: dati di riga mancanti per i file .numbers|
|CELLSJAVA-43463|La sequenza temporale è interrotta dopo il salvataggio del file|
|CELLSJAVA-43464|PivotField.hideItem() non ha effetto nel file di output|
|CELLSJAVA-43470|Il testo dopo un tag "br" all'interno di un tag "th" viene troncato durante l'importazione di un documento HTML|
|CELLSJAVA-43481|Ottenere la formula sbagliata da una cella|
|CELLSJAVA-43490|Le proprietà del documento non possono essere estratte|
|CELLSJAVA-43491|Il valore della formula che utilizza la tabella dati non può essere estratto correttamente|
|CELLSJAVA-43498|Il risultato formattato del valore numerico non è corretto per la locale zh_CN|
|CELLSJAVA-43451|Il contenuto del file Excel viene visualizzato in modo errato e la demo di ChangeStyle (primavera) non funziona correttamente|
|CELLSJAVA-43484|Il layout del contenuto non è coerente nel rendering da Excel a PDF|
|CELLSJAVA-43465|Mancano poche serie di grafici durante la conversione di Excel in PDF|
|CELLSJAVA-43468|Problema con l'equazione della linea retta in Excel per il rendering PDF|
|CELLSJAVA-43432|Il contenuto del grafico non corrispondeva durante il nuovo salvataggio di un formato di file XLS|
|CELLSJAVA-43475|Regressione: le celle a capo rigato vengono tagliate|
|CELLSJAVA-43478|Regressione: NUMERI a PDF, molti dati mancanti|
|CELLSJAVA-43485|Regressione: contenuto extra durante il rendering PDF da ODS|
|CELLSJAVA-43492| La conversione di un file XML (SpreadsheetML) rimuove l'impostazione nascosta in "Definizione nome" nell'output XLS e XLSX|
|CELLSJAVA-43417|Eccezione sollevata durante l'apertura di XLSX da file di grandi dimensioni|
|CELLSJAVA-43431|java.lang.NullPointerException sollevata durante la chiamata a Cells.deleteColumn() con l'ultima versione 21.3 mentre funziona con 21.2|
|CELLSJAVA-43437|IndexOutOfBoundsException quando si fa clic su altre pagine del foglio in modalità di valutazione|
|CELLSJAVA-43459|NullPointerException in getFormulaLocal() con impostazioni di globalizzazione personalizzate|
|CELLSJAVA-43447| Si è verificata l'eccezione "java.lang.NullPointerException" durante l'utilizzo del file di stile personalizzato in GridWeb|
|CELLSJAVA-43439|NegativeArraySizeException si verifica al caricamento della cartella di lavoro|
|CELLSJAVA-43453|NullPointerException sul metodo Workbook.save|
|CELLSJAVA-43486|NullPointerException durante la conversione di un documento HTML in una cartella di lavoro|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo sul forum di supporto Aspose.Cells.

### **Aggiunge i metodi StartAccessCache()/CloseAccessCache() per la cartella di lavoro e il foglio di lavoro.**

Fornire agli utenti la possibilità di accedere ai dati in modalità batch con prestazioni migliori.

### **Aggiunge le proprietà TxtSaveOptions.ExportQuotePrefix e TxtLoadOptions.TreatQuotePrefixAsValue.**

Fornire agli utenti la possibilità di decidere come fare con le virgolette singole iniziali del valore della cella durante l'esportazione/importazione di file CSV/TSV.

### **Aggiunge i metodi GlobalizationSettings.GetCollationKey(string,bool) e Compare(string,string,bool).**

Fornisci agli utenti la possibilità di sovrascrivere le regole predefinite del confronto tra stringhe. Per alcune impostazioni locali o valori di stringa, la regola predefinita del confronto delle stringhe potrebbe non essere quella prevista (il risultato di alcune funzionalità, come il calcolo della formula, l'ordinamento, ecc., è diverso da quello che dovrebbe essere ottenuto in ms excel). In tal caso, l'utente può sovrascrivere tali metodi con la regola prevista (ad esempio, l'utente può utilizzare l'implementazione della libreria icu).

### **Aggiunge enum ImageType.WebP.**

Rappresenta l'immagine Weppy.

### **Aggiunge il metodo OleObject.SetEmbeddedObject().**

Per verificare se l'icona di aggiornamento automatico.

### **Aggiunge la proprietà WorkbookDesigner.LineByLine.**

Indica se elaborare i marcatori intelligenti riga per riga.

### **Aggiunge la proprietà HtmlSaveOptions.ExportCellCoordinate.**

Indica se esportare coordinate Excel di celle non vuote durante il salvataggio del file in html. Il valore predefinito è false. Se desideri importare l'output html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà AutoFitterOptions.DefaultEditLanguage.**

Ottiene o imposta la lingua di modifica predefinita.

### **Aggiunge il metodo Slicer.AddPivotConnection(PivotTable pivot).**

Aggiunge la connessione alla tabella pivot per l'affettatrice.

### **Aggiunge il metodo Slicer.RemovePivotConnection(PivotTable pivot).**

Rimuove la connessione PivotTable dell'affettatrice.

### **Aggiunge la proprietà TxtSaveOptions.ExportAllSheets.**

Indica se esportare tutti i fogli di lavoro nel file. Il valore dafaut è falso come MS Excel.

### **Aggiunge FileFormatType.Numbers09 enum.**

Rappresenta il formato file .numbers 09. E FileFormatType.Number rappresenterà il tipo di formato di file latest.numbers in un secondo momento.

### **Aggiunge il metodo WorkbookSettings.SetPageOrientationType().**

Imposta il tipo di orientamento della pagina di stampa per l'intero file.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisAutomatic obsoleta.**

Usare invece l'enumerazione DataBarAxisPosition.Automatic.

### **Elimina DataBarAxisPosition.DataBarAxisMidpointe num obsoleto.**

Usare invece l'enumerazione DataBarAxisPosition.Midpoint.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisNone obsoleta.**

Usare invece l'enumerazione DataBarAxisPosition.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderNone obsoleta.**

Usare invece l'enumerazione DataBarBorderType.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderSolid obsoleta.**

Usare invece l'enumerazione DataBarBorderType.Solid.

### **Elimina l'enumerazione DataBarFillType.DataBarFillGradient obsoleta.**

Usare invece l'enumerazione DataBarFillType.Gradient.

### **Elimina l'enumerazione DataBarFillType.DataBarFillSolid obsoleta.**

Usare invece l'enumerazione DataBarFillType.Solid.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarColor obsoleta.**

Usare invece l'enumerazione DataBarNegativeColorTypeColor.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarSameAsPositive obsoleta.**

Usare invece l'enumerazione DataBarNegativeColorType.SameAsPositive.

### **Elimina l'enumerazione OleObject.FileFormatType obsoleta.**

Usare invece l'enumerazione OleObject.FileFormatType.

### **Elimina l'enumerazione DynamicFilterType.Februray obsoleta.**

Utilizzare invece l'enumerazione DynamicFilterType.February.

### **Aggiunge il metodo GridCells.MoveRange().**

Sposta l'intervallo.

### **Aggiunge il metodo GridCells.InsertRange().**

Inserisce un intervallo con l'opzione di spostamento.

### **Aggiunge il metodo GridCells.DeleteRange().**

Elimina un intervallo con l'opzione di spostamento.

### **Modifica il comportamento della proprietà Cell.IsErrorValue.**

Nelle versioni precedenti, questa proprietà si applica solo alle celle della formula. Per renderlo coerente con altre proprietà, da 21.6 controlliamo anche le celle non formula e se il suo valore è un valore di errore, restituiamo anche true. L'utente può controllare prima la proprietà Cell.IsFormula se ha solo bisogno di controllare il valore di errore per le celle della formula.

### **Modifica il comportamento della proprietà Cell.Value.**

Nelle vecchie versioni, questa proprietà restituisce sempre l'oggetto DateTime se la cella è formattata come data ora e il suo valore è numerico. A partire da 21.6, questa proprietà restituisce il valore numerico stesso se supera il valore DateTime massimo valido. Con questa modifica l'oggetto restituito è coerente con quanto mostrato nella barra della formula di ms excel.

### **Aggiunge la proprietà Cell.IsNumericValue.**

Fornisce all'utente un modo comodo ed efficiente per verificare se il valore di una cella è un valore numerico (int, double, datetime).

### **Aggiunge metodi sovraccaricati di Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Supporto per impostare formule di matrice e formule condivise con valori predefiniti.

### **Aggiunge enum PdfFontEncoding.**

Rappresenta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà PdfSaveOptions.FontEncoding.**

Ottiene o imposta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà SlicerCacheItem.Value.**

Restituisce il testo dell'etichetta per l'elemento slicer. Sola lettura.

### **Aggiunge il metodo GlobalizationSettings.GetProtectionNameOfPivotTable().**

Ottiene il nome della protezione nella tabella pivot.

### **Aggiunge il metodo FileFormatUtil.FileFormatToSaveFormat.**

Converte il formato del file in formato di salvataggio.

---
title: Aspose.Cells for Android via Java Note sulla versione 18.12
type: docs
weight: 10
url: /it/java/aspose-cells-for-android-via-java-18-12-release-notes/
---
{{% alert color="primary" %}}

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 18.12.

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42745|Modifica il valore restituito per ottenere i punti di connessione|Nuova caratteristica|
|CELLSJAVA-42662|Fornire la possibilità di esportare l'intervallo come HTML|Nuova caratteristica|
|CELLSJAVA-42746|Mancano le barre dei dati quando XLSX viene convertito in HTML|Nuova caratteristica|
|CELLSJAVA-42747|Il valore esiste ancora quando XLSX viene convertito in HTML|Nuova caratteristica|
|CELLSJAVA-42634|Converti la forma del nastro sinistra destra in immagine|Aumento|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - manca il file dell'elenco dei pacchetti|Aumento|
|CELLSJAVA-42528|Il carattere non è un HTML5 valido e un tag di chiusura automatica e i browser web ne travisano il contenuto|Aumento|
|CELLSJAVA-42738|Il conteggio errato dei valori di convalida viene letto da XLSX|Aumento|
|CELLSJAVA-42734|Problema durante il trattamento dei delimitatori consecutivi come distinti|Aumento|
|CELLSJAVA-42731|Il formato della data non è corretto per le impostazioni locali giapponesi|Aumento|
|CELLSJAVA-42748|L'API LightCells non riesce a caricare un file enorme|Aumento|
|CELLSJAVA-42728|Viene sollevata un'eccezione (StackOverFlow) durante il salvataggio nell'output PDF|Insetto|
|CELLSJAVA-42729|Valore errato calcolato da ROUNDUP()|Insetto|
|CELLSJAVA-42724|Copia un intervallo con PasteType.ALL (opzioni Incolla) che non copia correttamente le altezze delle righe|Insetto|
|CELLSJAVA-42722|La formattazione del testo del collegamento ipertestuale viene persa quando viene impostato un nuovo testo|Insetto|
|CELLSJAVA-42688|Output formato data russo non valido|Insetto|
|CELLSJAVA-42721|Problema con i font SheetRender|Insetto|
|CELLSJAVA-42723|Eccezione "java.lang.OutOfMemoryError: Java heap space" durante il rendering di file MS Excel in PDF|Insetto|
|CELLSJAVA-42725|Le virgolette appaiono nella formula quando si recupera la formula della cella tramite Aspose.Cells|Insetto|
|CELLSJAVA-42720|Degrado delle prestazioni quando si utilizza la formattazione condizionale|Insetto|
|CELLSJAVA-42737|Linea del grafico mancante nella conversione XLSX->PNG|Insetto|
|CELLSJAVA-42735|Problema con il metodo getActualChartSize|Insetto|
|CELLSJAVA-40861|SmartArt non viene copiato quando la cartella di lavoro viene copiata|Insetto|
|CELLSJAVA-42727|La formattazione del testo è mancante nell'output HTML dell'intervallo Excel|Insetto|
|CELLSJAVA-42744|I set di icone diventano disallineati quando XLSX viene convertito in HTML|Insetto|
|CELLSJAVA-42772|L'esportazione dei dati dell'intervallo denominato non viene visualizzata correttamente in HTML (Java)|Insetto|
|CELLSJAVA-42753|Problema dell'intervallo denominato|Insetto|
|CELLSJAVA-42764|La convalida restituisce sempre true per il metodo 'getInCellDropDown()'|Insetto|
|CELLSJAVA-42768|Il formato personalizzato della cultura errato viene restituito per impostazioni locali diverse (Germania, francese, Italia e Spagna)|Insetto|
|CELLSJAVA-42758|Conversione da Excel a PDF - Problema di rendering del grafico del misuratore|Insetto|
|CELLSJAVA-42761|Il rendering PDF genera un'eccezione OutOfMemoryError|Insetto|
|CELLSJAVA-42759|CellsException durante la conversione dei file|Eccezione|
|CELLSJAVA-42755|Eccezione "NullPointerException" durante la creazione di un'istanza dei file XLSX|Eccezione|
|CELLSJAVA-42762|NumberFormatException durante l'elaborazione dei file|Eccezione|
|CELLSJAVA-42774|NullPointerException durante il caricamento di un CSV|Eccezione|
|CELLSJAVA-42765|Eccezione "com.aspose.cells.CellsException" durante il rendering di un file Excel in formato file PDF|Eccezione|
|CELLSJAVA-42754|Eccezione "IllegalStateException: codifica non valida: null" quando si crea un'istanza di un formato di file XLS|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. sul forum di supporto Aspose.Cells.

**Aggiunge la proprietà HtmlSaveOptions.WidthScalable**

Indica se si utilizza l'unità scalabile per descrivere la larghezza della colonna durante l'esportazione del file in HTML. Il valore predefinito è falso.

**Aggiunge la proprietà WorkbookDesigner.UpdateEmptyStringAsNull**

Indica se elaborare il valore della stringa vuota come null.

**Aggiorna il valore restituito del metodo DocumentProperty.ToDateTime(), delle proprietà BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted e BuiltInDocumentPropertyCollection.LastSavedTime**

Restituisce l'ora nel fuso orario locale.

**Richiede un vincolo più forte per l'input dell'utente per FormatCondition.Formula1/Formula2**

La semplice stringa di input non può essere determinata se deve fare riferimento a un riferimento al nome o è solo un valore di stringa costante. Quindi, ora richiediamo che la formula inizi con il segno '='. Per il valore di stringa semplice "sss", utilizza un formato come "=\"sss\"".

**Aggiunge la proprietà PivotTable.RefreshedByWho**

Ottiene il nome dell'utente che ha aggiornato la tabella pivot l'ultima volta.

**Aggiunge la proprietà PivotTable.RefreshDate**

Ottiene la data dell'ultimo aggiornamento della tabella pivot.

**Aggiunge le proprietà CalculationData.CellRow/CellColumn**

Fornisce all'utente un modo efficiente per ottenere gli indici di riga e colonna della cella invece di recuperare l'oggetto Cell.

**Aggiunge la classe CalculationCell**

Rappresenta i dati di calcolo relativi a una cella calcolata.

**Aggiunge il metodo AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData).**

Fornisce all'utente un metodo per raccogliere ed elaborare i riferimenti circolari.

**Aggiunge la proprietà TxtLoadOptions.TreatConsecutiveDelimitersAsOne**

Consente all'utente di scegliere se i delimitatori consecutivi devono essere presi come uno solo durante l'importazione del file CSV.

**Aggiunge il metodo FormatCondition.SetFormulas(string formula1, string formula2, bool isR1C1, bool isLocal)**

Fornisce un modo efficiente e conveniente per l'utente di impostare le formule per FormatCondition.

**Aggiunge il metodo Validation.GetListValue(int row, int column).**

Consente all'utente di ottenere il valore per produrre l'elenco per la convalida di una cella specifica.

**Metodo obsoleto ValidationCollection.Add(Validation validation).**

Usare invece il metodo ValidationCollection.Add(CellArea).

**Aggiunge il metodo Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**

Convalida delle copie.

**Aggiunge le proprietà CreatedUniversalTime, LastPrintedUniversalTime e LastSavedUniversalTime di BuiltInDocumentPropertyCollection**

Restituisce l'ora UTC relativa alle proprietà integrate.

**Aggiunge la proprietà OoxmlSaveOptions.UpdateSmartArt**

Indica se aggiornare la smart art.

**Aggiunge la classe SmartArtShape** 

Rappresenta la forma artistica intelligente.

**Aggiunge la proprietà HtmlSaveOptions.ExportSingleTab**

Indica se esportare la singola scheda quando il file ha un solo foglio di lavoro. Il valore predefinito è falso.

**Aggiunge la proprietà HtmlSaveOptions.ExportPrintAreaOnly**

Indica se si esporta solo l'area di stampa in un file html. Il valore predefinito è falso.

**Elimina il metodo Workbook.Initialize() obsoleto**

Utilizzare invece il costruttore di cartelle di lavoro.

**Elimina la proprietà Workbook.Styles obsoleta**

Utilizzare Workbook.CreateStyle() per creare e manipolare lo stile per la cartella di lavoro anziché StyleCollection.Add();
Utilizzare Workbook.GetNamedStyle(string) per ottenere lo stile con nome anziché StyleCollection

**Elimina il metodo Workbook.CheckWriteProtectedPassword() obsoleto**

Usare invece il metodo WorkbookSettings.WriteProtection.ValidatePassword.

**Aggiunge l'enumerazione LoadDataFilterOptions.VBA**

L'opzione per ignorare i progetti VBA durante il caricamento del file modello.

**Aggiunge la proprietà Style.InvariantCustom**

Ottiene la stringa del modello indipendente dalle impostazioni cultura per il formato numerico (inclusa la stringa del modello per il numero predefinito).

**Aggiunge la proprietà FindOptions.ValueTypeSensitive**

Indica se il tipo di valore della cella cercata deve essere uguale alla chiave cercata.

**Proprietà FindOptions.SearchNext obsoleta**

Utilizzare invece la proprietà FindOptions.SearchBackward, valore true per questa nuova proprietà corrispondente a false di SearchNext.

**Elimina i metodi obsoleti Cells.FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains e FindNumber**

Usare invece il metodo Cells.Find(object,Cell,FindOptions). Per ottenere lo stesso risultato con i metodi FindNumber, FindString, imposta FindOptions.ValueTypeSensitive come true.

Elimina la proprietà Cells.Start obsoleta

Utilizzare invece la proprietà Cells.FirstCell.

**Elimina la proprietà Cells.End obsoleta**

Utilizzare invece la proprietà Cells.LastCell.

**Elimina la proprietà Cells[int].**

Usa invece il metodo Cells.GetEnumerator() per iterare tutte le celle in questo foglio di lavoro.

**Elimina la proprietà Shape.Rotation obsoleta**

Usare invece la proprietà Shape.RotationAngle.

**Elimina la proprietà Validation.AreaList obsoleta**

Utilizzare invece la proprietà Validation.Areas.

**Elimina il costruttore di stili obsoleto**

Utilizzare invece il metodo CellsFactory.CreateStyle() o Workbook.CreateStyle().

**Elimina la proprietà Shape.IsPrinted obsoleta**

Usare invece la proprietà Shape.IsPrintable.

**Elimina il metodo PivotItem.Move(int) obsoleto**

Usare invece il metodo PivotItem.Move(int , bool ).

**Elimina obsoleto Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,object[]), Cells.ExportDataTable(int, int, int, int,bool) , Cells.ExportDataTable(DataTable, int, int[],int, bool) e Cells.ExportDataTable(DataTable,int, int, int, bool, bool)metodi**

Utilizzare invece il metodo ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions).

{{% alert color="primary" %}}

Poiché la base di codice di Aspose.Cells for Android via Java corrisponde al codice delle versioni .NET e Java pertinenti, la maggior parte delle modifiche, dei miglioramenti e delle correzioni sono incluse in Aspose.Cells for .NET v18.10, Aspose.Cells for .NET v18.11, 07607161818 , Aspose.Cells for Java v18.10, Aspose.Cells for Java v18.11 e Aspose.Cells for Java v18.12 sono inclusi anche in questo Aspose.Cells for Android 0761183482 v18.12.

{{% /alert %}}

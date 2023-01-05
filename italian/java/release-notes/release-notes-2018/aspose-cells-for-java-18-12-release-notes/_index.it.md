---
title: Aspose.Cells for Java Note sulla versione 18.12
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-18-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.12.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42745|Non ottiene i punti di connessione poiché il suo tipo restituito è 'zo[]'|Nuova caratteristica|
|CELLSJAVA-42662|Fornire la possibilità di esportare l'intervallo come HTML|Nuova caratteristica|
|CELLSJAVA-42746|Mancano le barre dei dati quando XLSX viene convertito in HTML|Nuova caratteristica|
|CELLSJAVA-42747|Il valore esiste ancora quando XLSX viene convertito nel formato file HTML|Nuova caratteristica|
|CELLSJAVA-42748|LightCells API non riesce a caricare un file enorme|Aumento|
|CELLSJAVA-42727|La formattazione del testo è mancante nell'output HTML dell'intervallo MS Excel|Insetto|
|CELLSJAVA-42744|I set di icone diventano disallineati quando XLSX viene convertito in HTML|Insetto|
|CELLSJAVA-42772|L'esportazione dei dati dell'intervallo denominato non viene visualizzata correttamente in HTML (Java)|Insetto|
|CELLSJAVA-42753|Un problema riscontrato nell'intervallo denominato|Insetto|
|CELLSJAVA-42764|La convalida restituisce sempre true per il metodo 'getInCellDropDown()'|Insetto|
|CELLSJAVA-42768|Il formato personalizzato della cultura errato viene restituito per impostazioni locali diverse (Germania, francese, Italia e Spagna)|Insetto|
|CELLSJAVA-42758|Conversione da Excel a PDF - Problema di rendering del grafico del misuratore|Insetto|
|CELLSJAVA-42761|La resa PDF genera un'eccezione OutOfMemoryError|Insetto|
|CELLSJAVA-42759|CellsException durante la conversione dei file|Eccezione|
|CELLSJAVA-42755|Eccezione "NullPointerException" durante la creazione di un'istanza dei file XLSX|Eccezione|
|CELLSJAVA-42762|NumberFormatException durante l'elaborazione dei file|Eccezione|
|CELLSJAVA-42774|NullPointerException durante il caricamento di un CSV|Eccezione|
|CELLSJAVA-42765|Eccezione "com.aspose.cells.CellsException" durante il rendering di un file Excel nel formato file PDF|Eccezione|
|CELLSJAVA-42754|"IllegalStateException: codifica non valida: null" quando si crea un'istanza di un formato di file XLS|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HtmlSaveOptions.ExportSingleTab**
Indica se esportare la singola scheda quando il file contiene un solo foglio di lavoro. Il valore predefinito è false.
### **Aggiunge la proprietà HtmlSaveOptions.ExportPrintAreaOnly**
Indica se si esporta solo l'area di stampa in un file html. Il valore predefinito è falso.
### **Elimina il metodo Workbook.Initialize() obsoleto**
Utilizzare invece il costruttore di cartelle di lavoro.
### **Elimina la proprietà Workbook.Styles obsoleta**
Utilizzare Workbook.CreateStyle() per creare e manipolare lo stile per la cartella di lavoro anziché StyleCollection.Add(); Utilizzare Workbook.GetNamedStyle(string) per ottenere lo stile con nome anziché StyleCollection.
### **Elimina il metodo Workbook.CheckWriteProtectedPassword() obsoleto**
Usare invece il metodo WorkbookSettings.WriteProtection.ValidatePassword.
### **Aggiunge l'enumerazione LoadDataFilterOptions.VBA**
L'opzione da utilizzare per ignorare i progetti VBA durante il caricamento del file modello.
### **Aggiunge la proprietà Style.InvariantCustom**
Ottiene la stringa del modello indipendente dalle impostazioni cultura per il formato numerico (inclusa la stringa del modello per il numero predefinito).
### **Aggiunge la proprietà FindOptions.ValueTypeSensitive**
Indica se il tipo di valore della cella cercata deve essere uguale alla chiave cercata.
### **Proprietà FindOptions.SearchNext obsoleta**
Utilizzare invece la proprietà FindOptions.SearchBackward, il valore true per questa nuova proprietà corrisponde a false di SearchNext.
### **Elimina i metodi obsoleti Cells.FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains e FindNumber**
Utilizzare invece il metodo Cells.Find (oggetto,Cell,FindOptions). Per ottenere gli stessi risultati con i metodi FindNumber, FindString, imposta FindOptions.ValueTypeSensitive come true.
### **Elimina il metodo Cells.ImportGridView(System.Web.UI.WebControls.GridView,int ,int , bool ,bool ,bool ) obsoleto**
Utilizzare il metodo Cells.ImportGridView (System.Web.UI.WebControls.GridView gridView,int firstRow,int firstColumn,ImportTableOptions options). invece.
### **Elimina la proprietà Cells.Start obsoleta**
Utilizzare invece la proprietà Cells.FirstCell.
### **Elimina la proprietà Cells.End obsoleta**
Utilizzare invece la proprietà Cells.LastCell.
### **Elimina la proprietà Cells[int].**
Usa invece il metodo Cells.GetEnumerator() per iterare tutte le celle in questo foglio di lavoro.
### **Elimina i metodi Cells.ImportDataColumn() obsoleti**
Usare invece il metodo Cells.ImportData (DataTable,int,int,ImportTableOptions).
### **Elimina i metodi Cells.ImportDataReader() obsoleti**
Usare invece il metodo Cells.ImportData (IDataReader, int, int,ImportTableOptions).
### **Elimina la proprietà Shape.Rotation obsoleta**
Usare invece la proprietà Shape.RotationAngle.
### **Elimina la proprietà Validation.AreaList obsoleta**
Utilizzare invece la proprietà Validation.Areas.
### **Elimina il costruttore di stili obsoleto**
Utilizzare invece il metodo CellsFactory.CreateStyle() o Workbook.CreateStyle().
### **Elimina la proprietà Shape.IsPrinted obsoleta**
Usare invece la proprietà Shape.IsPrintable.
### **Elimina il metodo PivotItem.Move(int) obsoleto**
Usando invece il metodo PivotItem.Move(int , bool ).
### **Elimina obsoleto Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,object[]), Cells.ExportDataTable(int, int, int, int,bool) , Cells.ExportDataTable(DataTable, int, int[],int, bool) e Cells.ExportDataTable(DataTable,int, int, int, bool, bool) metodi**
Utilizzare invece il metodo ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions).
### **Aggiunge ExtPage.setServlet(HttpServletRequest req,HttpServletResponse resp)**
 Inizializza il contesto servlet per ExtPage.
### **Aggiunge il metodo ExtPage.getBean()**
 Ottiene l'istanza GridWebBean da ExtPage.
### **Elimina il metodo ExtPage.getBean(HttpServletRequest req).**
 Utilizzare invece ExtPage.getBean().
### **Aggiunge la proprietà ExtPage.Maxholders**
Indica il numero massimo di istanze di GridWeb per il server da conservare (la creazione di ogni nuova pagina o aggiornamento è considerata come una nuova istanza di controllo), il valore predefinito è 1000.
### **Aggiunge la proprietà ExtPage.Memoryinstanceexpires**
 Indica il tempo di scadenza in secondi dell'istanza di controllo sul server, se il tempo scade, verrà rimosso sul server, il valore predefinito è 3600, circa un'ora.
### **Aggiunge la proprietà ExtPage.MemoryCleanRateTime**
 Indica ogni volta la durata in secondi per eseguire il lavoro di verifica, per verificare se l'istanza di controllo è scaduta, se scaduta la rimuove, il valore di default è 7200, circa due ore.

---
title: Aspose.Cells for .NET Note sulla versione 18.12
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-18-12-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.12](https://www.nuget.org/packages/Aspose.Cells/18.12.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46479|Nome scheda non disponibile quando la cartella di lavoro a foglio singolo viene convertita in HTML|Nuova caratteristica|
|CELLSNET-46503|Controllare il caricamento dei dati VBA utilizzando LoadDataFilterOptions|Nuova caratteristica|
|CELLSNET-42414|Modifiche rilevate perse durante la conversione da XLSB a XLSM e da XLS a XLSM|Aumento|
|CELLSNET-46090|Il testo si è leggermente spostato dopo aver separato la forma durante il salvataggio di un XLS in XLSX|Aumento|
|CELLSNET-46439|Ottimizzazione per le prestazioni della memoria: rilascia il flusso originale dopo aver caricato la cartella di lavoro|Prestazione|
|CELLSNET-46371|Le griglie non vengono visualizzate in alcuni fogli durante la conversione XLSX->HTML->XLSX|Insetto|
|CELLSNET-46447|Formattazioni perse nel rendering da HTML a XLS|Insetto|
|CELLSNET-46494|Conversione da MHT a XLSX - problema del contenuto della cella|Insetto|
|CELLSNET-46468|MS Excel richiede un errore all'apertura del file di output|Insetto|
|CELLSNET-46487|La formula locale non inglese non funziona|Insetto|
|CELLSNET-46489|L'eliminazione di una riga con un indice e la lettura della riga con lo stesso indice restituisce Cell.ValuType: IsNull|Insetto|
|CELLSNET-46406|Impossibile aprire il documento ODS protetto da password|Insetto|
|CELLSNET-46466|Il testo inferiore sotto il codice a barre non è presente nel rendering da MS Excel a PDF|Insetto|
|CELLSNET-46470|L'immagine non è presente dopo il rendering nell'output TIFF|Insetto|
|CELLSNET-46499|Le immagini non vengono visualizzate correttamente quando vengono convertite da Excel a PDF|Insetto|
|CELLSNET-46443|Il testo extra è apparso nell'immagine resa dal grafico MS Excel|Insetto|
|CELLSNET-46450|L'immagine renderizzata dal grafico MS Excel ha più unità di assi rispetto al grafico originale|Insetto|
|CELLSNET-46451|Problema durante il rendering del file modello (contenente il grafico) nel formato di file PDF|Insetto|
|CELLSNET-46454|Ordine della legenda reso in modo diverso dal grafico di Excel nella sessione 0 rispetto alla sessione 1|Insetto|
|CELLSNET-46471|Impossibile impostare l'indicatore di colore LineWithDataMarkers nel formato di file XLS|Insetto|
|CELLSNET-42729|Il testo viene spostato quando i grafici SmartArt vengono visualizzati come formato di file HTML|Insetto|
|CELLSNET-46462|Testo ripetuto durante la sostituzione del tag con il testo|Insetto|
|CELLSNET-46483|Errore dopo la conversione del documento con Custom UI xml da XLSB a XLSM|Insetto|
|CELLSNET-46495|Problemi riscontrati durante la conversione del grafico in immagine|Insetto|
|CELLSNET-46486|Eccezione sollevata durante la conversione di XLS in PDF|Eccezione|
|CELLSNET-46472|PivotTable.GetChildren() solleva l'eccezione "Nome Cell non valido"|Eccezione|
|CELLSNET-46452|Eccezione "NullReferenceException" durante il caricamento di un formato di file XLSB|Eccezione|
|CELLSNET-46456|ArgumentException al caricamento della cartella di lavoro|Eccezione|
|CELLSNET-46460|Eccezione durante l'accesso a TextBox.HtmlText da XLS|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportSingleTab**
Indica se esportare la singola scheda quando il file contiene un solo foglio di lavoro. Il valore predefinito è false.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportPrintAreaOnly**
Indica se si esporta solo l'area di stampa in un file html. Il valore predefinito è falso.
#### **Elimina il metodo Workbook.Initialize() obsoleto**
Utilizzare invece il costruttore di cartelle di lavoro.
#### **Elimina la proprietà Workbook.Styles obsoleta**
Utilizzare Workbook.CreateStyle() per creare e manipolare lo stile per la cartella di lavoro anziché StyleCollection.Add(); Utilizzare Workbook.GetNamedStyle(string) per ottenere lo stile con nome anziché StyleCollection.
#### **Elimina il metodo Workbook.CheckWriteProtectedPassword() obsoleto**
Usare invece il metodo WorkbookSettings.WriteProtection.ValidatePassword.
#### **Aggiunge l'enumerazione LoadDataFilterOptions.VBA**
L'opzione da utilizzare per ignorare i progetti VBA durante il caricamento del file modello.
#### **Aggiunge la proprietà Style.InvariantCustom**
Ottiene la stringa del modello indipendente dalle impostazioni cultura per il formato numerico (inclusa la stringa del modello per il numero incorporato).
#### **Aggiunge la proprietà FindOptions.ValueTypeSensitive**
Indica se il tipo di valore della cella cercata deve essere uguale alla chiave cercata.
#### **Proprietà FindOptions.SearchNext obsoleta**
Utilizzare invece la proprietà FindOptions.SearchBackward, il valore true per questa nuova proprietà corrisponde a false di SearchNext.
#### **Elimina i metodi obsoleti Cells.FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains e FindNumber**
Utilizzare invece il metodo Cells.Find (oggetto,Cell,FindOptions). Per ottenere gli stessi risultati con i metodi FindNumber, FindString, imposta FindOptions.ValueTypeSensitive come true.
#### **Elimina il metodo Cells.ImportGridView(System.Web.UI.WebControls.GridView,int ,int , bool ,bool ,bool ) obsoleto**
Utilizzare il metodo Cells.ImportGridView (System.Web.UI.WebControls.GridView gridView,int firstRow,int firstColumn,ImportTableOptions options). invece.
#### **Elimina la proprietà Cells.Start obsoleta**
Utilizzare invece la proprietà Cells.FirstCell.
#### **Elimina la proprietà Cells.End obsoleta**
Utilizzare invece la proprietà Cells.LastCell.
#### **Elimina la proprietà Cells[int].**
Usa invece il metodo Cells.GetEnumerator() per iterare tutte le celle in questo foglio di lavoro.
#### **Elimina i metodi Cells.ImportDataColumn() obsoleti**
Usare invece il metodo Cells.ImportData (DataTable,int,int,ImportTableOptions).
#### **Elimina i metodi Cells.ImportDataReader() obsoleti**
Usare invece il metodo Cells.ImportData (IDataReader, int, int,ImportTableOptions).
#### **Elimina la proprietà Shape.Rotation obsoleta**
Usare invece la proprietà Shape.RotationAngle.
#### **Elimina la proprietà Validation.AreaList obsoleta**
Utilizzare invece la proprietà Validation.Areas.
#### **Elimina il costruttore di stili obsoleto**
Utilizzare invece il metodo CellsFactory.CreateStyle() o Workbook.CreateStyle().
#### **Elimina la proprietà Shape.IsPrinted obsoleta**
Usare invece la proprietà Shape.IsPrintable.
#### **Elimina il metodo PivotItem.Move(int) obsoleto**
Usando invece il metodo PivotItem.Move(int , bool ).
#### **Elimina obsoleto Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,object[]), Cells.ExportDataTable(int, int, int, int,bool) , Cells.ExportDataTable(DataTable, int, int[],int, bool) e Cells.ExportDataTable(DataTable,int, int, int, bool, bool) metodi**
Utilizzare invece il metodo ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions).

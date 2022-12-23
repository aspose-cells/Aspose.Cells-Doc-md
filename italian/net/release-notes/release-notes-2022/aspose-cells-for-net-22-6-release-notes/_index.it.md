---
title: Aspose.Cells for .NET 22.6 Note di rilascio
type: docs
weight: 7
url: /it/net/aspose-cells-for-net-22-6-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.6](https://www.nuget.org/packages/Aspose.Cells/22.6.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50880|Nuove API per convertire i dati in ICellsDataTable per comodità dell'utente|
|CELLSNET-51140|Supporta l'archiviazione dei dati 5.0 di .numbers|
|CELLSNET-51144|Supporta la lettura di immagini di Numbers13|
|CELLSNET-51230| Supporto per impostare lo stile per CellRange|
|CELLSNET-50996|Aggiunta del metodo di overload ChartCollection.Add (ChartType, String, Boolean, Int32, Int32, Int32, Int32)|
|CELLSNET-51184| Supporta l'importazione del valore dell'array se l'intervallo è una cella semplice|
|CELLSNET-51215|Supporta il salvataggio dei formati di tabella in xlsb|
|CELLSNET-50226|l'immagine è sfocata|
|CELLSNET-50954|UpperLeftRow errato di CheckBox dopo il caricamento della cartella di lavoro|
|CELLSNET-51153| Caselle di controllo duplicate|
|CELLSNET-51158|I caratteri scritti su oggetti come forme e caselle di testo sono confusi in Linux|
|CELLSNET-51180|Il file XLS con la tabella pivot convertito in XLSM è danneggiato e i dettagli delle connessioni dati sono stati eliminati|
|CELLSNET-50598|La formula dinamica con la funzione FILTRO non può essere aggiornata e calcolata correttamente|
|CELLSNET-51069|Cell.Calculate() non aggiorna le dipendenze delle formule quando la catena di calcolo è abilitata per la cartella di lavoro|
|CELLSNET-51186| Problema con la funzione CEILING nel motore di calcolo della formula Aspose.Cells'|
|CELLSNET-51192|La funzione DATE è stata calcolata come #NUM! per il 1/0/1900|
|CELLSNET-51195|La conversione di un file XLSB con tabelle dati nel formato XLSM ha comportato l'eliminazione della tabella dati|
|CELLSNET-51235|Alcune celle con formule molto lunghe non vengono calcolate entro Aspose.Cells|
|CELLSNET-51268|Problema con la formula COUNTIFS che tratta 0 in modo errato|
|CELLSNET-51041|I caratteri cinesi sono corrotti durante il caricamento di html|
|CELLSNET-51072|Problema di ImportXml con il campo Data|
|CELLSNET-51081|Il formato personalizzato viene modificato dopo aver ricaricato l'html salvato nella cartella di lavoro|
|CELLSNET-51092|Il carattere barrato non funziona nel rendering SVG/image su Linux|
|CELLSNET-51120|Eccezione generata durante l'esportazione di dati xml collegati a Xml Map|
|CELLSNET-51197|Problema di ImportXml con il campo booleano|
|CELLSNET-50854|Da XLSX a PDF: grafici a barre non visualizzati correttamente|
|CELLSNET-50983|Le etichette dell'asse X sono sbagliate|
|CELLSNET-50998| L'ultimo parametro dell'asse x non viene visualizzato|
|CELLSNET-50999|Le etichette del grafico non si adattano alla scatola - la scatola è sovradimensionata|
|CELLSNET-51000|Etichetta del grafico allineata verticalmente anziché orizzontalmente|
|CELLSNET-51043| Output errato dei nomi delle serie durante il salvataggio della cartella di lavoro in PDF|
|CELLSNET-51159| Bug con Chart.Title.IsVisible=false durante il salvataggio del pdf|
|CELLSNET-51211| Numeri mancanti durante la creazione di un'immagine da un grafico di Excel|
|CELLSNET-49105|Il file .ods salvato è danneggiato quando il file contiene la convalida dell'elenco|
|CELLSNET-50691|Perdere gli intervalli di ErrorCheckOption|
|CELLSNET-50995| Chart.SetChartDataRange salterà le celle vuote nell'intervallo di dati|
|CELLSNET-51056|Chart.SetChartDataRange non ha riconosciuto le celle unite|
|CELLSNET-51062|Il tipo di grafico vuoto deve essere ChartType.Line se contiene il nodo Marker|
|CELLSNET-51116| L'attributo has revisions restituisce true ma il rilevamento delle modifiche è disabilitato|
|CELLSNET-51199| workbook.save(filePath) Annulla il blocco dei riquadri|
|CELLSNET-51228|Workbook.CalculateFormula causa l'eccezione "Riferimento oggetto non impostato su un'istanza di un oggetto".|
|CELLSNET-51045|Eccezione "Cell è stata rimossa: D7" quando si imposta lo stile su un intervallo in Aspose.Cells.GridDesktop|
|CELLSNET-47707|Eccezione "Questo file Excel contiene record (formato file Excel2.1 o precedente)" durante il caricamento di un file XLS|
|CELLSNET-47960|la nuova cartella di lavoro non riesce a generare un'eccezione: questo file Excel contiene record (Excel4.0 o formato di file precedente).|
|CELLSNET-51227| System.FormatException. La stringa non è stata riconosciuta come DateTime valido durante il caricamento del file Excel di Suomi|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la classe CellsDataTableFactory**

Questa classe fornisce API per creare un'istanza di ICellsDataTable da oggetti personalizzati per comodità dell'utente.

### **Aggiunge la proprietà Workbook.CellsDataTableFactory**

Fornire all'utente CellsDataTableFactory per creare un'istanza di ICellsDataTable da oggetti personalizzati.

### **Aggiunge il metodo Cell.GetDependentsInCalculation(bool).**

In base all'attuale catena di calcolo, ottieni tutte le celle il cui risultato calcolato dipende da questa cella.

### **Aggiunge il metodo Cell.GetPrecedentsInCalculation()**

In base all'attuale catena di calcolo, ottieni tutti i precedenti (riferimento alle celle nella cartella di lavoro corrente) utilizzati dalla formula di questa cella durante il calcolo.

### **Metodi obsoleti Cell.GetLeafs() e Cell.GetLeafs(bool)**

Utilizzare invece il metodo Cell.GetDependentsInCalculation(bool).

### **Aggiunge il metodo PivotTable.FormatRow(int row, Style style).**

Formatta i dati della riga nell'area della tabella pivot.

### **Aggiunge la proprietà Shapes.CreateId**

Ottiene l'ID di creazione della forma.

### **Aggiunge l'enumerazione WarningType.InvalidData**

Rappresenta il tipo di dati non valido.

### **Aggiunge il metodo di sovraccarico ChartCollection.Add()**

Aggiunge un grafico con l'origine dati.

### **Aggiunge il metodo Chart.GetActualSize()**

Ottiene la dimensione effettiva del grafico in unità di pixel.

### **Proprietà Chart.ActualChartSize obsoleta**

Utilizzare invece il metodo Chart.GetActualSize().

### **Proprietà PdfSaveOptions.ImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Proprietà ImageOrPrintOptions.ChartImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.ImageFormat**

Utilizzare invece la proprietà ImageOrPrintOptions.ImageType.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.IsImageFitToPage**

La proprietà è inutile.

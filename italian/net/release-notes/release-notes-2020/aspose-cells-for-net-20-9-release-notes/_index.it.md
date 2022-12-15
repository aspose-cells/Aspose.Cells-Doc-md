---
title: Aspose.Cells for .NET 20.9 Note di rilascio
type: docs
weight: 8
url: /it/net/aspose-cells-for-net-20-9-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.9](https://www.nuget.org/packages/Aspose.Cells/20.9.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47567|Supporto per ottenere/impostare le proprietà della forma dell'affettatrice|Nuova caratteristica|
|CELLSNET-47549|API client per aggiungere/rimuovere commenti per GridWeb|Nuova caratteristica|
|CELLSNET-47555|Il grafico non consente di trattare #N/D come celle vuote durante il salvataggio come PDF|Aumento|
|CELLSNET-47579|Il carattere Kaiti non è reso correttamente|Aumento|
|CELLSNET-47154|Le tabelle delle query non vengono caricate dal file ODS|Aumento|
|CELLSNET-47556|Miglioramento per il congelamento e la divisione del foglio di lavoro|Aumento|
|CELLSNET-47570|Le macro dovrebbero essere rimosse quando si combinano/copiano le cartelle di lavoro|Aumento|
|CELLSNET-47543|Problema con i marcatori intelligenti con formattazione condizionale applicata|Insetto|
|CELLSNET-47561|La valuta con formato personalizzato viene mostrata all'esterno della cella in HTML|Insetto|
|CELLSNET-47562|Salvataggio di un foglio vuoto con le impostazioni delle linee della griglia esportate in HTML|Insetto|
|CELLSNET-47569|La tabella pivot non viene visualizzata correttamente dopo la conversione da XLSX a PDF|Insetto|
|CELLSNET-47475|CalculateFormula() calcola in modo diverso rispetto a MS Excel|Insetto|
|CELLSNET-47531|Le formule contenenti nomi che non esistono vengono visualizzate come `WorkbookName`!Nome|Insetto|
|CELLSNET-47545|Numero negativo personalizzato reso in modo errato nel PDF|Insetto|
|CELLSNET-47548|Problema con l'importazione di file di testo con virgolette doppie|Insetto|
|CELLSNET-47558|Numeri negativi personalizzati (utilizzando la regione Svizzera) visualizzati in modo errato nel PDF|Insetto|
|CELLSNET-47075|È necessario sincronizzare lo scorrimento di due griglie proprio come SyncScrollingSideBySide di Excel.|Insetto|
|CELLSNET-47559|Impossibile selezionare le celle utilizzando i tasti freccia della tastiera quando il foglio è impostato come di sola lettura|Insetto|
|CELLSNET-47360|I punti indicatori trasparenti nel grafico nel file Excel vengono distorti nel PDF di output|Insetto|
|CELLSNET-47565|L'immagine del piè di pagina in primo piano diventa sfondo|Insetto|
|CELLSNET-46502|La conversione da XLSX a TIFF produce una scatola nera|Insetto|
|CELLSNET-46821|Conversione del foglio di lavoro in TIFF: l'immagine è oscurata|Insetto|
|CELLSNET-47458|Distorsione della forma dopo la conversione in file PDF|Insetto|
|CELLSNET-47551|Asse X non corretto durante la conversione del grafico Excel in PDF|Insetto|
|CELLSNET-47546| Elimina righe/colonne vuote corrompe il documento Excel|Insetto|
|CELLSNET-47552|PowerQueryFormula.FormulaDefinition errata|Insetto|
|CELLSNET-47573|Impossibile produrre la formattazione desiderata utilizzando shift|Insetto|
|CELLSNET-47574|Da XLS a HTML produce un file vuoto|Insetto|
|CELLSNET-47581|MaxColumn è impostato su Column XFD dopo aver chiamato InsertCutCells()|Insetto|
|CELLSNET-47586|La cartella di lavoro con il grafico a cascata non può essere aperta utilizzando Excel 2016 dopo la copia|Insetto|
|CELLSNET-47547|Eccezione sollevata durante l'aggiunta dell'affettatrice per la tabella|Eccezione|
|CELLSNET-47553|Eccezione durante il salvataggio di un file XLS in XLSX|Eccezione|
|CELLSNET-47563|Eccezione "File danneggiato" durante il caricamento di un formato di file XLS|Eccezione|
|CELLSNET-47580|ArgumentOutOfRangeException durante la conversione di Excel|Eccezione|
|CELLSNET-47592|Eccezione durante la conversione di particolari XLSX in XLS|Eccezione|
|CELLSNET-47557|Alcune proprietà mancano quando si combinano le cartelle di lavoro|Regressione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà AbstractCalculationEngine.ProcessBuiltInFunctions**

Per motivi di prestazioni e comodità dell'utente, abbiamo aggiunto questa proprietà e impostato il suo valore predefinito come**falso** così l'utente può concentrarsi su quelle funzioni che non sono state supportate dal motore integrato. Se l'implementazione esistente dell'utente di**Motore di calcolo astratto** modificato il calcolo di alcune funzioni integrate, l'utente deve sovrascrivere questa proprietà per renderla come**VERO** da**20.9**.

### **Aggiunge la proprietà TxtLoadOptions.HasTextQualifier**

Indica se è presente un qualificatore di testo per i valori delle celle nel file modello.

### **Aggiunge la proprietà TxtLoadOptions.TextQualifier**

Specifica il qualificatore di testo per i valori delle celle nel file modello.

### **Aggiunge la proprietà HtmlSaveOptions.ImageScalable**

 Indica se utilizzare l'unità scalabile per descrivere la larghezza dell'immagine. Il valore predefinito della proprietà è**VERO**.

### **Aggiunge la proprietà Slicer.AlternativeText**

Ottiene o imposta la stringa di testo descrittiva (alternativa) dell'oggetto Slicer.

### **Aggiunge la proprietà Slicer.ColumnWidthPixel**

Ottiene o imposta la larghezza in unità di pixel per ogni colonna dell'affettatrice.

### **Aggiunge la proprietà Slicer.HeightPixel**

Ottiene o imposta l'altezza dell'affettatrice specificata, in pixel.

### **Aggiunge la proprietà Slicer.IsLocked**

Indica se la forma dell'affettatrice è bloccata.

### **Aggiunge la proprietà Slicer.IsPrintable**

Indica se l'oggetto slicer è stampabile.

### **Aggiunge la proprietà Slicer.LeftPixel**

Ottiene o imposta l'offset orizzontale della forma affettatrice dalla relativa colonna sinistra, in pixel.

### **Aggiunge la proprietà Slicer.LockedAspectRatio**

Indica se bloccare le proporzioni.

### **Aggiunge la proprietà Slicer.Placement**

Rappresenta il modo in cui l'oggetto di disegno è collegato alle celle sottostanti. La proprietà controlla il posizionamento di un oggetto in un foglio di lavoro.

### **Aggiunge la proprietà Slicer.RowHeightPixel**

Restituisce o imposta l'altezza, in pixel, di ogni riga nell'affettatrice specificata.

### **Aggiunge la proprietà Slicer.Title**

Specifica il titolo dell'oggetto Slicer corrente.

### **Aggiunge la proprietà Slicer.TopPixel**

Ottiene o imposta l'offset verticale della forma affettatrice dalla relativa riga superiore, in pixel.

### **Aggiunge la proprietà Slicer.WidthPixel**

Ottiene o imposta la larghezza dell'affettatrice specificata, in pixel.

### **Aggiunge la proprietà Worksheet.PaneState e l'enumerazione PaneStateType.**

Rappresenta lo stato del riquadro nel foglio di lavoro.

### **Aggiunge la proprietà OdsLoadOptions.RefreshPivotTables.**

Indica se aggiornare la tabella pivot durante il caricamento dei file .ods.

### **Aggiunge la proprietà FilterColumn.IsDropdownVisible.**

Indica se il pulsante Filtro automatico per questa colonna è visibile.

### **Proprietà Filter.Visibledropdown obsoleta.**

Usare invece FilterColumn.IsDropdownVisible.

### **Aggiunge la proprietà CopyOptions.KeepMacros.**

Indica se conservare i macor nella cartella di lavoro di destinazione. Ha effetto solo quando la cartella di lavoro originale non contiene macro.

### **Aggiunge il metodo Workbook.Copy(Workbook,CopyOptions) di overload.**

Copia la cartella di lavoro con le opzioni.

### **Aggiunge l'enumerazione WarningType.InvalidAutoFilterRange.**

Rappresenta il tipo di avviso che non è stato possibile filtrare automaticamente l'intervallo.

### **Aggiunge la proprietà Chart.DisplayNaAsBlank.**

Indica se visualizzare #N/A come valore vuoto.

### **Aggiunge l'enumerazione CrossType.Minimum.**

Rappresenta gli assi incrociati al valore minimo.

### **Aggiunge la proprietà XlsbSaveOptions.ExportAllColumnIndexes.**

Indica se esportare gli indici di colonna per tutte le celle.

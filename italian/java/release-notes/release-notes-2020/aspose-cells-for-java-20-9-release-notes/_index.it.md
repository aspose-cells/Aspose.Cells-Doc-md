---
title: Aspose.Cells for Java 20.9 Note di rilascio
type: docs
weight: 7
url: /it/java/aspose-cells-for-java-20-9-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.9/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-40792|La tabella pivot non viene creata per il file ODS|Nuova caratteristica|
|CELLSJAVA-43263|Problema SmartMarker quando una cella è impostata sul colore di riempimento e sulla formattazione condizionale|Insetto|
|CELLSJAVA-43269|Impossibile ottenere valore dal foglio pivot|Insetto|
|CELLSJAVA-43272|L'immagine si restringe dopo aver impostato la larghezza scalabile|Insetto|
|CELLSJAVA-43280|Problema di filtro dopo l'aggiornamento della tabella pivot|Insetto|
|CELLSJAVA-43281|Aggiorna il problema della tabella pivot|Insetto|
|CELLSJAVA-43285|I filtri statici vengono persi dopo l'aggiornamento della tabella pivot|Insetto|
|CELLSJAVA-43288|Il file XLSB risultante è corrotto durante il salvataggio del file in XLSB|Insetto|
|CELLSJAVA-43289|Problema di filtro dopo l'aggiornamento della tabella pivot|Insetto|
|CELLSJAVA-43293|Problema con le opzioni di filtro dopo PivotTable.refreshData()|Insetto|
|CELLSJAVA-43279|I valori non vengono recuperati correttamente utilizzando getStringValue()|Insetto|
|CELLSJAVA-43291|Contenuto della griglia non visibile|Insetto|
|CELLSJAVA-43037|Problema di carattere nella conversione PDF|Insetto|
|CELLSJAVA-43249|Problemi di stampa durante l'utilizzo di stampanti fisiche, XPS e stampante PDF|Insetto|
|CELLSJAVA-43254|Differenza di carattere durante la conversione del foglio di calcolo in immagine|Insetto|
|CELLSJAVA-43266|La versione Java non supporta il caricamento del carattere dalla cartella dei caratteri dell'utente corrente per impostazione predefinita|Insetto|
|CELLSJAVA-43268|Rendering da Excel a TIFF: alcuni valori vengono sostituiti con caratteri "#".|Insetto|
|CELLSJAVA-43275|Aspose.Cell for Java 20.8 com.aspose.cells.CellsException: errore per ZipFile|Insetto|
|CELLSJAVA-43277|Problema con il rapporto tra altezza e larghezza|Insetto|
|CELLSJAVA-43245|Il grafico combinato non viene visualizzato correttamente dopo la conversione del file Excel in PDF|Insetto|
|CELLSJAVA-43276|Problemi di interruzione di riga durante la conversione di XLSX in PDF|Insetto|
|CELLSJAVA-43261|SmartMarker: quando si utilizza group:merge con Number Format Percentage, il risultato dell'espansione è errato|Insetto|
|CELLSJAVA-43265|Impossibile caricare il file XLSX|Insetto|
|CELLSJAVA-43270|Duplicazione del contenuto (Word incorporato) durante la copia del foglio di lavoro|Insetto|
|CELLSJAVA-43271|Grafico WaterFall che non preserva la proprietà SetAsTotal|Insetto|
|CELLSJAVA-43287|L'aggiunta del filtro automatico danneggia la cartella di lavoro|Insetto|
|CELLSJAVA-43290|L'elaborazione non viene ripristinata durante il salvataggio del file XML Spreadsheet 2003 in formato cartella di lavoro MS Excel|Insetto|
|CELLSJAVA-43267|Eccezione "java.lang.NullPointerException" durante il calcolo della tabella pivot nel foglio|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà AbstractCalculationEngine.ProcessBuiltInFunctions**

 Per considerazioni relative alle prestazioni e alla comodità dell'utente, aggiungiamo questa proprietà e impostiamo il suo valore predefinito su false in modo che l'utente possa concentrarsi su quelle funzioni che non sono state supportate dal motore integrato. Se l'implementazione esistente dell'utente di AbstractCalculationEngine ha modificato il calcolo di alcune funzioni integrate, l'utente deve eseguire l'override di questa proprietà per renderla come**VERO** da**20.9**.

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

Indica se mantenere le macro nella cartella di lavoro di destinazione. Ha effetto solo quando la cartella di lavoro originale non contiene macro.

### **Aggiunge il metodo Workbook.Copy(Workbook,CopyOptions) di overload.**

Copia la cartella di lavoro con le opzioni.

### **Aggiunge l'enumerazione WarningType.InvalidAutoFilterRange.**

Rappresenta il tipo di avviso che non è stato possibile filtrare automaticamente l'intervallo.

### **Aggiunge la proprietà Chart.DisplayNaAsBlank.**

Indica se visualizzare #N/A come valore vuoto.

### **Aggiunge l'enumerazione CrossType.Minimum.**

Rappresenta gli assi incrociati al valore minimo.

### **Aggiunge la proprietà XlsbSaveOptions.ExportAllColumnIndexes.**

Indica se esportare gli indici di colonna per tutte le celle durante il salvataggio dei file XLSB.

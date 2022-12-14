---
title: Aspose.Cells per Android tramite Java 21.3 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-android-via-java-21-3-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 21.3.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43375|Controlla la password VBA di Excel|
|CELLSJAVA-43400|Supporta la funzione UNIQUE()|
|CELLSJAVA-42863|Recupera il sottotitolo del grafico|
|CELLSJAVA-43401|Supporta il risultato di formattazione unificato per l'era giapponese per tutti i JDK|
|CELLSJAVA-43398|La formattazione condizionale non viene visualizzata correttamente nella conversione da ODS a HTML|
|CELLSJAVA-43371|La conversione da XLSX a PDF si blocca|
|CELLSJAVA-43353|Diversi diagrammi su excel in pdf|
|CELLSJAVA-43377|Problemi di posizionamento delle immagini durante la conversione di Excel in Html|
|CELLSJAVA-43381|Errore di calcolo della funzione GIORNI|
|CELLSJAVA-43342|Il grafico combinato non può essere visualizzato correttamente in Excel in PDF|
|CELLSJAVA-43354|Le percentuali non sono state mostrate negli istogrammi piccoli|
|CELLSJAVA-40264|Errore con controlli modulo o controlli ActiveX durante il salvataggio come EXCEL_97_TO_2003|
|CELLSJAVA-43372|File danneggiato creato durante la conversione di ODS in XLSX|
|CELLSJAVA-43378|Visualizza come modifiche vuote da true a false dopo la clonazione della cartella di lavoro|
|CELLSJAVA-43382|La copia produce una cartella di lavoro danneggiata|
|CELLSJAVA-43364|Problema durante il salvataggio del grafico con un'immagine nel marcatore dell'immagine|
|CELLSJAVA-43389|Impostazioni di protezione password cartella di lavoro/foglio di lavoro perse durante il salvataggio come formato di file XLSB|
|CELLSJAVA-43392| La copia del foglio produce una cartella di lavoro danneggiata|
|CELLSJAVA-43388|Il file di output è danneggiato dopo aver copiato la cartella di lavoro|
|CELLSJAVA-43406|Problemi durante la conversione di HTML in Excel|
|CELLSJAVA-43399|CalculateFormula() crea molti valori di tipo di errore #VALUE|
|CELLSJAVA-43362|Problema di percentuale per le etichette durante la stampa dei grafici|
|CELLSJAVA-43384|Problema relativo alle percentuali per alcune etichette durante il rendering in PDF e la stampa di grafici|
|CELLSJAVA-43402|Genera l'immagine esatta del grafico dal file Excel|
|CELLSJAVA-43408|La parte superiore del grafico viene tagliata e la linea obliqua sale|
|CELLSJAVA-43379|Eccezione sollevata durante il salvataggio della cartella di lavoro come HTML|
|CELLSJAVA-43376|Eccezione "java.lang.ClassCastException: Overflow nella conversione da int a byte. Valore int: 144" durante il caricamento di un file XLSX|
|CELLSJAVA-43387|L'esportazione di un singolo foglio in HTML genera un'eccezione|
|CELLSJAVA-43412|CellsException nella conversione da xlsx a html|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.

### **Costruttore PdfSaveOptions(SaveFormat) obsoleto.**

Utilizzare invece il costruttore PdfSaveOptions().

### **Costruttore XlsbSaveOptions(SaveFormat) obsoleto.**

Utilizzare invece il costruttore XlsbSaveOptions().

### **Costruttore XlsSaveOptions(SaveFormat) obsoleto.**

Utilizzare invece il costruttore XlsSaveOptions().

### **Costruttore SpreadsheetML2003SaveOptions(SaveFormat) obsoleto.**

Utilizzare invece il costruttore SpreadsheetML2003SaveOptions().

### **Aggiunge il metodo Chart.GetChartDataRange().**

Ottiene l'origine dell'intervallo di dati del grafico.

### **Aggiunge il metodo Chart.SwitchRowColumn().**

Scambia riga/colonna dell'origine dell'intervallo di dati del grafico.

### **Aggiunge il metodo OleObject.SetEmbeddedObject().**

Imposta l'oggetto incorporato.

### **Aggiunge il metodo VbaProject.ValidatePassword().**

Convalida la password del progetto VBA.

### **Elimina le proprietà obsolete ChartPoint.MarkerBackgroundColor e Series.MarkerBackgroundColor , aggiunge la proprietà Marker.BackgroundColor.**

Utilizza invece Marker.BackgroundColor.

### **Elimina le proprietà obsolete ChartPoint.MarkerForegroundColor e Series.MarkerForegroundColor , aggiunge la proprietà Marker.ForegroundColor.**

Utilizza invece Marker.ForegroundColor.

### **Elimina le proprietà obsolete ChartPoint.MarkerBackgroundColorSetType e Series.MarkerBackgroundColorSetType , aggiunge la proprietà Marker.BackgroundColorSetType.**

Utilizza invece Marker.BackgroundColorSetType.

### **Elimina le proprietà obsolete ChartPoint.MarkerForegroundColorSetType e Series.MarkerForegroundColorSetType , aggiunge la proprietà Marker.ForegroundColorSetType.**

Utilizza invece Marker.ForegroundColorSetType.

### **Elimina le proprietà obsolete ChartPoint.MarkerSize e Series.MarkerSize.**

Utilizza invece Marker.MarkerSize.

### **Elimina le proprietà obsolete ChartPoint.MarkerStyle e Series.MarkerStyle.**

Utilizza invece Marker.MarkerStyle.

### **Modifica il comportamento di Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

Nelle vecchie versioni, eliminiamo tutte le impostazioni della colonna mentre eliminiamo le righe vuote se il foglio di lavoro è vuoto (nessun dato di celle). Ciò rende impossibile per l'utente eliminare solo le righe vuote e mantenere tutte le impostazioni della colonna. Dalla versione 21.2 non cancelliamo più le impostazioni delle colonne. Se l'utente deve eliminare le impostazioni della colonna per un foglio di lavoro vuoto, deve controllare che non ci siano dati nel foglio e quindi cancellare manualmente ColumnCollection.
Nelle vecchie versioni, non eliminiamo le righe vuote sotto forma. Ciò rende impossibile per l'utente eliminare tutte le righe vuote come previsto. Da 12.2, eliminiamo quelle righe vuote sotto forma insieme ad altre righe vuote comuni.

### **Proprietà Range.CellCount obsoleta.**

Utilizzare invece Range.RowCount e Range.ColumnCount per ottenere il conteggio totale delle celle.

### **Aggiunge la proprietà AutoFilter.ShowFilterButton.**

Indica se mostrare il pulsante filtro del filtro automatico.

### **Elimina la proprietà SeriesCollection.SecondCatergoryData.**

Utilizzare invece la proprietà SeriesCollection.SecondCategoryData.

### **Elimina l'enumerazione StyleModifyFlag.Spacing.**

Non è usato.

### **Aggiunge la proprietà SignatureLine.Id.**

Ottiene o imposta l'identificatore per questa riga della firma.

### **Aggiunge la proprietà DigitalSignature.Id.**

Specifica un UUID che può essere incrociato con l'UUID della riga della firma memorizzata nel contenuto del documento.

### **Aggiunge la proprietà DigitalSignature.ProviderId.**

Specifica l'ID classe del provider della firma.

### **Aggiunge la proprietà DigitalSignature.Image.**

Specifica un'immagine per la firma digitale.

### **Aggiunge la proprietà DigitalSignature.Text.**

Specifica il testo della firma effettiva nella firma digitale.

### **Aggiunge il metodo Cells.ClearMergedCells().**

Rimuove tutte le celle unite.

### **Aggiunge il metodo Workbook.RemovePersonalInformation().**

Rimuove tutte le informazioni personali.

### **Aggiunge la proprietà WorkbookSettings.ForceFullCalculate.**

La proprietà indica a ms excel di eseguire il calcolo completo ogni volta che viene attivato un calcolo.

### **Aggiunge il costruttore DocxSaveOptions(Boolean).**

Rappresenta le opzioni di salvataggio dei file .docx.

### **Elimina la proprietà WorkbookSettings.IsWriteProtected obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.IsWriteProtected.

### **Elimina la proprietà WorkbookSettings.RecommendReadOnly obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.RecommendReadOnly.

### **Elimina la proprietà WorkbookSettings.WriteProtectedPassword obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.Password.

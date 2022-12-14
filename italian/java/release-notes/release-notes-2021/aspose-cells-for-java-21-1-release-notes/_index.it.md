---
title: Aspose.Cells for Java 21.1 Note di rilascio
type: docs
weight: 12
url: /it/java/aspose-cells-for-java-21-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.1/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43375|Controlla la password VBA di Excel|
|CELLSJAVA-43371|La conversione da XLSX a PDF si blocca|
|CELLSJAVA-43353|Diversi diagrammi su excel in pdf|
|CELLSJAVA-43377|Problemi di posizionamento delle immagini durante la conversione di Excel in Html|
|CELLSJAVA-43381|Errore di calcolo della funzione GIORNI|
|CELLSJAVA-43342|Il grafico combinato non può essere visualizzato correttamente in Excel in PDF|
|CELLSJAVA-43354|Le percentuali non sono state mostrate negli istogrammi piccoli|
|CELLSJAVA-40264|Errore con controlli modulo o controlli ActiveX durante il salvataggio come EXCEL_97_TO_2003|
|CELLSJAVA-43372|File danneggiato creato durante la conversione di ODS in XLSX|
|CELLSJAVA-43378|Visualizza come modifiche vuote da true a false dopo la clonazione della cartella di lavoro|
|CELLSJAVA-43379|Eccezione sollevata durante il salvataggio della cartella di lavoro come HTML|
|CELLSJAVA-43376|Eccezione "java.lang.ClassCastException: Overflow nella conversione da int a byte. Valore int: 144" durante il caricamento di un file XLSX|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

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

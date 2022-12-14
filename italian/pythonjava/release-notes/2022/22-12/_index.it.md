---
title: Aspose.Cells per Python tramite Java 22.12 Note di rilascio
type: docs
weight: 1
url: /it/python-java/aspose-cells-for-python-via-java-22-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells per Python via Java 22.12](https://releases.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.12/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43645|L'attributo "formato 3D" del rettangolo non viene visualizzato correttamente|
|CELLSJAVA-44936|Imposta le impostazioni DPI dell'immagine del grafico (PNG).|
|CELLSJAVA-44937|Imposta le impostazioni DPI dell'immagine del grafico (JPG).|
|CELLSJAVA-44998|Le virgolette doppie che causano lo stile in linea non sono riuscite in HTML|
|CELLSJAVA-44970|Ottimizza l'effetto ombra|
|CELLSJAVA-44967|Grafico getDataLabels().getText() che restituisce un valore diverso nella versione 22.6.0 e successive|
|CELLSJAVA-44969|Converti Excel in HTML, le etichette dati visualizzano errori|
|CELLSJAVA-44949|Trasparenza modificata quando si inserisce l'intervallo di Excel come immagine con formato diverso nella diapositiva PowerPoint|
|CELLSJAVA-44985|Conversione da Excel a HTML: la legenda del grafico non viene visualizzata e l'area del tracciato viene troncata|
|CELLSJAVA-44952|Problema con il metodo DataBar.toImage relativo alla larghezza|
|CELLSJAVA-44986|Le immagini importate non sono allineate in linea quando le immagini sono in formato Div|
|CELLSJAVA-44987|Alcune immagini sono coperte da altre durante il caricamento dell'html|
|CELLSJAVA-44988|Il testo non viene ruotato durante il caricamento di html|
|CELLSJAVA-44989|Le impostazioni dei caratteri in div vengono perse durante il caricamento di html|
|CELLSJAVA-44997|Dati e formattazioni persi nella conversione da HTML a Excel|
|CELLSJAVA-44999| Aspose.Cells Le impostazioni di globalizzazione personalizzate non funzionano per la maggior parte della tabella pivot|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge enum JsonExportHyperlinkType**

Rappresenta il tipo di collegamento ipertestuale di esportazione ai file json.

### **Aggiunge JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) e rende obsoleto il metodo ExportRangeToJson(Range, ExportRangeToJsonOptions)**

Usare invece JsonUtility.ExportRangeToJson(Range, JsonSaveOptions).

### **Aggiunge la proprietà PivotTable.DataFieldHeaderName**

Ottiene e imposta il nome dell'intestazione del campo dell'area del valore nella tabella pivot.

### **Aggiunge il metodo di override Range.SetStyle(Style,System.Boolean).**

Sovrascrivi solo la formattazione impostata in modo esplicito quando viene impostato il flag

### **Aggiunge la proprietà PivotField.NonAutoSortDefault**

Indica se un'operazione di ordinamento che verrà applicata a questo campo pivot è un'operazione di ordinamento automatico o un semplice ordinamento dei dati.

### **Aggiunge il metodo GlobalizationSettings.GetDataFieldHeaderNameOfPivotTable()**

Ottiene il nome locale dell'intestazione del campo dell'area del valore nella tabella pivot.

### **Aggiunge la proprietà Chart.PlotVisibleCellsOnly e rende obsoleta la proprietà Chart.PlotVisibleCells.**

Usare invece la proprietà Chart.PlotVisibleCellsOnly.

### **Aggiunge la proprietà JsonSaveOptions.ExportEmptyCells.**

Indica se esportare le celle vuote come null.

### **Aggiunge la proprietà JsonSaveOptions.ExportHyperlinkType.**

Rappresenta il tipo di collegamento ipertestuale di esportazione in json.

### **Aggiunge la proprietà JsonSaveOptions.ExportNestedStructure.**

Esportato come struttura Json della gerarchia padre-figlio.

### **Aggiunge la proprietà JsonSaveOptions.SkipEmptyRows.**

Indica se saltare le righe vuote.

### **Elimina il metodo SheetRender.GetPageSize(System.Int32) obsoleto**

Usare invece SheetRender.GetPageSizeInch(System.Int32).

### **Elimina il metodo WorkbookRender.GetPageSize(System.Int32) obsoleto**

Usare invece WorkbookRender.GetPageSizeInch(System.Int32).

### **Elimina l'enumerazione AutoShapeType.TextWave3 e AutoShapeType.TextWave4 obsoleta**

Usare invece UseAutoShape.TextDoubleWave1 e UseAutoShape.TextDoubleWave2.
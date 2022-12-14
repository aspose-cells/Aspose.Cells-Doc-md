---
title: Aspose.Cells per Android tramite Java 22.12 Note di rilascio
type: docs
weight: 1
url: /it/java/aspose-cells-for-android-via-java-22-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 22.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44890|supporta il file di importazione con openpassword per GridWeb|
|CELLSJAVA-43645|L'attributo "formato 3D" del rettangolo non viene visualizzato correttamente|
|CELLSJAVA-44936|Imposta le impostazioni DPI dell'immagine del grafico (PNG).|
|CELLSJAVA-44937|Imposta le impostazioni DPI dell'immagine del grafico (JPG).|
|CELLSJAVA-44998|Le virgolette doppie che causano lo stile in linea non sono riuscite in HTML|
|CELLSJAVA-44884| I numeri di elenco non sono corretti dopo la conversione da XLSX a HTML o PDF|
|CELLSJAVA-44883|La cartella di lavoro contenente la tabella pivot viene danneggiata dopo l'elaborazione della tabella pivot al suo interno|
|CELLSJAVA-44879|Il risultato formattato per GridWeb era diverso da Cell.DisplayStringValue|
|CELLSJAVA-44327|Bordi e meno linee mostrate nelle fette di torta in bianco e nero nel grafico per il rendering dell'immagine|
|CELLSJAVA-44853|I dati sull'angolo dell'asse x non sono gli stessi di Excel nel grafico per il rendering dell'immagine|
|CELLSJAVA-44854|I dati sul passaggio dell'asse y non sono gli stessi di Excel nel rendering da grafico a immagine|
|CELLSJAVA-44904|Problemi durante il rendering dei grafici Excel nella conversione JPG|
|CELLSJAVA-44850|Importando un file XLT, il testo non viene visualizzato completamente utilizzando le demo più recenti con l'ultima versione Aspose.Cells.GridWeb con i file di risorse più recenti|
|CELLSJAVA-44857|Quando si utilizza la versione Aspose.Cells.GridWeb for Java v22.8 con i file di risorse più recenti per aprire un documento Excel, l'effetto delle celle è diverso dal documento originale|
|CELLSJAVA-44903|La resa SVG non funziona come previsto|
|CELLSJAVA-44909| Quando più righe sono in grassetto, sembra che trabocchi inutilmente sulle altre righe|
|CELLSJAVA-44888|"+" e "-" sono scomparsi dopo la conversione: rendering da Excel a HTML|
|CELLSJAVA-44775|Etichette del grafico sovrapposte nel rendering del grafico all'immagine|
|CELLSJAVA-44882|Rendering dal grafico all'immagine: una delle etichette si trova all'interno del grafico ad anello|
|CELLSJAVA-44943|Da XLSX a PDF: le etichette dei grafici non sono visualizzate correttamente|
|CELLSJAVA-44928|Da XLS a PDF: dati insufficienti per un'immagine|
|CELLSJAVA-44910|Converti Excel in HTML produce migliaia di piccole immagini simili|
|CELLSJAVA-44944|Il ridimensionamento delle tabelle modifica la formattazione delle celle|
|CELLSJAVA-44948| Le immagini non possono essere visualizzate nel foglio durante la conversione da HTML a Excel|
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
|CELLSJAVA-44898|La lettura da GZIPInputStream a volte genera un falso errore "File danneggiato" nelle versioni 22.7 e successive|
|CELLSJAVA-44881|Eccezione "java.lang.ArrayIndexOutOfBoundsException: 15070" durante il caricamento di un file XLS|
|CELLSJAVA-44908|Eccezione "java.lang.OutOfMemoryError: Java spazio heap" durante il caricamento di file XLSB di grandi dimensioni|
|CELLSJAVA-44929|Regressione: "java.lang.NullPointerException" su Workbook.calculateFormula()|
|CELLSJAVA-44927|Eccezione "java.lang.IndexOutOfBoundsException: Index: 5, Size: 5" durante la conversione di file Excel in HTML|
|CELLSJAVA-44939|Errore "java.lang.StringIndexOutOfBoundsException: Indice stringa fuori intervallo: 0" durante il tentativo di leggere un file Excel|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.

### **Modificato il limite di spostamento delle celle fuori dal foglio per l'inserimento di righe**

Nelle vecchie versioni, se ci sono celle che hanno impostazioni di formattazione ma non hanno valore e verranno spostate fuori dal foglio, l'operazione di inserimento non è consentita. Dal 22.10, l'operazione di inserimento è consentita per questo tipo di situazione e tale comportamento è lo stesso con ms excel ora.

### **Aggiunge la classe DataModelConnection**

Specifica una connessione al modello di dati.

### **Aggiunge i metodi Chart.ChangeTemplate(byte[]).**

Modifica il tipo di grafico con il file modello preimpostato.

### **Aggiunge il metodo ChartCollection.Add(byte[] data, string dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Aggiunge grafico con file modello preimpostato.

### **Aggiunge la proprietà Cell.IsDynamicArrayFormula**

Indica se la formula della cella è una formula di matrice dinamica (vero) o una formula di matrice legacy (falso).

### **Rende obsoleta la proprietà SparklineGroup.SparklineCollection e aggiunge la proprietà SparklineGroup.Sparklines**

Usare invece la proprietà SparklineGroup.Sparklines.

### **Rende obsoleta la proprietà Worksheet.SparklineGroupCollection e aggiunge la proprietà Worksheet.SparklineGroups**

Usare invece la proprietà Worksheet.SparklineGroups.

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


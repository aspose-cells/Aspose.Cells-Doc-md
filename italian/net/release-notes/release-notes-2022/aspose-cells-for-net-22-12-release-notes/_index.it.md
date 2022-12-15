---
title: Aspose.Cells for .NET 22.12 Note di rilascio
type: docs
weight: 1
url: /it/net/aspose-cells-for-net-22-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.12](https://www.nuget.org/packages/Aspose.Cells/22.12.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42315|Supporto per file crtx - applicazione di modelli di grafici personalizzati|
|CELLSNET-47895|Le immagini sono distorte nel rendering da Excel a PDF/HTML|
|CELLSNET-47946|L'effetto di rotazione dell'immagine non viene visualizzato correttamente in pdf/html|
|CELLSNET-47947|L'effetto di rotazione della scatola rettangolare nel gruppo grafico non viene visualizzato correttamente in pdf/html|
|CELLSNET-52126|Alcune forme vengono modificate dopo la conversione del file Excel in PDF|
|CELLSNET-52197|Caselle modificate durante la conversione del documento XLSX in PDF|
|CELLSNET-52330|Le forme del disegno non vengono visualizzate correttamente in HTML|
|CELLSNET-50042| Il nome definito viene modificato dopo il nuovo salvataggio|
|CELLSNET-52270|YEARFRAC La funzione non viene calcolata correttamente|
|CELLSNET-52305|MMULT con OFFSET non viene calcolato correttamente|
|CELLSNET-52307|La formula del collegamento interrotto restituisce 0 invece di #REF!|
|CELLSNET-52325| Workbook.CalculateFormula si blocca in alcune circostanze|
|CELLSNET-52387|Cell i riferimenti alle tabelle generano errori #REF dopo l'eliminazione delle colonne|
|CELLSNET-52290|Grafici Asse non catturato correttamente|
|CELLSNET-52301|Grafico XLSX a immagine: barre del grafico combinate personalizzate visualizzate in modo errato|
|CELLSNET-52336|Il grafico dell'istogramma non viene visualizzato correttamente nella conversione da XLSX a HTML/PDF|
|CELLSNET-52292|Il testo viene visualizzato nella pagina sbagliata nel PDF di output - Conversione da Excel a PDF|
|CELLSNET-52367|AutofitRows genera testo ritagliato nell'output di conversione PDF|
|CELLSNET-52242|La gerarchia padre-figlio non è corretta durante la conversione di Excel in JSON e viceversa|
|CELLSNET-52281|L'intestazione Json non può essere ignorata|
|CELLSNET-52289|Il formato numerico viene perso durante la conversione di HTML in Excel|
|CELLSNET-52298|L'opzione Ordinamento automatico è abilitata per il campo pivot durante il nuovo salvataggio di XLSX|
|CELLSNET-52299| L'attributo HasRevisions non è corretto dopo il salvataggio di una cartella di lavoro|
|CELLSNET-52332|I numeri vengono visualizzati come '#' o numero scientifico durante la conversione in html|
|CELLSNET-52338| L'HTML di output è non deterministico|
|CELLSNET-52344|Mancano collegamenti ipertestuali nella conversione da HTML a JSON|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

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

Utilizzare invece WorkbookRender.GetPageSizeInch(System.Int32).

### **Elimina l'enumerazione AutoShapeType.TextWave3 e AutoShapeType.TextWave4 obsoleta**

Usare invece UseAutoShape.TextDoubleWave1 e UseAutoShape.TextDoubleWave2.

---
title: Aspose.Cells for .NET 21.1 Note di rilascio
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-21-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.1](https://www.nuget.org/packages/Aspose.Cells/21.1.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47376|Rilascio Aspose.Cells for .NET 5.0|Nuova caratteristica|
|CELLSNET-40624| Come cambiare le serie di dati riga/colonna usando aspose|Nuova caratteristica|
|CELLSNET-42195|Converti il controllo da xlsm a xls|Nuova caratteristica|
|CELLSNET-47806|Ottiene l'intervallo di origini dati del grafico.|Nuova caratteristica|
|CELLSNET-47756|Le forme SmartArt non vengono visualizzate correttamente nella conversione da Excel a PDF|Insetto|
|CELLSNET-47391|Le forme non sono posizionate correttamente nelle conversioni da Excel a PDF|Insetto|
|CELLSNET-47766|Il grafico della freccia è incompleto|Insetto|
|CELLSNET-47653|I blocchi Diagram vengono spostati durante la conversione in HTML|Insetto|
|CELLSNET-47720|Markup CSS e HTML non valido durante la conversione di XLSX in HTML|Insetto|
|CELLSNET-47746|Virgolette non codificate nei valori degli attributi HTML|Insetto|
|CELLSNET-47792|Le immagini si sovrappongono al testo durante l'importazione di HTML in Excel|Insetto|
|CELLSNET-47797|Collegamento errato quando il file XLSM viene visualizzato in HTML|Insetto|
|CELLSNET-47807|Markup HTML non valido con elementi A nidificati|Insetto|
|CELLSNET-47778|Il calcolo IRR restituisce #NUM|Insetto|
|CELLSNET-47814|Le barre di scorrimento di GridDesktop non sono nascoste|Insetto|
|CELLSNET-47744|I grafici radiali vengono schiacciati quando vengono esportati in pdf|Insetto|
|CELLSNET-47786|XErrorBar non viene visualizzato nel grafico|Insetto|
|CELLSNET-47787|XErrorBars scompare quando si copia il grafico da una cartella di lavoro a un'altra|Insetto|
|CELLSNET-43907|WordArt non viene visualizzato durante la conversione di XLS in PDF|Insetto|
|CELLSNET-47780|Problema durante l'impostazione di due intervalli come origine dati del grafico|Insetto|
|CELLSNET-47781|Il testo a capo non funziona per i file ODS|Insetto|
|CELLSNETCORE-94| Il gruppo di tabelle pivot per giorno aumenta quando viene aggiornato|Insetto|
|CELLSNETCORE-77|Errore durante la conversione di XLSX in PDF in Azure|Insetto|
|CELLSNETCORE-90|Problemi durante l'inserimento di allegati nel foglio di lavoro Excel|Insetto|
|CELLSNETCORE-93|Tag H1 non reso senza tag aggiuntivi come sottolineato, corsivo o grassetto|Insetto|
|CELLSNETCORE-97|La chiamata a RemoveExternalLinks() solleva un'eccezione|Insetto|
|CELLSNET-47719|Impossibile salvare xlsb in xlsx|Eccezione|
|CELLSNET-47784|Eccezione durante l'importazione di documenti HTML con IStreamProvider|Eccezione|
|CELLSNET-47801|CalculateData sulla tabella pivot genera un'eccezione|Eccezione|
|CELLSNET-47809|Cell.ContainsExternalLink genera "Impossibile trasmettere|Eccezione|
|CELLSNET-47791| Grafico che causa l'esito negativo di Workbook.Save|Eccezione|
|CELLSNET-47808|Eccezione sollevata durante il calcolo di un grafico vuoto|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Elimina la proprietà ReplaceOptions.IsCaseSensitive obsoleta (SOLO .NET).**

Utilizzare invece ReplaceOptions.CaseSensitive.

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


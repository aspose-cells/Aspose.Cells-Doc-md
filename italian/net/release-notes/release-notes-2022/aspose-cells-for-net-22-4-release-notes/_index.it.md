---
title: Aspose.Cells for .NET 22.4 Note di rilascio
type: docs
weight: 9
url: /it/net/aspose-cells-for-net-22-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.4](https://www.nuget.org/packages/Aspose.Cells/22.4.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50624|Supporto per rimuovere le celle vuote di coda per il salvataggio di csv|
|CELLSNET-50747|Aggiungi Style.HasBorders per verificare se ci sono bordi per esso|
|CELLSNET-50627|Ottieni l'intervallo unito rispetto alla cella del foglio di lavoro in Aspose.Cells.GridDesktop|
|CELLSNET-50675|aggiungi GridLoadDataFilterOptions per GridDesktop e Worksheet.GetMergeByCell api|
|CELLSNET-50816|Supporta temi ad alto contrasto in Aspose.Cells.GridDesktop|
|CELLSNET-50751|Supporta PasteType.ValuesAndFormats durante la copia dell'intervallo.|
|CELLSNET-50620|Quando si converte xls in pdf, la dimensione della riga vuota del testo nella casella di testo non viene visualizzata correttamente|
|CELLSNET-50684|Problema con l'estrazione degli allegati OLE dal file ODS|
|CELLSNET-50712|Gli effetti e le forme WordArt non vengono visualizzati correttamente nella conversione da Excel a PDF|
|CELLSNET-50714|Il file XLSB è danneggiato durante l'apertura e il salvataggio tramite API Aspose.Cells|
|CELLSNET-50778|Mancano linee verticali per la tabella pivot nel PDF di output|
|CELLSNET-50517|Riferimento errato nella formula di formattazione condizionale dopo l'inserimento/eliminazione di righe|
|CELLSNET-50622|L'intestazione riga/colonna vuota con stile personalizzato non viene esportata in csv|
|CELLSNET-50645|Risultati errati con il metodo Workbook.CalculateFormula|
|CELLSNET-50695|Name.RefersTo/R1C1RefersTo modificato quando si fa riferimento a un indirizzo di cella singola|
|CELLSNET-50553| Lo stile della colonna non viene applicato alla colonna completa in GridDesktop|
|CELLSNET-50641|Problema con l'apertura di un file protetto da password con password vuota ("") in Aspose.Cells.GridDesktop|
|CELLSNET-50672| aggiungere l'evento FailLoadFile|
|CELLSNET-50815| il comportamento del doppio clic sulla modifica del valore della cella non è corretto|
|CELLSNET-50594|Il testo è nascosto dietro i campi di input durante la conversione di XLSX in HTML|
|CELLSNET-50665|Convalida Pdf/A-1b non riuscita dopo aver impostato CreatedTime durante la conversione in pdf|
|CELLSNET-50701|La luminosità e il contrasto dell'immagine inserita vengono reimpostati nella conversione da Excel a PDF|
|CELLSNET-50834|Problema con le celle unite della tabella nella conversione da Excel a HTML|
|CELLSNET-50595|Da XLSX a SVG: Differenze nel grafico|
|CELLSNET-50596|Le unità dell'asse non vengono modificate nel file XLSX di output|
|CELLSNET-50740|Da XLSX a JPG: testo spostato a destra sui grafici|
|CELLSNET-50309|Intervallo a PNG: output non come previsto|
|CELLSNET-50610|RecalculateBeforeSave sempre false nelle versioni più recenti|
|CELLSNET-50611|Problema con il valore booleano nel rendering da Excel a PDF|
|CELLSNET-50706| La dimensione del file si è ridotta molte volte quando si salva con SaveToStream() la seconda volta|
|CELLSNET-50749|DeleteBlankColumns(options) metodo che elimina le colonne che hanno solo commenti|
|CELLSNET-50759|Le formule non vengono salvate correttamente quando una cartella di lavoro contiene collegamenti esterni a una cartella di lavoro che non è stata salvata|
|CELLSNET-50776|Gli indicatori intelligenti non vengono elaborati quando si utilizza un elenco generico di tipo System.Dynamic.ExpandoObject come origine dati per oggetti nidificati|
|CELLSNET-50779| Potenziale perdita di dati relativi agli oggetti incorporati durante la conversione di XLS -> XLSX -> XLS|
|CELLSNET-50821|Problema con Range.AutoFill: i dati non vengono compilati automaticamente correttamente se l'area dell'intervallo è intersecata|
|CELLSNET-50777|Il metodo PutValue genera System.StackOverflowException nel formato regionale australiano|
|CELLSNET-50275|Eccezione "Riferimento oggetto non impostato su un'istanza di un oggetto" durante il rendering di ODS in HTML|
|CELLSNET-50713|System.NullReferenceException durante il caricamento di un file XLSB|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la classe DefaultStyleSettings.**

Gruppo di valori predefiniti per le proprietà relative allo stile.

### **Aggiunge la proprietà LoadOptions.DefaultStyleSettings.**

Supporto per impostare i valori predefiniti delle proprietà relative allo stile per l'inizializzazione di una cartella di lavoro.

### **Aggiunge la proprietà TxtSaveOptions.TrimTailingBlankCells.**

Supporto per rimuovere tutte le celle vuote (caratteri ripetuti di separatore come "~,~,~,~,") alla fine del record di riga durante l'esportazione di csv/tsv.

### **Aggiunge la proprietà Style.HasBorders.**

Supporto per verificare se sono stati impostati bordi per lo stile.

### **Proprietà LoadOptions.StandardFont/StandardFontSize obsolete.**

Utilizzare invece LoadOptions.DefaultStyleSettings.FontName/FontSize.

### **Rimuove l'enumerazione obsoleta StyleModifyFlag.FontSubscript e FontSuperscript.**

Utilizzare invece StyleModifyFlag.FontScript.

### **Proprietà Shape.ConnectionPoints obsolete.**

Utilizzare invece il metodo GetConnectionPoints().

### **Aggiunge il metodo Shape.GetConnectionPoints().**

Ottieni i punti di connessione.

### **Aggiunge le proprietà Row.IsCollapsed e Column.IsCollapsed.**

Indica se la riga e la colonna sono compresse.

### **Aggiunge l'enumerazione PasteType.ValuesAndFormats.**

Indica solo la copia di valori e formati.

### **Aggiunge la proprietà Shape.IsInGroup.**

Indica se la forma è raggruppata.

### **Aggiunge il metodo AutoFilter.GetCellArea().**

Ottiene l'area a cui si applica il filtro automatico specificato.

### **Aggiunge il metodo Cells.GetRowOriginalHeightPoint().**

Ottiene l'altezza della riga originale, in unità di punti.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, PivotField baseField).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, int row, int column, PivotField baseField).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, int baseFieldIndex).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, int row, int column, int baseFieldIndex).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, string baseFieldName).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge l'enumerazione DataLabelShapeType.Line.**

Rappresenta la forma della linea. Questo tipo non è disponibile in Excel, viene utilizzato solo per alcuni file speciali.

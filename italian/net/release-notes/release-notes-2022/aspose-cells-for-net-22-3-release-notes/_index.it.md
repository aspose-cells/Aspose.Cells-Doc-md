---
title: Aspose.Cells for .NET 22.3 Note di rilascio
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-22-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.3](https://www.nuget.org/packages/Aspose.Cells/22.3.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50375|Supporta l'ordinamento di PivotField tramite i valori nella riga/colonna selezionata|
|CELLSNET-50559|Supporto per ottenere le foglie della cella in modo ricorsivo|
|CELLSNET-50512|Supporto per ricalcolare le celle che fanno riferimento al nome definito quando il nome definito viene modificato e la catena di calcolo è abilitata|
|CELLSNET-50403|Aggiungere SaveFormat.Ots e SaveFormat.Xlt|
|CELLSNET-50422|Supporta l'impostazione all'interno dei bordi|
|CELLSNET-50342|Tabella pivot non ordinata all'aggiornamento|
|CELLSNET-50451|L'eliminazione del foglio di lavoro comporta l'eliminazione dei filtri dei dati|
|CELLSNET-50462|Regressione: dopo aver copiato l'intervallo di celle, le formule vengono perse|
|CELLSNET-50545| I campi formattati in modo condizionale non sono colorati con il colore giusto|
|CELLSNET-50565|Le formule non sono state calcolate correttamente|
|CELLSNET-50309|Intervallo fino a PNG: output non come previsto|
|CELLSNET-50334|Regressione: da XLS a PDF: intestazione non visualizzata correttamente|
|CELLSNET-50367|La conversione da .XLSX a PDF richiede molto tempo e produce pagine extra|
|CELLSNET-50401|I valori numerici oi numeri seguiti da voci non sono visibili nel pdf risultante|
|CELLSNET-50478|Workbook.ExportXml restituisce solo la prima riga dei dati della tabella|
|CELLSNET-50507|Xml Import mostra le colonne precedentemente nascoste nel modello|
|CELLSNET-50554|Il contenuto non viene visualizzato correttamente nella conversione da Excel a PDF|
|CELLSNET-50316|I testi a capo non funzionano sui grafici durante la generazione di PDF|
|CELLSNET-50411|Le etichette dell'asse orizzontale del grafico non vengono visualizzate correttamente nell'output PDF|
|CELLSNET-50341|Problema con Comprimi ed espandi gruppi a più livelli|
|CELLSNET-50368|Conversione da ODS a PDF errata|
|CELLSNET-50377|La formattazione personalizzata "Testo" non viene applicata nel file XLS|
|CELLSNET-50380| La proprietà ImportTableOptions.IsHtmlString non restituisce correttamente i collegamenti|
|CELLSNET-50418|Carica HTML nella cartella di lavoro non funzionante|
|CELLSNET-50494|Problema con il colore per le celle formattate in modo condizionale nel file di output XLSX|
|CELLSNET-50563|Problema durante l'impostazione della licenza incorporata su Produci singolo file nell'applicazione .NET 6.0|
|CELLSNET-50585|Nessuna barra in avanti ma barre all'indietro per collegamenti esterni con URL|
|CELLSNET-50390| System.ArgumentException: il numero di riga o il numero di colonna non può essere zero durante l'importazione dei dati JSON come tabella|
|CELLSNET-50555| ArgumentOutOfRangeException durante il tentativo di ottenere la formula di una cella|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Modifica il valore predefinito di HtmlSaveOptions.ExcludeUnusedStyles.**

Quando si salvano i file html, per le vecchie versioni a volte rimuoviamo automaticamente gli stili inutilizzati quando ci sono molti oggetti di stile nel pool, indipendentemente dal valore di questa proprietà. Per i file html generati, l'esclusione degli stili inutilizzati può ridurre le dimensioni del file senza influire sugli effetti visivi. Quindi da questa versione rendiamo vero il valore predefinito di questa proprietà per renderlo coerente con il comportamento di salvataggio. Se l'utente deve mantenere tutti gli stili nella cartella di lavoro per l'html generato (come lo scenario in cui l'utente deve ripristinare la cartella di lavoro dall'html generato in un secondo momento), impostare questa proprietà su false durante il salvataggio dell'html.

### **Aggiunge il metodo Cell.GetLeafs(bool recursive).**

Supporta l'utente a ottenere ricorsivamente tutte le foglie di una cella.

### **Aggiunge il metodo Range.SetInsideBorders(BorderType, CellBorderType, CellsColor).**

Supporto per impostare i bordi interni per l'intervallo.

### **Aggiunge SaveFormat.Ots, SaveFormat.Xlt e LoadFormat.Ots enum.**

Miglioramento per il caricamento e il salvataggio di file ots e xlt.

### **Aggiunge la classe FormulaSettings.**

Separare tutte le impostazioni relative alle formule da WorkbookSettings e raggrupparle come FormulaSettings.

### **Aggiunge la proprietà WorkbookSettings.FormulaSettings.**

Ottiene le impostazioni raggruppate per le formule.

### **Aggiunge la proprietà PivotItem.IsHideDetail.**

Ottiene e imposta se l'elemento pivot nasconde i dettagli.

### **Proprietà WorkbookSettings.ReCalculateOnOpen obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.CalculateOnOpen.

### **Proprietà WorkbookSettings.RecalculateBeforeSave obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.CalculateOnSave.

### **Proprietà WorkbookSettings.ForceFullCalculate obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.ForceFullCalculation.

### **Proprietà WorkbookSettings.PrecisionAsDisplayed obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.PrecisionAsDisplayed.

### **Proprietà WorkbookSettings.CalcMode obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.CalculationMode.

### **Proprietà WorkbookSettings.Iteration obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.EnableIterativeCalculation.

### **Proprietà WorkbookSettings.MaxIteration obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.MaxIteration.

### **Proprietà WorkbookSettings.MaxChange obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.MaxChange.

### **Proprietà WorkbookSettings.CalculationId obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.CalculationId.

### **Proprietà WorkbookSettings.CreateCalcChain obsoleta.**

Utilizzare invece WorkbookSettings.FormulaSettings.EnableCalculationChain.

### **Proprietà WorkbookSettings.CalcStackSize obsoleta.**

Utilizzare invece CalculationOptions con la dimensione dello stack specificata durante il calcolo delle formule.

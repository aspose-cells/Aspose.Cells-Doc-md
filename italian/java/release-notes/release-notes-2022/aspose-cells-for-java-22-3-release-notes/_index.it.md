---
title: Aspose.Cells for Java 22.3 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-22-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 22.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.3/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44369| l'altezza della forma non è corretta|
|CELLSJAVA-44366|Copiare il contenuto del foglio in una nuova pagina del foglio e salvarlo come html causa uno stile anomalo della formula matematica di Excel|
|CELLSJAVA-44408|Il formato percentuale di Cell viene perso quando espandiamo quelle 2 righe che abbiamo modificato|
|CELLSJAVA-44341|La larghezza Cell non è corretta nell'output DOCX nella conversione da Excel a DOCX|
|CELLSJAVA-44383|La formattazione condizionale ha smesso di funzionare dopo l'aggiunta di proprietà personalizzate|
|CELLSJAVA-44370|Il file Excel viene danneggiato quando viene aperto e salvato con Aspose.Cells|
|CELLSJAVA-44344| Problema con la copia orizzontale degli intervalli nell'output XLSX|
|CELLSJAVA-44363| l'altezza dell'intestazione della riga non corrisponde al contenuto della riga nel file con freezepane|
|CELLSJAVA-44349|l'immagine/forma deve essere conservata dopo il riavvio del server per GridWeb|
|CELLSJAVA-44367|Il colore dell'istogramma diventa bianco durante la conversione in html|
|CELLSJAVA-44328| Alcune etichette dati dei grafici Excel vengono perse durante il salvataggio del file Excel come HTML|
|CELLSJAVA-44193|L'angolo degli elementi dell'asse delle categorie nel grafico è diverso nella conversione da Excel a PDF|
|CELLSJAVA-44314|Etichette dell'asse delle categorie del grafico errate nel rendering dal grafico all'immagine|
|CELLSJAVA-44332|Cell la sottolineatura del collegamento non può essere rimossa quando si converte xlsx in html|
|CELLSJAVA-44323|Eccezione durante l'aggiunta della riga della firma|
|CELLSJAVA-44361|CellsException sollevata durante la conversione di xlsx in html|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

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
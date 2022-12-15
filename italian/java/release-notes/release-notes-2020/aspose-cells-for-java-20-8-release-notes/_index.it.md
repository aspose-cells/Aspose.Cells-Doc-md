---
title: Aspose.Cells for Java 20.8 Note di rilascio
type: docs
weight: 8
url: /it/java/aspose-cells-for-java-20-8-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.8/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43242|Uno dei tag di stile trovati al di fuori del tag Head|Insetto|
|CELLSJAVA-43157|Il colore delle serie di dati personalizzate non viene mantenuto durante la creazione di un grafico a cascata|Insetto|
|CELLSJAVA-43240|Interruzioni di riga involontarie in forme/oggetti durante la conversione di Excel in PDF|Insetto|
|CELLSJAVA-43255|Problema di prestazioni nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-43250|Le celle delle etichette espanse non vengono unite in SmartMarker|Insetto|
|CELLSJAVA-43253|Il salvataggio del file utilizzando OoxmlSaveOptions dopo aver sostituito il testo in SmartArt converte XLS in XLSX|Insetto|
CELLSJAVA-43170|CellsException sul metodocalcFormula|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Contrassegna l'interfaccia ICustomFunction come obsoleta.**

 Questa interfaccia a volte causa ambiguità e incomprensioni per gli utenti. L'utente dovrebbe usare**Motore di calcolo astratto** invece che fornisce API più convenienti e flessibili per la manipolazione di funzioni personalizzate.

### **Contrassegna la proprietà CalculationOptions.CustomFunction come obsoleta.**

 Si prega di utilizzare**Motore di calcolo astratto** invece di**IFunzione personalizzata** dalla proprietà CalculationOptions.CustomEngine.

### **Contrassegna il metodo Workbook.CalculateFormula(bool, ICustomFunction) come obsoleto.**

 Si prega di utilizzare**Metodo Workbook.CalculateFormula(CalculationOptions).** invece.

### **Contrassegna il metodo Worksheet.CalculateFormula(bool, bool, ICustomFunction) come obsoleto.**

 Si prega di utilizzare**Worksheet.CalculateFormula(CalculationOptions, bool)** metodo invece.

### **Contrassegna il metodo Cell.Calculate(bool, ICustomFunction) come obsoleto.**

 Si prega di utilizzare**Cell.Calcola(Opzioni Calcolo)** metodo invece.

### **Aggiunge la classe DocxSaveOptions e l'enumerazione SaveFormat.Docx**

Rappresenta le opzioni e l'enumerazione per il salvataggio della cartella di lavoro come file con estensione docx.

### **Aggiunge la classe PptxSaveOptions e l'enumerazione SaveFormat.Pptx**

Rappresenta le opzioni e l'enumerazione per il salvataggio della cartella di lavoro come file con estensione pptx.

### **Aggiunge la classe PowerQueryFormulaFunction**

Rappresenta la funzione della formula di query di potenza.

### **Aggiunge SaveOptions.UpdateSmartArt ed elimina la proprietà OoxmlSaveOptions.UpdateSmartArt**

Indica se aggiornare il testo delle forme artistiche intelligenti durante il salvataggio dei file.

### **Aggiunge il metodo SlicerCollection.Add(ListObject table, int index, string destCellName).**

Aggiungi un nuovo Slicer utilizzando ListObject come origine dati.

### **Aggiunge il metodo SlicerCollection.Add(ListObject table, ListColumn listColumn, string destCellName)**

Aggiungi un nuovo Slicer utilizzando ListObject come origine dati.

### **Aggiunge il metodo SlicerCollection.Add(ListObject table, ListColumn listColumn, int row, int column)**

Aggiungi un nuovo Slicer utilizzando ListObject come origine dati.

---
title: Aspose.Cells for Java 8.8.1 Note di rilascio
type: docs
weight: 100
url: /it/java/aspose-cells-for-java-8-8-1-release-notes/
---
## **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41664 |Esportazione di DataBars in base alla formattazione condizionale in HTML| Nuova caratteristica|
|CELLSJAVA-40746 | Supporta ColorScale, DataBar, IconSet durante l'esportazione di XLSX in HTML| Nuova caratteristica|
|CELLSJAVA-41820 | Il foglio di lavoro non ha metodo calcualteFormula (formula stringa, opzioni CalculationOptions)| Nuova caratteristica|
|CELLSJAVA-40544 | Collo di bottiglia delle prestazioni su Workbook.calculateFormula| Aumento|
|CELLSJAVA-41817 | L'impostazione ShowAllItems per PivotField non sembra avere effetto| Insetto|
|CELLSJAVA-41810 | Il testo sta diventando congestionato e si sovrappone nell'immagine EMF| Insetto|
|CELLSJAVA-41801 | Le etichette di testo si sovrappongono nell'immagine EMF| Insetto|
|CELLSJAVA-41834 | Viene generata un'eccezione durante la copia della cartella di lavoro| Insetto|
|CELLSJAVA-41819 | Foglio di calcolo in HTML: l'allineamento del testo in una forma è errato dopo aver copiato il tema dal foglio di calcolo di origine| Insetto|
|CELLSJAVA-41824 | Il grafico non viene visualizzato nel PDF di output| Insetto|
|CELLSJAVA-41805 | Etichette dell'asse X mancanti nel PDF del grafico| Insetto|
|CELLSJAVA-41767 | Formato numerico errato delle etichette dell'asse X nel PDF del grafico| Insetto|
|CELLSJAVA-41640 | I trattini lunghi non vengono visualizzati correttamente nel PDF/immagine di output per il grafico| Insetto|
|CELLSJAVA-41604 | Le linee della griglia orizzontale del grafico non vengono visualizzate correttamente nel PDF di output| Insetto|
|CELLSJAVA-41832 |Mancano alcune barre del grafico durante il rendering da foglio di lavoro a immagine| Insetto|
|CELLSJAVA-41837 | Aggiungi Chart.toPDF(java.io.OutputStream, com.aspose.cells.PdfSaveOptions)| Insetto|
|CELLSJAVA-41839 | Un intervallo denominato viene creato quando il metodo Cells.copyRow() viene utilizzato all'interno di un intervallo denominato| Insetto|
|CELLSJAVA-41838 | Quando si applica autoSizeColumns sul foglio, la colonna non viene allargata correttamente| Insetto|
|CELLSJAVA-41835 | CellsException durante il salvataggio del foglio di calcolo in PDF| Eccezione|
|CELLSJAVA-41826 | Eccezione NaN| Eccezione|
## **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41719 | Come creare pulsanti di comando personalizzati in GridWeb (JAVA)| Nuova caratteristica|
|CELLSJAVA-41718 | Il metodo GridCell.createValidation() non è presente in GridWeb| Aumento|
|CELLSJAVA-41649 | Lo scorrimento non si ferma a volte - Aspose.Cells.GridWeb per JAVA| Insetto|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà WorkbookSettings.PaperSize.**
Viene utilizzato per impostare il formato carta della stampante predefinita come formato carta predefinito della cartella di lavoro.
### **Aggiunge la classe LoadDataFilterOptions e la proprietà LoadOptions.LoadDataFilterOptions.**
Viene utilizzato per specificare quale tipo di dati deve essere caricato durante la creazione della cartella di lavoro dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per lo scopo speciale dell'utente, in particolare quando si utilizzano le API LightCells.
### **Aggiunge il metodo Worksheet.CalculateFormula(string formula, CalculationOptions opts).**
Viene utilizzato per calcolare una determinata formula direttamente con le opzioni personalizzate dell'utente.
### **Aggiunge le classi dello spazio dei nomi Aspose.Cells.Drawing.Texts.**
Viene utilizzato per impostare le proprietà del carattere del testo della forma.
### **Proprietà Shape.TextFrame obsoleta.**
Usare invece la proprietà Shape.TextBody.TextAlignment.
### **Aggiunge la proprietà Shape.TextBody.**
Presenta l'impostazione del testo della forma.
### **Aggiunge il metodo GridCell.CreateValidation(GridValidationType validationType, bool isRequired).**
Crea un oggetto di convalida per una cella della griglia.
### **Aggiunge il metodo GridCell.RemoveValidation().**
Rimuove l'oggetto di convalida da una cella della griglia.
### **Aggiunge il metodo Chart.ToPdf(System.IO.Stream stream).**
Aggiunge il grafico di salvataggio al PDF come flusso.

{{% alert color="primary" %}} 

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.8.1 sono inclusi anche in questo Aspose.Cells for Java v8.8.1.

{{% /alert %}}

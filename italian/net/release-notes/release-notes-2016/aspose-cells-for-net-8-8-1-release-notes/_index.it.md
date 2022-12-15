---
title: Aspose.Cells for .NET 8.8.1 Note di rilascio
type: docs
weight: 100
url: /it/net/aspose-cells-for-net-8-8-1-release-notes/
---
### **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSNET-41817 | Impostazione dell'effetto del testo su Offset in forma rettangolare| Nuova caratteristica|
|CELLSNET-44407 | Lo spessore del bordo viene ridotto durante il rendering quando l'area di stampa passa attraverso le celle che condividono il bordo| Aumento|
|CELLSNET-44413 |Impostare il valore predefinito di WorkbookSettings.IsDefaultEncrypted su false| Aumento|
|CELLSNET-44392 | Aspose.Cells.xml non è presente nella cartella ".\Bin\net4.0"| Aumento|
|CELLSNET-44291 | Ottimizza il codice per rendere più efficienti le colonne e le righe vuote nascoste| Aumento|
|CELLSNET-44417 | L'API si blocca durante la conversione di un foglio di calcolo danneggiato e infetto in PDF| Prestazione|
|CELLSNET-44088 | Le icone per le regole di formattazione condizionale non vengono visualizzate in HTML| Insetto|
|CELLSNET-44263 | La formattazione viene persa durante l'importazione di HTML come XLSX| Insetto|
|CELLSNET-44427 | Le date in formato ISO 8601 vengono trattate come stringhe invece che come date| Insetto|
|CELLSNET-44414 | Problema con immagini di grandi dimensioni durante la conversione da Excel a PDF| Insetto|
|CELLSNET-44341 | Altezze di riga errate utilizzando AutoFitRows con l'opzione AutoFitMergedCells attivata per parole cinesi e inglesi nelle celle| Insetto|
|CELLSNET-44309 | Parentesi non mostrate ruotate nel PDF di output (conversione da Excel a PDF)| Insetto|
|CELLSNET-44302 | SheetRender.ToImage non esegue il rendering del bordo delle celle| Insetto|
|CELLSNET-43237 | I simboli verticali non vengono visualizzati correttamente durante la conversione di fogli di calcolo in PDF| Insetto|
|CELLSNET-41907 | Parte del testo verticale non può ancora essere visualizzato correttamente nel file PDF convertito| Insetto|
|CELLSNET-44405 |L'immagine del grafico ha la serie "La tua organizzazione" allo 0% anche se è impostata al 50%| Insetto|
|CELLSNET-44404 | Il metodo Worksheet.Copy non copia correttamente i grafici| Insetto|
|CELLSNET-44398 | Il rendering EMF del grafico non funziona correttamente nella versione più recente| Insetto|
|CELLSNET-44397 | Rendering dal grafico all'immagine: il testo (etichette dati) è più in grassetto rispetto al grafico originale| Insetto|
|CELLSNET-44387 | L'immagine generata utilizzando Chart.ToImage non è corretta| Insetto|
|CELLSNET-44365 | Parte dell'etichetta della serie di dati mancante per un grafico specifico generato come immagine utilizzando aspose.cells| Insetto|
|CELLSNET-44426 |L'impostazione ImportOptions.ConvertNumericData = true restituisce valori con '<' or '> cifra non vengono visualizzate| Insetto|
|CELLSNET-44408 | Problema con le voci dell'elenco a discesa/elenco di convalida dei dati contenenti una virgola| Insetto|
|CELLSNET-44403 | La filigrana di sfondo viene rimossa durante il salvataggio di XLS in XLSX| Insetto|
|CELLSNET-44402 | ExternalLink ha restituito DataSource errato con percorso esteso| Insetto|
|CELLSNET-44394 | Il raggruppamento dei marcatori intelligenti è interrotto nella versione più recente| Insetto|
|CELLSNET-44390 | Problema con l'attributo Gruppo degli indicatori intelligenti: tutti i dati non vengono elaborati| Insetto|
|CELLSNET-44388 | Le celle denominate su un foglio di lavoro diverso danneggiano la cartella di lavoro| Insetto|
|CELLSNET-44379 |Le etichette del grafico scompaiono dopo aver salvato nuovamente il foglio di calcolo| Insetto|
|CELLSNET-44329 | Diverse dimensioni della pagina del file Pdf salvato per le celle selezionate o non selezionate nel file Excel| Insetto|
|CELLSNET-44400 | Il testo viene ritagliato quando l'etichetta del segno di spunta dei grafici è lunga durante il rendering del foglio di lavoro nell'immagine| Insetto|
|CELLSNET-44401 | La casella di testo ruotata è posizionata in modo errato durante il rendering del foglio di lavoro nell'immagine| Insetto|
|CELLSNET-44420 | Errore durante l'apertura del file Excel2003XML in Aspose.Cells| Eccezione|
|CELLSNET-44393 | System.ArgumentOutOfRangeException con Assembly Aspose.Cells unito utilizzando ILMerge| Eccezione|
|CELLSNET-44389 | System.FormatException: la stringa di input non era in un formato corretto, in WorkbookDesigner.Process| Eccezione|
### **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSNET-42313 | Supporta la lettura della convalida dei dati nel file Excel - Aspose.Cells.GridDesktop| Nuova caratteristica|
|CELLSNET-44267 | Problema con il caricamento lento durante l'impostazione dell'attributo EnableAsync durante lo scorrimento nel controllo GridWeb| Aumento|
|CELLSNET-41793 | La freccia giù non funziona correttamente dopo l'unione delle celle| Aumento|
|CELLSNET-44424 | L'evidenziazione selezionata non è corretta in GridWeb| Insetto|
|CELLSNET-44364 | La formattazione della cella cambia dopo aver fatto clic sulla cella in GridWeb| Insetto|
|CELLSNET-44343 | GridDesktop non mostra il menu a discesa durante il caricamento del foglio di calcolo| Insetto|
|CELLSNET-44409 |Eccezione durante l'importazione di un file Excel in GridWeb| Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà WorkbookSettings.PaperSize.**
Viene utilizzato per impostare il formato carta della stampante predefinita come formato carta predefinito della cartella di lavoro.
#### **Aggiunge la classe LoadDataFilterOptions e la proprietà LoadOptions.LoadDataFilterOptions.**
Viene utilizzato per specificare quale tipo di dati deve essere caricato durante la creazione della cartella di lavoro dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per lo scopo speciale dell'utente, in particolare quando si utilizzano le API LightCells.
#### **Aggiunge il metodo Worksheet.CalculateFormula(string formula, CalculationOptions opts).**
Viene utilizzato per calcolare una determinata formula direttamente con le opzioni personalizzate dell'utente.
#### **Aggiunge le classi dello spazio dei nomi Aspose.Cells.Drawing.Texts.**
Viene utilizzato per impostare le proprietà del carattere del testo della forma.
#### **Proprietà Shape.TextFrame obsoleta.**
Usare invece la proprietà Shape.TextBody.TextAlignment.
#### **Aggiunge la proprietà Shape.TextBody.**
Presenta l'impostazione del testo della forma.
#### **Aggiunge il metodo GridCell.CreateValidation(GridValidationType validationType, bool isRequired).**
Crea un oggetto di convalida per una cella della griglia.
#### **Aggiunge il metodo GridCell.RemoveValidation().**
Rimuove l'oggetto di convalida da una cella della griglia.
#### **Aggiunge il metodo Chart.ToPdf(System.IO.Stream stream).**
Aggiunge il grafico di salvataggio al PDF come flusso.

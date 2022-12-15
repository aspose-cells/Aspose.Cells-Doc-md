---
title: Aspose.Cells for .NET 22.1 Note di rilascio
type: docs
weight: 12
url: /it/net/aspose-cells-for-net-22-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.1](https://www.nuget.org/packages/Aspose.Cells/22.1.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50082|Supporto per restituire indici originali di righe/colonne ordinate per la funzione sort()|Nuova caratteristica|
|CELLSNET-50088|Supporto per impostare il nome del lavoro di stampa con PrinterSettings durante il rendering sulla stampante|Nuova caratteristica|
|CELLSNET-50060|Rileva se il file di testo è csv o tsv.|Nuova caratteristica|
|CELLSNET-49939|Inserisci le righe e le colonne nascoste quando ottieni Cells.MaxDisplayRange|Aumento|
|CELLSNET-50054|Risultato errato per il calcolo della funzione FREQUENZA nella formula di matrice|Aumento|
|CELLSNET-50072|Funzione non supportata: CUBESET|Aumento|
|CELLSNET-50017|Come aggiungere una bolla accanto al titolo del grafico e al testo dell'asse del grafico|Aumento|
|CELLSNET-50038| Comportamento diverso riguardo alla compressione e all'espansione di gruppi a più livelli|Aumento|
|CELLSNET-50041| I file immagine BMP non vengono visualizzati nell'intestazione/piè di pagina|Aumento|
|CELLSNET-50108|Da XLS a PDF: la conversione si blocca con memoria esaurita|Prestazione|
|CELLSNET-50128|L'interlinea diventa più stretta - Conversione da Excel a PDF|Insetto|
|CELLSNET-50086|Cell i colori scompaiono dopo la conversione in PDF|Insetto|
|CELLSNET-49996|I valori RTF delle celle possono andare persi con la modalità MemoryPreference|Insetto|
|CELLSNET-50042| Il nome delle celle viene modificato durante la registrazione|Insetto|
|CELLSNET-50055|Proprietà del nome dell'intervallo locale FullText non viene sottoposto a escape se il foglio di lavoro padre ha un apostrofo|Insetto|
|CELLSNET-50154|GridWeb non riesce a caricare/salvare dalla cache per il file .csv|Insetto|
|CELLSNET-50063|La stampa del file Excel esegue il rendering di due pagine invece di una pagina|Insetto|
|CELLSNET-50094|I contenuti del foglio di lavoro non vengono visualizzati correttamente nella conversione da Excel a PDF|Insetto|
|CELLSNET-50129|La posizione di stampa aumenta man mano che la pagina viene seguita: conversione da Excel a PDF|Insetto|
|CELLSNET-50131|Mancano i caratteri - Conversione da Excel a PDF|Insetto|
|CELLSNET-49578| Valore max/min errato calcolato dai grafici di Aspose.Cells|Insetto|
|CELLSNET-50087|Il grafico di output non viene visualizzato correttamente dopo aver modificato il tipo di serie|Insetto|
|CELLSNET-50197|La legenda nel grafico a cascata non può essere eliminata o nascosta|Insetto|
|CELLSNET-50065|Comportamento diverso per quanto riguarda la compressione e l'espansione di gruppi di righe a più livelli|Insetto|
|CELLSNET-50137|Variabile non dichiarata da XLSX a HTML "nodo" nello script|Insetto|
|CELLSNET-50157|AutoFitMergedCellsType.EachLine non funziona per le colonne di adattamento automatico|Insetto|
|CELLSNET-50165|Il carattere della guida fonetica viene modificato dopo il salvataggio del file|Insetto|
|CELLSNET-50208|Alcuni testi vengono persi durante il salvataggio come Html|Insetto|
|CELLSNET-50095|Eccezione all'apertura del file XSLB|Eccezione|
|CELLSNET-50096| StackOverflowException durante l'eliminazione di colonne vuote|Eccezione|
|CELLSNET-50071|Conversione in eccezione HTML "Funzione non supportata: CUBESET"|Eccezione|
|CELLSNET-50097|Eccezione all'apertura del file XSLX tramite Aspose.Cells|Eccezione|
|CELLSNET-50133|NullReferenceException quando si confronta FillFormat|Eccezione|
|CELLSNET-50138|Eccezione all'apertura di un file XLSB|Eccezione|
|CELLSNET-50016|Dal grafico ai valori dell'asse errati EMF|Regressione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Modifica il comportamento della rimozione dei collegamenti esterni dalla cartella di lavoro.**

Nelle vecchie versioni, non rimuoviamo il collegamento esterno il cui URL contiene "AddIns". Tale comportamento è progettato per il requisito speciale di alcuni utenti. Il difetto di tale soluzione è evidente: gli utenti possono specificare qualsiasi nome di file o percorso valido per i riferimenti esterni e infatti la maggior parte di loro non vuole che quei collegamenti esterni vengano trattati in modo diverso. Da questa versione, non filtriamo più quei link esterni. Se gli utenti hanno requisiti speciali per alcuni collegamenti esterni, possono controllare tutti gli elementi in ExternalLinkCollection uno per uno e rimuovere solo quelli che desiderano eliminare (mediante il metodo ExternalLinkCollection.RemoveAt(int)).

### **Modifica il comportamento di Cell. Digitare per un valore data/ora non valido.**

Nelle versioni precedenti, se una cella deve essere formattata come data/ora, Cell.Type restituisce CellValueType.IsDateTime indipendentemente dal fatto che il valore numerico di questa cella sia valido o meno per la data/ora. Ciò può causare un'eccezione se gli utenti dipendono solo da Cell.Type e provano a chiamare Cell.DateTimeValue. Da questa versione, restituiamo CellValueType.IsNumeric per questo tipo di celle in modo che l'utente possa essere guidato per ottenere il valore della cella dall'API appropriata.

### **Modifica il comportamento di Cells.MaxDisplayRange.**

Nelle versioni precedenti, il valore dell'intervallo di questa proprietà copre tutte le celle di cui è stata creata un'istanza nella raccolta di celle. Da questa versione facciamo in modo che le righe/colonne invisibili siano escluse dai bordi dell'intervallo di visualizzazione se ci sono solo celle istanziate in quelle righe/colonne.

### **Modifica i metodi DataSorter.Sort() per restituire gli indici originali di righe/colonne ordinate.**

Nelle vecchie versioni i metodi DataSorter.Sort() non restituiscono nulla. Da questa versione, restituiamo gli indici originali di righe/colonne corrispondenti all'intervallo è stato ordinato. Ciò fornisce all'utente la possibilità di eseguire controlli avanzati e operazioni per lo smistamento.

### **Aggiunge la proprietà TxtLoadOptions.ExtendToNextSheet.**

Supporta l'importazione di dati CSV/TSV in più fogli di lavoro se il conteggio delle righe o delle colonne dei dati supera il limite di ms excel.

### **Aggiunge il metodo ExternalLinkCollection.Clear().**

Rimuove tutti i collegamenti esterni dalla cartella di lavoro.

### **Aggiunge il metodo ExternalLinkCollection.Clear(bool updateReferencesAsLocal).**

Quando si rimuovono tutti i collegamenti esterni dalla cartella di lavoro, l'utente può determinare come utilizzare le formule che contengono riferimenti a tali collegamenti esterni. Se "updateReferencesAsLocal" è vero, tutte le funzioni definite dall'utente nei collegamenti esterni verranno spostate nella cartella di lavoro corrente stessa. Ad esempio, la formula di una cella è "='externalsource.xlam'!customfunction()", dopo aver rimosso il collegamento esterno "externalsource.xlam", la formula di questa cella diventerà "=customfunction()".

### **Aggiunge il metodo ExternalLinkCollection.RemoveAt(int).**

Rimuove un collegamento esterno specificato dalla cartella di lavoro.

### **Aggiunge il metodo ExternalLinkCollection.RemoveAt(int, bool updateReferencesAsLocal).**

Analogamente al metodo ExternalLinkCollection.Clear(bool updateReferencesAsLocal), l'utente può determinare il modo di agire con le formule che fanno riferimento al collegamento esterno specificato durante la rimozione dalla cartella di lavoro.

### **Aggiunge il metodo ExternalLinkCollection.GetEnumerator().**

Fornisce un enumeratore per scorrere tutti i collegamenti esterni nella cartella di lavoro.

### **Metodo Workbook.RemoveExternalLinks() obsoleto.**

Utilizzare invece il metodo ExternalLinkCollection.Clear().

### **Metodo Workbook.HasExernalLinks() obsoleto.**

Utilizzare ExternalLinkCollection.Count per verificare se sono presenti collegamenti esterni nella cartella di lavoro.

### **Elimina la classe obsoleta StyleCollection.**

Utilizzare Workbook.CreateStyle() e Workbook.GetNamedStyle(string) per manipolare gli stili.

### **Aggiunge il costruttore PptxSaveOptions(bool saveAsImage).**

Rappresenta le opzioni di salvataggio del file .pptx. Se True, la cartella di lavoro verrà convertita in alcune immagini del file .pptx. Se False, la cartella di lavoro verrà convertita in alcune tabelle del file .pptx.

### **Aggiunge il metodo SheetRender.ToPrinter(PrinterSettings printerSettings, string jobName).**

Renderizza il foglio di lavoro alla stampante con le impostazioni della stampante e il nome del lavoro della stampante.

### **Aggiunge il metodo WorkbookRender.ToPrinter(PrinterSettings printerSettings, string jobName).**

Eseguire il rendering della cartella di lavoro sulla stampante con le impostazioni della stampante e il nome del processo della stampante.

### **Aggiunge la classe ChartGlobalizationSettings.**

 Rappresenta le impostazioni di globalizzazione per il grafico.

### **Aggiunge la proprietà DataLabels.IsNeverOverlap.**

Indica se le etichette dati non si sovrappongono mai. (Per grafico a torta)

### **Aggiunge la classe TickLabelItem.**

Includi le informazioni di un elemento Ticklabel.

### **Aggiunge la proprietà TickLabelItem.Height.**

Ottiene l'altezza dell'elemento Ticklabel in rapporto all'altezza del grafico.

### **Aggiunge la proprietà TickLabelItem.Width.**

Ottiene la larghezza dell'elemento Ticklabel in rapporto alla larghezza del grafico.

### **Aggiunge la proprietà TickLabelItem.X.**

Ottiene X dell'elemento Ticklabel in rapporto alla larghezza del grafico.

### **Aggiunge la proprietà TickLabelItem.Y.**

Ottiene Y dell'elemento Ticklabel in rapporto all'altezza del grafico.

### **Aggiunge la proprietà TickLabels.TickLabelItems.**

Ottiene gli elementi di TickLabel.


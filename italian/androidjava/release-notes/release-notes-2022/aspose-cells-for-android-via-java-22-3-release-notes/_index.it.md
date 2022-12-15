---
title: Aspose.Cells for Android via Java 22.3 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-android-via-java-22-3-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 22.3.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44162|Supporto per rimuovere il collegamento esterno senza rimuovere le formule|
|CELLSJAVA-44214|Supporto per l'adattamento automatico delle righe per GridWeb|
|CELLSJAVA-44205|Supporta il testo dell'unità dipendente dalle impostazioni locali per gli assi delle coordinate del grafico|
|CELLSJAVA-44238|Supporto per mantenere la sessione dopo il riavvio del server per GridWeb|
|CELLSJAVA-44317|Il testo in questo xlsx è confuso|
|CELLSJAVA-44126|Cell.getDependents() genera un'eccezione se la formula della cella non è stata analizzata|
|CELLSJAVA-44161|Errore nella formula esterna durante l'importazione di una cartella di lavoro in un'altra cartella di lavoro|
|CELLSJAVA-44130|Il testo delle etichette dati va a capo nell'immagine del grafico di output|
|CELLSJAVA-44204|problema di impaginazione per csv|
|CELLSJAVA-43934|Le etichette del grafico a torta non vengono abbinate a Excel dopo aver manipolato o aggiornato il grafico|
|CELLSJAVA-44122|Quando si esporta HTML, le etichette dei dati sono diverse da quelle di Excel|
|CELLSJAVA-41949| Il rendering del contenuto è diverso quando si salva la cartella di lavoro nei formati XLSX e HTML|
|CELLSJAVA-44207|Quando esporti in HTML, l'altezza della riga aumenta|
|CELLSJAVA-44233|Ciclo infinito durante la conversione di file XLSX|
|CELLSJAVA-44271|Quando si converte Excel in PDF, la posizione di output si sposta rispetto al caso della conversione manuale|
|CELLSJAVA-44197|Quando si converte XLSX in PDF, la forma della timeline della tabella pivot (finestra) non viene visualizzata|
|CELLSJAVA-44267|La cartella di lavoro contenente una tabella pivot viene danneggiata|
|CELLSJAVA-44114|Da XLSX a PDF: i dati in formato numerico Scientific dal file XLSX non corrispondono ai dati nel file PDF di output|
|CELLSJAVA-44293|Il file Excel salvato di nuovo deve essere recuperato quando lo si apre in MS Excel|
|CELLSJAVA-43194|Immagini visualizzate in modo errato|
|CELLSJAVA-44243|Il file di salvataggio della demo primaverile di GridWeb non è riuscito in jdk1.8|
|CELLSJAVA-44276|mancata corrispondenza dell'altezza dell'intestazione di riga con il contenuto della riga dopo la modifica della cella per il file 249.xls|
|CELLSJAVA-44284|sollevare un'eccezione di memoria insufficiente per il file bug.xlsx|
|CELLSJAVA-44229|La formula viene persa quando il contenuto td viene avvolto dal tag div|
|CELLSJAVA-44247|Il testo a riga singola viene avvolto durante la conversione in pdf|
|CELLSJAVA-44175| problema con le etichette del grafico a ciambella sovrapposte|
|CELLSJAVA-44192| Il nome dell'elemento dell'asse delle categorie nel grafico viene tagliato nella conversione da Excel a PDF|
|CELLSJAVA-44233|Ciclo infinito durante la conversione di file XLSX|
|CELLSJAVA-44263|L'impostazione della direzione del testo dell'etichetta del grafico su verticale non ha effetto|
|CELLSJAVA-44268| Eccezione "java.lang.NullPointerException" sul metodo Chart.toPdf|
|CELLSJAVA-44302|La direzione del testo dell'asse delle coordinate è errata dopo che il file Excel è stato convertito in HTML|
|CELLSJAVA-44314|Etichette dell'asse delle categorie del grafico errate nel rendering dal grafico all'immagine|
|CELLSJAVA-44274|Il formato SVG è supportato per la lettura o il rendering in PDF|
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
|CELLSJAVA-44234|Problema di memoria insufficiente per il file data.xls|
|CELLSJAVA-44246|Eccezione "Indice endrow non valido" per file vuoto|
|CELLSJAVA-44258| Eccezione puntatore nullo per file|
|CELLSJAVA-44311|Eccezione "java.lang.OutOfMemoryError: Java heap space" durante il rendering nel formato di file HTML|
|CELLSJAVA-44285|Eccezione "java.lang.ClassCastException: impossibile eseguire il cast di com.aspose.cells.n2f su com.aspose.cells.o90" quando si chiama Workbook.calculateFormula()|
|CELLSJAVA-44323|Eccezione durante l'aggiunta della riga della firma|
|CELLSJAVA-44361|CellsException sollevata durante la conversione di xlsx in html|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. sul forum di supporto Aspose.Cells.

### **Modifica il comportamento della rimozione dei collegamenti esterni dalla cartella di lavoro.**

Nelle vecchie versioni, non rimuoviamo il collegamento esterno il cui URL contiene "AddIns". Tale comportamento è progettato per il requisito speciale di alcuni utenti. Il difetto di tale soluzione è evidente: gli utenti possono specificare qualsiasi nome di file o percorso valido per i riferimenti esterni e infatti la maggior parte di loro non vuole che quei collegamenti esterni vengano trattati in modo diverso. Da questa versione, non filtriamo più quei link esterni. Se gli utenti hanno requisiti speciali per alcuni collegamenti esterni, possono controllare tutti gli elementi in ExternalLinkCollection uno per uno e rimuovere solo quelli che desiderano eliminare (mediante il metodo ExternalLinkCollection.RemoveAt(int)).

### **Modifica il comportamento di Cell. Digitare per un valore data/ora non valido.**

Nelle versioni precedenti, se una cella deve essere formattata come data/ora, Cell.Type restituisce CellValueType.IsDateTime indipendentemente dal fatto che il valore numerico di questa cella sia valido o meno per la data/ora. Ciò può causare un'eccezione se gli utenti dipendono solo da Cell.Type e provano a chiamare Cell.DateTimeValue. Da questa versione, restituiamo CellValueType.IsNumeric per questo tipo di celle in modo che l'utente possa essere guidato per ottenere il valore della cella dall'API appropriata.

### **Modifica il comportamento di Cells.MaxDisplayRange.**

Nelle versioni precedenti, il valore dell'intervallo di questa proprietà copre tutte le celle di cui è stata creata un'istanza nella raccolta di celle. Da questa versione facciamo in modo che le righe/colonne invisibili siano escluse dai bordi dell'intervallo di visualizzazione se ci sono solo celle istanziate in quelle righe/colonne.

### **Modifica i metodi DataSorter.Sort() per restituire gli indici originali di righe/colonne ordinate.**

Nelle vecchie versioni? I metodi DataSorter.Sort() non restituiscono nulla. Da questa versione, restituiamo gli indici originali di righe/colonne corrispondenti all'intervallo è stato ordinato. Ciò fornisce all'utente la possibilità di eseguire controlli avanzati e operazioni per lo smistamento.

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

### **Metodo Cells.AddAddInFunction() obsoleto.**

Utilizzare invece i metodi WorksheetCollection.RegisterAddInFunction().

### **Aggiunge il metodo NameCollection.Filter() e l'enumerazione NameScopeType.**

Ottiene i nomi definiti in base all'ambito.

### **Aggiunge l'enumerazione MsoDrawingType.Timeline.**

Rappresenta il tipo di oggetti di disegno della linea temporale.

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
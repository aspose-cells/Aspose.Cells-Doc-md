---
title: Aspose.Cells for PHP via Java 22.1 Note di rilascio
type: docs
weight: 12
url: /it/php-java/aspose-cells-for-php-via-java-22-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for PHP via Java 22.1](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.1/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44162|Supporto per rimuovere il collegamento esterno senza rimuovere le formule|
|CELLSJAVA-44214|Supporto per l'adattamento automatico delle righe per GridWeb|
|CELLSJAVA-44205|Supporta il testo dell'unità dipendente dalle impostazioni locali per gli assi delle coordinate del grafico|
|CELLSJAVA-44238|Supporto per mantenere la sessione dopo il riavvio del server per GridWeb|
|CELLSJAVA-44126|Cell.getDependents() genera un'eccezione se la formula della cella non è stata analizzata|
|CELLSJAVA-44161|Errore nella formula esterna durante l'importazione di una cartella di lavoro in un'altra cartella di lavoro|
|CELLSJAVA-44130|Il testo delle etichette dati va a capo nell'immagine del grafico di output|
|CELLSJAVA-44204|problema di impaginazione per csv|
|CELLSJAVA-43934|Le etichette del grafico a torta non vengono abbinate a Excel dopo aver manipolato o aggiornato il grafico|
|CELLSJAVA-44122|Quando si esporta HTML, le etichette dei dati sono diverse da quelle di Excel|
|CELLSJAVA-41949| Il contenuto viene visualizzato in modo diverso quando si salva la cartella di lavoro nei formati XLSX e HTML|
|CELLSJAVA-44207|Quando si esporta in HTML, l'altezza della riga aumenta|
|CELLSJAVA-44233|Ciclo infinito durante la conversione del file XLSX|
|CELLSJAVA-44234|Problema di memoria insufficiente per il file data.xls|
|CELLSJAVA-44246|Eccezione "Indice endrow non valido" per file vuoto|
|CELLSJAVA-44258| Eccezione puntatore nullo per file|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Modifica il comportamento della rimozione dei collegamenti esterni dalla cartella di lavoro.**

Nelle vecchie versioni, non rimuoviamo il collegamento esterno il cui URL contiene "AddIns". Tale comportamento è progettato per il requisito speciale di alcuni utenti. Il difetto di tale soluzione è evidente: gli utenti possono specificare qualsiasi nome di file o percorso valido per i riferimenti esterni e infatti la maggior parte di loro non vuole che quei collegamenti esterni vengano trattati in modo diverso. Da questa versione, non filtriamo più quei link esterni. Se gli utenti hanno requisiti speciali per alcuni collegamenti esterni, possono controllare tutti gli elementi in ExternalLinkCollection uno per uno e rimuovere solo quelli che desiderano eliminare (mediante il metodo ExternalLinkCollection.RemoveAt(int)).

### **Modifica il comportamento di Cell. Digitare per un valore data/ora non valido.**

Nelle versioni precedenti, se una cella deve essere formattata come data/ora, Cell.Type restituisce CellValueType.IsDateTime indipendentemente dal fatto che il valore numerico di questa cella sia valido o meno per la data/ora. Ciò può causare un'eccezione se gli utenti dipendono solo da Cell.Type e provano a chiamare Cell.DateTimeValue. Da questa versione, restituiamo CellValueType.IsNumeric per questo tipo di celle in modo che l'utente possa essere guidato a ottenere il valore della cella tramite API corretto.

### **Modifica il comportamento di Cells.MaxDisplayRange.**

Nelle versioni precedenti, il valore dell'intervallo di questa proprietà copre tutte le celle di cui è stata creata un'istanza nella raccolta di celle. Da questa versione facciamo in modo che le righe/colonne invisibili siano escluse dai bordi dell'intervallo di visualizzazione se ci sono solo celle istanziate in quelle righe/colonne.

### **Modifica i metodi DataSorter.Sort() per restituire gli indici originali di righe/colonne ordinate.**

Nelle vecchie versioni? I metodi DataSorter.Sort() non restituiscono nulla. Da questa versione, restituiamo gli indici originali di righe/colonne corrispondenti all'intervallo è stato ordinato. Ciò fornisce all'utente la possibilità di eseguire controlli avanzati e operazioni per lo smistamento.

### **Aggiunge la proprietà TxtLoadOptions.ExtendToNextSheet.**

Supporta l'importazione di dati CSV/TSV in più fogli di lavoro se il conteggio delle righe o il conteggio delle colonne dei dati supera il limite di ms excel.

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


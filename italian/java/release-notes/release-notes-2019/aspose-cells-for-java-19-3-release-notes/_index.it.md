---
title: Aspose.Cells for Java 19.3 Note di rilascio
type: docs
weight: 100
url: /it/java/aspose-cells-for-java-19-3-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.3.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42845|Mantieni i separatori per le righe vuote durante l'esportazione di un file XLS in CSV|Nuova caratteristica|
|CELLSJAVA-42846|risultati dell'estrazione del testo differiscono dall'originale|Aumento|
|CELLSJAVA-42844|Il testo non è correttamente allineato nell'output PDF|Insetto|
|CELLSJAVA-42834|Il colore del testo (nero) viene modificato in rosso nel rendering HTML|Insetto|
|CELLSJAVA-42839|Il grafico a dispersione non viene visualizzato nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-42840|Le etichette dell'asse orizzontale non vengono visualizzate correttamente per i grafici nel rendering da Excel a PDF|Insetto|
|CELLSJAVA-42842|Il grafico a bolle 2D non viene visualizzato nella conversione da Excel a PDF|Insetto|
|CELLSJAVA-42833|Problema durante l'incorporamento dello stesso file PDF in più fogli in una cartella di lavoro|Insetto|
|CELLSJAVA-42836|Workbook.hasExernalLinks() non restituisce true per i collegamenti DDE|Insetto|
|CELLSJAVA-42848|Impostazione dei caratteri e altri oggetti non copiati utilizzando la funzione Range.copy()|Insetto|
|CELLSJAVA-42849|Eccezione IndexOutOfBoundsException durante la conversione di XLSX in HTML|Eccezione|
|CELLSJAVA-42831|Eccezione sollevata da MS Excel dopo aver applicato lo stile all'intervallo di celle di intestazione|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Modifiche per il carattere predefinito del file modello XLS caricato**
Nelle versioni precedenti, non supportavamo l'applicazione del carattere definito nel tema (funzionalità avanzata in MS Excel 2007 e versioni successive) in base alla regione durante il caricamento dei file modello XLS. Su richiesta di alcuni utenti, lo abbiamo supportato dalla v19.3. Se la regione è stata specificata nel file modello XLS, applicheremo il carattere definito nel tema in base al valore della regione specificato salvato. Altrimenti applicheremo il carattere definito nel tema in base alle impostazioni regionali dell'ambiente dell'applicazione. Ciò causerà la modifica del carattere predefinito della cartella di lavoro (caricato dal file modello XLS che ha specificato i dati del tema) e quindi influenzerà altre funzionalità, come la larghezza della colonna, la dimensione della forma, l'effetto di rendering, ... ecc.
### **Aggiunge il metodo Name.GetReferredAreas(bool recalculate).**
Fornisce i riferimenti a cui fa riferimento il nome definito come metodo GetRanges(bool recalculate). Ma i riferimenti restituiti sono rappresentati dall'oggetto ReferredArea che fornisce funzionalità più ricche, inclusi collegamenti esterni.
### **Aggiunge la proprietà TxtSaveOptions.KeepSeparatorsForBlankRow**
Indica se i separatori devono essere emessi per la riga vuota. Il valore predefinito è false, il che significa che il contenuto della riga vuota sarà vuoto.
### **Aggiunge enum AutoFitMergedCellsType**
Rappresenta il tipo di celle unite con adattamento automatico.
### **Obsoleta la proprietà AutoFitterOptions.AutoFitMergedCells e aggiunge la proprietà AutoFitterOptions.AutoFitMergedCellsType**
Ottiene e imposta il tipo di altezza della riga di adattamento automatico.
### **Aggiunge le classi JSONUtility e JsonLayoutOptions**
È usato per importare file json.
### **Aggiunge la classe TableToRangeOptions e il metodo ListObject.ConvertToRange(TableToRangeOptions options)**
Converte la tabella in un intervallo con opzioni.

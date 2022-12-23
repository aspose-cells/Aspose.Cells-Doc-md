---
title: Aspose.Cells for Node.js via Java 21.12 Note di rilascio
type: docs
weight: 1
url: /it/nodejs-java/aspose-cells-for-node-js-via-java-21-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Node.js via Java 21.12](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.12/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43994|Supporto per interrompere l'esecuzione di WorkbookDesigner.process in SmarkMarker|
|CELLSJAVA-44039|Modifica PDF Attributo produttore dal PDF generato|
|CELLSJAVA-43469|Possibile regressione: riduzione delle prestazioni di FormatConditionCollection.addArea()|
|CELLSJAVA-43983|Regressione: ciclo infinito durante la conversione da XLSX a PDF|
|CELLSJAVA-44029|Da XLSX a PDF: l'immagine non viene convertita|
|CELLSJAVA-44093| Problema di troncamento del testo con le forme rettangolari durante il rendering dell'immagine nelle versioni Aspose.Cells for Java più recenti|
|CELLSJAVA-44089|DataLabels.setShadow() non è disponibile e non è uguale al metodo Series.setShadow()|
|CELLSJAVA-44000|Lo stile Cells non è corretto in HTML quando si utilizza il set di icone e altra formattazione condizionale contemporaneamente|
|CELLSJAVA-43932|Problema con l'impostazione della posizione delle etichette dei dati per i grafici a ciambella esplosi nell'immagine di output|
|CELLSJAVA-43934|Le etichette del grafico a torta non corrispondono a Excel dopo aver manipolato o aggiornato il grafico|
|CELLSJAVA-44094|Titolo del grafico troncato durante l'esportazione in PDF|
|CELLSJAVA-43533|XLSX al problema di creazione di Html in Ubuntu|
|CELLSJAVA-43987|Il bordo destro delle celle unite viene perso in html|
|CELLSJAVA-44016|Problema durante la conversione del file Excel contenente l'URL dell'immagine in HTML|
|CELLSJAVA-44071|com.aspose.cells.CellsException: hai inserito troppi pochi parametri per la funzione IF quando chiami Workbook.calculateFormula()|
|CELLSJAVA-44104|NullPointerException durante l'importazione di SpreadSheetML|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Ulteriori vincoli per l'aggiunta di aree per la convalida.**

Abbiamo modificato il modello di area per la convalida e la formattazione condizionale per tener conto delle prestazioni. Il nuovo modello richiede più vincoli per la sequenza delle aree aggiunte. Per Validation.AddArea(CellArea cellArea, bool checkIntersection, bool checkEdge) e Validation.AddAreas(CellArea[]areas, bool checkIntersection, bool checkEdge), se i due parametri "check" sono false, l'utente deve assicurarsi che le aree aggiunte sono ordinati in ordine crescente dagli angoli in alto a sinistra. In caso contrario, si potrebbero ottenere risultati imprevisti per altre operazioni. Nella nuova versione, poiché le prestazioni dell'aggiunta di grandi quantità di aree sono state migliorate in modo significativo, non pensiamo che Validation.AddArea(CellArea cellArea) sarà più un collo di bottiglia. Quindi pensiamo che gli utenti possano semplicemente chiamare direttamente AddArea(CellArea cellArea), senza la necessità di utilizzare questi due metodi speciali.

### **Comportamento modificato per la modifica delle aree di convalida/formattazione condizionale.**

Per Validation e ConditionalFormatting, nelle vecchie versioni le loro aree possono essere supportate dall'oggetto CellArea ottenuto o impostato su di esse. Quindi, se l'utente modifica il valore del campo dell'oggetto CellArea, anche le aree possono essere modificate e viceversa. In realtà questo è un risultato inaspettato dal punto di vista del design API. Da questa versione, questo effetto collaterale è stato rimosso e l'utente non può più modificare le aree modificando l'oggetto CellArea.

### **Comportamento modificato per l'aggiunta della condizione di formato in FormatConditionCollection.**

Per i metodi FormatConditionCollection.AddCondition(...), le versioni precedenti rendono la priorità di quella appena aggiunta come la più bassa. È diverso dal comportamento di MS Excel. Da questa versione, proprio come quello che otterrai per l'operazione in ms excel, rendiamo la priorità della condizione di formato appena aggiunta come la più alta.

### **Aggiunge la proprietà AbstractInterruptMonitor.TerminateWithoutException.**

Questa proprietà indica quando è stata richiesta un'interruzione per un processo, se il processo deve essere terminato da un'eccezione o semplicemente uscire silenziosamente. Per impostazione predefinita, questa proprietà è false, ovvero il processo verrà terminato da un'eccezione quando viene interrotto.

### **Aggiunge la proprietà WorkbookSettings.ResourceProvider.**

Proprietà rinominata per WorkbookSettings.StreamProvider per renderla più adatta alla sua funzione e più facile da comprendere per gli utenti.

### **Aggiunge l'opzione LoadDataFilterOptions.Revision.**

Alcuni file modello possono contenere una grande quantità di registri di revisione e causare scarse prestazioni per il caricamento della cartella di lavoro. L'utente può utilizzare questa opzione per controllare se tali registri di revisione debbano essere caricati o meno.

### **Proprietà WorkbookSettings.StreamProvider obsoleta.**

Utilizzare invece la proprietà WorkbookSettings.ResourceProvider.

### **Elimina la proprietà obsoleta PdfSaveOptions.StreamProvider.**

Utilizzare invece la proprietà WorkbookSettings.ResourceProvider.

### **Aggiunge la proprietà JsonLoadOptions.MultipleWorksheets.**

Indica se importare ogni attributo dell'oggetto JsonObject come un foglio di lavoro quando tutti i nodi figlio sono nodi matrice.

### **Aggiunge FileFormatType.SqlScript, SaveFormat.SqlScript e SqlScriptSaveOptions**

Rappresenta le opzioni di salvataggio dello script sql.

### **Aggiunge SaveFormat.Xml, LoadFormat.Xml, XmlSaveOptions e XmlLoadOptions**

Rappresenta le opzioni dei file R/W xml.

### **Aggiunge la proprietà HtmlSaveOptions.SaveAsSingleFile.**

 Indica se salvare excel come un singolo file.

### **Aggiunge la proprietà JsonLoadOptions.MultipleWorksheets.**

 Indica se caricare i dati del file Json su più fogli di lavoro

### **Aggiunge la proprietà PdfSaveOptions.Producer.**

 Ottiene e imposta il produttore del documento pdf generato.

### **Aggiunge i metodi ListColumn.GetCustomTotalsRowFormula() e ListColumn.SetCustomTotalsRowFormula()**

 Ottiene e imposta la formula personalizzata della riga dei totali nella tabella.


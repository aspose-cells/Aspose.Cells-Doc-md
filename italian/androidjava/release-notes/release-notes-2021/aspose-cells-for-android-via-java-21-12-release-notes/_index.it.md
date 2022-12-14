---
title: Aspose.Cells per Android tramite Java 21.12 Note di rilascio
type: docs
weight: 1
url: /it/java/aspose-cells-for-android-via-java-21-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Android tramite Java 21.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43994|Supporto per interrompere l'esecuzione di WorkbookDesigner.process in SmarkMarker|
|CELLSJAVA-44039|Modifica l'attributo PDF Producer dal PDF generato|
|CELLSJAVA-43768|Java Problema di spazio nell'heap durante la conversione del file XLSX in PDF|
|CELLSJAVA-43875|Eccezione "Invalid FontUnderlineType string val" durante il caricamento del file XLSX|
|CELLSJAVA-43876|Eccezione "java.lang.ArrayIndexOutOfBoundsException" durante il caricamento di un file XLSX|
|CELLSJAVA-43844|Un miglioramento necessario per il formato dei numeri contabili|
|CELLSJAVA-43953|Renderizza testo/parte specifici "Cell" e "Commento" da tradurre in giapponese nella conversione da Excel a PDF|
|CELLSJAVA-43469|Possibile regressione: riduzione delle prestazioni di FormatConditionCollection.addArea()|
|CELLSJAVA-43646|L'effetto ombra del testo non è reso correttamente|
|CELLSJAVA-43760|L'orientamento del triangolo isoscele non è corretto|
|CELLSJAVA-43786|Quando si converte il file XLS in XLSX, alcune parti relative alle forme non vengono visualizzate correttamente|
|CELLSJAVA-43838|Dopo l'esecuzione di XlsToXlsx, la forma si perde|
|CELLSJAVA-43839|Dopo l'esecuzione di XlsToXlsx, LeftBracket viene perso|
|CELLSJAVA-43842|Dopo aver eseguito XlsToXlsx, la forma di LeftBracket è diversa dall'originale|
|CELLSJAVA-43848|Conversione da Excel a PDF: alcuni caratteri WordArt non vengono racchiusi nello stesso modo del file Excel|
|CELLSJAVA-43880|Angoli arrotondati errati della casella di testo dopo la conversione da xls a xlsx|
|CELLSJAVA-43867|L'icona del formato condizionale è diversa quando si esporta in html|
|CELLSJAVA-43812|excelToHtml: l'offset della posizione della forma non è corretto|
|CELLSJAVA-43871|Prisma 9 Oggetti OLE non visualizzati nel PDF di output|
|CELLSJAVA-43883|Dimensioni della pagina visualizzate errate|
|CELLSJAVA-43881|L'unione dei file causa la mancanza dell'impostazione del colore di sfondo dei fogli|
|CELLSJAVA-43892|Mancano i bordi di Excel convertito in HTML|
|CELLSJAVA-43935|Problema relativo alla dimensione del carattere del testo durante il salvataggio e il caricamento del file XLS|
|CELLSJAVA-43952|Problema di scadenza della licenza temporanea|
|CELLSJAVA-43954|Da XLSX a PDF: l'immagine causa un'eccezione "java.lang.OutOfMemoryError: Java spazio heap"|
|CELLSJAVA-43902|Alcuni bordi di Excel convertiti in HTML sono ridondanti|
|CELLSJAVA-43933|Quando si esporta in HTML con un solo dato, il formato condizionale è diverso da Excel|
|CELLSJAVA-43878| Posizione errata delle etichette dei dati del grafico a barre del cluster di Excel|
|CELLSJAVA-43895|La forma della linea e altre forme del grafico non vengono visualizzate correttamente durante la conversione da XLS a XLSX|
|CELLSJAVA-43934|Le etichette del grafico a torta non corrispondono a Excel dopo aver manipolato o aggiornato il grafico|
|CELLSJAVA-43519|Le celle unite incluse in righe o colonne nascoste producono una tabella HTML irregolare|
|CELLSJAVA-43962|L'effetto è incoerente dopo che il formato condizionale in Excel è stato convertito in HTML|
|CELLSJAVA-43983|Regressione: ciclo infinito durante la conversione di XLSX in PDF|
|CELLSJAVA-44029|XLSX in PDF: l'immagine non viene convertita|
|CELLSJAVA-44093| Problema di troncamento del testo con le forme rettangolari durante il rendering dell'immagine nelle versioni Aspose.Cells for Java più recenti|
|CELLSJAVA-44089|DataLabels.setShadow() non è disponibile e non è uguale al metodo Series.setShadow()|
|CELLSJAVA-44000|Lo stile Cells non è corretto in HTML quando si utilizzano contemporaneamente set di icone e altra formattazione condizionale|
|CELLSJAVA-43932|Problema con l'impostazione della posizione delle etichette dei dati per i grafici a ciambella esplosi nell'immagine di output|
|CELLSJAVA-44094|Titolo del grafico troncato durante l'esportazione in PDF|
|CELLSJAVA-43533|Problema di creazione da XLSX a Html in Ubuntu|
|CELLSJAVA-43987|Il bordo destro delle celle unite viene perso in html|
|CELLSJAVA-44016|Problema durante la conversione del file Excel contenente l'URL dell'immagine in HTML|
|CELLSJAVA-43787|Eccezione "IllegalArgumentException: lunghezze trattino tutte zero ..." nel rendering da Excel a HTML|
|CELLSJAVA-43885|IllegalArgumentException durante la conversione di excel|
|CELLSJAVA-43874|Workbook.save genera un'eccezione su un file specifico entro Aspose.Cells solo quando viene applicata la licenza Aspose|
|CELLSJAVA-43969|Un nome con funzione CONTA.SE e riferimento esterno produce un'eccezione NullPointerException|
|CELLSJAVA-43903|java.lang.NumberFormatException: per la stringa di input durante il rendering del file Excel in HTML|
|CELLSJAVA-44071|com.aspose.cells.CellsException: hai inserito troppi pochi parametri per la funzione IF quando chiami Workbook.calculateFormula()|
|CELLSJAVA-44104|NullPointerException durante l'importazione di SpreadSheetML|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate al numero API pubblico come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells per Android tramite Java. In caso di dubbi su qualsiasi modifica elencata, si prega di sollevalo sul forum di supporto Aspose.Cells.

### **Aggiunge il metodo di overload Name.GetRefersTo().**

Ottiene l'espressione della formula basata sulla cella specificata.

### **Aggiunge il metodo di overload Range.AutoFill().**

Riempi automaticamente l'intervallo target con il tipo di riempimento.

### **Aggiunge la proprietà Comment.IsThreadedComment.**

Indica se questo commento è un commento con thread.

### **Aggiunge la proprietà HtmlSaveOptions.IgnoreInvisibleShapes.**

Indica se inserire forme invisibili durante il salvataggio di html.

### **Aggiunge la proprietà Range.CurrentRegion.**

Restituisce un intervallo delimitato da qualsiasi combinazione di righe e colonne vuote.

### **Aggiunge la classe AxisBins.**

 Rappresenta i contenitori degli assi per i grafici a istogramma.

### **Aggiunge il metodo SheetRender.GetPageSizeInch(int pageIndex)**

Ottieni la dimensione della pagina dell'immagine di output? in unità di pollice.

### **Aggiunge il metodo WorkbookRender.GetPageSizeInch(int pageIndex)**

Ottieni l'immagine di output delle dimensioni della pagina? in unità di pollici.

### **Aggiunge enum CellValueFormatStrategy.DisplayString.**

Con questa strategia, Cell.GetStringValue(CellValueFormatStrategy) prenderà in considerazione il limite della larghezza della colonna durante la formattazione dei valori della cella con lo stile di visualizzazione. Se il risultato formattato supera la larghezza disponibile, possono essere restituiti uno o più "#", proprio come mostra ms excel per questo tipo di celle.

### **Aggiunge la proprietà WorksheetCollection.ActiveSheetName.**

Ottiene e imposta il nome del foglio attivo della cartella di lavoro.

### **Aggiunge le classi JsonLoadOptions e JsonSaveOptions.**

Rappresenta le opzioni di caricamento o salvataggio dei file.

### **Aggiunge la proprietà ImageSaveOptions.StreamProvider.**

Fornisci gli stream se sono presenti due o più pagine.

### **Aggiunge l'enumerazione LoadFormat.Image e LoadFormat.Json.**

Rappresenta l'immagine e il tipo json.

### **Aggiunge SaveFormat.Bmp, SaveFormat.Emf, SaveFormat.Gif, SaveFormat.Jpg, SaveFormat.Json e SaveFormat.Png enum**

Nuovi formati di salvataggio supportati.

### **Aggiunge FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nuovi tipi di formati di file supportati.

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

### **Metodo obsoleto SheetRender.GetPageSize(int pageIndex)**

Usare invece SheetRender.GetPageSizeInch(int pageIndex).

### **Proprietà WorkbookSettings.StreamProvider obsoleta.**

Utilizzare invece la proprietà WorkbookSettings.ResourceProvider.

### **Elimina la proprietà obsoleta PdfSaveOptions.StreamProvider.**

Utilizzare invece la proprietà WorkbookSettings.ResourceProvider.


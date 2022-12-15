---
title: Aspose.Cells for .NET 21.12 Note di rilascio
type: docs
weight: 1
url: /it/net/aspose-cells-for-net-21-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.12](https://www.nuget.org/packages/Aspose.Cells/21.12.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-49680|Supporta la conversione di Excel in script SQL.|Nuova caratteristica|
|CELLSNET-49717|Supporta la conversione di Excel in dati xml|Nuova caratteristica|
|CELLSNET-49853| Supporta l'importazione di dati xml|Nuova caratteristica|
|CELLSNET-48190|Aggiorna le priorità quando aggiungi una nuova condizione di formato|Aumento|
|CELLSNET-49758| L'ordinamento con DataSorter influisce sulla formattazione della tabella|Aumento|
|CELLSNET-49828|FormatConditionCollection.AddCondition() fornisce un comportamento diverso per la formula|Aumento|
|CELLSNET-49981|Aggiungi l'opzione di filtro per i registri di revisione durante la creazione della cartella di lavoro dal file modello|Aumento|
|CELLSNET-49739|Ignora i riferimenti 3D per la formattazione condizionale durante la copia in un'altra cartella di lavoro|Aumento|
|CELLSNET-49984|Leggi alcuni dati dal file xls corrotto.|Aumento|
|CELLSNET-49990|Supporto per l'impostazione della formula di riga dei totali personalizzati della tabella.|Aumento|
|CELLSNET-49825|Problema di prestazioni con l'attributo ExportImagesAsBase64 nella conversione da Excel a HTML|Prestazione|
|CELLSNET-49827|RefersTo dell'intervallo definito è sfuggito in modo errato|Insetto|
|CELLSNET-49759|Le celle vuote vengono comunque esportate come elementi XML vuoti|Insetto|
|CELLSNET-49817|Il testo non è allineato al centro con il carattere "Credit Suisse Type Light" durante il rendering in Emf|Insetto|
|CELLSNET-49864|Parole che appaiono in ordine inverso per il testo da destra a sinistra nel rendering da XLSX a PDF|Insetto|
|CELLSNET-49873|Xlsx in pdf: l'interruzione di pagina è diversa rispetto al pdf generato da Excel|Insetto|
|CELLSNET-49922|I caratteri non si adattano a una pagina e la posizione di stampa viene modificata nel rendering da Excel a PDF|Insetto|
|CELLSNET-49998|Impossibile visualizzare file XLS specifici con markup HTML|Insetto|
|CELLSNET-49742|Differenze in chart1.xml dopo il salvataggio|Insetto|
|CELLSNET-49875|Segni di graduazione sovrapposti da XLSX a EMF|Insetto|
|CELLSNET-49904|Dal grafico alle date PNG non convertite correttamente|Insetto|
|CELLSNET-49905|Regressione: problema durante la conversione del grafico in PNG|Insetto|
|CELLSNET-49969|Errore di overflow durante il salvataggio del documento XLS in XLSX/XSLM|Insetto|
|CELLSNET-49760|L'area unita viene visualizzata in modo errato durante la conversione in html.|Insetto|
|CELLSNET-49789|La griglia originale di Excel non deve essere modificata durante il salvataggio del file html|Insetto|
|CELLSNET-49850|Immagine: il parametro FitToCell non funziona nei marcatori intelligenti dell'immagine|Insetto|
|CELLSNET-49870|L'intestazione si allarga quando si combinano più fogli nei fogli di calcolo Excel|Insetto|
|CELLSNET-49898|Mostra il bordo delle celle mentre adatta le immagini alle celle utilizzando i marcatori intelligenti|Insetto|
|CELLSNET-49924|File XLSX generati da Aspose che si aprono con errore|Insetto|
|CELLSNETCORE-301|L'aggiunta del foglio di lavoro non riesce quando il collegamento ipertestuale ha un indirizzo nullo|Insetto|
|CELLSNET-49812|Eccezione quando si apre il file ODS|Eccezione|
|CELLSNET-49876|Eccezione durante il nuovo salvataggio di un file XLSX|Eccezione|
|CELLSNET-49943|System.NullReferenceException durante la copia della cartella di lavoro|Eccezione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Ulteriori vincoli per l'aggiunta di aree per la convalida.**

Abbiamo modificato il modello di area per la convalida e la formattazione condizionale per tener conto delle prestazioni. Il nuovo modello richiede più vincoli per la sequenza delle aree aggiunte. Per Validation.AddArea(CellArea cellArea, bool checkIntersection, bool checkEdge) e Validation.AddAreas(CellArea[]areas, bool checkIntersection, bool checkEdge), se i due parametri "check" sono false, l'utente deve assicurarsi che le aree aggiunte sono ordinati in ordine crescente dagli angoli in alto a sinistra. In caso contrario, si potrebbero ottenere risultati imprevisti per altre operazioni. Nella nuova versione, poiché le prestazioni dell'aggiunta di grandi quantità di aree sono state migliorate in modo significativo, non pensiamo che Validation.AddArea(CellArea cellArea) sarà più un collo di bottiglia. Quindi pensiamo che gli utenti possano semplicemente chiamare direttamente AddArea(CellArea cellArea), senza la necessità di utilizzare questi due metodi speciali.

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


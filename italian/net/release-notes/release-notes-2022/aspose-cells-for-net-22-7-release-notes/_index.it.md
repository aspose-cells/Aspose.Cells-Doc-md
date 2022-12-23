---
title: Aspose.Cells for .NET 22.7 Note di rilascio
type: docs
weight: 6
url: /it/net/aspose-cells-for-net-22-7-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.7](https://www.nuget.org/packages/Aspose.Cells/22.7.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-51296| Gridweb continua a tornare all'inizio quando prova a copiare e incollare|
|CELLSNET-51355|Range.Top, Left, Width ,Height in unità di punti|
|CELLSNET-51367|Converti tutti i fogli in una pagina quando salvi come html.|
|CELLSNET-51486|Il testo reso come quadratini|
|CELLSNET-51492|Il carattere predefinito non viene applicato durante la conversione da XLSX a HTML|
|CELLSNET-51306|Stili di tabella pivot non copiati correttamente utilizzando l'ultima versione di Aspose.Cells for .NET|
|CELLSNET-51268|Problema con la formula COUNTIFS che tratta 0 in modo errato|
|CELLSNET-51297|Cell.GetPrecedents() non fornisce tutti i precedenti quando la formula fa riferimento a un nome definito|
|CELLSNET-51399|Print_Titles intervallo denominato e la funzione MATCH restituisce l'errore #NOME|
|CELLSNET-51456|le celle saltano quando fai ctrl+c ctrl+v quando l'altezza di GridWeb è impostata su 100%|
|CELLSNET-51457|il menu contestuale non viene visualizzato quando l'altezza è impostata al 100% dopo alcune righe|
|CELLSNET-51471|l'elenco di convalida non viene visualizzato nella cella vuota|
|CELLSNET-51469|Manca il testo nell'immagine dopo la conversione in pdf|
|CELLSNET-51476|L'elemento freccia diventa distorto nell'immagine|
|CELLSNET-51001|L'oggetto forma sul grafico non è posizionato correttamente|
|CELLSNET-51156| Conversione da grafico a immagine - Visualizzazione diversa del grafico nell'immagine di output|
|CELLSNET-51213|Grafico a torta 3D non correttamente visualizzato - Conversione da grafico a immagine|
|CELLSNET-51472|Le etichette del grafico mancano da SVG quando sono impostate sull'estremità esterna|
|CELLSNET-51491|Valori errati utilizzati nelle serie di grafici durante il rendering nell'immagine o HTML|
|CELLSNET-51525|Il grafico a cascata è diverso se esportato in HTML/PNG o PDF|
|CELLSNET-51353|La conversione di un file XLSB con collegamento DDE al file XLSM sta modificando la posizione dell'applicazione DDE nel collegamento|
|CELLSNET-51376|La dimensione della pagina viene modificata automaticamente da A4 ? Lettera per un foglio|
|CELLSNET-51379| Il collegamento esterno di tipo OLE nel file XLS viene letto come di tipo DDE|
|CELLSNET-51402|Il contenuto viene spostato fuori dalla cella durante il salvataggio del file html|
|CELLSNET-51417|I collegamenti dalla forma al foglio nel file vengono rimossi dopo l'aggiornamento dalla versione 22.5 alla versione 22.6.1|
|CELLSNET-51418|Un collegamento esterno di tipo xlPathMissing viene modificato nel normale tipo externalLinkPath nella conversione da XLSB a XLSM|
|CELLSNET-51420|Differenze nelle proprietà del documento nel file app.xml|
|CELLSNET-51427|Collegamento esterno contenente il carattere speciale "#" che non è sfuggito a Aspose.Cells|
|CELLSNET-51482|La combinazione di fogli di diverse cartelle di lavoro produce file corrotti che possono causare l'arresto anomalo di MS Excel|
|CELLSNET-51507|Valori numerici dal file XLSX letti come 0|
|CELLSNET-51280|Eccezione durante il salvataggio del file ODS (RB-60121)|
|CELLSNET-51483|Il caricamento del file non riesce con l'eccezione "L'array di origine non era abbastanza lungo..."|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cells.GetDependentsInCalculation(int,int,bool)**

Ottiene tutte le celle il cui risultato calcolato dipende dalla cella specificata da riga e colonna in base alla catena di calcolo corrente. Per la cella che è vuota e non è stata istanziata nel modello di celle corrente, l'utente può utilizzare questo metodo invece di Cell.GetDependentsInCalculation(bool) perché il successivo deve prima istanziare l'oggetto cella nel modello di celle corrente.

### **Cambia il bordo sinistro/destro della cella per Cell.GetStyle() quando la colonna adiacente è nascosta**

Nelle versioni precedenti, se la colonna adiacente è nascosta per una cella, il bordo sinistro/destro di questa cella non verrà verificato con la cella adiacente, quindi il bordo restituito potrebbe essere diverso da quello mostrato nella finestra di dialogo di ms excel quando si imposta il bordo di questa cella. Da 22.7, facciamo in modo che il bordo restituito sia sempre il valore effettivo (che dovrebbe essere coerente con il bordo della sua cella adiacente) della cella per Cell.GetStyle(). Se l'utente ha bisogno di quanto mostrato per la cella in ms excel (quando la colonna adiacente è nascosta, il bordo mostrato potrebbe essere quello della successiva colonna visibile), l'utente può provare Cell.GetDisplayStyle().

### **Aggiungere le proprietà Range.Top, Range.Left, Range.Height e Range.Width.**

Ottiene la posizione e le dimensioni dell'intervallo in unità di punti.

### **Elimina la classe PowerQueryFormulaCollction e aggiungi la classe PowerQueryFormulaCollection.**

C'è un errore di battitura nella vecchia classe.

### **Aggiungere le proprietà HtmlSaveOptions.ExportPageFooters e HtmlSaveOptions.ExportPageHeaders.**

Indica se esportare intestazioni e piè di pagina durante il salvataggio come singolo file html.

### **Aggiunge la proprietà HtmlSaveOptions.ShowAllSheets.**

Indica se visualizzare tutti i fogli durante il salvataggio come singolo file html.

### **Rende obsoleta la proprietà HtmlSaveOptions.ExportHeadings e aggiunge la proprietà HtmlSaveOptions.ExportRowColumnHeadings.**

Utilizzare invece HtmlSaveOptions.ExportRowColumnHeadings.

### **Obsoleto Chart.ToImage(string, ImageFormat) e aggiunto Chart.ToImage(string, ImageType)**

Utilizzare invece Chart.ToImage(string, ImageType).

### **Obsoleto Chart.ToImage(Stream, ImageFormat) e aggiunto Chart.ToImage(Stream, ImageType)**

Utilizzare invece Chart.ToImage(Stream, ImageType).

### **Rende obsoleto Shape.ToImage(Stream, ImageFormat) e aggiunge Shape.ToImage(Stream, ImageType)**

Utilizzare invece Shape.ToImage(Stream, ImageType).

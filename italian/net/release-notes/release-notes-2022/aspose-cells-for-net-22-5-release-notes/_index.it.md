---
title: Aspose.Cells for .NET 22.5 Note di rilascio
type: docs
weight: 8
url: /it/net/aspose-cells-for-net-22-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.5](https://www.nuget.org/packages/Aspose.Cells/22.5.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50663|Migliora le prestazioni di eliminazione delle colonne vuote|
|CELLSNET-50877|Inizializza il valore calcolato della cella durante l'impostazione della formula dell'array dinamico|
|CELLSNET-51006|Rimuovere il metodo SetDataSource(string variable, object[]dataArray).|
|CELLSNET-50685|Problema con il recupero degli allegati OLE collegati nel file ODS|
|CELLSNET-50920|Problema di conversione da Excel a Tiff|
|CELLSNET-50820| Problema di esportazione della stringa JSON in Excel|
|CELLSNET-50853|Il filtro dei filtri dei dati scompare dopo il nuovo salvataggio da parte delle API Aspose.Cells|
|CELLSNET-50960|Cartella di lavoro danneggiata durante il nuovo salvataggio di un file XLSM (contenente una tabella pivot) da Aspose.Cells|
|CELLSNET-50648|L'errore DIV/0 viene trasformato in errore NUM durante il calcolo della funzione NPER|
|CELLSNET-50694|Problema con DeleteBlankColumns(options) quando i commenti sono presenti nei fogli Excel|
|CELLSNET-50730|Errore di calcolo del modulo della matrice della funzione INDICE|
|CELLSNET-50781|Formula non calcolata come in MS Excel|
|CELLSNET-50861| Contiene per Cells.Find() non funziona con i caratteri tilde|
|CELLSNET-50879|Il valore calcolato di Cell non è stato aggiornato durante l'aggiornamento delle formule di matrice dinamica con valore vero per il parametro "calcola"|
|CELLSNET-50992|Il valore di data e ora è stato modificato per le proprietà del documento personalizzato dopo il salvataggio in ODS|
|CELLSNET-50953|Disattiva copia/incolla da tastiera in GridDesktop|
|CELLSNET-50771| Il carattere diventa in grassetto durante la conversione da Excel a PDF|
|CELLSNET-50924|Cell sfondo perso dopo la conversione in html|
|CELLSNET-50951|Conversione di Excel in risultati HTML con problemi|
|CELLSNET-50962| Problema con l'interruzione del processo di salvataggio con l'opzione PdfSaveOptions.OnePagePerSheet per cartelle di lavoro di grandi dimensioni|
|CELLSNET-50997|I contorni punteggiati della scatola delle celle si rompono sul lato destro della scatola in altezza|
|CELLSNET-50865|Da grafico a immagine: rendering non corretto|
|CELLSNET-50952|La conversione da XLS a XLSX modifica il gradiente a due colori dei formati condizionali|
|CELLSNET-50989|La larghezza delle colonne adattate automaticamente non è corretta se le celle vengono unite.|
|CELLSNET-50987|La regolazione della forma del trapezio risulta in "System.ArgumentOutOfRangeException"|
|CELLSNET-50930| Il processo non può accedere all'eccezione file dal Aspose.Cells 22.1|
|CELLSNET-50946|Una conversione del foglio di lavoro di Excel non riesce con l'errore "Impossibile trasmettere .."|
|CELLSNET-51009|TextToColumns causa "System.NullReferenceException" al salvataggio|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Modifiche per il salvataggio della cartella di lavoro con LightCells**

Per rendere disponibili le funzionalità relative alle formule per LightCells, nelle versioni precedenti manteniamo in memoria tutti i dati delle formule nel modello di celle durante il salvataggio della cartella di lavoro con LightCells. Ciò ha causato incomprensioni e uso improprio di LightCells per alcuni utenti. L'utente aveva pensato che i dati della formula della cella fossero stati rilasciati al di fuori dell'ambito di StartCell(Cell) ma in realtà no. Per la maggior parte degli utenti che utilizzano LightCells, la loro preoccupazione principale sono le prestazioni (costo della memoria). Poche persone useranno funzioni relative alle formule diverse dall'impostazione di una formula semplice nella cella nel processo di salvataggio della cartella di lavoro. Quindi, da questa versione aggiungiamo alcune restrizioni per la modifica dell'oggetto cella nell'ambito del metodo StartCell(Cell). Ora non è consentito impostare formule condivise, formule di matrice per l'oggetto cella specificato nel metodo StartCell(Cell). Se sono necessari tali tipi di formule, l'utente deve impostarle prima di salvare la cartella di lavoro. Con questa modifica, abbiamo migliorato le prestazioni per la maggior parte degli utenti che devono salvare una semplice formula per le celle nel file del foglio di calcolo risultante con LightCells.

### **Elimina il metodo obsoleto Cell.SetAddInFormula()**

Utilizzare invece WorksheetCollection.RegisterAddInFunction() e Cell.Formula/Cell.SetFormula().

### **Aggiunge l'enumerazione ExceptionType.FileCorrupted**

Rappresenta il tipo di eccezione in cui il file è danneggiato.

### **Aggiunge l'enumerazione WarningType.Limitation**

Rappresenta il tipo di avviso è la limitazione di Excel.

### **Aggiunge il metodo ShapeGuideCollection.Add(string name, double val).**

Aggiunge una guida forma.

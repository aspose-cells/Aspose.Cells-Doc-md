---
title: Aspose.Cells for Android via Java 22.6 Note di rilascio
type: docs
weight: 7
url: /it/java/aspose-cells-for-android-via-java-22-6-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 22.6.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44632|Supporta la formattazione dell'intera riga di dati nella tabella pivot|
|CELLSJAVA-44415|Migliaia di chiamate getResourceAsAStream causano un carico elevato della CPU e un consumo di memoria elevato durante la generazione del report|
|CELLSJAVA-44490|aggiungere GridWorkbookSetting per GridWeb|
|CELLSJAVA-44554|Migliora il modello LightCells per l'impostazione delle formule|
|CELLSJAVA-44535|implementare la cella di messa a fuoco con barra di scorrimento verticale/orizzontale scorrimento automatico alla posizione adatta|
|CELLSJAVA-44588|Rileva il formato del file per lo streaming con password|
|CELLSJAVA-44611|Miglioramento per la lettura di celle vuote da file xlsx|
|CELLSJAVA-44616|Le impostazioni originali della formattazione condizionale nell'intervallo di destinazione devono essere rimosse durante la copia dell'intervallo|
|CELLSJAVA-44658|Supporto BouncyCastle v1.71|
|CELLSJAVA-44455|Quando si converte il file XLSX in PDF, la data nella tabella pivot diventa un numero di serie|
|CELLSJAVA-44370|Il file Excel viene danneggiato quando viene aperto e salvato con Aspose.Cells|
|CELLSJAVA-44381|Problema di formattazione della condizione durante l'eliminazione della riga o della colonna|
|CELLSJAVA-44442|L'apertura e il salvataggio con Aspose.Cells danneggia la cartella di lavoro|
|CELLSJAVA-44356|problema di posizione dell'immagine per la stampa per il file fs.zip in GridWeb|
|CELLSJAVA-44357|problemi per la visualizzazione di ofd.zip in GridWeb|
|CELLSJAVA-44398|Problemi di visualizzazione di GridWeb da parte del cliente|
|CELLSJAVA-44464|problema aggiuntivo 1, colonna Un colore di sfondo non è lo stesso di Excel per yscl.xls a sheet4|
|CELLSJAVA-44466| problema aggiuntivo 3, setCalculateFormula su false non funziona|
|CELLSJAVA-44496|Includi il tag/elemento didascalia per la tabella durante il caricamento dell'html|
|CELLSJAVA-44429|L'effetto del grafico Excel in Excel è diverso da quello in HTML|
|CELLSJAVA-44414| Unicode in JSON interromperà i generati XLSX e CSV|
|CELLSJAVA-44481|Problema con il metodo ThreadedComment.setCreatedTime()|
|CELLSJAVA-44483|L'ordinamento non funziona dopo aver raggruppato le righe|
|CELLSJAVA-44522|Il doppio valore della stringa dà tailing zero che non è corretto se confrontato con il risultato di ms excel|
|CELLSJAVA-44501| cerca nel prossimo numero il file duohangduolie.zip|
|CELLSJAVA-44529|implementare la ricerca di freezepane|
|CELLSJAVA-44530|indagare sul problema di setactivecell a volte non funziona|
|CELLSJAVA-44534|Grafica nell'area di stampa non esportata in Excel alla conversione HTML|
|CELLSJAVA-44539|Il grafico viene spostato a destra durante la conversione in html con area di stampa|
|CELLSJAVA-44568|I sottotitoli su più righe vengono persi tranne la prima riga nella conversione da HTML a XLS|
|CELLSJAVA-44512|Il grafico non è presente durante l'esportazione del grafico in formato svg in html|
|CELLSJAVA-44556|Problema con la visualizzazione dei dati nella tabella dati dopo che l'asse delle coordinate è stato impostato su scala logaritmica - Conversione da Excel a HTML/PDF|
|CELLSJAVA-44628|Come conservare il formato percentuale di determinate righe pivot quando si espandono i dati del nodo di una colonna/campo pivot|
|CELLSJAVA-44483|L'ordinamento non funziona dopo aver raggruppato le righe|
|CELLSJAVA-44609|Copia lenta con formattazione condizionale utilizzando la versione più recente|
|CELLSJAVA-44622|Quando si ordinano gruppi di grandi dimensioni con più chiavi, genera "java.lang.ArrayIndexOutOfBoundsException"|
|CELLSJAVA-44630|Problema con la funzione Smart Markers dal Aspose Cells 22.5|
|CELLSJAVA-44646|Il contenuto chiaro sul foglio copiato genera NullPointerException|
|CELLSJAVA-44656|Cells.getMaxDataColumn restituisce un valore diverso (errato) in 22.5|
|CELLSJAVA-44650|La pagina del documento Excel è disordinata durante il caricamento in Aspose.Cells.GridWeb(Java)|
|CELLSJAVA-44660|Problema con l'allineamento dei dati durante il caricamento di XLS in Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44661|Problema durante il caricamento del file et in Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44584|Il titolo dell'asse nel grafico viene ruotato nell'immagine di output - Conversione da grafico a immagine|
|CELLSJAVA-44615|Linea grigia tracciata nell'immagine di output dal file XLS|
|CELLSJAVA-44665|Il caricamento del file ODS si blocca|
|CELLSJAVA-44404|Eccezione "java.lang.IllegalArgumentException: indice di colonna non valido" durante il caricamento di un file XLSX in GridWeb|
|CELLSJAVA-44651|Errore "Non un valore numerico" durante la conversione del foglio Excel in HTML/PDF|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo sul forum di supporto Aspose.Cells.

### **Aggiunge la classe DefaultStyleSettings.**

Gruppo di valori predefiniti per le proprietà relative allo stile.

### **Aggiunge la proprietà LoadOptions.DefaultStyleSettings.**

Supporto per impostare i valori predefiniti delle proprietà relative allo stile per l'inizializzazione di una cartella di lavoro.

### **Aggiunge la proprietà TxtSaveOptions.TrimTailingBlankCells.**

Supporto per rimuovere tutte le celle vuote (caratteri ripetuti di separatore come "~,~,~,~,") alla fine del record di riga durante l'esportazione di csv/tsv.

### **Aggiunge la proprietà Style.HasBorders.**

Supporto per verificare se sono stati impostati bordi per lo stile.

### **Proprietà LoadOptions.StandardFont/StandardFontSize obsolete.**

Utilizzare invece LoadOptions.DefaultStyleSettings.FontName/FontSize.

### **Rimuove l'enumerazione obsoleta StyleModifyFlag.FontSubscript e FontSuperscript.**

Utilizzare invece StyleModifyFlag.FontScript.

### **Proprietà Shape.ConnectionPoints obsolete.**

Utilizzare invece il metodo GetConnectionPoints().

### **Aggiunge il metodo Shape.GetConnectionPoints().**

Ottieni i punti di connessione.

### **Aggiunge le proprietà Row.IsCollapsed e Column.IsCollapsed.**

Indica se la riga e la colonna sono compresse.

### **Aggiunge l'enumerazione PasteType.ValuesAndFormats.**

Indica solo la copia di valori e formati.

### **Aggiunge la proprietà Shape.IsInGroup.**

Indica se la forma è raggruppata.

### **Aggiunge il metodo AutoFilter.GetCellArea().**

Ottiene l'area a cui si applica il filtro automatico specificato.

### **Aggiunge il metodo Cells.GetRowOriginalHeightPoint().**

Ottiene l'altezza della riga originale, in unità di punti.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, PivotField baseField).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, int row, int column, PivotField baseField).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, int baseFieldIndex).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, int row, int column, int baseFieldIndex).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge il metodo TimelineCollection.Add(PivotTable pivot, string destCellName, string baseFieldName).**

Aggiungi una nuova sequenza temporale utilizzando la tabella pivot come origine dati.

### **Aggiunge l'enumerazione DataLabelShapeType.Line.**

Rappresenta la forma della linea. Questo tipo non è disponibile in Excel, viene utilizzato solo per alcuni file speciali.

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

### **Aggiunge la classe CellsDataTableFactory**

Questa classe fornisce API per creare un'istanza di ICellsDataTable da oggetti personalizzati per comodità dell'utente.

### **Aggiunge la proprietà Workbook.CellsDataTableFactory**

Fornire all'utente CellsDataTableFactory per creare un'istanza di ICellsDataTable da oggetti personalizzati.

### **Aggiunge il metodo Cell.GetDependentsInCalculation(bool).**

In base all'attuale catena di calcolo, ottieni tutte le celle il cui risultato calcolato dipende da questa cella.

### **Aggiunge il metodo Cell.GetPrecedentsInCalculation()**

In base all'attuale catena di calcolo, ottieni tutti i precedenti (riferimento alle celle nella cartella di lavoro corrente) utilizzati dalla formula di questa cella durante il calcolo.

### **Metodi obsoleti Cell.GetLeafs() e Cell.GetLeafs(bool)**

Utilizzare invece il metodo Cell.GetDependentsInCalculation(bool).

### **Aggiunge il metodo PivotTable.FormatRow(int row, Style style).**

Formatta i dati della riga nell'area della tabella pivot.

### **Aggiunge la proprietà Shapes.CreateId**

Ottiene l'ID di creazione della forma.

### **Aggiunge l'enumerazione WarningType.InvalidData**

Rappresenta il tipo di dati non valido.

### **Aggiunge il metodo di sovraccarico ChartCollection.Add()**

Aggiunge un grafico con l'origine dati.

### **Aggiunge il metodo Chart.GetActualSize()**

Ottiene la dimensione effettiva del grafico in unità di pixel.

### **Proprietà Chart.ActualChartSize obsoleta**

Utilizzare invece il metodo Chart.GetActualSize().

### **Proprietà PdfSaveOptions.ImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Proprietà ImageOrPrintOptions.ChartImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.ImageFormat**

Utilizzare invece la proprietà ImageOrPrintOptions.ImageType.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.IsImageFitToPage**

La proprietà è inutile.
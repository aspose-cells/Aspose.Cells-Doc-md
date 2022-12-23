---
title: Aspose.Cells for PHP via Java 22.5 Note di rilascio
type: docs
weight: 8
url: /it/php-java/aspose-cells-for-php-via-java-22-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for PHP via Java 22.5](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.5/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44554|Migliora il modello LightCells per l'impostazione delle formule|
|CELLSJAVA-44535|implementare la cella di messa a fuoco con barra di scorrimento verticale/orizzontale scorrimento automatico alla posizione adatta|
|CELLSJAVA-44588|Rileva il formato del file per lo streaming con password|
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

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

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



---
title: Aspose.Cells per Python tramite Java 22.4 Note di rilascio
type: docs
weight: 9
url: /it/python-java/aspose-cells-for-python-via-java-22-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells per Python tramite Java 22,4](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.4/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44415|Migliaia di chiamate getResourceAsAStream causano un carico elevato della CPU e un consumo di memoria elevato durante la generazione del report|
|CELLSJAVA-44490|aggiungere GridWorkbookSetting per GridWeb|
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
|CELLSJAVA-44414| Unicode in JSON interromperà XLSX e CSV generati|
|CELLSJAVA-44404|Eccezione "java.lang.IllegalArgumentException: indice di colonna non valido" durante il caricamento di un file XLSX in GridWeb|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

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
---
title: Aspose.Cells per Python tramite Java 21.2 Note di rilascio
type: docs
weight: 12
url: /it/python-java/aspose-cells-for-python-via-java-21-2-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per Python tramite Java 21.2.

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43382|La copia produce una cartella di lavoro danneggiata|
|CELLSJAVA-43364|Problema durante il salvataggio del grafico con un'immagine nel marcatore dell'immagine|
|CELLSJAVA-43389|Impostazioni di protezione password cartella di lavoro/foglio di lavoro perse durante il salvataggio come formato di file XLSB|
|CELLSJAVA-43392| La copia del foglio produce una cartella di lavoro danneggiata|
|CELLSJAVA-43387|L'esportazione di un singolo foglio in HTML genera un'eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Modifica il comportamento di Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

Nelle vecchie versioni, eliminiamo tutte le impostazioni della colonna mentre eliminiamo le righe vuote se il foglio di lavoro è vuoto (nessun dato di celle). Ciò rende impossibile per l'utente eliminare solo le righe vuote e mantenere tutte le impostazioni della colonna. Dalla versione 21.2 non cancelliamo più le impostazioni delle colonne. Se l'utente deve eliminare le impostazioni della colonna per un foglio di lavoro vuoto, deve controllare che non ci siano dati nel foglio e quindi cancellare manualmente ColumnCollection.
Nelle vecchie versioni, non eliminiamo le righe vuote sotto forma. Ciò rende impossibile per l'utente eliminare tutte le righe vuote come previsto. Da 12.2, eliminiamo quelle righe vuote sotto forma insieme ad altre righe vuote comuni.

### **Proprietà Range.CellCount obsoleta.**

Utilizzare invece Range.RowCount e Range.ColumnCount per ottenere il conteggio totale delle celle.

### **Aggiunge la proprietà AutoFilter.ShowFilterButton.**

Indica se mostrare il pulsante filtro del filtro automatico.

### **Elimina la proprietà SeriesCollection.SecondCatergoryData.**

Utilizzare invece la proprietà SeriesCollection.SecondCategoryData.

### **Elimina l'enumerazione StyleModifyFlag.Spacing.**

Non è usato.


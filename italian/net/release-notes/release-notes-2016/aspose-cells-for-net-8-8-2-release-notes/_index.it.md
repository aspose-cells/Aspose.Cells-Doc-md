---
title: Aspose.Cells for .NET 8.8.2 Note di rilascio
type: docs
weight: 90
url: /it/net/aspose-cells-for-net-8-8-2-release-notes/
---
### **1) Aspose.Cells**

|**Chiave** |**Sommario** |**Categoria** |
|:- |:- |:- |
|CELLSNET-44314 | Come rendere i caratteri supplementari Unicode| Nuova caratteristica|
|CELLSNET-41817 | Impostazione dell'effetto del testo su Offset in forma rettangolare| Aumento|
|CELLSNET-41454 | Aspose.Cells determina erroneamente alcuni formati di file| Aumento|
|CELLSNET-44476 | La direzione del testo viene ignorata durante il salvataggio nel formato file HTML| Insetto|
|CELLSNET-44457 | I bordi inferiori nella tabella vengono persi durante la conversione nel file HTML| Insetto|
|CELLSNET-44446 | Tutti gli stili CSS non sono preceduti durante il salvataggio come HTML| Insetto|
|CELLSNET-44444 | L'apertura e il salvataggio del file contenente la tabella pivot generano un foglio di calcolo corrotto| Insetto|
|CELLSNET-44443 | Ruota il grafico su PDF - Asse y secondario incasinato| Insetto|
|CELLSNET-44450 | La rotazione dell'immagine non è corretta nel risultante PDF| Insetto|
|CELLSNET-44303 | SheetRender.ToImage non esegue correttamente il rendering delle etichette dei dati del grafico| Insetto|
|CELLSNET-44478 | Il livello di zoom cambia dopo l'apertura e la riscrittura del file Excel| Insetto|
|CELLSNET-44477 | Elenca i nomi degli oggetti in conflitto nella copia del foglio di lavoro| Insetto|
|CELLSNET-44472 | CustomXmlParts non funziona correttamente per il file XLS| Insetto|
|CELLSNET-44466 |Impossibile visualizzare correttamente le immagini dopo l'esportazione di HTML in Excel| Insetto|
|CELLSNET-44465 | I grafici vengono rimossi quando si eliminano righe/colonne vuote| Insetto|
|CELLSNET-44463 | Il testo nero in TextBox viene reso bianco in PDF| Insetto|
|CELLSNET-44456 | Lo stile in grassetto nel file di destinazione è andato perso dopo la chiamata Range.CopyData()| Insetto|
|CELLSNET-44453 | La proprietà ExternalLink.IsReferred non funziona come previsto| Insetto|
|CELLSNET-44445 | CopyStyle (marcatori intelligenti) non funziona su tutte le celle unite| Insetto|
|CELLSNET-44263 | La formattazione viene persa durante l'importazione di HTML come XLSX| Insetto|
|CELLSNET-44439 | NullReferenceException in PivotField.IsAscendSort| Eccezione|
|CELLSNET-44430 | Si verifica un errore durante l'esecuzione di calcoli complessi| Eccezione|
### **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Sommario** |**Categoria** |
|:- |:- |:- |
|CELLSNET-44441 | Quando la riga è selezionata nella versione più recente, seleziona anche la prima cella della riga successiva| Insetto|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la classe DeleteOptions.**
Rappresenta l'impostazione di eliminazione di righe/colonne.
#### **Aggiunge i metodi override Cells.DeleteBlankRows (Opzioni DeleteOptions) e Cells.DeleteBlankColumns (Opzioni DeleteOptions).**
Elimina righe o colonne vuote con l'impostazione.

---
title: Aspose.Cells for Java 20.3 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-20-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.3/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43137|Light Cells API: elaborazione di fogli in un ordine specifico|Nuova caratteristica|
|CELLSJAVA-43135|Rimuovi ActiveXControl dalla forma dell'immagine|Nuova caratteristica|
|CELLSJAVA-43141|Aggiungere la proprietà ThreadedComment.CreatedTime|Nuova caratteristica|
|CELLSJAVA-42068|La GIF nel foglio di lavoro è errata quando la cartella di lavoro viene convertita in HTML|Insetto|
|CELLSJAVA-43127|La tabella pivot di Excel non viene aggiornata automaticamente quando il file viene aperto per la prima volta|Insetto|
|CELLSJAVA-43129|Il testo cinese è confuso nella conversione da HTML a XLS|Insetto|
|CELLSJAVA-43139|I grafici nel foglio non vengono aggiornati durante il rendering del foglio di lavoro nell'immagine|Insetto|
|CELLSJAVA-43148|Errore di posizione dell'etichetta del grafico|Insetto|
|CELLSJAVA-43124|Durante la conversione in PDF, due colonne vengono tagliate dalla tabella|Insetto|
|CELLSJAVA-43091|Le etichette dei dati sul grafico a ciambelle sono sovrapposte nel file PDF|Insetto|
|CELLSJAVA-43132|Etichette dati mancanti in alcuni grafici durante l'esportazione del grafico nell'immagine|Insetto|
|CELLSJAVA-43143|Dopo WorkbookDesigner.process, l'output del grafico è nullo in HTML|Insetto|
|CELLSJAVA-43098|La sostituzione dell'oggetto incorporato con un'immagine non funziona per il formato di file XLS|Insetto|
|CELLSJAVA-43122|Un problema con l'ordine dei commenti in thread dopo l'importazione nel formato file XLSX di Office365|Insetto|
|CELLSJAVA-43134|Il valore stringa di una cella è vuoto in Apple Numbers'09|Insetto|
|CELLSJAVA-43144|Proprietà IsItalic rilevata in modo diverso rispetto a MS Excel (Java)|Insetto|
|CELLSJAVA-43140|IllegalArgumentException durante la chiamata acalcFormula()|Eccezione|
|CELLSJAVA-43110|Conversione in PDF - java.lang.NullPointerException|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiungere la proprietà LoadFilter.SheetsInLoadingOrder**
Gli utenti possono sovrascrivere questa proprietà per specificare i fogli e l'ordine da caricare durante l'importazione delle cartelle di lavoro dai file modello.
### **Elimina la proprietà TickLabels.Background obsoleta**
Utilizzare invece la proprietà TickLabels.BackgroundMode.
### **Rende obsoleta la proprietà TickLabels.TextDirection e aggiunge la proprietà TickLabels.ReadingOrder**
Utilizzare invece la proprietà TickLabels.ReadingOrder.
### **Obsoleta TickLabels.DirectionTypeproperty e aggiunge enum ChartTextDirectionType**
Rappresenta la direzione del testo.
### **Aggiunge il metodo Shape.RemoveActiveXControl().**
Rimuove i dati ActiveX dalla forma.
### **Aggiunge la proprietà ThreadedComment.CreatedTime.**
Ottiene e imposta l'ora di creazione dei commenti in thread.
### **Aggiunge la proprietà Worksheet.UniqueId.**
Ottiene e imposta l'ID univoco del foglio di lavoro.
### **Aggiunge enum IconSetType.ColorSmilies3 e IconSetType.Smilies3.**
Rappresenta le formattazioni condizionali del set di icone 3smiles. Solo per file .ods
### **Aggiunge enum TimePeriodType.LastYear,TimePeriodType.NextYear e ThisYear.**
Rappresenta le formattazioni condizionali dell'anno scorso, dell'anno prossimo e di quest'anno. Solo per file .ods.
### **Aggiunge il metodo WorksheetCollection.RefreshPivotTables().**
Aggiornamento di tutte le tabelle pivot nel file.

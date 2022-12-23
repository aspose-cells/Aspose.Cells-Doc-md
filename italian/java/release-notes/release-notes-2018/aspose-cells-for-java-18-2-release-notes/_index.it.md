---
title: Aspose.Cells for Java 18.2 Note di rilascio
type: docs
weight: 110
url: /it/java/aspose-cells-for-java-18-2-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.2.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42509|Aggiungere la costante LoadDataFilterOptions.NAMES per filtrare i nomi definiti durante il caricamento della cartella di lavoro|Nuova caratteristica|
|CELLSJAVA-42510|Osserva il filtraggio molto lento in Microsoft Excel 2013 e 2016 quando viene applicato il filtro|Aumento|
|CELLSJAVA-42497|Le forme Sheet1 vengono perse e le stelle in Sheet2 vengono arrotondate|Insetto|
|CELLSJAVA-42512|Codifica non valida: si verifica un'eccezione durante il caricamento del file Excel|Insetto|
|CELLSJAVA-42507|I fogli macro e di dialogo vengono rilevati come normali fogli di lavoro|Insetto|
|CELLSJAVA-42503|MS Excel non consente di salvare nuovamente il file XLS|Insetto|
|CELLSJAVA-42502|Aspose.Cells non filtra correttamente i dati invece nasconde tutte le righe|Insetto|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge l'enumerazione LoadDataFilterOptions.DefinedNames**
Indica se caricare gli oggetti Name definiti durante il caricamento del file modello.
### **Modifica il comportamento di LoadDataFilterOptions.Formula enum**
Nelle versioni precedenti carichiamo sempre gli oggetti Nome definiti durante il caricamento delle formule. Ora forniamo un enum separato per gli oggetti Name definiti in modo esplicito, quindi Formula enum indicherà solo che le formule devono essere caricate ora, indipendentemente dal fatto che gli oggetti Name definiti vengano caricati o meno. Tuttavia, una cosa dovrebbe essere notata, gli oggetti Nome comunemente definiti sono usati dalle formule, se l'utente carica solo le formule e non carica gli oggetti Nome definiti, la formula della cella che fa riferimento a quei Nomi verrà danneggiata e potrebbe causare un'eccezione. Quindi, generalmente se l'utente desidera caricare formule, devono essere caricati anche gli oggetti Nome definiti. Ma l'utente può caricare solo oggetti Nome definiti senza caricare formule.
### **Aggiungere l'enumerazione SheetType.Dialog**
Rappresenta il foglio di dialogo.
### **Aggiunge la proprietà WorkbookSettings.MaxRowsOfSharedFormula**
Ottiene e imposta il numero massimo di righe della formula condivisa. La formula condivisa verrà suddivisa in più formule condivise se le righe totali della formula condivisa sono maggiori di essa.
### **Aggiunge la proprietà WorkbookSettings.StreamProvider**
Ottiene e imposta il provider di flussi per la risorsa esterna.
### **Aggiunge la proprietà ShapeTextAlignment.IsAutoMargin**
Indica se il margine della cornice di testo è automatico.
### **Aggiunge la proprietà ImportTableOptions.IsFormulas**
Rappresenta quale colonna nel datatable deve essere importata come formule.

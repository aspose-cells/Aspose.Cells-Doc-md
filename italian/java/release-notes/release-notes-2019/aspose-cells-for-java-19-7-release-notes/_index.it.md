---
title: Aspose.Cells for Java 19.7 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-19-7-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.7.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42861|Impossibile ottenere il testo alternativo della forma nel formato file ODS|Insetto|
|CELLSJAVA-42929|Il titolo del grafico cambia nella conversione da XLSX a PDF|Insetto|
|CELLSJAVA-42933|Il colore della grafica cambia durante la conversione del file Excel in PDF|Insetto|
|CELLSJAVA-42946|Rendering errato del grafico a barre in pila con serie in PDF|Insetto|
|CELLSJAVA-42942|Pagine stampate a livello di foglio di lavoro e non a livello di cartella di lavoro|Insetto|
|CELLSJAVA-42952|Rientro errato dalla parte superiore della cella in alcune parole|Insetto|
|CELLSJAVA-42902|Lo stile del grafico a cascata non viene copiato correttamente durante la copia della cartella di lavoro|Insetto|
|CELLSJAVA-42939|Avviso generato da Excel se chiamiamo Workbook.getVbaProject() solo per una cartella di lavoro|Insetto|
|CELLSJAVA-42940|Avviso di sicurezza dopo aver rimosso tutti gli script del modulo VBA|Insetto|
|CELLSJAVA-42955|L'apertura di VBAProject danneggia la cartella di lavoro|Insetto|
|CELLSJAVA-42945|Salva come HTML genera un'eccezione se ExportImagesAsBase64 è impostato|Eccezione|
|CELLSJAVA-42953|NullPointerException durante la conversione di file XLS in HTML|Eccezione|
|CELLSJAVA-42951|java.lang.NullPointerException generata da comment.setHtmlNote()|Eccezione|
|CELLSJAVA-42954|Eccezione sollevata durante il caricamento e il salvataggio di XLSX|Eccezione|
|CELLSJAVA-42957|Viene generato un valore FontUnderlineType non valido durante il salvataggio di XLSX|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiorna la libreria BouncyCastle di riferimento a 1.60**
La libreria BouncyCastle allegata nell'archivio di rilascio è stata aggiornata alla versione 1.60. Tuttavia, Aspose.Cells è compatibile anche con le vecchie versioni, quindi l'utente può ancora utilizzare le vecchie versioni come 1.46.
### **Obsoleta la classe HTMLLoadOptions e aggiunta la classe HtmlLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
### **Obsoleta la classe ODSLoadOptions e aggiunta la classe OdsLoadOptions**
Utilizzare invece la classe OdsLoadOptions.
### **Rende obsoleta la classe JSONUtility e aggiunge la classe JsonUtility**
Utilizzare invece la classe JsonUtilityclass.
### **Aggiunge l'interfaccia IPageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
### **Aggiunge la classe PageSavingArgs**
Informazioni per un processo di salvataggio della pagina.
### **Aggiunge la classe PageStartSavingArgs**
Le informazioni per una pagina avviano il processo di salvataggio.
### **Aggiunge la classe PageEndSavingArgs**
Le informazioni per una pagina terminano il processo di salvataggio.
### **Aggiunge la proprietà PdfSaveOptions.PageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
